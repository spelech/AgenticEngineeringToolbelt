---
title: "Agent Rules & Context Guidelines"
description: "Universal and runtime-specific markdown rules for autonomous coding agents."
---

# Agent Rules and Context Guidelines

The toolbelt provides standardized prompt rules, context manifests, and executable skills for multi-agent engineering workflows.

---

## Rule Manifests

| Manifest | Target Runtime | Primary Scope | Guide |
| :--- | :--- | :--- | :--- |
| **`AGENTS.md`** | Universal (All Agents & IDEs) | Git Flow, APIs First, SOLID modularity, polyglot matrix, and anti-test-theatre verification. | [Universal Agent Rules](/rules/agents) |
| **`CLAUDE.md`** | Claude Code | Runtime execution tenets, skill bindings, and deterministic verification links. | [Claude Code Rules](/rules/claude) |
| **`GEMINI.md`** | Google Antigravity & Gemini CLI | Tool orchestration, workspace discipline, and simulation harness requirements. | [Antigravity & Gemini Rules](/rules/gemini) |
| **`.agents/skills/`** | Antigravity, Claude Code, Cursor | Executable skills for project scaffolding, archetype enforcement, and harness generation. | [Toolbelt Skills Manifests](/rules/skills) |

---

## Runtime Integration Matrix

### Repository Root Integration

Link `AGENTS.md` into the root of any software repository that embeds the toolbelt as a submodule:

```bash
ln -sf .toolbelt/rules/AGENTS.md AGENTS.md
```

### Local Skill Registry Installation

Install the executable skills into your local agent directories (`~/.gemini/skills/`, `~/.claude/skills/`) by running:

```bash
bash .toolbelt/scripts/install.sh
```
