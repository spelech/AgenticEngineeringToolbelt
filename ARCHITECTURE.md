# 🏛️ Architecture: AgenticEngineeringToolbelt

This document explains the organization, design principles, and consumption models of **AgenticEngineeringToolbelt**.

---

## 🏗️ System Overview & Consumption Topology

```mermaid
flowchart TD
    subgraph Toolbelt["AgenticEngineeringToolbelt Repository"]
        Archetypes["archetypes/<br>• 5 Polyglot profiles<br>• Controls, CLI, FastMCP, Vite UI, C++"]
        Standards["standards/<br>• ENGINEERING_STYLE_GUIDE.md<br>• TESTING_HARNESS_PATTERNS.md<br>• CI_CD_PIPELINES.md"]
        Skills[".agents/skills/<br>• engineering-archetype<br>• scaffold-project<br>• test-harness-builder"]
        Rules["rules/<br>• AGENTS.md (Universal)<br>• GEMINI.md (Antigravity)<br>• CLAUDE.md (Claude Code)"]
        Templates["templates/<br>• configs/<br>• docs/ (VitePress & ASD-STE100)<br>• workflows/ (4-stage CI/CD)<br>• scripts/"]
    end

    subgraph Clients["Consumers & Agentic Runtimes"]
        Antigravity["Antigravity / Gemini CLI (~/.gemini/skills/)"]
        Claude["Claude Code (~/.claude/skills/)"]
        Cursor["Cursor / OpenClaw (.cursorrules)"]
        Projects["Software Repositories (Git Submodule .toolbelt/)"]
    end

    Archetypes & Standards --> Skills & Rules
    Skills --> Antigravity & Claude
    Rules --> Projects & Cursor
    Standards --> Skill & Rules
    Templates --> Projects
```

---

## 🧩 Subsystem Breakdown

### 1. `archetypes/`
Curated polyglot engineering profiles codifying complete tech stacks, dependencies, and patterns:
- `fullstack-dotnet-react.md`: C# .NET 10 Minimal APIs/Controllers, Dapper + Stored Procs, SQLite WAL / MSSQL, React 19 + TypeScript + Zustand UI.
- `console-cli-dotnet.md`: C# .NET 10 Console & CLI utilities via `System.CommandLine` and Microsoft DI.
- `python-fastapi-mcp.md`: Python 3.12+ services, FastMCP tool servers, Pydantic v2 validation, and async I/O.
- `react-ts-vite-ui.md`: Standalone React 19 + TypeScript + Vite frontends, CSS Modules, and Playwright layout audits.
- `native-cpp-algorithms.md`: High-performance C++20/23 libraries, CMake/MSBuild, `vcpkg`, and C#/Python interop.

### 2. `standards/`
Canonical reference specifications for software design, testing, and delivery:
- `ENGINEERING_STYLE_GUIDE.md`: Master architectural guide covering traditional Git Flow, APIs First, ASD-STE100, VitePress, and polyglot conventions.
- `TESTING_HARNESS_PATTERNS.md`: Simulation and control harnesses treating software as observable dynamic systems, tiered testing cadence (Tier 1-3), and 6-part feedback envelopes.
- `CI_CD_PIPELINES.md`: 4-stage GitHub Actions quality gate specification (Integrity, Build & Test, Smoke, Analysis & Release).

### 3. `.agents/skills/`
Executable skill manifests compatible with agent skill registries (Antigravity, Claude Code, Cursor):
- `engineering-archetype/`: Instructs agents on architectural standards, prototyping, clarifying questions, and verification.
- `scaffold-project/`: Automates end-to-end scaffolding of projects with Git Flow, VitePress living docs, 4-stage CI/CD, and test harness baselines.
- `test-harness-builder/`: Generates high-volume stress loops, mock STDIO transports, diagnostic tap points, disturbance injection, Playwright UI drivers, and 6-part feedback envelopes.

### 4. `rules/`
Drop-in prompt rule files enforcing engineering discipline:
- `AGENTS.md`: Universal markdown rules for any repository root. Enforces Git Flow, APIs First, ASD-STE100, and harness patterns.
- `GEMINI.md`: Antigravity / Gemini specific context rules.
- `CLAUDE.md`: Claude Code context rules.

### 5. `templates/`
Generic configuration boilerplates, living documentation assets, workflows, and automation scripts:
- `configs/`: `Directory.Build.props`, `vite.config.ts`, `tsconfig.json`, `eslint.config.js`, `playwright.config.ts`, `vcpkg.json`, `pyproject.toml`.
- `docs/`: Starter `ARCHITECTURE.md` (with Mermaid templates), `REQUIREMENTS.md`, `CHANGELOG.md`, and VitePress configuration.
- `workflows/`: 4-stage `ci.yml`, `codeql.yml`, and `release.yml`.
- `scripts/`: `commit.sh` (atomic build & version bump) and `verify_release.py` (markdown link & version auditor).

---

## 🔄 Traditional Git Flow & Release Model

```mermaid
gitGraph
    commit id: "v1.0.0"
    branch develop
    checkout develop
    commit id: "dev-start"
    branch feature/harness-engine
    checkout feature/harness-engine
    commit id: "feat: tap points"
    commit id: "feat: closed-loop simulation"
    checkout develop
    merge feature/harness-engine id: "PR #1 (Tier 2/3 pass)"
    branch release/v1.1.0
    checkout release/v1.1.0
    commit id: "chore(release): bump v1.1.0"
    checkout main
    merge release/v1.1.0 id: "tag: v1.1.0"
    checkout develop
    merge release/v1.1.0 id: "sync back"
```

- **`main`**: Production tagged releases only (`vX.Y.Z`). Never commit directly.
- **`develop`**: Integration branch for completed feature branches.
- **`feature/*`**: Feature development branches branched off `develop`.
- **`release/*`**: Stabilization and version bumping branches off `develop`, merging to `main` and `develop`.
- **`hotfix/*`**: Urgent production bugfixes branching off `main`, merging to both `main` and `develop`.

---

## 🧪 Simulation & Controls Testing Cadence

```mermaid
flowchart TD
    subgraph T1["Tier 1: Inner Loop (On Demand)"]
        Unit["Fast Unit Tests<br>In-memory, isolated domain logic assertions"]
    end
    subgraph T2["Tier 2: Stabilization Gate (Pre-Manual)"]
        Integ["Targeted Integration Tests<br>Boundary contracts & provider mocks"]
    end
    subgraph T3["Tier 3: Quality Gate (Pre-PR / Pre-Release / CI)"]
        Matrix["Pairwise & Multi-Provider Matrix"]
        Sim["Simulation Harnesses & Stress Loops"]
        E2E["Playwright Layout Inspector & E2E"]
        Smoke["Fullstack Smoke Gate"]
    end

    T1 -->|Interfaces Stabilize| T2
    T2 -->|Manual Verification Passes| T3
    Matrix --> Sim --> E2E --> Smoke
```

---

## 📐 Non-Functional Guarantees

1. **Zero External Runtime Dependencies**: The toolbelt consists of portable Markdown, YAML, Shell, Python, and JSON configuration files.
2. **Submodule Safety**: Does not contain hardcoded absolute filesystem paths; all references are relative or template placeholders.
3. **Multi-Agent Interoperability**: Formatted to be recognized natively by Antigravity, Claude Code, Cursor, Codex, and custom MCP router gateways.
4. **Living Documentation Integrity**: ASD-STE100 rules ensure technical clarity, and Mermaid diagrams provide visual architecture in sync with source code.

