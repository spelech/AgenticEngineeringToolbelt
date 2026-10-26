---
name: code-review-foci
description: Execute a multi-lens code review across Steven T. Pelech's six engineering reviewer foci (Requirement Traceability, Architecture & Serialization, Anti-Test-Theatre, Security & Container Immutability, UI & Real Screenshots, and Living Docs & Release Sync) before opening or finalizing a pull request.
---

# Multi-Lens Code Review and Reviewer Foci

Use this skill to perform a thorough, read-only code review across six orthogonal reviewer foci before opening a Pull Request, merging a feature branch, or signing off on subagent task work.

---

## Review Preparation and Diff Scope

1. **Determine the Git Diff Range**:
   ```bash
   BASE_SHA=$(git merge-base HEAD origin/develop 2>/dev/null || git merge-base HEAD origin/main)
   HEAD_SHA=$(git rev-parse HEAD)
   git --no-pager diff --stat "$BASE_SHA..$HEAD_SHA"
   git --no-pager diff "$BASE_SHA..$HEAD_SHA"
   ```
2. **Read-Only Discipline**:
   - Do not mutate the working tree, staging index, or branch state during review.
   - Cite exact `file:line` references for every finding.

---

## The Six Reviewer Foci Checklist

Evaluate the diff against each focus independently (see [Code Review Foci and Operational Guardrails](../../../standards/CODE_REVIEW_AND_GUARDRAILS.md#multi-lens-code-review-and-the-six-reviewer-foci)):

### Focus 1: Requirement Traceability and Feature Preservation

- [ ] Every new or modified test carries a formal requirement annotation (`[Requirement("AUTH-01", ...)]` in C#, `@requirement` JSDoc in Vitest/Playwright, or `@pytest.mark.requirement` in Python) using the standard category codes (`AUTH`, `DB`, `GUARD`, `MCP`, `SEC`, `TRANS`, `UI`—never generic `REQ-` prefixes).
- [ ] `REQUIREMENTS.md` or the generated SRS catalog is updated in lockstep with zero drift.
- [ ] Existing features, endpoints, and configurations are preserved unless removal was explicitly requested.
- [ ] Replaced implementations are removed cleanly without leaving dead legacy shims.

### Focus 2: Architecture, Modularity, and Safe Serialization

- [ ] No file or class exceeds **500 lines of code** (`≤ 500` lines).
- [ ] Services expose client-focused interfaces (`I*` / `Protocol`) and use role-based semantic names (zero `*Manager`, `*Helper`, `*Util`, `*Data` junk drawers).
- [ ] **APIs First, MCP Later**: Business logic lives in typed domain services; MCP tools are thin wrapper adapters (`<serverId>__<toolName>`).
- [ ] **Safe Payload Manipulation**: JSON and JSON-RPC payloads are parsed and mutated via `JsonNode`/`JsonDocument` or Pydantic v2 models—never via `string.Replace` or regex splicing.

### Focus 3: Anti-Test-Theatre and Live-Executor Isolation

- [ ] Integration and persistence tests run against real SQLite WAL / in-memory databases and real in-process transports (`WebApplicationFactory`, `httpx.AsyncClient`, `InMemorySessionClient`), not mocked internal interfaces.
- [ ] Tests cover `0-1-N` boundaries, match the AST Test Budget (`1 Nominal + N_Branches + N_Boundaries + N_Disturbances`), and maintain `≥ 80%` coverage.
- [ ] Assertions verify state mutations and output deltas rather than mock `.Verify()` call counts.
- [ ] Automated test runs exclude live CLI/network executors (`pytest -m "not live"`), emit zero warnings (`eslint --max-warnings 0`, `ruff check`), and leave zero orphaned background processes.

### Focus 4: Security, Subprocess Safety, and Container Immutability

- [ ] CLI subprocess invocations pass sanitized argument arrays (`subprocess.run(["cmd", arg1], capture_output=True, timeout=...)`) and never use `shell=True`.
- [ ] `CancellationToken` or async timeouts propagate across 100% of I/O calls.
- [ ] Persisted secrets use AES-256-GCM encryption at rest; zero secrets or runtime databases (`*.db`, `*.key`, `.env`, `venv/`, `data/`) are tracked by Git.
- [ ] Containers are treated as immutable build artifacts (zero `docker cp` or live container file edits).

### Focus 5: UI Consistency, Layout Stability, and Real Screenshots

- [ ] Styles use centralized CSS variables (`variables.css` / `theme.css`) and prevent layout shifts (`scrollbar-gutter: stable`, `align-items: flex-start`).
- [ ] Zustand stores use granular selectors (`useStore(s => s.slice)`).
- [ ] Primary views and modals pass the 4-point `playwright-layout-inspector` audit (`toHaveNoLayoutOverflow`, `toHaveMobileFit`, `toHaveTouchFriendlyTargets({ minSize: 24 })`, `toPassLayoutAudit({ minScore: 85 })`).
- [ ] All documentation and UI PR screenshots are captured from the live running application via Playwright/Puppeteer (never AI-generated mockups).

### Focus 6: Living Documentation, Atomic Commits, and Release Sync

- [ ] `README.md`, `ARCHITECTURE.md`, and `docs/` are updated alongside code changes using ASD-STE100 and Google Developer Documentation Style Guide rules, native Mermaid diagrams, Unicode numeric symbols (`≥`, `≤`), and section-scoped `#anchor` links.
- [ ] Code changes synchronize version numbers across all manifests and `CHANGELOG.md` (while documentation-only changes skip version bumps and container rebuilds).
- [ ] `python3 templates/scripts/verify_release.py --ci` and `python3 templates/scripts/verify_release.py --audit-tests` pass locally, and GitHub Actions CI checks (`gh pr checks --watch`) are verified green before finalizing the PR.

---

## Structured Review Output Format

Report findings using this calibrated structure:

```markdown
## Code Review Report (`<BASE_SHA>..<HEAD_SHA>`)

### Strengths
- Cite specific well-structured components, real-transport test harnesses, or clean boundary separations (`file:line`).

### Findings by Severity

#### Critical (Must Fix Before PR / Merge)
- **[Focus N] `path/to/file.ext:line`**: Description of defect, security risk, or test-theatre violation and how to fix it.

#### Important (Should Fix Before Proceeding)
- **[Focus N] `path/to/file.ext:line`**: Description of architectural drift, missing boundary test, or documentation gap.

#### Minor (Polish)
- **[Focus N] `path/to/file.ext:line`**: Non-blocking readability or ergonomic improvement.

### Verdict
- **Ready to Merge / Finalize PR?**: `Yes` | `No` | `With Fixes`
```
