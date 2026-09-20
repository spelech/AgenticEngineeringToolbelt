---
name: scaffold-project
description: Scaffolds a new project adhering to Steven T. Pelech's engineering archetypes (dotnet-fullstack, dotnet-cli, python-fastapi-mcp, react-ts-ui, cpp-algorithms) with living documentation, VitePress site, 4-stage CI/CD, and test harness baselines.
---

# 🚀 Project Scaffolding Skill (`scaffold-project`)

Use this skill when initializing a new repository or service stack.

---

## 📋 Available Archetypes

1. **`dotnet-fullstack`**: Fullstack (.NET + React + SQL) with Simulation & Control Harness (C# .NET 10, Dapper, Stored Procs, SQLite WAL, Zustand, Simulation Harness, Playwright Layout Inspector, Git Flow, 4-stage CI/CD).
2. **`dotnet-cli`**: C# .NET 10 Console Utility (`System.CommandLine`, full DI, Native AOT ready, `--json` stream, `-v` debug dumps, `--dry-run`).
3. **`python-fastapi-mcp`**: Python 3.12+ Service (**APIs First, MCP Later**: `uv`, typed FastAPI endpoints first, thin FastMCP tool wrappers second, Pydantic v2, SQLite `aiosqlite`, `pytest`).
4. **`react-ts-ui`**: Standalone Frontend (React + TS strict + Vite, Zustand stores, pure CSS Modules, `playwright-layout-inspector`).
5. **`cpp-algorithms`**: Native Systems Library (C++20/23, MSBuild/CMake, `vcpkg`, GoogleTest, ASan, Benchmark, C#/Python interop).

---

## ⚡ Execution Modes

### 1. Autonomous Defaults Mode (`--defaults`)
When `--defaults` is passed, the agent immediately generates the project using recommended defaults:
- Traditional Git Flow branching (`main`, `develop`).
- C# / .NET 10 / Modern `.slnx` solution format.
- SQLite WAL configured with MySQL-compatible types.
- Forward Auth + Bearer tokens for machine auth.
- VitePress living documentation site in `docs/` targeting GitHub Pages.
- 4-stage GitHub Actions CI/CD with `verify_release.py` and `commit.sh`.

### 2. Interactive Mode (Default)
When `--defaults` is not supplied, the agent prompts the user with clarifying questions, explicitly presenting the recommended defaults:
- **Project Name & Target Directory**
- **Archetype Selection** (Recommended default presented first)
- **Database Engine** (Recommended: SQLite WAL, with MSSQL/MySQL options)
- **Port Assignment** (if web service)
- **Living Documentation Engine** (Recommended: VitePress in `docs/` with GitHub Pages deployment)

---

## 📦 Scaffolding Steps Performed by Agent

1. **Create Solution & Project Files**:
   - Solution file (`.slnx`, `CMakeLists.txt`, or `pyproject.toml`).
   - Project dependencies and `Directory.Build.props`.
2. **Scaffold Directory Layout**:
   - `src/` (domain models, interfaces, services, controllers/endpoints, store slices).
   - `tests/` (Tier 1 unit tests + Tier 2 simulation test harness).
3. **Add Living Documentation (ASD-STE100 & VitePress)**:
   - `ARCHITECTURE.md` adhering to ASD-STE100 ($\le$ 20-25 words/sentence, active voice) with Mermaid top-down topology (`flowchart TD`) and sequence diagram (`sequenceDiagram autonumber`).
   - `README.md` with badges, architecture overview, and quickstart commands.
   - **VitePress Living Doc Site** under `docs/` (`docs/.vitepress/config.mts`, `docs/index.md`, `docs/guide/architecture.md`) configured for automatic GitHub Pages deployment.
4. **Add CI/CD & Release Automation**:
   - `.github/workflows/ci.yml` (4-stage gate mapped to Git Flow branch triggers).
   - `commit.sh` and `verify_release.py`.
5. **Add Agent Rules**:
   - Symlink or copy `.toolbelt/rules/AGENTS.md` into repository root.
6. **Verification & Build Smoke**:
   - Run compilation command (`dotnet build`, `pytest`, `npm test`, or `cmake --build`).
   - Verify zero errors and zero linter warnings.
