# Curated Engineering Archetypes

This directory contains battle-tested, standardized engineering archetypes that AI coding agents follow when scaffolding new projects, authoring code, or refactoring services.

---

## Available Archetypes

| Archetype | Primary Stack | Key Highlights | Blueprint |
| :--- | :--- | :--- | :--- |
| **Fullstack Simulation & Control** | C# .NET 10 + React + SQL | Dapper, Stored Procedures (`.sql` files), SQLite WAL / MSSQL, Zustand, Simulation & Control Harness, Playwright Layout Inspector, Git Flow, 4-Stage CI/CD. | [**View Archetype**](fullstack-dotnet-react.md) |
| **C# Console & CLI** | C# .NET 10 | `System.CommandLine`, full DI, Native AOT ready, `--json` stream, `-v` debug dumps, `--dry-run`, subprocess harness. | [**View Archetype**](console-cli-dotnet.md) |
| **Python FastAPI & FastMCP** | Python 3.12+ | **APIs First, MCP Later**: `uv`, typed FastAPI REST endpoints first, thin FastMCP tool wrappers second, Pydantic v2 schemas, `aiosqlite`, `pytest`. | [**View Archetype**](python-fastapi-mcp.md) |
| **React, TypeScript & Vite UI** | React / TypeScript / Vite | Zustand domain stores, pure CSS Modules + custom properties, zero heavy UI bloat, 4-point layout audit. | [**View Archetype**](react-ts-vite-ui.md) |
| **Modern C++ Native Systems** | C++20/23 | MSBuild / CMake, `vcpkg`, strict RAII, GoogleTest boundary sweeps, ASan/UBSan, Benchmark, C# / Python interop. | [**View Archetype**](native-cpp-algorithms.md) |

---

## Agent Execution Workflow

### Project Scaffolding and Git Flow

1. **Git Flow Discipline**: Always work on isolated `feature/*` branches off `develop` and create atomic Conventional Commits (see [Traditional Git Flow Discipline](../standards/ENGINEERING_STYLE_GUIDE.md#traditional-git-flow-discipline)).
2. **Automated Scaffolding**: Invoke the [`scaffold-project` skill](../.agents/skills/scaffold-project/SKILL.md) with `--archetype <name>` to instantiate a compilable baseline.
3. **APIs First, MCP Later**: Implement and test core domain logic and typed APIs before exposing MCP adapter tools (see [APIs First, MCP Later](../standards/ENGINEERING_STYLE_GUIDE.md#apis-first-mcp-later)).

### Implementation and Verification Cadence

1. **Modularity Discipline**: Adhere to persistence, state management, and file size limits (**≤ 500 LOC**) specified in the [Master Engineering Style Guide](../standards/ENGINEERING_STYLE_GUIDE.md#solid-and-modularity).
2. **Tiered Verification**: Execute Tier 1 unit tests during development, Tier 2 simulation harnesses and layout audits before manual verification, and Tier 3 quality gates before opening Pull Requests (see [Tiered Testing Cadence](../standards/TESTING_HARNESS_PATTERNS.md#tiered-testing-cadence)).
