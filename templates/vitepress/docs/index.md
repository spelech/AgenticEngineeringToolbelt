---
layout: home

hero:
  name: "Project Documentation"
  text: "Living Architecture & System Specifications"
  tagline: "Observable software architecture, test harness guidelines, and quality gates."
  actions:
    - theme: brand
      text: Explore Architecture
      link: /architecture
    - theme: alt
      text: System Requirements
      link: /requirements

features:
  - title: Observable Architecture
    details: Living specifications keep documentation synchronized with implementation. Native Mermaid diagrams visualize subsystem topology.
  - title: Simulation & Control Harnesses
    details: Observable dynamic loops with diagnostic tap points and standardized 6-part feedback envelopes for developers and AI.
  - title: Traditional Git Flow Automation
    details: Structured branching with develop, main, and release stabilization gates enforced by multi-stage CI/CD pipelines.
---

## 🏛️ Architecture Overview

```mermaid
flowchart TD
    Client["Client / User Interface"] --> API["Core Application API"]
    API --> Domain["Domain Engine & State Machine"]
    Domain --> Database["Data Storage / External Adapters"]
    Harness["Simulation & Control Harness"] -.->|"Diagnostic Tap Points"| Domain
```

---

## 🚀 Getting Started

1. **Architecture**: Read [System Overview](/architecture) for subsystem topology.
2. **Requirements**: Review [System Requirements](/requirements) for behavioral specifications.
3. **Changelog**: Audit [Changelog](/changelog) for historical version releases.
