---
title: "Multi-Stage CI/CD Pipelines"
description: "4-stage quality gate architecture, Git Flow triggers, and living documentation deployment."
---

# Multi-Stage GitHub Actions CI/CD Pipeline Blueprint

This document details the standardized 4-stage GitHub Actions CI/CD architecture deployed across projects. It codifies [Traditional Git Flow](/standards/engineering-style-guide#traditional-git-flow-discipline) triggers, quality gates, and automated living documentation deployment.

---

## Pipeline Topology

```mermaid
flowchart TD
    Triggers["Git Flow Triggers<br>• Push to main (Tagged Release)<br>• Push to develop or release/*<br>• PR to develop or main"]
    G1["Stage 1: Integrity Gate<br>• Version sync in manifests<br>• Markdown link & anchor validation<br>• Static anti-test-theatre audit"]
    G2A["Stage 2A: Backend Build & Tests<br>• Release build (.slnx / uv)<br>• xUnit / pytest (>= 80% cov)<br>• TRX & coverage artifacts"]
    G2B["Stage 2B: Frontend Quality & Tests<br>• ESLint (0 max warnings)<br>• Production build (Vite)<br>• Vitest & Playwright layout audit"]
    G3["Stage 3: Fullstack Smoke Gate<br>• Background server spawn<br>• Health probe loop (/health)<br>• Live SSE/HTTP handshake"]
    G4A["Stage 4A: CodeQL<br>Security Analysis"]
    G4B["Stage 4B: VitePress Docs<br>(GitHub Pages)"]
    G4C["Stage 4C: Docker Publish<br>(GHCR linux/amd64)"]

    Triggers --> G1
    G1 --> G2A & G2B
    G2A & G2B --> G3
    G3 --> G4A & G4B & G4C
```

---

## Git Flow Trigger Matrix

The pipeline adapts execution stages based on the Git Flow branch and lifecycle event:

| Branch / Context | Trigger Event | Executed Stages | Output Deliverables |
| :--- | :--- | :--- | :--- |
| `feature/*` | Pull Request to `develop` | Stage 1 (Integrity), Stage 2 (Build & Test), Stage 3 (Smoke) | PR test reports, coverage deltas |
| `develop` | Push / Merged PR | Stage 1 (Integrity), Stage 2 (Build & Test), Stage 3 (Smoke), Stage 4 (CodeQL) | Integration build verification |
| `release/*` | Push / Release branch creation | Stage 1 (Integrity & Version Audit), Stage 2 (Build & Test), Stage 3 (Smoke) | Release staging validation, draft release |
| `hotfix/*` | Pull Request to `main` and `develop` | Stage 1 (Integrity), Stage 2 (Build & Test), Stage 3 (Smoke) | Critical hotfix verification |
| `main` | Push with SemVer Tag (`vX.Y.Z`) | All Stages (1, 2, 3, 4: CodeQL, Docs, Docker) | Production GHCR containers, GitHub Release, GitHub Pages docs |

---

## Stage Descriptions

### Stage 1: Release and Link Integrity Gate

Runs `templates/scripts/verify_release.py` to verify that:
- Version numbers match across all manifest files (`.csproj`, `package.json`, `pyproject.toml`, and `CHANGELOG.md`).
- All relative markdown links and `#section` anchor targets resolve to existing files and valid headings.
- Documentation contains zero unrendered LaTeX math sequences (`$\ge$`, `$\le$`, `$$...$$`).
- Test suites pass the static anti-test-theatre audit (see [Tier 3 Quality Gate](/standards/testing-harness-patterns#tier-3-pre-pr-pre-release-and-ci-quality-gate)).

### Stage 2: Parallel Builds and Tests

- **Backend**:
  - Restores dependencies and compiles in `Release` configuration.
  - Executes unit and integration test suites with code coverage collection (**≥ 80% coverage** required).
  - Uploads TRX test result files and code coverage summaries.
- **Frontend**:
  - Installs dependencies cleanly via `npm ci`.
  - Runs ESLint with zero-warning tolerance (`--max-warnings 0`).
  - Compiles production assets via `vite build`.
  - Executes Vitest unit suites and [Playwright Layout Inspector Audits](/standards/testing-harness-patterns#ui-layout-stability-and-ergonomics-auditing).

### Stage 3: Fullstack Integration Smoke Gate

- Spawns compiled backend and frontend services in the background.
- Polls the `/health` endpoint until a healthy response returns within timeout limits.
- Executes real HTTP and Server-Sent Events (SSE) communication handshakes.
- Terminates background processes cleanly and verifies zero orphan processes.

### Stage 4: Security, Documentation, and Release

- **CodeQL Security Analysis**: Runs multi-language static analysis across C#, Python, and TypeScript to detect vulnerabilities.
- **VitePress Living Documentation Deployment**:
  - Builds the static documentation site using `npx vitepress build docs`.
  - Renders native Mermaid diagrams into accessible SVG assets.
  - Publishes static assets to GitHub Pages on verified release tags and `main` branch updates.
- **Docker Container Publish**:
  - Builds native `linux/amd64` container images without emulation overhead.
  - Pushes multi-stage container images to GitHub Container Registry (GHCR).
  - Attaches release tags matching repository SemVer (`ghcr.io/org/repo:vX.Y.Z` and `:latest`).
