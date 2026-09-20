# 🏛️ Curated Engineering Archetypes

This directory contains battle-tested, standardized engineering archetypes that AI coding agents follow when scaffolding new projects, authoring code, or refactoring services.

---

## 📚 Available Archetypes

| Archetype | Primary Stack | Key Highlights | Link |
| :--- | :--- | :--- | :--- |
| **Fullstack Simulation & Control** | C# .NET 9 + React + SQL | Dapper, Stored Procs (SQL files), SQLite WAL / MSSQL, Zustand, Simulation & Control Harness, Playwright Layout Inspector, Git Flow, 4-Stage CI/CD. | [**View Archetype**](controls-fullstack-dotnet-react.md) |
| **C# Console & CLI** | C# .NET 9 | `System.CommandLine`, full DI, Native AOT ready, `--json` stream, `-v` debug dumps, `--dry-run`. | [**View Archetype**](console-cli-dotnet.md) |
| **Python FastAPI & MCP** | Python 3.12+ | **APIs First, MCP Later**: `uv`, typed FastAPI REST endpoints first, thin FastMCP tool wrappers second, Pydantic v2 schemas, `aiosqlite`, `pytest`. | [**View Archetype**](python-fastapi-mcp.md) |
| **React + TS + Vite UI** | React / TypeScript / Vite | Zustand domain stores, pure CSS Modules + custom properties, zero heavy UI bloat, 4-point layout audit. | [**View Archetype**](react-ts-vite-ui.md) |
| **Modern C++ Native** | C++20/23 | MSBuild / CMake, `vcpkg`, strict RAII, GoogleTest, ASan/UBSan, Benchmark, C# / Python interop. | [**View Archetype**](native-cpp-algorithms.md) |

---

## 🚀 How Agents Use These Archetypes

1. **Git Flow Discipline**: Always work on isolated `feature/*` branches off `develop`, creating atomic Conventional Commits.
2. **Scaffolding**: Call the `scaffold-project` skill with `--archetype <name>` to instantiate a complete, compilable baseline.
3. **APIs First**: Implement and test core domain logic and typed APIs before exposing MCP adapter tools.
4. **Implementation Discipline**: Adhere to persistence, state management, and file size limits ($\le$ 500 LOC) specified in the archetype.
5. **Tiered Verification**: Execute Tier 1 unit tests during development, Tier 2 simulation harnesses and layout audits before manual verification, and Tier 3 gates before opening PRs.
