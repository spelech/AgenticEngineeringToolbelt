# Anti-Test-Theatre Guardrails & Representative Testing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Codify the Four Pillars of Anti-Test Theatre, the 12-Dimension Banned vs. Mandated Patterns Matrix, deterministic test budget and mock algorithms, polyglot archetype harness recipes, and automated audit tooling across the Agentic Engineering Toolbelt repository.

**Architecture:** Update universal agent rules (`rules/`), engineering standards (`standards/`), and core skills (`.agents/skills/`) to mandate real implementations over mocks and state outcome assertions. Update polyglot archetype blueprints (`archetypes/`) with working in-memory test recipes. Implement `--audit-tests` heuristic detection in `templates/scripts/verify_release.py` and wire it into GitHub Actions CI workflows (`.github/workflows/ci.yml`). Synchronize living documentation into VitePress (`docs/`).

**Tech Stack:** Markdown, Python 3.12 (`pytest`, AST parsing, regex), C# (.NET 10, `WebApplicationFactory`), TypeScript (Playwright), GitHub Actions, VitePress.

## Global Constraints

- Adhere strictly to **ASD-STE100 (Simplified Technical English)** (sentences $\le$ 20-25 words, active voice, imperative mood).
- Use native **Mermaid diagrams** (`flowchart TD`, `flowchart LR`).
- All file edits must preserve existing comments and docstrings.
- Conventional Commits enforced (`feat:`, `docs:`, `test:`, `ci:`).

---

### Task 1: Universal Agent Rules (`rules/AGENTS.md`, `rules/CLAUDE.md`, `rules/GEMINI.md`)

**Files:**
- Modify: `rules/AGENTS.md`
- Modify: `rules/CLAUDE.md`
- Modify: `rules/GEMINI.md`

**Interfaces:**
- Consumes: Spec Sections 2, 3, 4.
- Produces: Universal rule requirements for all AI coding agents operating on projects using this toolbelt.

- [ ] **Step 1: Update `rules/AGENTS.md` with Section 4 testing discipline and Anti-Test Theatre rules**
  - Add explicit "Anti-Test Theatre & Representative Verification" subclause to Section 4.
  - Mandate the Four Pillars: Real Over Mock, Outcomes Over Calls, Representative Dogfooding/Smoke Loops, and Value Over Numeric Vanity.
  - Ban mocking internal interfaces, repository mocks, and `mock.Verify()` as primary assertion.
  - Add the Deterministic Test Budget Formula and 5-Question Mock Decision Tree.

- [ ] **Step 2: Update `rules/CLAUDE.md` and `rules/GEMINI.md`**
  - Ensure CLAUDE.md and GEMINI.md include anti-test theatre rules and links to `standards/TESTING_HARNESS_PATTERNS.md`.

- [ ] **Step 3: Verify changes against markdown formatting and ASD-STE100**
  - Confirm short sentences and no markdown syntax errors.

- [ ] **Step 4: Commit**
  ```bash
  git add rules/AGENTS.md rules/CLAUDE.md rules/GEMINI.md
  git commit -m "docs(rules): codify anti-test theatre pillars and deterministic testing protocols"
  ```

---

### Task 2: Testing Standards & Style Guide (`standards/TESTING_HARNESS_PATTERNS.md`, `standards/ENGINEERING_STYLE_GUIDE.md`)

**Files:**
- Modify: `standards/TESTING_HARNESS_PATTERNS.md`
- Modify: `standards/ENGINEERING_STYLE_GUIDE.md`

**Interfaces:**
- Consumes: Spec Sections 2, 3, 4.
- Produces: The master standard reference document for simulation, harnesses, and anti-test theatre.

- [ ] **Step 1: Expand `standards/TESTING_HARNESS_PATTERNS.md`**
  - Embed the Four Pillars in Section 1.
  - Insert the 12-Dimension Banned vs. Mandated Patterns Matrix.
  - Document the Deterministic Test Budget Formula: $\text{Nominal} + N_{\text{Branches}} + N_{\text{0-1-N Boundaries}} + N_{\text{Disturbances}}$.
  - Document the Deterministic 5-Question Mock Decision Tree with Mermaid diagram.

- [ ] **Step 2: Update `standards/ENGINEERING_STYLE_GUIDE.md`**
  - Reference the Anti-Test Theatre rules under Testing & Code Quality section.
  - Explicitly mark mock-heavy testing without integration tests as a banned code smell.

- [ ] **Step 3: Commit**
  ```bash
  git add standards/TESTING_HARNESS_PATTERNS.md standards/ENGINEERING_STYLE_GUIDE.md
  git commit -m "docs(standards): add 12-dimension anti-test theatre matrix and deterministic algorithms"
  ```

---

### Task 3: Agent Skills Update (`test-harness-builder`, `engineering-archetype`)

**Files:**
- Modify: `.agents/skills/test-harness-builder/SKILL.md`
- Modify: `.agents/skills/engineering-archetype/SKILL.md`

**Interfaces:**
- Consumes: Task 1 and Task 2 standards.
- Produces: Actionable instructions for agents when constructing harnesses or evaluating archetypes.

- [ ] **Step 1: Update `.agents/skills/test-harness-builder/SKILL.md`**
  - Add mandatory checklist step: "Run Deterministic Test Budget Formula".
  - Add mandatory checklist step: "Pass dependencies through 5-Question Mock Decision Tree".
  - Add "Anti-Test-Theatre Guardrails" section with Banned vs. Mandated table.

- [ ] **Step 2: Update `.agents/skills/engineering-archetype/SKILL.md`**
  - Ensure Testing Strategy sections across C#, Python, TypeScript, and C++ explicitly require representative integration harnesses and ban mock-heavy unit test theatre.

- [ ] **Step 3: Commit**
  ```bash
  git add .agents/skills/test-harness-builder/SKILL.md .agents/skills/engineering-archetype/SKILL.md
  git commit -m "feat(skills): embed deterministic test budget and mock tree into test-harness-builder"
  ```

---

### Task 4: Polyglot Archetype Blueprints Update (`archetypes/*.md`)

**Files:**
- Modify: `archetypes/fullstack-dotnet-react.md`
- Modify: `archetypes/console-cli-dotnet.md`
- Modify: `archetypes/python-fastapi-mcp.md`
- Modify: `archetypes/react-ts-vite-ui.md`
- Modify: `archetypes/native-cpp-algorithms.md`

**Interfaces:**
- Consumes: Spec Section 5 recipes.
- Produces: Concrete test recipes embedded directly into each archetype specification.

- [ ] **Step 1: Update `archetypes/fullstack-dotnet-react.md` and `console-cli-dotnet.md`**
  - Add `WebApplicationFactory<Program>` + in-memory SQLite WAL recipe.
  - Add CLI execution fixture recipe for subprocess testing.

- [ ] **Step 2: Update `archetypes/python-fastapi-mcp.md`**
  - Add `httpx.AsyncClient` ASGI in-memory transport + in-memory SQLite recipe.
  - Add FastMCP `InMemorySessionClient` tool execution recipe.

- [ ] **Step 3: Update `archetypes/react-ts-vite-ui.md` and `native-cpp-algorithms.md`**
  - Add Playwright E2E + `playwright-layout-inspector` 4-point audit recipe.
  - Add C++ GoogleTest `TEST_P` boundary parameter sweep recipe.

- [ ] **Step 4: Commit**
  ```bash
  git add archetypes/
  git commit -m "docs(archetypes): add representative dogfood test recipes across polyglot archetypes"
  ```

---

### Task 5: Verification Engine & Static Test Theatre Audit (`templates/scripts/verify_release.py`)

**Files:**
- Modify: `templates/scripts/verify_release.py`

**Interfaces:**
- Consumes: Spec Section 6.1 requirements.
- Produces: `--audit-tests` CLI flag that scans test directories and warns/fails on mock dominance or missing integration baselines.

- [ ] **Step 1: Write unit tests for test theatre auditor in `templates/scripts/verify_release.py`**
  - Test mock-to-assertion ratio detection.
  - Test detection of test files with `.Verify()` / `assert_called_with` and 0 state assertions.
  - Test detection of projects with mock libraries but 0 integration harnesses.

- [ ] **Step 2: Implement `--audit-tests` in `templates/scripts/verify_release.py`**
  - Add `audit_test_theatre(repo_root: Path) -> List[str]` function.
  - Scan `.cs`, `.py`, `.ts`, `.tsx`, `.cpp` test files.
  - Detect mock verification dominance over concrete assertions.
  - Flag tautological assertions (`Assert.Equal(x, x)`).
  - Wire `--audit-tests` into argument parser and general verification runner.

- [ ] **Step 3: Run verification tests and self-audit**
  - Execute `python3 templates/scripts/verify_release.py --audit-tests`.
  - Ensure zero regressions on existing codebase.

- [ ] **Step 4: Commit**
  ```bash
  git add templates/scripts/verify_release.py
  git commit -m "feat(tooling): implement --audit-tests static heuristic check in verify_release.py"
  ```

---

### Task 6: CI Quality Gate Workflows (`templates/workflows/ci.yml`, `.github/workflows/ci.yml`)

**Files:**
- Modify: `templates/workflows/ci.yml`
- Modify: `.github/workflows/ci.yml`

**Interfaces:**
- Consumes: Task 5 CLI command.
- Produces: Automated GitHub Actions validation blocking mock-heavy test theatre in PRs.

- [ ] **Step 1: Update `.github/workflows/ci.yml` and `templates/workflows/ci.yml`**
  - Add step in Tier 2 quality gate:
    ```yaml
    - name: Audit Test Theatre & Mock Dominance
      run: python3 templates/scripts/verify_release.py --audit-tests
    ```

- [ ] **Step 2: Commit**
  ```bash
  git add .github/workflows/ci.yml templates/workflows/ci.yml
  git commit -m "ci: integrate test theatre audit into Tier 2 CI quality gate"
  ```

---

### Task 7: VitePress Documentation Site Synchronization & Build Verification

**Files:**
- Modify/Create: `docs/standards/testing-harness-patterns.md`
- Modify/Create: `docs/standards/engineering-style-guide.md`
- Modify/Create: `docs/rules/agents.md`
- Modify/Create: `docs/archetypes/*.md`

**Interfaces:**
- Consumes: Tasks 1-4 markdown files.
- Produces: Synchronized VitePress documentation that compiles cleanly with `npm run docs:build`.

- [ ] **Step 1: Synchronize all updated markdown documents to `docs/`**
  - Copy updated standards, rules, and archetypes into corresponding `docs/` paths.

- [ ] **Step 2: Run VitePress build and link verification**
  - Run `npm run docs:build`
  - Run `python3 templates/scripts/verify_release.py --all`
  - Verify zero build errors, zero broken markdown links.

- [ ] **Step 3: Commit**
  ```bash
  git add docs/
  git commit -m "docs: synchronize anti-test-theatre standards and recipes to VitePress site"
  ```
