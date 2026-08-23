# 🏛️ Archetype: Controls-Grade Fullstack (.NET + React + SQL)

> **Architect**: Steven T. Pelech  
> **Focus**: Controls engineering, simulation, deterministic high-concurrency systems, and closed-loop testing.

---

## 🤝 1. Collaboration & Iterative Design Model

```mermaid
flowchart LR
    A["💡 Vision in Steven's Head"] --> B["❓ Agent Proactive Questioning & Clarification"]
    B --> C["📐 Rapid Prototype & Test Harness"]
    C --> D["🔄 Closed-Loop Testing & Iterative Learning"]
    D --> E["✨ Hardened, Extensible & Verified Solution"]
```

- **Vision & Exploration**: Steven drives the conceptual vision, architecture, and feature ideas. Because ideas start in his head and evolve, **part of the agent's primary job is to ask insightful clarifying questions** to flesh out requirements, edge cases, and design constraints before or during development.
- **Iterative Prototyping**: We build via rapid prototyping and closed-loop evaluation—prototyping early, running test harnesses, learning from live behavior, and refining architecture iteratively.
- **Git Branch & PR Workflow**:
  - All new features and significant plans start on a **fresh feature branch** off `develop` (or `main`/`master`).
  - Work is committed with **fine-grained, atomic commits** to keep history transparent and legible.
  - Features culminate in a **Pull Request (PR)** where all multi-stage CI quality gates must pass before merging.

---

## 🎯 2. The 12 Core Tenets

1. **Division of Labor & Proactive Questioning**: Agent asks clarifying questions to flesh out requirements; iterative prototyping with fast feedback loops.
2. **Controls, Modeling & Simulation Mindset**: Systems gravitate towards rich test harnesses, simulated environments (mock transports like `mock_stdio.js`, SSE emulators), loopback tests, and dedicated debug tooling.
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

## 💻 3. Backend Architecture (Modern .NET / C#)

- **Language & Runtime**: Modern .NET (C#) with `<Nullable>enable</Nullable>`, `<ImplicitUsings>enable</ImplicitUsings>`, and `.slnx` solution format.
- **Persistence Philosophy**: Relational SQL (SQLite WAL, MS SQL, MySQL) over NoSQL or heavy ORMs (like Entity Framework Core).
  - Use **Dapper** / ADO.NET with **Stored Procedures** where appropriate (e.g. security evaluation, audit logging, batch operations) and parameterized queries with `IDbConnectionFactory`.
  - Enable SQLite WAL mode where applicable (`PRAGMA journal_mode = WAL;`).
  - **No Heavy ORMs**: Do not introduce Entity Framework Core or NoSQL document databases unless explicitly requested.
- **API Architecture**: Choose pragmatically between **Controllers** (`[ApiController]`) for rich domain slices and **Minimal APIs** (`Map*Endpoints()`) for lightweight routing and streaming.
- **Resilience**: Thread-safe state machines (`ConcurrentDictionary`, `PendingRequestTcs`), full `CancellationToken` propagation.

---

## 🎨 4. Frontend Architecture (React / TypeScript / Zustand / Vite)

- **Stack**: React, TypeScript in strict mode (`strict: true`), Vite.
- **State Management**: **Zustand** stores (`use*Store.ts`) with focused state slices and selector hooks.
- **Linter Policy**: Zero linter warnings permitted (`eslint . --max-warnings 0`).
- **Styling**: CSS custom properties and theme tokens with dark mode support. Avoid heavy UI library bloat.

---

## 🧪 5. Testing & UI Layout UX

- **Unit & Integration**: xUnit + NSubstitute in C#; Vitest + `@testing-library/react` + `happy-dom` in TS.
- **Pairwise Matrices**: Multi-provider database and authentication integration tests.
- **Mock Transports**: Synthetic STDIO/SSE harnesses (`mock_stdio.js`) for deterministic protocol testing.
- **E2E & Layout UX**: Playwright paired with `playwright-layout-inspector` to audit:
  - Zero horizontal overflow (`expect(page).toHaveNoLayoutOverflow()`)
  - Mobile viewport fit & zoom accessibility (`expect(page).toHaveMobileFit()`)
  - Touch ergonomics (`expect(page).toHaveTouchFriendlyTargets({ minSize: 24 })`)
  - Composite UX score (`expect(page).toPassLayoutAudit({ minScore: 85 })`)
