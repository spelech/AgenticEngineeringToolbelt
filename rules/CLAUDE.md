# Claude Code Agent Configuration (CLAUDE.md)

This repository adheres to the architecture, coding standards, test harness conventions, and CI/CD quality gates codified in **AgenticEngineeringToolbelt**.

---

## Master Rules Reference

Always follow the complete guidelines in:
- [**Universal Agent Rules (`AGENTS.md`)**](AGENTS.md)
- [**Master Engineering Style Guide**](../standards/ENGINEERING_STYLE_GUIDE.md)
- [**Simulation and Control Harnesses**](../standards/TESTING_HARNESS_PATTERNS.md)

---

## Active Skills

- [**`engineering-archetype`**](../.agents/skills/engineering-archetype/SKILL.md): Enforces master architectural standards across C#, Python, TypeScript, and C++.
- [**`scaffold-project`**](../.agents/skills/scaffold-project/SKILL.md): Scaffolds projects adhering to traditional Git Flow, living documentation, and 4-stage CI/CD.
- [**`test-harness-builder`**](../.agents/skills/test-harness-builder/SKILL.md): Builds closed-loop simulation harnesses, diagnostic tap points, Playwright UI drivers, and 6-part feedback envelopes.

---

## Core Execution Tenets

### Workflow and Architecture Tenets

1. **Traditional Git Flow**: Work in `feature/*` branches off `develop`. Release through `release/*` branches to `main` with SemVer tags and sync back to `develop`. Route urgent fixes through `hotfix/*` off `main` (see [Traditional Git Flow Discipline](../standards/ENGINEERING_STYLE_GUIDE.md#traditional-git-flow-discipline)).
2. **APIs First, MCP Later**: Keep domain logic inside typed, standalone libraries and REST APIs. Expose Model Context Protocol (MCP) tools strictly as thin wrappers (see [APIs First, MCP Later](../standards/ENGINEERING_STYLE_GUIDE.md#apis-first-mcp-later)).
3. **Living Documentation Standards**: Apply [Technical Writing Standards](../docs/standards/asd-ste100.md) (≤ 25 words per sentence, active voice, imperative mood, section-scoped cross-links). Embed native Mermaid diagrams and publish via VitePress.

### Verification and Anti-Test Theatre Tenets

1. **Simulation and Control Harnesses**: Treat software as an observable dynamic system with [Diagnostic Tap Points](../standards/TESTING_HARNESS_PATTERNS.md#diagnostic-tap-points-and-agent-introspection), stress loops, disturbance injection, and [Six-Part Agent Feedback Envelopes](../standards/TESTING_HARNESS_PATTERNS.md#the-six-part-agent-feedback-envelope).
2. **Tiered Testing Cadence**: Follow the [Tiered Testing Cadence](../standards/TESTING_HARNESS_PATTERNS.md#tiered-testing-cadence) across Tier 1 (inner loop on demand), Tier 2 (stabilization gate before manual testing), and Tier 3 (full matrix, harness sweeps, and Playwright audits before PR or release).
3. **Anti-Test Theatre and Deterministic Protocols**:
   - Test with real implementations (SQLite WAL, real DI, and full HTTP roundtrips) per the [Four Pillars of Anti-Test Theatre](../standards/TESTING_HARNESS_PATTERNS.md#the-four-pillars-of-anti-test-theatre).
   - Never mock internal interfaces or repositories, and never use `mock.Verify()` as a primary assertion.
   - Compute required test suite size using the [Deterministic Test Budget Formula](../standards/TESTING_HARNESS_PATTERNS.md#deterministic-test-budget-formula) (`1 + Branches + Boundaries + Disturbances`).
   - Evaluate every dependency with the [Deterministic Five-Question Mock Decision Tree](../standards/TESTING_HARNESS_PATTERNS.md#deterministic-five-question-mock-decision-tree).
