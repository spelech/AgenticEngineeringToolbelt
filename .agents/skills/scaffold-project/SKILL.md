---
name: scaffold-project
description: Scaffolds a new project adhering to Steven T. Pelech's engineering archetypes (dotnet-fullstack, dotnet-cli, python-fastapi-mcp, react-ts-ui, cpp-algorithms) with living documentation, VitePress site, 4-stage CI/CD, and test harness baselines.
---

# Project Scaffolding Skill (`scaffold-project`)

Use this skill when initializing a new repository or service stack.

---

## Available Archetypes

1. **`dotnet-fullstack`**: Fullstack (.NET + React + SQL) with Simulation & Control Harness (C# .NET 10, Dapper, Stored Procedures, SQLite WAL, Zustand, Simulation Harness, Playwright Layout Inspector, Git Flow, 4-stage CI/CD).
2. **`dotnet-cli`**: C# .NET 10 Console Utility (`System.CommandLine`, full DI, Native AOT ready, `--json` stream, `-v` debug dumps, `--dry-run`).
3. **`python-fastapi-mcp`**: Python 3.12+ Service (**APIs First, MCP Later**: `uv`, typed FastAPI endpoints first, thin FastMCP tool wrappers second, Pydantic v2, SQLite `aiosqlite`, `pytest`).
4. **`react-ts-ui`**: Standalone Frontend (React + strict TS + Vite, Zustand stores, pure CSS Modules, `playwright-layout-inspector`).
5. **`cpp-algorithms`**: Native Systems Library (C++20/23, MSBuild/CMake, `vcpkg`, GoogleTest, ASan, Benchmark, C#/Python interop).

---

## Execution Modes

### Autonomous Defaults Mode (`--defaults`)

When `--defaults` is passed, generate the project immediately using recommended defaults:
- Traditional Git Flow branching (`main`, `develop`).
- C# / .NET 10 / Modern `.slnx` solution format.
- SQLite WAL configured with MySQL-compatible types.
- Forward Auth + Bearer tokens for machine authentication.
- VitePress living documentation site in `docs/` targeting GitHub Pages with left-rail and right-rail (`H2`/`H3`) navigation.
- Four-stage GitHub Actions CI/CD with `verify_release.py` and `commit.sh`.

### Interactive Mode (Default)

When `--defaults` is not supplied, prompt the user with clarifying questions and present the recommended defaults first:
- **Project Name and Target Directory**
- **Archetype Selection** (Recommended default presented first)
- **Database Engine** (Recommended: SQLite WAL, with MSSQL and MySQL options)
- **Port Assignment** (if web service)
- **Living Documentation Engine** (Recommended: VitePress in `docs/` with GitHub Pages deployment)

---

## Scaffolding Steps Performed by Agent

1. **Create Solution and Project Files**:
   - Solution file (`.slnx`, `CMakeLists.txt`, or `pyproject.toml`).
   - Project dependencies and `Directory.Build.props`.
2. **Scaffold Directory Layout**:
   - `src/` (domain models, interfaces, services, controllers/endpoints, store slices).
   - `tests/` (Tier 1 unit tests + Tier 2 simulation test harness).
3. **Add Living Documentation (VitePress)**:
   - `ARCHITECTURE.md` adhering to ASD-STE100 and Google Developer Documentation Style Guide rules (≤ 25 words per sentence, active voice, scannable `H2`/`H3` headings) with Mermaid top-down topology (`flowchart TD`) and sequence diagram (`sequenceDiagram autonumber`).
   - `README.md` with badges, architecture overview, and quickstart commands.
   - **VitePress Living Documentation Site** under `docs/` (`docs/.vitepress/config.mts`, `docs/index.md`, `docs/architecture.md`) configured for automatic GitHub Pages deployment.
4. **Add CI/CD and Release Automation**:
   - `.github/workflows/ci.yml` (4-stage gate mapped to Git Flow branch triggers).
   - `commit.sh` and `verify_release.py`.
5. **Add Agent Rules**:
   - Symlink or copy `.toolbelt/rules/AGENTS.md` into the repository root.
6. **Verification and Build Smoke**:
   - Run compilation and test commands (`dotnet build`, `pytest`, `npm test`, or `cmake --build`).
   - Verify zero errors and zero linter warnings.
