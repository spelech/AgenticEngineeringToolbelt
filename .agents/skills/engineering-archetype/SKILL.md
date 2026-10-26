---
name: engineering-archetype
description: Architectural guidelines and master engineering standards for Steven T. Pelech's engineering archetypes across C#, TypeScript, Python, and C++.
---

# Engineering Archetype and Master Guidelines

This skill equips agents to collaborate effectively with Steven T. Pelech across new project setups, feature development, test harness creation, and architectural refactoring.

---

## Division of Responsibility and Collaboration

### Human Architect and AI Agent Roles

- **Steven's Role**: System architecture, structural design, feature conceptualization, domain modeling, requirement specifications, stored procedure and data design, and Mermaid diagram designs.
- **Agent's Role**:
  - **Proactive Questioning**: Ask insightful clarifying questions to define requirements, edge cases, and design constraints as ideas evolve during design.
  - **Iterative Prototyping**: Build prototypes, run simulation harnesses with closed-loop feedback, and iterate based on empirical findings.

### Traditional Git Flow and Atomic Commits

- **`main`**: Production releases with immutable SemVer tags (`vX.Y.Z`).
- **`develop`**: Primary integration branch for verified feature work.
- **`release/*`**: Release stabilization branches branched from `develop` and merged into both `main` and `develop`.
- **`feature/*`**: Feature branches branched from `develop` and merged back into `develop` via Pull Request.
- **`hotfix/*`**: Emergency production fixes branched from `main` and merged into both `main` and `develop`.
- Create fine-grained Conventional Commits (`feat:`, `fix:`, `test:`, `docs:`) and open Pull Requests that pass all 4-stage CI quality gates before merging.

---

## Core Driving Principles and Code Discipline

### Architecture and Modularity Rules

1. **APIs First, MCP Later**:
   - Business logic, schemas, validation, and domain state transitions live in first-class, typed APIs (Minimal APIs, Controllers, FastAPI endpoints, or CLI commands).
   - All functionality must be independently testable via unit tests or HTTP clients.
   - Model Context Protocol (MCP) tools are implemented strictly as lightweight adapter wrappers around the underlying domain engine or internal APIs.
2. **SOLID and Modularity**:
   - Enforce single responsibility per class and module.
   - Decompose classes exceeding **500 lines of code (≤ 500 LOC)** into partial classes or distinct sub-services.
   - Build client-focused interfaces (`I*` in C#) even for single implementations to ensure testability and loose coupling.
3. **DRY vs. YAGNI and KISS**:
   - **Rule of Three**: Permit duplication across two instances; abstract on the **third occurrence**.
   - Do not invent speculative multi-tier frameworks or unused generic abstractions (YAGNI).
4. **Semantic Naming Standard**:
   - **Banned**: Never use `*Manager`, `*Helper`, `*Util`, or `*Data` junk-drawer names.
   - **Enforced**: Use role- and action-based names (`DatabaseSeederService`, `UserAuthenticator`, `OrderProcessor`, `ServerStatusCard`, `use*Store.ts`).

### Performance, Diagnostics, and Documentation

1. **Efficiency and Performance**:
   - **Database**: Consolidate operations requiring three or more round-trips into a single **Stored Procedure** or multi-result query.
   - **Frontend**: Mandate **granular Zustand selectors** (`useServerStore(s => s.servers.length)`) to prevent render cascades.
   - **API**: Provide focused HTTP endpoints for decoupled store and component lifecycles.
2. **Error Handling and Diagnostics**:
   - Never leak raw stack traces to API clients.
   - Log structured debug payloads containing the input arguments and state that triggered the error.
3. **Technical Writing and Living Documentation**:
   - Write all technical prose adhering to **ASD-STE100 (Simplified Technical English)** and the **Google Developer Documentation Style Guide**:
     - Keep sentences short and direct (**≤ 25 words per sentence**).
     - Use active voice and second-person imperative mood.
     - Organize dense topics into scannable `H2` and `H3` headings and scope cross-links to single-topic `#section` anchors.
     - Use clean Unicode symbols (`≥`, `≤`) instead of raw LaTeX math syntax in prose.
   - Pair prose with native Mermaid diagrams (`flowchart TD`, `sequenceDiagram autonumber`).
   - Scaffold living documentation using **VitePress** hosted on GitHub Pages.
4. **Anti-Test Theatre and Representative Verification**:
   - Automated tests must assert real system state mutations, never mock invocations.
   - Mock-heavy unit testing without authentic integration tests is strictly prohibited.
   - Adhere to the Four Pillars: Real Over Mock, Outcomes Over Calls, Representative Dogfooding, and Value Over Vanity.

---

## Polyglot Language Matrix

| Language | Primary Domains | Core Conventions and Libraries |
| :--- | :--- | :--- |
| **C# (.NET 10)** | High-perf systems, control planes, protocols, daemons, native UIs | `System.CommandLine`, full DI, `.slnx`, Dapper + Stored Proc `.sql` files, SQLite WAL / MSSQL, Native WPF/WinForms/Avalonia (no Electron), `ConcurrentDictionary`, `Channel<T>`, `SemaphoreSlim`, `Interlocked`, `CancellationToken` throughout.<br>**Testing**: `WebApplicationFactory` + SQLite WAL integration tests, CLI subprocess fixtures, strict ban on mock-heavy test theatre. |
| **Python (3.12+)** | Scrapers, data pipelines, vision, ML, automation | **APIs First, MCP Later**: `uv`, `pyproject.toml`, FastAPI endpoints first, FastMCP tool wrappers second, Pydantic v2 schemas, `asyncio`, `pytest` (≥ 80% coverage), `ruff`.<br>**Testing**: `httpx.AsyncClient` ASGI in-memory transport + SQLite, FastMCP `InMemorySessionClient`, ban on `unittest.mock` domain patching. |
| **TypeScript / React** | Web UIs, interactive dashboards, browser tools | React + strict TS + Vite, Zustand domain stores, pure CSS Modules + custom properties, bespoke components, `playwright-layout-inspector` 4-point audit.<br>**Testing**: Playwright E2E journey tests, 4-point layout audit, real Zustand store integration, ban on shallow mocked unit tests. |
| **C++ (C++20/23)** | Algorithms, geometry, native compute, low-level protocol engines | MSBuild (Win) / CMake (Linux), `vcpkg`, strict RAII, smart pointers, GoogleTest (`gtest`), ASan/UBSan, Google Benchmark, C# `[LibraryImport]` / Python `pybind11` interop.<br>**Testing**: GoogleTest `TEST_P` parameterized boundary sweeps, ASan/UBSan memory checks, ban on algorithmic mocks and happy-path-only tests. |

---

## Simulation and Control Testing Framework

Software operates as an **observable dynamic system** with closed-loop verification across three tiers.

### Anti-Test Theatre Principles and Deterministic Protocols

1. **The Four Pillars of Anti-Test Theatre**:
   - **Pillar 1: Real Over Mock**: Test software using real components and in-memory databases (SQLite WAL). Permit mocks only at external third-party network boundaries (such as Stripe). Never mock internal domain services.
   - **Pillar 2: Outcomes Over Calls**: Assert observable state mutations (database rows, generated files, API response payloads). Never use mock call verifications (`mock.Verify()`) as primary proof of success.
   - **Pillar 3: Representative Dogfooding**: Every feature requires a representative roundtrip (real HTTP pipeline request, real CLI subprocess execution, or Playwright E2E journey).
   - **Pillar 4: Value Over Vanity**: Prioritize boundary conditions (0-1-N), disturbances, and concurrency over shallow line coverage. Do not write tests for boilerplate POCOs, DTOs, or auto-properties.
2. **Deterministic Testing Protocols**:
   - **Test Budget Formula**: Compute required test suite size before authoring tests:
     `Test Budget = 1 (Nominal) + N_Branches + N_Boundaries (0-1-N) + N_Disturbances`
   - **Five-Question Mock Decision Tree**: Pass every collaborator through the 5-question tree. If the collaborator is internal, persistent storage, time, external HTTP, or child STDIO, apply the designated real or stubbed strategy. Otherwise, mocking is forbidden.

### Polyglot Testing Strategies

#### C# (.NET 10) Testing Strategy

- **Mandated Integration Harnesses**:
  - Web APIs: Execute full HTTP roundtrips via `WebApplicationFactory<Program>` against in-memory SQLite in WAL mode with real schema migrations and Dapper queries.
  - Console CLIs: Execute CLI commands via real subprocess invocation (`CliExecutionHarness`) in isolated temporary workspaces.
- **Banned Test Theatre**:
  - Mocking `IRepository<T>`, `DbContext`, or internal business services using Moq or NSubstitute.
  - Verifying mock invocation counts (`mock.Verify(x => x.Save(), Times.Once)`) instead of verifying mutated database records.
  - Instantiating controller classes directly with mocked dependencies.

#### Python (3.12+) Testing Strategy

- **Mandated Integration Harnesses**:
  - FastAPI: Execute full HTTP request-response cycles using `httpx.AsyncClient` with `ASGITransport(app=app)` and ephemeral SQLite databases.
  - FastMCP Tools: Execute MCP tools via `InMemorySessionClient` to verify live tool execution and structured output schemas.
- **Banned Test Theatre**:
  - Patching internal domain logic or service classes with `unittest.mock.patch`.
  - Asserting `mock.assert_called_with` instead of checking state deltas in the database or filesystem.

#### TypeScript and React Testing Strategy

- **Mandated Integration Harnesses**:
  - Web UIs: Execute realistic operator journeys using Playwright against live running frontend and backend applications.
  - Layout & Ergonomics: Enforce the 4-point `playwright-layout-inspector` audit (zero layout overflow, mobile viewport fit, touch targets ≥ 24px, layout score ≥ 85).
  - State Management: Test Zustand stores with real action dispatches and granular selector assertions.
- **Banned Test Theatre**:
  - Shallow component unit tests where child components and hooks are mocked to empty `<div>` elements.
  - Fragile DOM snapshot testing where developers blindly accept generated diffs.

#### C++ (C++20/23) Testing Strategy

- **Mandated Integration Harnesses**:
  - Numerical & Algorithms: Execute parameterized boundary sweeps using GoogleTest (`TEST_P`, `INSTANTIATE_TEST_SUITE_P`) across boundary spaces (`-1e5`, `-1.0`, `0.0`, `1.0`, `1e5`).
  - Memory & Safety: Execute test suites under AddressSanitizer (ASan) and UndefinedBehaviorSanitizer (UBSan).
- **Banned Test Theatre**:
  - Mocking internal mathematical algorithms, numerical convergence solvers, or hardware state machines.
  - Authoring happy-path-only tests that ignore boundary conditions or floating-point divergence.

### Tiered Testing Cadence

1. **Tier 1 (Inner Loop / Rapid Development)**: Run fast unit tests (xUnit, pytest, Vitest) on demand during active implementation.
2. **Tier 2 (Stabilization Gate / Pre-Manual Verification)**: Run simulation harnesses, diagnostic tap point checks, parameter sweeps, and Playwright layout audits before manual verification.
3. **Tier 3 (Pre-PR / Pre-Release / CI Quality Gate)**: Run the full regression suite, pairwise database matrices, live smoke tests, and multi-stage CI verification before merging.

### Controls and Simulation Mechanics

1. **Diagnostic Tap Points**: In-memory ring buffers (`DiagnosticTapRingBuffer`) and state getters allowing developers and AI agents to inspect internal state transitions.
2. **High-Volume Simulation and Parameter Sweeps**: High-throughput stress loops and parameter sweeps verifying convergence and stability.
3. **Disturbance Injection**: Malformed payloads, network disconnects, latency spikes, and cancellation storms verifying resilience and clean `CancellationToken` propagation.
4. **Frontend UI Harness**: `data-testid` attributes and Playwright drivers (`playwright-layout-inspector`) for automated UI layout and ergonomics audits.
5. **Agent Feedback Envelope**: Standardized 6-part failure schema (`inputs`, `assumptions`, `active_settings`, `action_history`, `output_delta`, `captured_logs`, and `reproduction_command`).
6. **Coverage**: Maintain **≥ 80% code coverage** across unit, integration, and end-to-end suites, excluding boilerplate POCOs and DTOs.

---

## Multi-Stage GitHub Actions CI/CD

1. **Gate 1: Release and Link Integrity**: `verify_release.py` verifying SemVer across manifests, relative markdown links and section anchors, and static anti-test-theatre rules.
2. **Gate 2: Parallel Builds and Tests**: Backend build + xUnit/pytest/gtest coverage (≥ 80%); Frontend ESLint (0 warnings) + Vitest.
3. **Gate 3: Fullstack Smoke Gate**: Live background process spawn + `/health` probe loop + live handshake.
4. **Gate 4: Security and Release**: CodeQL multi-language analysis + Docker container publish (`linux/amd64`) + VitePress GitHub Pages documentation deployment.
