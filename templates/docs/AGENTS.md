# AGENTS.md

Instructions and architectural guidelines for AI coding agents working on **{{PROJECT_NAME}}**.

## 🛑 Guardrails & Rules
1. **Never introduce Entity Framework Core or NoSQL databases**: All database interactions use direct SQL via **Dapper** and connection factories (`IDbConnectionFactory`).
2. **Strict TypeScript & Zero Linter Warnings**: Frontends must pass `npm run lint` (`--max-warnings 0`) and `npm run build`.
3. **CancellationToken Propagation**: Always accept and pass `CancellationToken` in asynchronous C# methods.
4. **Mandatory Test Verification**: Do not claim a feature or fix is complete without running automated tests (`dotnet test` / `npm test`).
5. **Layout Inspection**: Use `playwright-layout-inspector` to audit UI changes on mobile and desktop viewports.

## 🛠️ Verification Commands
```bash
# Backend Build & Test
dotnet build --configuration Release
dotnet test --configuration Release

# Frontend Lint, Test & Build
cd frontend
npm run lint
npm test
npm run build
```
