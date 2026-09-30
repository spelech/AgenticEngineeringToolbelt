#!/usr/bin/env python3
"""
Unit tests for Static Test Theatre Audit in verify_release.py
Following TDD: red -> green -> refactor
"""

import sys
import tempfile
import unittest
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from verify_release import audit_test_theatre


class TestVerifyReleaseTestTheatreAudit(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_mock_to_assertion_ratio_detected(self):
        """Test files where mock invocations exceed concrete state assertions are flagged."""
        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)

        # File with 3 mock verifications and only 1 state assertion
        test_file = tests_dir / "test_service.py"
        test_file.write_text(
            """
import unittest
from unittest.mock import MagicMock

class ServiceTests(unittest.TestCase):
    def test_workflow(self):
        mock_repo = MagicMock()
        mock_repo.assert_called_with("arg1")
        mock_repo.assert_called_once()
        mock_repo.assert_any_call("arg2")
        self.assertEqual(actual, 42)
"""
        )

        # Add integration harness to avoid failing on missing baseline
        harness = self.root / "tests" / "test_integration.py"
        harness.write_text(
            """
from httpx import AsyncClient
async def test_api():
    async with AsyncClient() as client:
        res = await client.get("/health")
        assert res.status_code == 200
"""
        )

        passed, issues = audit_test_theatre(self.root)
        self.assertFalse(passed)
        self.assertTrue(
            any("mock" in issue.lower() and "ratio" in issue.lower() or "exceed" in issue.lower() for issue in issues),
            f"Expected mock ratio violation in issues: {issues}"
        )

    def test_mock_calls_with_zero_state_assertions_detected(self):
        """Test files with mock verification calls and 0 concrete state assertions are flagged."""
        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)

        csharp_test = tests_dir / "OrderServiceTests.cs"
        csharp_test.write_text(
            """
using Moq;
using Xunit;

public class OrderServiceTests
{
    [Fact]
    public void PlaceOrder_CallsRepository()
    {
        var mockRepo = new Mock<IOrderRepository>();
        var service = new OrderService(mockRepo.Object);
        service.PlaceOrder(new Order());
        mockRepo.Verify(r => r.Save(It.IsAny<Order>()), Times.Once());
    }
}
"""
        )

        # Add integration fixture to isolate this test
        (tests_dir / "IntegrationFixture.cs").write_text(
            """
using Microsoft.AspNetCore.Mvc.Testing;
public class CustomWebApplicationFactory : WebApplicationFactory<Program> {}
"""
        )

        passed, issues = audit_test_theatre(self.root)
        self.assertFalse(passed)
        self.assertTrue(
            any("zero state assertions" in issue.lower() or "0 concrete state assertions" in issue.lower() or "sole assertions" in issue.lower() or "exceed" in issue.lower() for issue in issues),
            f"Expected 0-state-assertion warning in issues: {issues}"
        )

    def test_missing_integration_baseline_detected(self):
        """Test detection of projects that use mock libraries but have 0 integration harnesses."""
        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)

        # Test uses mock library and has state assertions, but no integration harness in repo
        py_test = tests_dir / "test_user_service.py"
        py_test.write_text(
            """
from unittest.mock import MagicMock
import pytest

def test_user_creation():
    mock_db = MagicMock()
    user = create_user(mock_db, "alice")
    assert user.name == "alice"
    assert user.is_active is True
    assert user.id == 123
"""
        )

        passed, issues = audit_test_theatre(self.root)
        self.assertFalse(passed)
        self.assertTrue(
            any("integration" in issue.lower() and ("baseline" in issue.lower() or "harness" in issue.lower()) for issue in issues),
            f"Expected missing integration baseline violation in issues: {issues}"
        )

    def test_integration_baseline_present_passes(self):
        """Test project with mocks AND integration harness passes integration check."""
        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)

        py_test = tests_dir / "test_user_service.py"
        py_test.write_text(
            """
from unittest.mock import MagicMock
import pytest

def test_user_creation():
    mock_db = MagicMock()
    user = create_user(mock_db, "alice")
    assert user.name == "alice"
    assert user.is_active is True
"""
        )

        # Add integration harness (FastAPI AsyncClient)
        integration_test = tests_dir / "test_api_integration.py"
        integration_test.write_text(
            """
from httpx import AsyncClient, ASGITransport
import pytest

@pytest.mark.asyncio
async def test_full_pipeline():
    async with AsyncClient(transport=ASGITransport(app=None), base_url="http://test") as ac:
        res = await ac.get("/api/v1/users")
        assert res.status_code == 200
"""
        )

        passed, issues = audit_test_theatre(self.root)
        self.assertTrue(passed, f"Expected audit to pass, but got issues: {issues}")

    def test_tautological_assertions_python_detected(self):
        """Test detection of tautological assertions in Python."""
        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)

        bad_test = tests_dir / "test_tautology.py"
        bad_test.write_text(
            """
def test_something():
    actual = compute_result()
    assert actual == actual
"""
        )

        passed, issues = audit_test_theatre(self.root)
        self.assertFalse(passed)
        self.assertTrue(
            any("tautological" in issue.lower() and "actual" in issue for issue in issues),
            f"Expected tautological assertion detection in issues: {issues}"
        )

    def test_tautological_assertions_csharp_detected(self):
        """Test detection of tautological assertions in C#."""
        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)

        bad_test = tests_dir / "OrderTests.cs"
        bad_test.write_text(
            """
using Xunit;
public class OrderTests {
    [Fact]
    public void TestValue() {
        var status = "Pending";
        Assert.Equal(status, status);
    }
}
"""
        )

        passed, issues = audit_test_theatre(self.root)
        self.assertFalse(passed)
        self.assertTrue(
            any("tautological" in issue.lower() and "status" in issue for issue in issues),
            f"Expected tautological assertion detection in issues: {issues}"
        )

    def test_tautological_assertions_typescript_detected(self):
        """Test detection of tautological assertions in TypeScript."""
        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)

        bad_test = tests_dir / "ui.test.ts"
        bad_test.write_text(
            """
import { test, expect } from 'vitest';
test('order validation', () => {
    const id = "ord-123";
    expect(id).toBe(id);
});
"""
        )

        passed, issues = audit_test_theatre(self.root)
        self.assertFalse(passed)
        self.assertTrue(
            any("tautological" in issue.lower() and "id" in issue for issue in issues),
            f"Expected tautological assertion detection in issues: {issues}"
        )

    def test_tautological_assertions_cpp_detected(self):
        """Test detection of tautological assertions in C++."""
        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)

        bad_test = tests_dir / "solver_test.cpp"
        bad_test.write_text(
            """
#include <gtest/gtest.h>
TEST(SolverTest, Converges) {
    int iterations = 10;
    EXPECT_EQ(iterations, iterations);
}
"""
        )

        passed, issues = audit_test_theatre(self.root)
        self.assertFalse(passed)
        self.assertTrue(
            any("tautological" in issue.lower() and "iterations" in issue for issue in issues),
            f"Expected tautological assertion detection in issues: {issues}"
        )

    def test_clean_polyglot_test_suite_passes(self):
        """Test that a healthy polyglot suite with state assertions and integration harness passes."""
        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)

        # C#
        (tests_dir / "ServiceTests.cs").write_text(
            """
using Xunit;
public class ServiceTests {
    [Fact]
    public void TestCalc() {
        var res = 2 + 2;
        Assert.Equal(4, res);
        Assert.True(res > 0);
    }
}
"""
        )
        # C# WebApplicationFactory integration harness
        (tests_dir / "WebIntegrationTests.cs").write_text(
            """
using Microsoft.AspNetCore.Mvc.Testing;
public class ApiFactory : WebApplicationFactory<Program> {}
"""
        )

        # Python
        (tests_dir / "test_calc.py").write_text(
            """
def test_addition():
    val = 10 + 20
    assert val == 30
    assert val > 0
"""
        )

        # TypeScript
        (tests_dir / "component.test.tsx").write_text(
            """
import { test, expect } from 'vitest';
test('renders element', () => {
    const text = "hello";
    expect(text).toBe("hello");
    expect(text).toHaveLength(5);
});
"""
        )

        # C++
        (tests_dir / "algo_test.cpp").write_text(
            """
#include <gtest/gtest.h>
TEST(AlgoTest, Solves) {
    int ans = 42;
    EXPECT_EQ(42, ans);
    EXPECT_GT(ans, 0);
}
"""
        )

        passed, issues = audit_test_theatre(self.root)
        self.assertTrue(passed, f"Expected clean suite to pass, but got: {issues}")
        self.assertEqual(len(issues), 0)

    def test_cli_audit_tests_success(self):
        """Test CLI execution with --audit-tests passes with exit code 0 on clean repo."""
        import subprocess

        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)
        (tests_dir / "test_example.py").write_text(
            """
def test_ok():
    val = 1 + 1
    assert val == 2
"""
        )

        script_path = Path(__file__).parent / "verify_release.py"
        res = subprocess.run(
            [sys.executable, str(script_path), "--audit-tests", "--root", str(self.root)],
            capture_output=True,
            text=True
        )
        self.assertEqual(res.returncode, 0, f"Expected 0 exit code, got {res.returncode}. Output:\n{res.stdout}\n{res.stderr}")
        self.assertIn("All test suites passed anti-theatre audit", res.stdout)

    def test_cli_audit_tests_failure(self):
        """Test CLI execution with --audit-tests fails with exit code 1 on test theatre violations."""
        import subprocess

        tests_dir = self.root / "tests"
        tests_dir.mkdir(parents=True)
        (tests_dir / "test_theatre.py").write_text(
            """
def test_tautology():
    x = 42
    assert x == x
"""
        )

        script_path = Path(__file__).parent / "verify_release.py"
        res = subprocess.run(
            [sys.executable, str(script_path), "--audit-tests", "--root", str(self.root)],
            capture_output=True,
            text=True
        )
        self.assertEqual(res.returncode, 1, f"Expected 1 exit code, got {res.returncode}. Output:\n{res.stdout}\n{res.stderr}")
        self.assertIn("Tautological assertion detected", res.stdout)


if __name__ == "__main__":
    unittest.main()
