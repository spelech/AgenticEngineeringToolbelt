#!/usr/bin/env bash
set -e

# Toolbelt installer / symlinker script
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "🛠️ Installing AgenticEngineeringToolbelt into local agent directories..."

# 1. Antigravity / Gemini CLI
GEMINI_SKILLS_DIR="$HOME/.gemini/antigravity-cli/skills"
if [ -d "$HOME/.gemini/antigravity-cli" ]; then
    mkdir -p "$GEMINI_SKILLS_DIR"
    ln -sfn "$REPO_ROOT/.agents/skills/engineering-archetype" "$GEMINI_SKILLS_DIR/engineering-archetype"
    echo "✅ Linked skill to Antigravity: $GEMINI_SKILLS_DIR/engineering-archetype"
fi

# 2. Claude Code
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
if [ -d "$HOME/.claude" ]; then
    mkdir -p "$CLAUDE_SKILLS_DIR"
    ln -sfn "$REPO_ROOT/.agents/skills/engineering-archetype" "$CLAUDE_SKILLS_DIR/engineering-archetype"
    echo "✅ Linked skill to Claude Code: $CLAUDE_SKILLS_DIR/engineering-archetype"
fi

echo "✨ Installation complete! You can now invoke the 'engineering-archetype' skill in your AI agent sessions."
