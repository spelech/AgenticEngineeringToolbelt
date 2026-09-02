# 🏛️ Master Engineering Style Guide & Architecture Archetype

This document codifies the core engineering principles, architectural patterns, polyglot language standards, test harness conventions, and living documentation practices established across Steven T. Pelech's repositories and agent workflows.

---

## 🤝 1. Collaboration & Iterative Design Model

```mermaid
flowchart LR
    A["💡 Conceptual Vision & Domain Model"] --> B["❓ Agent Clarification & Edge-Case Discovery"]
    B --> C["📐 Rapid Prototype & Controls Test Harness"]
    C --> D["🔄 Closed-Loop High-Volume Testing & Feedback"]
    D --> E["✨ Hardened, Extensible & Verified Solution"]
```

- **Vision & Exploration**: Steven drives the conceptual vision, architecture, and feature ideas. Because ideas start conceptually and evolve during design, **part of the agent's primary job is to ask insightful clarifying questions** to flesh out requirements, edge cases, and design constraints before or during development.
- **Iterative Prototyping**: Build via rapid prototyping and closed-loop evaluation—prototyping early, running test harnesses, learning from live behavior, and refining architecture iteratively.
- **Git Branch & PR Discipline**:
  - All new features and significant plans start on a **fresh feature branch** off `develop` (or `main`/`master`).
  - Use `develop` as the active integration branch for consolidating multiple feature tracks prior to a production release on `main`.
  - Work is committed with **fine-grained, atomic Conventional Commits** (`feat:`, `fix:`, `test:`, `docs:`, `chore:`).
  - Features culminate in a **Pull Request (PR)** where all 4-stage CI quality gates must pass before merging.

---

## 🎯 2. Foundational Engineering Principles

### 2.1 SOLID & Modularity
1. **Single Responsibility**: Each class, module, and component must have a single, well-defined reason to change. Decompose large files and multi-concern classes.
2. **File Size & Cohesion Limit**: Classes or files exceeding **500 lines of code** must be broken down into focused partial classes, sub-services, or distinct domain helpers.
3. **Open / Closed**: Design for pluggability and extensibility without modifying core engine logic.
4. **Interface Segregation**: Enforce narrow, client-focused interfaces (`IStateReader`, `IStateWriter`, `IHealthCheckable`) over fat monolithic interfaces.
5. **Dependency Inversion**: High-level modules must depend on abstractions. **Build interfaces (`I*`) even for single implementations** to ensure 100% testability, mockability, and loose coupling.

### 2.2 DRY vs. YAGNI & KISS
1. **Rule of Three for DRY**: Duplication is acceptable across 2 instances if contexts or data shapes differ slightly. Refactor into a shared utility or generic abstraction on the **3rd occurrence**.
2. **YAGNI (You Aren't Gonna Need It)**: Do not build speculative multi-tier frameworks, premature plugin registries, or unused generic abstractions. Build cleanly and simply for the concrete requirement.
3. **KISS (Keep It Simple, Stupid)**: Choose direct, readable implementations over clever indirection.

### 2.3 Semantic Naming & Anti-Pattern Bans
1. **Banned "Junk-Drawer" Anti-Patterns**: Explicitly forbid catch-all class names such as `GeneralManager`, `AppHelper`, `DataUtil`, or `CommonHandler` that accumulate unrelated functions.
2. **Role- & Verb-Based Naming**:
   - **Services / Handlers**: Name strictly by role or action: `DatabaseSeederService`, `UserAuthenticator`, `OrderProcessor`, `StateTransitionLogger`.
   - **Interfaces**: C# interfaces MUST use the `I` prefix (`IDbConnectionFactory`, `ITransportChannel`). TypeScript/Python interfaces use descriptive role names or `*able` traits.
   - **UI Components**: Name strictly after the visual entity or view role (`ServerStatusCard`, `DeviceListTable`, `HeaderNavbar`). Never name components after temporary feature names, tasks, or git branches.
   - **Zustand Stores**: Prefix with `use*Store.ts` (`useAuthStore.ts`, `useServerStore.ts`).

### 2.4 Performance & Efficiency Discipline
1. **Database Trips**: If an operation requires 3+ database round-trips or multi-table joins, consolidate into a single **Stored Procedure** or multi-result batch query.
2. **Frontend Re-renders**: Mandate **granular Zustand selectors** (`useServerStore(s => s.serverCount)`) to eliminate unnecessary component re-renders. Separate high-frequency reactive widgets from static layout trees.
3. **API Independence**: Provide focused, individual REST/HTTP endpoints so UI components and stores can independently fetch and manage their own data lifecycles.

### 2.5 Error Handling & Diagnostics
1. **Never Leak Raw Stacks**: Prevent raw stack traces or internal database schemas from leaking to clients. Return clean error payloads with correlation IDs.
2. **Domain Exceptions**: Use well-defined domain exceptions for unexpected system failures; use Result/boolean patterns for expected validation failures.
3. **Reproducible Debug Payloads**: All error logs must capture the error description, stack trace, and the exact input payload/state that caused the failure to aid deterministic reproduction.

---

## 💻 3. Polyglot Language & Archetype Standards

```mermaid
flowchart TD
    Task["Select Project Archetype"]
    Task -->|High-Performance Systems / Protocols / Control Planes| CSharp["C# (.NET 9)<br>• System.CommandLine + DI<br>• Dapper + Stored Procs (SQL files)<br>• SQLite WAL (MySQL-like) / MSSQL<br>• Native WPF/WinForms/Avalonia (No Electron)"]
    Task -->|Scrapers / ML / Vision / Data Pipelines / Automation| Python["Python (3.12+)<br>• uv package management<br>• Typer + Pydantic models<br>• FastAPI + FastMCP<br>• asyncio runtime"]
    Task -->|Web UIs / Layout Analyzers / Interactive Apps| TypeScript["TypeScript / React<br>• Strict TS + Vite<br>• Zustand stores per domain/controller<br>• Pure CSS Modules & CSS variables<br>• Playwright Layout Inspector 4-point audit"]
    Task -->|Algorithms / Native Systems / High-Compute| Cpp["C++ (C++20/23)<br>• MSBuild (Win) / CMake (Linux)<br>• vcpkg manifest mode<br>• Strict RAII & std::smart_pointers<br>• GoogleTest + ASan/UBSan + Benchmark<br>• C# [LibraryImport] & Python pybind11 interop"]
```

---

## 🏛️ 4. Backend Architecture & Persistence

### 4.1 C# .NET 9
- **Project Structure**: Modern `.slnx` solution format with `<Nullable>enable</Nullable>`, `<ImplicitUsings>enable</ImplicitUsings>`, and `Directory.Build.props`.
- **API Routing Division**:
  - **Minimal APIs**: Reserved for small projects, simple feed-through endpoints, lightweight vertical slices, and streaming routes.
  - **Controllers (`[ApiController]`)**: Standard for larger control planes, rich multi-route resources, admin portals, and distinct domain slices.
- **Persistence & Stored Procedures**:
  - Dedicated `.sql` stored procedure files preferred over inline code queries.
  - MCG-style idempotent schema migrations and seeders (`DatabaseSeederService.cs`).
  - Configure SQLite schemas and types to be as MySQL/relational-compatible as possible to ensure friction-free migrations to containerized SQL engines.
  - Mandatory SQLite WAL pragmas: `PRAGMA journal_mode = WAL; PRAGMA synchronous = NORMAL; PRAGMA busy_timeout = 5000; PRAGMA foreign_keys = ON;`.
- **Configuration & Auth**:
  - Prefer `appsettings.json` (with environment overrides) as the primary configuration vehicle.
  - Forward auth headers (`Remote-User`, `Remote-Groups`) for human web traffic; **Bearer tokens** for machine / agent service-to-service auth.
  - Encryption at rest via self-contained AES-256-GCM symmetric encryption (avoiding OS-locked DPAPI/Vault dependencies).
- **Concurrency & Resilience**:
  - `ConcurrentDictionary` for thread-safe lookups/caches.
  - `System.Threading.Channels.Channel<T>` for high-throughput, decoupled producer-consumer pipelines.
  - `SemaphoreSlim` for rate-limiting and atomic locks; `Interlocked` for parallel execution metrics.
  - **100% CancellationToken propagation** across all async database, I/O, and streaming calls.
- **Diagnostics**:
  - Standard `/health` probe on all web services.

---

## 🎨 5. Frontend Architecture (React / TypeScript / Zustand / Vite)

- **Framework & Stack**: React with TypeScript in strict mode (`"strict": true`), bundled via Vite.
- **Folder Structure**: Clean domain/view-oriented structure (`components/common/`, `components/[ComponentName]/`, `hooks/`, `stores/`, `views/`). Never organized by temporary feature/branch names.
- **State Management**: **Zustand** stores organized into separate files mapped directly per domain, data source, or backend API controller.
- **Selectors**: Mandatory granular selector hooks (`const count = useServerStore(s => s.servers.length)`).
- **Data Fetching**: Lean, native `fetch` API wrappers by default; avoid TanStack Query bloat unless caching/sync complexity strictly justifies the package weight.
- **Styling**: Pure CSS with standard CSS Modules and theme variables (`theme.css`). Bespoke, lightweight UI components over heavy external UI libraries.
- **Desktop Strategy**: Native **C# UI frameworks** (WPF / WinForms / Avalonia). Avoid Electron completely.
- **UI Quality Gates (`playwright-layout-inspector`)**:
  - Mandatory 4-point automated layout audit across mobile and desktop viewports:
    1. `expect(page).toHaveNoLayoutOverflow()` (Zero horizontal bleed)
    2. `expect(page).toHaveMobileFit()` (Responsive viewport scaling)
    3. `expect(page).toHaveTouchFriendlyTargets({ minSize: 24 })` (Touch target sizing)
    4. `expect(page).toPassLayoutAudit({ minScore: 85 })` (Composite UX health)
  - UI components must include `data-testid` attributes so AI agents can drive automated browser journeys.
  - Live validation against running backend instances is always preferred over pure mocking.

---

## 🧪 6. Testing, Harnesses & Simulation

- **Controls Mindset**: Software is a dynamic system. Build dedicated test harnesses whenever crossing an API/network boundary or implementing algorithms with tunable variability.
- **High-Volume & Closed-Loop Testing**: Harnesses run high-volume throughput tests, parameter sweeps, and convergence checks.
- **Disturbance Ingestion**: Inject malformed payloads and abrupt disconnects/terminations to test error fallbacks and graceful degradation.
- **Agent Tap Points**: Agents inject internal diagnostic hooks during development (and clean them up before production) to expose internal state without relying solely on string logs.
- **Agent Feedback Envelope**: On harness or test failure, provide a structured diagnostic payload:
  1. **Inputs** & **Assumptions**
  2. **Active Settings / Environment**
  3. **History of Actions** (state transition trace)
  4. **Actual Output vs Expected Output**
  5. **Captured Execution Logs**
  6. **Deterministic Reproduction Script / Command**
- **Coverage Target**: $\ge$ 80% code coverage across unit, integration, and E2E suites.

---

## 📑 7. Living Documentation & Automation

- **`ARCHITECTURE.md`**:
  - Top-down Mermaid topology flowchart (`flowchart TD`).
  - Step-numbered sequence diagrams (`sequenceDiagram autonumber`).
  - Subsystem breakdowns and non-functional SLAs.
- **`README.md`**: Standardized badges (CI, Coverage, Language, Docker, License), Architecture diagram, Quick start (Docker & Local), REST/MCP Tool reference.
- **Automated Commit & Verification**:
  - `commit.sh`: Checks compilation, runs automated version bumping, and produces atomic commits.
  - `verify_release.py`: Verifies version sync across manifests (`.csproj`, `package.json`, `pyproject.toml`) and validates all relative markdown links and anchors.

---

## 🚀 8. 4-Stage GitHub Actions CI/CD Pipeline

```mermaid
flowchart LR
    subgraph S1["1. Integrity Gate"]
        G1["Release Verification<br>(verify_release.py)<br>• Version sync across manifests<br>• Markdown relative links & anchors"]
    end
    subgraph S2["2. Build & Test Gates"]
        G2A["Backend Build & Tests<br>xUnit / pytest / gtest (>80% cov) & TRX"]
        G2B["Frontend Build & Tests<br>ESLint 0-warn & Vitest Suite"]
    end
    subgraph S3["3. Smoke Gate"]
        G3["Fullstack Smoke Run<br>Health probe loop & live handshake"]
    end
    subgraph S4["4. Analysis & Release"]
        G4["CodeQL Security Analysis<br>Multi-platform Container Publish"]
    end

    S1 --> S2
    S2 --> S3
    S3 --> S4
```
