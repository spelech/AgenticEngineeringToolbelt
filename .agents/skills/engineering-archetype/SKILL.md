---
name: engineering-archetype
description: Architectural guidelines and master engineering standards for Steven T. Pelech's engineering archetypes across C#, TypeScript, Python, and C++.
---

# Engineering Archetype & Master Guidelines

This skill equips agents to collaborate effectively with Steven T. Pelech across new project setups, feature development, test harness creation, and architectural refactoring.

---

## 🤝 1. Division of Responsibility & Collaboration

- **Steven's Role**: System architecture, structural design, feature conceptualization, domain modeling, requirement specifications, stored procedure/data design, and Mermaid diagram designs.
- **Agent's Role**:
  - **Proactive Questioning**: Ask insightful clarifying questions to flesh out requirements, edge cases, and design constraints since Steven's ideas evolve during design.
  - **Iterative Prototyping**: Build prototypes, run simulation harnesses with closed-loop feedback, and iterate based on empirical findings.
  - **Traditional Git Flow Discipline**:
    - `main`: Production releases with immutable SemVer tags (`vX.Y.Z`).
    - `develop`: Primary integration branch for verified feature work.
    - `release/*`: Release stabilization branches branched from `develop`, merged into both `main` and `develop`.
    - `feature/*`: Feature branches branched from `develop`, merged back into `develop` via PR.
    - `hotfix/*`: Emergency production fixes branched from `main`, merged into both `main` and `develop`.
  - **Atomic Commits & PRs**: Create fine-grained Conventional Commits (`feat:`, `fix:`, `test:`, `docs:`) and open PRs that pass all 4-stage CI quality gates before merging.

---

## 🏛️ 2. Core Driving Principles & Code Discipline

1. **APIs First, MCP Later**:
   - Business logic, schemas, validation, and domain state transitions live in first-class, typed APIs (Minimal APIs, Controllers, FastAPI endpoints, or CLI commands).
   - All functionality must be independently testable via unit tests or HTTP clients.
   - MCP (Model Context Protocol) tools are implemented strictly as lightweight adapter wrappers around the underlying domain engine or internal APIs.
2. **SOLID & Modularity**:
   - Strict single responsibility per class/module.
   - Decompose classes exceeding **500 lines of code** into partial classes or distinct sub-services.
   - Build client-focused interfaces (`I*` in C#) even for single implementations to ensure 100% testability, substitutability, and loose coupling.
3. **DRY vs. YAGNI & KISS**:
   - **Rule of Three**: Duplication is acceptable across 2 instances; abstract on the **3rd occurrence**.
   - Do not invent speculative multi-tier frameworks or unused generic abstractions (YAGNI).
4. **Semantic Naming Standard**:
   - **Banned**: `*Manager`, `*Helper`, `*Util`, `*Data` junk drawers.
   - **Enforced**: Role/action-based names (`DatabaseSeederService`, `UserAuthenticator`, `OrderProcessor`, `ServerStatusCard`, `use*Store.ts`).
5. **Efficiency & Performance**:
   - **Database**: Consolidate into a single **Stored Procedure** or multi-result query rather than making 3+ database round-trips.
   - **Frontend**: Mandatory **granular Zustand selectors** (`useServerStore(s => s.servers.length)`) to prevent render cascades.
   - **API**: Provide focused individual HTTP endpoints for decoupled store/component lifecycles.
6. **Error Handling & Diagnostics**:
   - Never leak raw stack traces to API clients.
   - Log rich debug payloads containing the input arguments and state that triggered the error to enable deterministic reproduction.
7. **Living Documentation & ASD-STE100**:
   - All technical prose must adhere to **ASD-STE100 (Simplified Technical English)** principles:
     - Sentences limited to $\le$ 20-25 words.
     - Active voice only ("The engine validates..." instead of "Validation is performed by...").
     - Unambiguous terminology with consistent nomenclature throughout.
   - Pair prose with visual Mermaid diagrams (`flowchart TD`, `sequenceDiagram autonumber`).
   - Scaffold living documentation using **VitePress** hosted on GitHub Pages.
8. **Anti-Test Theatre & Representative Verification**:
   - Automated tests must assert real system state mutations, never mock invocations.
   - Mock-heavy unit testing without authentic integration tests is strictly prohibited.
   - Adhere to the Four Pillars: Real Over Mock, Outcomes Over Calls, Representative Dogfooding, and Value Over Vanity.

---

## 💻 3. Polyglot Language Matrix

| Language | Primary Domains | Core Conventions & Libraries |
| :--- | :--- | :--- |
| **C# (.NET 10)** | High-perf systems, control planes, protocols, daemons, native UIs | `System.CommandLine`, full DI, `.slnx`, Dapper + Stored Proc `.sql` files, SQLite WAL (MySQL-like) / MSSQL, Native WPF/WinForms/Avalonia (no Electron), `ConcurrentDictionary`, `Channel<T>`, `SemaphoreSlim`, `Interlocked`, `CancellationToken` throughout.<br>**Testing**: `WebApplicationFactory` + SQLite WAL integration tests, CLI subprocess fixtures, strict ban on Moq/mock-heavy test theatre. |
| **Python (3.12+)** | Scrapers, data pipelines, vision, ML, automation | **APIs First, MCP Later**: `uv`, `pyproject.toml`, FastAPI endpoints first, FastMCP tool wrappers second, Pydantic v2 schemas, `asyncio`, `pytest` ($\ge$ 80% coverage), `ruff`.<br>**Testing**: `httpx.AsyncClient` ASGI in-memory transport + SQLite, FastMCP `InMemorySessionClient`, ban on `unittest.mock` domain patching. |
| **TypeScript / React** | Web UIs, interactive dashboards, browser tools | React + TS strict + Vite, Zustand domain stores, pure CSS Modules + custom properties, bespoke components, `playwright-layout-inspector` 4-point audit.<br>**Testing**: Playwright E2E journey tests, 4-point layout audit, real Zustand store integration, ban on shallow mocked unit tests. |
| **C++ (C++20/23)** | Algorithms, geometry, native compute, low-level protocol engines | MSBuild (Win) / CMake (Linux), `vcpkg`, strict RAII, smart pointers, GoogleTest (`gtest`), ASan/UBSan, Google Benchmark, C# `[LibraryImport]` / Python `pybind11` interop.<br>**Testing**: GoogleTest `TEST_P` parameterized boundary sweeps, ASan/UBSan memory checks, ban on algorithmic mocks and happy-path-only tests. |

---

## 🧪 4. Simulation & Control Testing Framework (Tiered Cadence)

Software operates as an **observable dynamic system** with closed-loop verification across three tiers.

### 4.1 Anti-Test Theatre Principles & Deterministic Protocols
Agents and developers must never write test theatre. Tests must verify real system behavior, not mock invocations.

1. **The Four Pillars of Anti-Test Theatre**:
   - **Pillar 1: Real Over Mock**: Test software using real components and in-memory databases (SQLite WAL). Mocks are permitted only at external third-party network boundaries (e.g., Stripe). Never mock internal domain services.
   - **Pillar 2: Outcomes Over Calls**: Assert observable state mutations (database rows, generated files, API response payloads). Never use mock call verifications (`mock.Verify()`) as primary proof of success.
   - **Pillar 3: Representative Dogfooding**: Every feature requires a representative roundtrip (real HTTP pipeline request, real CLI subprocess execution, or Playwright E2E journey).
   - **Pillar 4: Value Over Vanity**: Prioritize boundary conditions (0-1-N), disturbances, and concurrency over shallow line coverage. Do not write tests for boilerplate POCOs, DTOs, or auto-properties.

2. **Deterministic Testing Protocols**:
   - **Test Budget Formula**: Compute required test suite size before authoring tests:
     $$\text{Test Budget} = \text{Nominal (1)} + N_{\text{Branches}} + N_{\text{0-1-N Boundaries}} + N_{\text{Disturbances}}$$
   - **5-Question Mock Decision Tree**: Pass every collaborator through the 5-question tree. If the collaborator is internal, persistent storage, time, external HTTP, or child STDIO, apply the designated real or stubbed strategy. Otherwise, mocking is forbidden.

### 4.2 Polyglot Testing Strategies (Mandated vs. Banned)

Every language archetype enforces explicit representative integration harnesses and bans mock-heavy unit test theatre:

#### C# (.NET 10) Testing Strategy
- **Mandated Integration Harnesses**:
  - Web APIs: Execute full HTTP roundtrips via `WebApplicationFactory<Program>` against in-memory SQLite in WAL mode with real schema migrations and Dapper queries.
  - Console CLIs: Execute CLI commands via real subprocess invocation (`CliExecutionHarness`) in isolated temporary workspaces. Assert exit codes, stdout, stderr, and file outputs.
- **Banned Test Theatre**:
  - Mocking `IRepository<T>`, `DbContext`, or internal business services using Moq or NSubstitute.
  - Verifying mock invocation counts (`mock.Verify(x => x.Save(), Times.Once)`) instead of verifying mutated database records.
  - Instantiating controller classes directly with mocked dependencies and calling action methods as plain functions.

#### Python (3.12+) Testing Strategy
- **Mandated Integration Harnesses**:
  - FastAPI: Execute full HTTP request-response cycles using `httpx.AsyncClient` with `ASGITransport(app=app)` and ephemeral SQLite databases. Validate through routing, dependency injection, and middleware.
  - FastMCP Tools: Execute MCP tools via `InMemorySessionClient` to verify live tool execution and structured output schemas.
- **Banned Test Theatre**:
  - Patching internal domain logic or service classes with `unittest.mock.patch`.
  - Asserting `mock.assert_called_with` instead of checking state deltas in the database or filesystem.
  - Writing tests for trivial Pydantic model instantiation or pass-through properties.

#### TypeScript / React Testing Strategy
- **Mandated Integration Harnesses**:
  - Web UIs: Execute realistic operator journeys using Playwright against live running frontend and backend applications.
  - Layout & Ergonomics: Enforce the 4-point `playwright-layout-inspector` audit (zero layout overflow, mobile viewport fit, touch targets &ge; 24px, layout score &ge; 85).
  - State Management: Test Zustand stores with real action dispatches and granular selector assertions.
- **Banned Test Theatre**:
  - Shallow component unit tests where sub-components and custom hooks are mocked to empty `<div>` elements.
  - Fragile DOM snapshot testing with Jest or Vitest where developers blindly accept generated diffs.
  - Testing pure presentational markup without verifying user interaction behavior.

#### C++ (C++20/23) Testing Strategy
- **Mandated Integration Harnesses**:
  - Numerical & Algorithms: Execute parameterized boundary sweeps using GoogleTest (`TEST_P`, `INSTANTIATE_TEST_SUITE_P`) across boundary spaces (-1e5, -1.0, 0.0, 1.0, 1e5).
  - Memory & Safety: Execute test suites under AddressSanitizer (ASan) and UndefinedBehaviorSanitizer (UBSan).
- **Banned Test Theatre**:
  - Mocking internal mathematical algorithms, numerical convergence solvers, or hardware state machines.
  - Authoring happy-path-only tests that ignore boundary conditions, floating-point divergence, or null pointer guards.

### 4.3 Tiered Testing Cadence ("Test When It Makes Sense")
1. **Tier 1 (Inner Loop / Rapid Development)**:
   - High-speed unit tests (xUnit, pytest, Vitest).
   - Run on demand during active implementation to verify algorithmic correctness.
2. **Tier 2 (Stabilization Gate / Pre-Manual Verification)**:
   - Simulation & control harnesses, diagnostic tap points, parameter sweeps, and Playwright layout audits.
   - Mandatory gate before manual user verification or before declaring a milestone complete.
3. **Tier 3 (Pre-PR / Pre-Release / CI Quality Gate)**:
   - Full regression suite, pairwise database matrices, live background process smoke tests, and multi-stage CI verification.
   - Mandatory before opening/merging PRs and cutting releases.

### 4.4 Controls & Simulation Mechanics
1. **Diagnostic Tap Points**: In-memory ring buffers (`DiagnosticTapRingBuffer`) and state getters allowing developers and AI agents to introspect internal state transitions.
2. **High-Volume Simulation & Parameter Sweeps**: Harnesses execute high-throughput stress loops and parameter sweeps to verify convergence and stability.
3. **Disturbance Injection**: Inject malformed payloads, network disconnects, latency spikes, and cancellation storms to verify resilience and clean `CancellationToken` propagation.
4. **Frontend UI Harness**: Include `data-testid` attributes and Playwright drivers (`playwright-layout-inspector`) for autonomous UI layout and ergonomics audits.
5. **Agent Feedback Envelope**: Format all test failures with the standardized 6-part schema:
   - `inputs` & `assumptions`
   - `active_settings`
   - `action_history` (state transitions)
   - `output_delta` (expected vs actual)
   - `captured_logs`
   - `reproduction_command`
6. **Coverage**: Maintain $\ge$ 80% code coverage across unit, integration, and E2E suites. Do not count boilerplate or trivial POCO tests toward this goal.

---

## 🚀 5. Multi-Stage GitHub Actions CI/CD (4-Stage Gate)

1. **Gate 1: Release & Link Integrity**: `verify_release.py` verifying SemVer across manifests and relative markdown link integrity.
2. **Gate 2: Parallel Builds & Tests**: Backend build + xUnit/pytest/gtest coverage ($\ge$ 80%); Frontend ESLint (0 warnings) + Vitest.
3. **Gate 3: Fullstack Smoke Gate**: Live background process spawn + `/health` probe loop + live handshake.
4. **Gate 4: Security & Release**: CodeQL multi-language analysis + Docker container publish (`linux/amd64`) + VitePress GitHub Pages documentation deployment.
