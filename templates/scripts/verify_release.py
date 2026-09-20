#!/usr/bin/env python3
"""
Release and Version Verification Engine
Validates SemVer formats, changelog headers, manifest synchronizations,
and markdown relative links across the repository.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple

# Ensure UTF-8 output encoding across Windows and POSIX environments
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
        sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    except Exception:
        pass

SEMVER_REGEX = re.compile(
    r"^v?(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)

EXCLUDED_DIRS = {
    ".git", ".github", ".gemini", ".vscode", ".venv", "node_modules",
    "bin", "obj", "TestResults", "coverage", "dist", ".system_generated"
}

def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS or (part.startswith(".") and part != ".") for part in path.parts)

def is_valid_semver(version: str) -> bool:
    return bool(SEMVER_REGEX.match(version.strip()))

def normalize_semver(version: str) -> str:
    v = version.strip()
    return v[1:] if v.startswith("v") else v

def get_current_git_context() -> Tuple[Optional[str], Optional[str]]:
    branch = None
    tag = None
    try:
        res = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, check=False
        )
        if res.returncode == 0:
            b = res.stdout.strip()
            if b and b != "HEAD":
                branch = b
    except Exception:
        pass

    try:
        res = subprocess.run(
            ["git", "describe", "--tags", "--exact-match"],
            capture_output=True, text=True, check=False
        )
        if res.returncode == 0:
            t = res.stdout.strip()
            if t:
                tag = t
    except Exception:
        pass

    return branch, tag

def check_semver_format(target_version: Optional[str]) -> bool:
    print("🔍 Validating Semantic Versioning (SemVer) format...")
    if not target_version:
        branch, tag = get_current_git_context()
        if tag:
            target_version = tag
        elif branch and (branch.startswith("release/v") or branch.startswith("hotfix/v")):
            target_version = branch.split("/v", 1)[1]

    if target_version:
        if not is_valid_semver(target_version):
            print(f"❌ Error: Target version '{target_version}' violates SemVer 2.0.0 specification.")
            return False
        print(f"✅ SemVer format validated: {target_version}")
    else:
        print("ℹ️ No target version specified via argument, tag, or release branch. Format check skipped.")
    return True

def check_changelog_headers(root_dir: Path, target_version: Optional[str] = None) -> bool:
    print("🔍 Auditing CHANGELOG.md headers and SemVer compliance...")
    changelogs = [
        f for f in root_dir.rglob("*.md")
        if not is_excluded(f) and f.name.lower() == "changelog.md"
    ]

    if not changelogs:
        print("ℹ️ No CHANGELOG.md found. Skipping changelog audit.")
        return True

    all_valid = True
    header_pattern = re.compile(r"^##\s+\[?([^\]\r\n]+)\]?(?:\s+-\s+(\d{4}-\d{2}-\d{2}))?", re.MULTILINE)

    for changelog in changelogs:
        content = changelog.read_text(encoding="utf-8", errors="ignore")
        headers = header_pattern.findall(content)

        if not headers:
            print(f"⚠️ Warning: {changelog.relative_to(root_dir)} has no level-2 release headers (e.g. '## [1.0.0]').")
            continue

        versions_found: List[str] = []
        for version_str, date_str in headers:
            version_clean = version_str.strip()
            if version_clean.lower() == "unreleased":
                continue
            if not is_valid_semver(version_clean):
                print(f"❌ Invalid SemVer header in {changelog.relative_to(root_dir)}: '## [{version_str}]'")
                all_valid = False
            else:
                versions_found.append(normalize_semver(version_clean))

        if target_version:
            norm_target = normalize_semver(target_version)
            if norm_target not in versions_found:
                print(f"❌ Target version '{target_version}' not recorded in {changelog.relative_to(root_dir)}.")
                all_valid = False
            else:
                print(f"✅ Found target version '{norm_target}' in {changelog.relative_to(root_dir)}.")

    if all_valid:
        print("✅ All changelog headers verified successfully.")
    return all_valid

def is_template_dir(path: Path) -> bool:
    return "templates" in path.parts and ("configs" in path.parts or "docs" in path.parts)

def check_manifest_versions(root_dir: Path, target_version: Optional[str] = None) -> bool:
    print("🔍 Auditing project manifests for version synchronization...")
    found_versions: List[Tuple[Path, str]] = []

    # package.json
    for pkg_json in root_dir.rglob("package.json"):
        if is_excluded(pkg_json) or is_template_dir(pkg_json):
            continue
        try:
            data = json.loads(pkg_json.read_text(encoding="utf-8"))
            if "version" in data and is_valid_semver(data["version"]):
                found_versions.append((pkg_json, normalize_semver(data["version"])))
        except Exception:
            pass

    # Directory.Build.props / .csproj
    version_tag_regex = re.compile(r"<Version>([^<]+)</Version>")
    for csproj in list(root_dir.rglob("*.csproj")) + list(root_dir.rglob("Directory.Build.props")):
        if is_excluded(csproj) or is_template_dir(csproj):
            continue
        try:
            content = csproj.read_text(encoding="utf-8", errors="ignore")
            match = version_tag_regex.search(content)
            if match and is_valid_semver(match.group(1)):
                found_versions.append((csproj, normalize_semver(match.group(1))))
        except Exception:
            pass

    # pyproject.toml
    pyproject_regex = re.compile(r'version\s*=\s*"([^"]+)"')
    for pyproject in root_dir.rglob("pyproject.toml"):
        if is_excluded(pyproject) or is_template_dir(pyproject):
            continue
        try:
            content = pyproject.read_text(encoding="utf-8", errors="ignore")
            match = pyproject_regex.search(content)
            if match and is_valid_semver(match.group(1)):
                found_versions.append((pyproject, normalize_semver(match.group(1))))
        except Exception:
            pass

    if not found_versions:
        print("ℹ️ No versioned project manifests detected.")
        return True

    all_valid = True
    first_file, baseline_version = found_versions[0]

    for f_path, ver in found_versions:
        if not is_valid_semver(ver):
            print(f"❌ Invalid SemVer '{ver}' in {f_path.relative_to(root_dir)}")
            all_valid = False
        if target_version and ver != normalize_semver(target_version):
            print(f"❌ Version mismatch in {f_path.relative_to(root_dir)}: expected '{normalize_semver(target_version)}', got '{ver}'")
            all_valid = False
        elif not target_version and ver != baseline_version:
            print(f"❌ Manifest version drift between {first_file.relative_to(root_dir)} ({baseline_version}) and {f_path.relative_to(root_dir)} ({ver})")
            all_valid = False

    if all_valid:
        print(f"✅ All manifests synchronized ({len(found_versions)} manifest(s) checked).")
    return all_valid

def check_markdown_links(root_dir: Path) -> bool:
    print("🔍 Auditing markdown relative links and anchors...")
    has_errors = False
    md_files = [f for f in root_dir.rglob("*.md") if not is_excluded(f)]

    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        links = link_pattern.findall(content)
        for text, link in links:
            # Skip external protocols, anchor-only links, and special editor schemes
            if any(link.startswith(proto) for proto in ["http://", "https://", "mailto:", "#", "file:", "conversation:"]):
                continue

            target_path = link.split("#")[0].strip()
            if not target_path:
                continue

            resolved = (md_file.parent / target_path).resolve()
            if not resolved.exists():
                print(f"❌ Broken link in {md_file.relative_to(root_dir)}: [{text}]({link})")
                has_errors = True

    if not has_errors:
        print("✅ All markdown links verified successfully.")
    return not has_errors

def main() -> None:
    parser = argparse.ArgumentParser(description="Release Verification Engine")
    parser.add_argument("--root", type=Path, default=None, help="Root directory to audit")
    parser.add_argument("--version", type=str, default=None, help="Target release version to verify")
    parser.add_argument("--skip-tests", action="store_true", help="Skip test suite execution")
    parser.add_argument("--ci", action="store_true", help="CI execution mode")
    args = parser.parse_args()

    root_dir = args.root.resolve() if args.root else Path.cwd().resolve()
    target_version = args.version or os.environ.get("RELEASE_VERSION")

    print("=" * 60)
    print("🚀 Git Flow Release Verification Engine")
    print(f"📂 Auditing root: {root_dir}")
    if target_version:
        print(f"🎯 Target version: {target_version}")
    print("=" * 60)

    v1 = check_semver_format(target_version)
    v2 = check_changelog_headers(root_dir, target_version)
    v3 = check_manifest_versions(root_dir, target_version)
    v4 = check_markdown_links(root_dir)

    success = all([v1, v2, v3, v4])
    print("=" * 60)
    if success:
        print("✅ Release verification passed all quality gates.")
        sys.exit(0)
    else:
        print("❌ Release verification failed one or more quality gates.")
        sys.exit(1)

if __name__ == "__main__":
    main()
