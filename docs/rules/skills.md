---
title: "Agent Skills Manifests"
description: "Composable skills for scaffolding projects, building simulation harnesses, enforcing archetypes, and running multi-lens code reviews."
---

# Agent Skills Manifests

The toolbelt provides four executable skills compatible with Antigravity, Gemini CLI, Claude Code, and Cursor.

---

## Engineering Archetype Skill

Enforces Steven T. Pelech's master engineering archetype across C#, Python, TypeScript, and C++.
- **Manifest Path**: `.agents/skills/engineering-archetype/SKILL.md`
- **Core Standards**: [SOLID and Modularity](/standards/engineering-style-guide#solid-and-modularity), [APIs First, MCP Later](/standards/engineering-style-guide#apis-first-mcp-later), [Traditional Git Flow Discipline](/standards/engineering-style-guide#traditional-git-flow-discipline), and [Tiered Testing Cadence](/standards/testing-harness-patterns#tiered-testing-cadence).

---

## Test Harness Builder Skill

Generates controls-grade simulation and control harnesses for developers and AI agents.
- **Manifest Path**: `.agents/skills/test-harness-builder/SKILL.md`
- **Core Capabilities**: [Deterministic Test Budget Formula](/standards/testing-harness-patterns#deterministic-test-budget-formula), [Five-Question Mock Decision Tree](/standards/testing-harness-patterns#deterministic-five-question-mock-decision-tree), [Diagnostic Tap Points](/standards/testing-harness-patterns#diagnostic-tap-points-and-agent-introspection), high-volume stress loops, and [Six-Part Agent Feedback Envelopes](/standards/testing-harness-patterns#the-six-part-agent-feedback-envelope).

---

## Scaffold Project Skill

Automates scaffolding of new repositories conforming to any of the five [Curated Engineering Archetypes](/archetypes/).
- **Manifest Path**: `.agents/skills/scaffold-project/SKILL.md`
- **Deliverables**: Directory layout, build manifests, [Multi-Stage CI/CD Pipelines](/standards/ci-cd-pipelines), and VitePress living documentation baseline.

---

## Code Review Foci Skill

Executes a read-only, multi-lens code review across the six orthogonal reviewer foci before opening or finalizing a pull request.
- **Manifest Path**: `.agents/skills/code-review-foci/SKILL.md`
- **Core Capabilities**: [The Six Reviewer Foci](/standards/code-review-and-guardrails#multi-lens-code-review-and-the-six-reviewer-foci), [Requirements Traceability Audit](/standards/code-review-and-guardrails#requirements-traceability-and-living-srs-catalogs), and [Operational and Deployment Guardrails](/standards/code-review-and-guardrails#operational-context-and-deployment-guardrails).
