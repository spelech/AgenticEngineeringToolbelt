# Agentic Engineering Toolbelt Refinements Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refine the Agentic Engineering Toolbelt repository with traditional Git Flow branching, "APIs First, MCP Later" architecture, reframed Simulation & Control Harnesses for developers and AI, Tiered Testing Cadence, ASD-STE100 living documentation with Mermaid, and a VitePress documentation engine deployed via GitHub Pages.

**Architecture:** Update foundational standards in `standards/`, drop-in agent rules in `rules/`, skills in `.agents/skills/`, and archetypes in `archetypes/`. Provide Git Flow release automation scripts and workflows in `templates/`, and establish a native VitePress documentation site with GitHub Pages deployment workflows for both the toolbelt and downstream projects.

**Tech Stack:** Markdown (ASD-STE100, Mermaid), Python 3.12 (`verify_release.py`), Bash / POSIX Shell (`commit.sh`, `git-flow-release.sh`), GitHub Actions CI/CD (`release.yml`, `ci.yml`, `deploy-docs.yml`), Node.js / VitePress / TypeScript.

## Global Constraints

- Traditional Git Flow: `main` (production tagged releases), `develop` (integration), `release/*` (release stabilization), `feature/*` (feature branches off `develop`), `hotfix/*` (urgent fixes off `main`).
- APIs First, MCP Later: Domain logic lives in typed, self-contained APIs; MCP tools act strictly as lightweight wrappers.
- Simulation & Control Harnesses: Observable dynamic systems with diagnostic tap points, parameter sweeps, disturbance injection, and 6-part feedback envelopes for developers and AI.
- Tiered Testing Cadence: Tier 1 (inner-loop unit tests on demand), Tier 2 (stabilization gate before manual testing), Tier 3 (Pre-PR / Pre-Release / CI quality gate).
- Living Documentation: ASD-STE100 (Simplified Technical English) rules ($\le$ 20-25 words per sentence, active voice, unambiguous terminology), Mermaid diagrams, and VitePress for GitHub Pages.
- Toolbelt verification: Markdown relative links and manifest versions must pass `verify_release.py`.
- User rules: Run `npm run lint` and `npx tsc --noEmit` after code changes when npm scripts are present.

---

### Task 1: Standards Refinement (`standards/`)

**Files:**
- Modify: `standards/ENGINEERING_STYLE_GUIDE.md`
- Modify: `standards/TESTING_HARNESS_PATTERNS.md`
- Modify: `standards/CI_CD_PIPELINES.md`

- [x] **Step 1: Update `standards/ENGINEERING_STYLE_GUIDE.md`**
  - In Collaboration & Iterative Design Model, specify traditional Git Flow (`main`, `develop`, `release/*`, `feature/*`, `hotfix/*`).
  - Add explicit "APIs First, MCP Later" architectural rule under Foundational Engineering Principles.
  - Add ASD-STE100 and Mermaid Documentation Standards section under Living Documentation.
  - Reframe Section 6 to "Simulation & Control Harnesses (For Developers & AI)" with Tiered Testing Cadence.
- [x] **Step 2: Update `standards/TESTING_HARNESS_PATTERNS.md`**
  - Reframe title to "🧪 Simulation & Control Harnesses: Observation, Testing & Feedback for Developers and AI".
  - Explain software as an observable dynamic system with tap points, parameter sweeps, and 6-part feedback envelopes.
  - Codify the 3-Tier Testing Cadence: Tier 1 (Inner Loop / Rapid Dev), Tier 2 (Stabilization Gate / Pre-Manual), Tier 3 (Pre-PR / Pre-Release / CI).
- [x] **Step 3: Update `standards/CI_CD_PIPELINES.md`**
  - Update pipeline trigger matrix to include `push` to `main`, `develop`, and `release/*`.
  - Add Git Flow stage mapping and VitePress documentation deployment stage.
- [x] **Step 4: Verify markdown integrity**
  Run: `python templates/scripts/verify_release.py`
  Expected: PASS
- [x] **Step 5: Commit changes**
  Run:
  ```bash
  git add standards/
  git commit -m "docs(standards): reframe simulation harnesses, add git flow, apis first, and tiered testing"
  ```

---

### Task 2: Archetypes & Skills Updates (`archetypes/`, `.agents/skills/`)

**Files:**
- Modify: `archetypes/controls-fullstack-dotnet-react.md`
- Modify: `archetypes/README.md`
- Modify: `archetypes/python-fastapi-mcp.md`
- Modify: `.agents/skills/test-harness-builder/SKILL.md`
- Modify: `.agents/skills/engineering-archetype/SKILL.md`
- Modify: `.agents/skills/scaffold-project/SKILL.md`

- [x] **Step 1: Reframe `archetypes/controls-fullstack-dotnet-react.md`**
  - Update title to "🏛️ Archetype: Fullstack (.NET + React + SQL) with Simulation & Control Harness".
  - Reframe harness descriptions to highlight developer & AI observation, tap points, and closed-loop feedback.
- [x] **Step 2: Update `archetypes/python-fastapi-mcp.md` and `archetypes/README.md`**
  - Reframe Python archetype to emphasize "APIs First, MCP Later": build FastAPI domain endpoints and Pydantic schemas first, wrap as FastMCP tools second.
  - Update archetype index in `archetypes/README.md`.
- [x] **Step 3: Update `.agents/skills/test-harness-builder/SKILL.md`**
  - Reframe skill description and header: "Simulation & Control Harness Builder for Developers and AI".
  - Add prompts for tap points, disturbance injection, simulation loops, and Tier 2/Tier 3 evaluation.
- [x] **Step 4: Update `.agents/skills/engineering-archetype/SKILL.md` and `scaffold-project/SKILL.md`**
  - Embed Git Flow branching rules, "APIs First, MCP Later", ASD-STE100 writing guidelines, and Tiered Testing Cadence into `engineering-archetype/SKILL.md`.
  - Add VitePress doc site scaffolding option to `scaffold-project/SKILL.md`.
- [x] **Step 5: Verify markdown integrity**
  Run: `python templates/scripts/verify_release.py`
  Expected: PASS
- [x] **Step 6: Commit changes**
  Run:
  ```bash
  git add archetypes/ .agents/skills/
  git commit -m "feat(archetypes,skills): align archetypes and skills with simulation harnesses and apis first"
  ```

---

### Task 3: Universal Agent Rules & Root Documentation (`rules/`, root)

**Files:**
- Modify: `rules/AGENTS.md`
- Modify: `rules/CLAUDE.md`
- Modify: `rules/GEMINI.md`
- Modify: `ARCHITECTURE.md`
- Modify: `README.md`

- [x] **Step 1: Update `rules/AGENTS.md`**
  - Update Section 1 with traditional Git Flow (`main`, `develop`, `release/*`, `feature/*`, `hotfix/*`).
  - Add "APIs First, MCP Later" tenet.
  - Add ASD-STE100 Documentation & Mermaid requirement.
  - Update Section 4 with Tiered Testing Cadence and Simulation & Control Harnesses.
- [x] **Step 2: Update `rules/CLAUDE.md` and `rules/GEMINI.md`**
  - Synchronize specific rules with the updated tenets from `AGENTS.md`.
- [x] **Step 3: Update `ARCHITECTURE.md` and `README.md`**
  - Update system diagrams and descriptions in `ARCHITECTURE.md` to reflect Git Flow, VitePress doc site, ASD-STE100, and Simulation & Control Harnesses.
  - Update `README.md` with refined terminology, Git Flow commands, and VitePress links.
- [x] **Step 4: Verify markdown integrity**
  Run: `python templates/scripts/verify_release.py`
  Expected: PASS
- [x] **Step 5: Commit changes**
  Run:
  ```bash
  git add rules/ ARCHITECTURE.md README.md
  git commit -m "docs(rules,arch): update agent rules and root architecture for git flow and harness patterns"
  ```

---

### Task 4: Git Flow Automation & Release Templates (`templates/`)

**Files:**
- Create: `templates/scripts/git-flow-release.sh`
- Modify: `templates/scripts/commit.sh`
- Modify: `templates/scripts/verify_release.py`
- Create: `templates/workflows/release.yml`
- Create: `.github/workflows/release.yml`

- [x] **Step 1: Create `templates/scripts/git-flow-release.sh`**
  - Implement commands:
    - `start <version>`: Verifies clean working tree, checks out `develop`, pulls latest, and branches `release/v<version>`.
    - `hotfix <version>`: Verifies clean working tree, checks out `main`, pulls latest, and branches `hotfix/v<version>`.
    - `help`: Displays usage guide.
- [x] **Step 2: Update `templates/scripts/commit.sh`**
  - Add branch protection check: warn/prevent direct commit to `main` without hotfix/release branch context.
- [x] **Step 3: Update `templates/scripts/verify_release.py`**
  - Add check for valid SemVer tag format and changelog headers.
  - Keep relative markdown link audit intact.
- [x] **Step 4: Create `templates/workflows/release.yml` and `.github/workflows/release.yml`**
  - Trigger on `workflow_dispatch` (with version/bump input) and on push to `release/v*`.
  - Stage 1: Runs release verification (`verify_release.py`).
  - Stage 2: Runs build and test gates.
  - Stage 3: Creates Git Tag, publishes GitHub Release with release notes.
  - Stage 4: Merges to `main` and syncs back to `develop`.
- [x] **Step 5: Test release script execution**
  Run: `bash templates/scripts/git-flow-release.sh help`
  Expected: Shows usage guide with zero exit code.
- [x] **Step 6: Commit changes**
  Run:
  ```bash
  git add templates/ .github/workflows/
  git commit -m "feat(templates,workflows): add git flow release automation workflows and helper scripts"
  ```

---

### Task 5: VitePress Documentation Engine & Templates

**Files:**
- Create: `package.json` (root)
- Create: `tsconfig.json` (root)
- Create: `docs/.vitepress/config.mts`
- Create: `docs/index.md`
- Create: `docs/standards/engineering-style-guide.md`
- Create: `docs/standards/testing-harness-patterns.md`
- Create: `docs/standards/ci-cd-pipelines.md`
- Create: `docs/standards/asd-ste100.md`
- Create: `.github/workflows/deploy-docs.yml`
- Create: `templates/vitepress/package.json`
- Create: `templates/vitepress/.vitepress/config.mts`
- Create: `templates/vitepress/docs/index.md`
- Create: `templates/workflows/deploy-docs.yml`

- [x] **Step 1: Create root `package.json` and install VitePress**
  - Configure `vitepress`, `typescript`, `@types/node` in `devDependencies`.
  - Configure scripts: `"docs:dev": "vitepress dev docs"`, `"docs:build": "vitepress build docs"`, `"docs:preview": "vitepress preview docs"`, `"lint": "eslint . || echo no linter configured"`.
- [x] **Step 2: Create `docs/.vitepress/config.mts`**
  - Configure site title: "Agentic Engineering Toolbelt".
  - Configure navigation links and sidebar mapping:
    - Standards (Style Guide, Simulation & Control Harnesses, CI/CD, ASD-STE100)
    - Archetypes (.NET CLI, Fullstack, C++ Algorithms, Python FastAPI, React UI)
    - Rules & Skills (AGENTS.md, Claude, Gemini, Toolbelt Skills)
  - Configure native Mermaid markdown support.
- [x] **Step 3: Create VitePress documentation content in `docs/`**
  - `docs/index.md`: ASD-STE100 home landing page with architecture diagram and quickstart links.
  - Mirror/link the standard specifications and create `docs/standards/asd-ste100.md` explaining the simplified technical English writing rules.
- [x] **Step 4: Create downstream VitePress template in `templates/vitepress/`**
  - Package json, `.vitepress/config.mts`, starter `index.md`, and `templates/workflows/deploy-docs.yml`.
- [x] **Step 5: Create `.github/workflows/deploy-docs.yml`**
  - GitHub Pages deployment workflow using `actions/deploy-pages@v4` on push to `main`.
- [x] **Step 6: Build VitePress site locally to verify zero build errors**
  Run: `npx vitepress build docs`
  Expected: Build succeeds with HTML assets generated in `docs/.vitepress/dist`.
- [x] **Step 7: Commit changes**
  Run:
  ```bash
  git add package.json package-lock.json tsconfig.json docs/ .github/workflows/deploy-docs.yml templates/vitepress/ templates/workflows/deploy-docs.yml
  git commit -m "feat(docs): setup vitepress doc site, asd-ste100 guide, and github pages deployment"
  ```

---

### Task 6: End-to-End Verification & Quality Audit

**Files:**
- Repository-wide audit

- [ ] **Step 1: Run markdown relative link and anchor audit**
  Run: `python templates/scripts/verify_release.py`
  Expected: `All markdown links verified successfully.`
- [ ] **Step 2: Run user-rule linting and typechecking**
  Run: `npm run lint` and `npx tsc --noEmit`
  Expected: Exits 0 without errors.
- [ ] **Step 3: Verify git status and working tree cleanliness**
  Run: `git status`
  Expected: On main, working tree clean.
