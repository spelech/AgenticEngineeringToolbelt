# 🤖 Universal AGENTS.md

Instructions and architectural guidelines for AI coding assistants.

## 🤝 Collaboration & Working Model
- **Proactive Questioning**: Steven has ideas in his head that evolve through discussion. **Always ask clarifying questions** to flesh out requirements, edge cases, and design constraints before or during development.
- **Iterative Prototyping**: Build via quick prototypes, run test feedback loops, and adjust based on findings.
- **Branching & PR Workflow**:
  - All new features and plans must be developed on a **fresh feature branch** off `develop` (or `main`/`master`).
  - Create fine-grained, **atomic commits** on the branch with clear messages so history is traceable.
  - Open a **Pull Request (PR)** so all CI quality gates run and pass before merging.

## 🏛️ Engineering Stack & Style Rules
1. **SOLID & DRY**: Break apart large files into focused sub-modules. Design for pluggability and reusability.
2. **Backend**: Modern .NET (C#) with `<Nullable>enable</Nullable>`, `<ImplicitUsings>enable</ImplicitUsings>`, `.slnx`.
   - **Database**: Relational SQL (SQLite WAL, MS SQL, MySQL) with **Dapper** and **Stored Procedures** where appropriate. Idempotent seeders (`DatabaseSeederService.cs`). No heavy ORMs (EF Core) or NoSQL unless explicitly requested.
   - **APIs**: Controllers (`[ApiController]`) or Minimal APIs (`Map*Endpoints()`) depending on domain complexity.
   - **MCP First**: If exposing an API, consider exposing a Model Context Protocol (MCP) server.
   - **Security**: Default to encrypting sensitive data at rest/transit and applying authentication.
   - **LLM Integration**: Standardize on LiteLLM / OpenAI SDK compatibility.
3. **Frontend**: React + TypeScript (strict mode) + Zustand stores + Vite + CSS custom properties with dark mode. Zero linter warnings (`eslint . --max-warnings 0`).
4. **Controls-Grade Testing**: Test harnesses, mock transports (`mock_stdio.js`), closed-loop feedback testing, >80% coverage target, and `playwright-layout-inspector` E2E UX audits.
5. **Living Documentation**: `ARCHITECTURE.md` (with Mermaid diagrams), narrative requirements (formal `REQ-xxx` only when ADRs present), and automated release scripts (`commit.sh`, `verify_release.py`).
