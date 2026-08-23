# 🛠️ AgenticEngineeringToolbelt

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-spelech%2FAgenticEngineeringToolbelt-black.svg)](https://github.com/spelech/AgenticEngineeringToolbelt)

> **Standardized architecture guidelines, controls-grade test harnesses, living documentation blueprints, and AI agent skills for high-velocity software engineering.**

`AgenticEngineeringToolbelt` codifies Steven T. Pelech's software engineering archetype, design-first workflows, and quality guardrails. It can be directly referenced by AI coding agents (Antigravity, Claude Code, Cursor, OpenClaw, Codex, etc.), linked into an IDE/CLI agent path, or embedded as a git submodule in any target repository.

---

## 🏛️ The 12 Core Tenets & Engineering Standards

```mermaid
flowchart TD
    subgraph Workflow["Workflow & Collaboration"]
        T1["1. Proactive Agent Questioning & Iterative Design"]
        T5["5. Fresh Branch & PR Discipline"]
        T6["6. Atomic, Legible Commits"]
        T12["12. Automated Docs, Commits & Releases"]
    end

    subgraph Stack["Tech Stack & Architecture"]
        T8["8. SOLID & DRY (No One-Offs, Extensible Modules)"]
        T2_stack["2. Modern .NET (C#) & React/TS/Zustand/Vite"]
        T2_db["2. Relational SQL & Stored Procedures (Dapper > Heavy ORMs)"]
        T2_api["2. Flexible Controllers & Minimal APIs"]
        T9["9. MCP-First API Integration"]
        T10["10. Default Encryption & Authentication"]
        T11["11. LiteLLM / OpenAI SDK Standard"]
    end

    subgraph Testing["Controls Testing & Guardrails"]
        T2_controls["2. Controls, Modeling & Simulation Mindset"]
        T4["4. Closed-Loop Test Feedback & Guardrails"]
        T7["7. >80% Code Coverage Target"]
        T3["3. Narrative Requirements (REQ-xxx only with ADRs)"]
    end

    Workflow --> Stack --> Testing
```

1. **Division of Labor & Proactive Questioning**: Steven drives the conceptual vision, architecture, and feature ideas. Because ideas start in his head and evolve, **part of the agent's primary job is to ask insightful clarifying questions** to flesh out requirements and edge cases. We design iteratively—prototyping early, learning from live behavior, and refining.
2. **Controls, Modeling & Simulation Mindset**: Rooted in a controls engineering and simulation background: systems gravitate towards rich test harnesses, simulated environments (mock transports like `mock_stdio.js`, SSE emulators), loopback tests, and dedicated debug tooling.
3. **Requirements & Architecture Decision Records (ADRs)**: Requirements use clear narrative acceptance criteria by default. Formal `REQ-xxx` prefixes are reserved for projects where formal ADR (Architecture Decision Record) catalogs are explicitly used.
4. **Guardrails & Closed-Loop Testing**: Establish tight guardrails via requirements, design plans, and test harnesses with **closed-loop feedback** (executing against running processes and using output metrics to iteratively improve performance, accuracy, and UI stability).
5. **Fresh Branch & PR Workflow**: All new features and plans start on a **fresh feature branch** off `develop` (or `main`/`master`). Features culminate in a **Pull Request (PR)** where all multi-stage CI gates must pass before merging.
6. **Atomic Commits**: Create fine-grained, **atomic commits** on the branch with clear messages so history is traceable and progress can be reviewed step-by-step.
7. **High Code Coverage**: Target **>80% code coverage** with meaningful unit, integration, and E2E test suites.
8. **SOLID & DRY Modularity**: Heavy emphasis on SOLID principles, small and focused files, and breaking apart multi-concern components. Avoid copy-paste and one-offs—design modules to be reusable, pluggable, and extensible.
9. **MCP Server First**: If a service exposes an API, the architecture should explicitly consider exposing a **Model Context Protocol (MCP) server** for AI agent integration.
10. **Security & Encryption by Default**: Encrypt sensitive data at rest and in transit (AES-256-GCM, DPAPI, SQLCipher, Vault) and apply authentication/authorization unless explicitly deemed unnecessary.
11. **LLM Integration Standard**: When implementing LLM features, standardize on **LiteLLM / OpenAI SDK** compatibility (for unified completions, streaming, embeddings, tool calling, and model routing).
12. **Automated Documentation & Releases**: Automate documentation generation (catalogs, schemas, API docs), automated version bumping (`bump_version.py`, `commit.sh`), and release pipelines (`verify_release.py`, GitHub Actions) wherever possible. Living `ARCHITECTURE.md` with Mermaid sequence and flow diagrams.

---

## 📂 Repository Structure

```text
AgenticEngineeringToolbelt/
├── .agents/
│   └── skills/
│       └── engineering-archetype/     # Standalone agent skill definition
│           └── SKILL.md
├── rules/                             # System instructions & agent rules
│   ├── AGENTS.md                      # Universal rule file for repositories
│   ├── GEMINI.md                      # Rule file for Antigravity / Gemini agents
│   └── CLAUDE.md                      # Rule file for Claude Code agents
├── standards/                         # In-depth architectural standards
│   ├── ENGINEERING_STYLE_GUIDE.md     # Master Style Guide & Architecture Archetype
│   ├── TESTING_HARNESS_PATTERNS.md    # Controls & closed-loop testing guide
│   └── CI_CD_PIPELINES.md             # 4-stage GitHub Actions CI/CD blueprint
├── templates/                         # Generic setup configurations & boilerplates
│   ├── configs/                       # Directory.Build.props, vite, tsconfig, eslint, playwright
│   ├── docs/                          # ARCHITECTURE.md, REQUIREMENTS.md, CHANGELOG.md
│   ├── workflows/                     # ci.yml (4-stage gate), codeql.yml, release.yml
│   └── scripts/                       # commit.sh (atomic build & bump), verify_release.py
└── scripts/
    └── install.sh                     # Symlink / setup helper for agent environments
```

---

## 🚀 How to Use & Integrate

### 1. As a Git Submodule in a Target Repository
To embed these standards and templates directly into any project:
```bash
git submodule add https://github.com/spelech/AgenticEngineeringToolbelt.git .toolbelt
git submodule update --init --recursive
```
Then create a symlink or include the rule:
```bash
ln -sf .toolbelt/rules/AGENTS.md AGENTS.md
```

### 2. Adding to AI Agent Environments (Antigravity, Claude Code, Cursor)
Run the built-in install script to symlink the skill and rules into your local agent directories:
```bash
./scripts/install.sh
```

Or manually copy or symlink the skill to your agent skills folder:
```bash
# Antigravity / Gemini CLI:
mkdir -p ~/.gemini/antigravity-cli/skills/
ln -sf $(pwd)/.agents/skills/engineering-archetype ~/.gemini/antigravity-cli/skills/engineering-archetype

# Claude Code:
mkdir -p ~/.claude/skills/
ln -sf $(pwd)/.agents/skills/engineering-archetype ~/.claude/skills/engineering-archetype
```

### 3. Prompt / Instruction Reference
Include this snippet in your system prompt or custom instructions:
> *"Always adhere to Steven T. Pelech's engineering archetype codified in [AgenticEngineeringToolbelt](https://github.com/spelech/AgenticEngineeringToolbelt): ask proactive clarifying questions during design, use modern .NET/C# with Dapper and Stored Procedures over heavy ORMs, React + TypeScript + Zustand + Vite, controls-grade test harnesses (>80% coverage with closed-loop feedback), and 4-stage GitHub Actions CI gates on fresh feature branches."*

---

## 📄 License

MIT © [Steven T. Pelech](LICENSE)
