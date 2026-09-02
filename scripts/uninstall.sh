#!/usr/bin/env bash
set -e

# AgenticEngineeringToolbelt uninstaller / unlink script
echo "🧹 Unlinking AgenticEngineeringToolbelt skills from agent directories..."

SKILLS=("engineering-archetype" "scaffold-project" "test-harness-builder")

# 1. Antigravity / Gemini CLI
GEMINI_SKILLS_DIR="$HOME/.gemini/antigravity-cli/skills"
for skill in "${SKILLS[@]}"; do
    if [ -L "$GEMINI_SKILLS_DIR/$skill" ]; then
        rm "$GEMINI_SKILLS_DIR/$skill"
        echo "🗑️  Unlinked from Antigravity: $GEMINI_SKILLS_DIR/$skill"
    fi
done

# 2. Claude Code
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
for skill in "${SKILLS[@]}"; do
    if [ -L "$CLAUDE_SKILLS_DIR/$skill" ]; then
        rm "$CLAUDE_SKILLS_DIR/$skill"
        echo "🗑️  Unlinked from Claude Code: $CLAUDE_SKILLS_DIR/$skill"
    fi
done

# 3. Workspace Shared .agents/skills (if on /containers)
WORKSPACE_SKILLS_DIR="/containers/.agents/skills"
for skill in "${SKILLS[@]}"; do
    if [ -L "$WORKSPACE_SKILLS_DIR/$skill" ]; then
        rm "$WORKSPACE_SKILLS_DIR/$skill"
        echo "🗑️  Unlinked from Workspace: $WORKSPACE_SKILLS_DIR/$skill"
    fi
done

echo "✨ Unlink complete! All toolbelt symlinks have been removed."
