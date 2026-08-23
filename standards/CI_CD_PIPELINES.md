# 🚀 Multi-Stage GitHub Actions CI/CD Pipeline Blueprint

This document details the standardized 4-stage GitHub Actions CI/CD architecture deployed across projects.

---

## 🏛️ Pipeline Topology

```mermaid
flowchart LR
    subgraph Trigger["Push / PR to main/develop"]
        Commit["Git Commit"]
    end

    subgraph S1["Stage 1: Integrity Gate"]
        G1["Python Release & Link Gate<br>• Version sync in csproj/package.json<br>• Markdown relative link validation<br>• GFM anchor integrity"]
    end

    subgraph S2["Stage 2: Parallel Builds & Tests"]
        G2A["Backend .NET Build & Tests<br>• Build Release<br>• xUnit + Code Coverage (>80%)<br>• TRX artifact upload"]
        G2B["Frontend Quality & Tests<br>• ESLint (0 max warnings)<br>• Vite build<br>• Vitest coverage & Playwright"]
    end

    subgraph S3["Stage 3: Fullstack Smoke Gate"]
        G3["Live Smoke Integration<br>• Background server spawn<br>• Health probe loop<br>• Live SSE/HTTP handshake"]
    end

    subgraph S4["Stage 4: Security & Release"]
        G4A["CodeQL Multi-Language Analysis"]
        G4B["Docker Multi-Arch Container Publish"]
    end

    Commit --> G1
    Commit --> G2A
    Commit --> G2B
    G1 & G2A & G2B --> G3
    G3 --> G4A & G4B
```

---

## 📋 Stage Descriptions

### Stage 1: Release & Link Integrity Gate
Runs `scripts/verify_release.py` to ensure that:
- Version strings are synchronized across all project files (`.csproj`, `package.json`, `CHANGELOG.md`, `README.md`).
- All relative markdown links and anchor targets in `docs/` and root files resolve to real files and headers.

### Stage 2: Parallel Builds & Tests
- **Backend**: Restores solution (`.slnx`), builds in Release mode, and runs unit and integration tests with code coverage collection.
- **Frontend**: Installs dependencies (`npm ci`), runs strict ESLint (`--max-warnings 0`), builds the production bundle (`vite build`), and runs unit and layout tests.

### Stage 3: Fullstack Integration Smoke Gate
Spawns the built backend and frontend in the background, probes the `/health` endpoint until healthy, executes live SSE/HTTP handshakes, and terminates cleanly.

### Stage 4: Security & Release
- Runs **CodeQL** static analysis across C# and TypeScript codebases.
- Builds and publishes multi-architecture Docker containers to GitHub Container Registry (GHCR) upon successful main branch builds or semver tags.
