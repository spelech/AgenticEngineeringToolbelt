#!/usr/bin/env bash
set -e

# AgenticEngineeringToolbelt installer / symlinker script
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "🛠️ Installing AgenticEngineeringToolbelt skills into agent directories..."

SKILLS=("engineering-archetype" "scaffold-project" "test-harness-builder")

# 1. Antigravity / Gemini CLI
GEMINI_SKILLS_DIR="$HOME/.gemini/antigravity-cli/skills"
if [ -d "$HOME/.gemini/antigravity-cli" ]; then
    mkdir -p "$GEMINI_SKILLS_DIR"
    for skill in "${SKILLS[@]}"; do
        ln -sfn "$REPO_ROOT/.agents/skills/$skill" "$GEMINI_SKILLS_DIR/$skill"
        echo "✅ Linked $skill to Antigravity: $GEMINI_SKILLS_DIR/$skill"
    done
fi

# 2. Claude Code
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
if [ -d "$HOME/.claude" ]; then
    mkdir -p "$CLAUDE_SKILLS_DIR"
    for skill in "${SKILLS[@]}"; do
        ln -sfn "$REPO_ROOT/.agents/skills/$skill" "$CLAUDE_SKILLS_DIR/$skill"
        echo "✅ Linked $skill to Claude Code: $CLAUDE_SKILLS_DIR/$skill"
    done
fi

# 3. Workspace Shared .agents/skills (if on /containers)
WORKSPACE_SKILLS_DIR="/containers/.agents/skills"
if [ -d "/containers/.agents" ]; then
    mkdir -p "$WORKSPACE_SKILLS_DIR"
    for skill in "${SKILLS[@]}"; do
        ln -sfn "$REPO_ROOT/.agents/skills/$skill" "$WORKSPACE_SKILLS_DIR/$skill"
        echo "✅ Linked $skill to Workspace: $WORKSPACE_SKILLS_DIR/$skill"
    done
fi

echo "✨ Installation complete! All skills (engineering-archetype, scaffold-project, test-harness-builder) are active."
