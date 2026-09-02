# 🏛️ Curated Engineering Archetypes

This directory contains battle-tested, standardized engineering archetypes that AI coding agents follow when scaffolding new projects, authoring code, or refactoring services.

---

## 📚 Available Archetypes

| Archetype | Primary Stack | Key Highlights | Link |
| :--- | :--- | :--- | :--- |
| **Controls Fullstack** | C# .NET 9 + React + SQL | Dapper, Stored Procs (SQL files), SQLite WAL / MSSQL, Zustand, Playwright Layout Inspector, 4-Stage CI/CD. | [**View Archetype**](controls-fullstack-dotnet-react.md) |
| **C# Console & CLI** | C# .NET 9 | `System.CommandLine`, full DI, Native AOT ready, `--json` stream, `-v` debug dumps, `--dry-run`. | [**View Archetype**](console-cli-dotnet.md) |
| **Python FastAPI & MCP** | Python 3.12+ | `uv`, FastAPI, FastMCP (Streamable HTTP / SSE), Pydantic v2 settings, SQLite `aiosqlite`, `pytest`. | [**View Archetype**](python-fastapi-mcp.md) |
| **React + TS + Vite UI** | React / TypeScript / Vite | Zustand domain stores, pure CSS Modules + custom properties, zero heavy UI bloat, 4-point layout audit. | [**View Archetype**](react-ts-vite-ui.md) |
| **Modern C++ Native** | C++20/23 | MSBuild / CMake, `vcpkg`, strict RAII, GoogleTest, ASan/UBSan, Benchmark, C# / Python interop. | [**View Archetype**](native-cpp-algorithms.md) |

---

## 🚀 How Agents Use These Archetypes

1. **Scaffolding**: Call the `scaffold-project` skill with `--archetype <name>` to instantiate a complete, compilable baseline.
2. **Implementation**: Adhere to the persistence, state management, and file size limits ($\le$ 500 LOC) specified in the archetype.
3. **Verification**: Run the archetype's test harness, sanitizers, and layout inspection suite before submitting PRs.
