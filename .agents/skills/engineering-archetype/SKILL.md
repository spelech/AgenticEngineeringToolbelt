---
name: engineering-archetype
description: Architectural guidelines and setup reference for Steven T. Pelech's engineering archetype (Modern .NET/C# Minimal APIs/Controllers, Dapper/Stored Procedures, React + Zustand + Vite, controls-grade test harnesses, Playwright Layout Inspector, and 4-stage GitHub Actions CI/CD).
---

# Engineering Archetype & Collaboration Skill

This skill equips agents to assist Steven T. Pelech across new project setups, feature development, and architectural refactoring.

## 🤝 Division of Responsibility & Working Model

- **Steven's Role**: System architecture, structural design, feature conceptualization, domain modeling, requirement specifications, stored procedure/data design, and Mermaid diagram designs.
- **Agent's Role**: 
  - **Proactive Questioning**: Ask insightful clarifying questions to flesh out requirements and edge cases since Steven's ideas evolve during design.
  - **Iterative Prototyping**: Build prototypes, run test harnesses with closed-loop feedback, and iterate based on empirical findings.
  - **Branch & PR Discipline**: Work on fresh feature branches off `develop`/`main`, make fine-grained atomic commits, and open PRs that pass all CI quality gates.

---

## 🏛️ Core Tech Stack & Design Idioms

### 1. SOLID, DRY & Extensibility
- Heavy emphasis on SOLID principles, modular file size, and breaking apart multi-concern components.
- Avoid one-offs and duplicate code; design for pluggability and reusability.

### 2. Backend Architecture (Modern .NET / C#)
- **Runtime**: Modern .NET with `<Nullable>enable</Nullable>`, `<ImplicitUsings>enable</ImplicitUsings>`, and `.slnx` solution format.
- **Persistence Philosophy**: Relational SQL (SQLite WAL, MS SQL, MySQL) over NoSQL or heavy ORMs (like Entity Framework Core).
  - Use **Dapper** / ADO.NET with **Stored Procedures** where appropriate (e.g. security evaluation, audit logging, batch operations) and parameterized queries with `IDbConnectionFactory`.
  - Enable SQLite WAL mode where applicable (`PRAGMA journal_mode = WAL;`).
  - **No Heavy ORMs**: Do not introduce Entity Framework Core or NoSQL document databases unless explicitly requested.
- **API Architecture**: Choose pragmatically between **Controllers** (`[ApiController]`) for rich domain slices and **Minimal APIs** (`Map*Endpoints()`) for lightweight routing and streaming.
- **MCP Server First**: If exposing an API, consider exposing a Model Context Protocol (MCP) server for agent integration.
- **Security**: Encrypt sensitive data at rest and in transit (AES-256-GCM, DPAPI, SQLCipher, Vault) and apply auth by default.
- **LLM Integration**: Standardize on LiteLLM / OpenAI SDK compatibility.
- **Resilience**: Thread-safe state machines (`ConcurrentDictionary`, `PendingRequestTcs`), full `CancellationToken` propagation.

### 3. Frontend Architecture (React / TypeScript / Zustand / Vite)
- **Stack**: React, TypeScript in strict mode (`strict: true`), Vite.
- **State Management**: **Zustand** stores (`use*Store.ts`) with focused state slices and selector hooks.
- **Linter Policy**: Zero linter warnings permitted (`eslint . --max-warnings 0`).
- **Styling**: CSS custom properties and theme tokens with dark mode support. Avoid heavy UI library bloat.

### 4. Controls & Simulation Testing Harnesses (>80% Target)
- **Controls Mindset**: Test harnesses, simulated mock transports (`mock_stdio.js`), debug tooling, and closed-loop feedback testing.
- **Code Coverage**: Target **>80% code coverage** across unit, integration, and E2E suites.
- **E2E & Layout UX**: Playwright paired with `playwright-layout-inspector` to audit:
  - Zero horizontal overflow (`expect(page).toHaveNoLayoutOverflow()`)
  - Mobile viewport fit & zoom accessibility (`expect(page).toHaveMobileFit()`)
  - Touch ergonomics (`expect(page).toHaveTouchFriendlyTargets({ minSize: 24 })`)
  - Composite UX score (`expect(page).toPassLayoutAudit({ minScore: 85 })`)

### 5. Living Documentation & Automation
- `ARCHITECTURE.md`: Mermaid flowchart (`flowchart TD`) and numbered sequence diagram (`sequenceDiagram autonumber`).
- Requirements: Narrative acceptance criteria by default; formal `REQ-xxx` prefixes only when ADR documents are present.
- Automated release scripts: `commit.sh` and `verify_release.py`.

### 6. Multi-Stage GitHub Actions CI/CD (4-Stage Gate)
1. **Gate 1: Release & Link Integrity**: Python `verify_release.py` checking semver sync and markdown link integrity.
2. **Gate 2: Parallel Builds & Tests**: Backend Release build + xUnit coverage (>80%); Frontend ESLint (0-warn) + Vitest.
3. **Gate 3: Fullstack Integration Smoke**: Background server spawn + `/health` probe loop + live SSE/HTTP handshake.
4. **Gate 4: Security & Release**: CodeQL multi-language analysis + Docker publish.
