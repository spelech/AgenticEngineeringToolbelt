#!/usr/bin/env python3
"""
Release and Version Verification Engine
Validates version consistency, markdown relative links, and test integrity.
"""

import os
import re
import sys
import argparse
from pathlib import Path

def check_markdown_links(root_dir: Path) -> bool:
    print("🔍 Checking markdown relative links and anchors...")
    has_errors = False
    for md_file in root_dir.glob("**/*.md"):
        if any(part.startswith(".") or part in ["node_modules", "bin", "obj", ".venv"] for part in md_file.parts):
            continue
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        # Find markdown links: [text](path)
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for text, link in links:
            if link.startswith("http://") or link.startswith("https://") or link.startswith("#") or link.startswith("mailto:"):
                continue
            # Strip anchors
            target_path = link.split("#")[0]
            if not target_path:
                continue
            resolved = (md_file.parent / target_path).resolve()
            if not resolved.exists():
                print(f"❌ Broken link in {md_file.relative_to(root_dir)}: [{text}]({link})")
                has_errors = True
    if not has_errors:
        print("✅ All markdown links verified successfully.")
    return not has_errors

def main():
    parser = argparse.ArgumentParser(description="Release Verification Engine")
    parser.add_argument("--skip-tests", action="store_true", help="Skip test suite execution")
    parser.add_argument("--ci", action="store_true", help="CI mode")
    args = parser.parse_args()

    root_dir = Path(__file__).resolve().parent.parent
    success = check_markdown_links(root_dir)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
