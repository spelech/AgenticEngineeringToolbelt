---
layout: home

hero:
  name: "Agentic Engineering Toolbelt"
  text: "High-Reliability Archetypes & Living Documentation"
  tagline: "Rigorous standards, observable simulation harnesses, and context rules for human-AI pair programming."
  actions:
    - theme: brand
      text: Get Started
      link: /standards/engineering-style-guide
    - theme: alt
      text: Architecture & Doc Map
      link: /architecture
    - theme: alt
      text: Browse Archetypes
      link: /archetypes/
    - theme: alt
      text: GitHub
      link: https://github.com/spelech/AgenticEngineeringToolbelt

features:
  - title: Living Architecture & Documentation
    details: Clear, scannable technical guides with active voice and concise prose. Native Mermaid diagrams visualize system architecture alongside source code.
  - title: Observable Systems & Simulation Harnesses
    details: Dynamic control loops with diagnostic tap points, parameter sweeps, and standardized 6-part feedback envelopes for developers and AI.
  - title: Traditional Git Flow Automation
    details: Deterministic branch topology with develop, main, and release branches. GitHub Actions workflows automate verification and publishing.
  - title: APIs First, MCP Later
    details: Encapsulate domain logic in typed, self-contained libraries and APIs. Expose Model Context Protocol tools strictly as thin wrapper adapters.
---

## System Architecture Topology

The following diagram illustrates how autonomous agents and consumer software repositories integrate the **AgenticEngineeringToolbelt**:

```mermaid
flowchart TD
    subgraph Toolbelt["AgenticEngineeringToolbelt Repository"]
        Standards["standards/<br>• Style Guide<br>• Simulation Harnesses<br>• CI/CD Pipelines<br>• Technical Writing Guide"]
        Archetypes["archetypes/<br>• .NET CLI<br>• Controls Fullstack<br>• C++ Native<br>• Python FastAPI<br>• React UI"]
        Skills[".agents/skills/<br>• engineering-archetype<br>• scaffold-project<br>• test-harness-builder"]
        Rules["rules/<br>• AGENTS.md<br>• GEMINI.md<br>• CLAUDE.md"]
        Templates["templates/<br>• configs/<br>• docs/<br>• workflows/<br>• scripts/"]
    end

    subgraph Agents["Autonomous AI Agents & Runtimes"]
        Antigravity["Google Antigravity / Gemini CLI"]
        Claude["Claude Code"]
        Cursor["Cursor IDE / OpenClaw"]
    end

    subgraph Projects["Downstream Software Projects"]
        ProjectA["Consumer Repo (.toolbelt submodule)"]
        ProjectB["Scaffolded New Project"]
    end

    Standards --> Skills & Rules
    Archetypes --> Templates
    Skills --> Antigravity & Claude
    Rules --> Projects & Cursor
    Templates --> Projects
```

---

## Quickstart Guide

### Submodule Installation

Add the toolbelt as a Git submodule in any software repository and link the executable agent skills:

```bash
# Add the toolbelt as a git submodule
git submodule add https://github.com/spelech/AgenticEngineeringToolbelt.git .toolbelt
git submodule update --init --recursive

# Run the installation script to link agent skills
bash .toolbelt/scripts/install.sh
```

### Local Documentation Development

Launch the VitePress live documentation development server to preview guides and diagrams locally:

```bash
# Install dependencies
npm install

# Start local dev server
npm run docs:dev

# Build static assets
npm run docs:build
```

---

## Core Navigation

| Section | Focus Area | Primary Entry Points |
| :--- | :--- | :--- |
| **Architecture & Map** | Subsystem topology, Git Flow model, and cross-linking map. | [System Architecture & Documentation Map](/architecture) |
| **Engineering Standards** | Core architectural rules, simulation harnesses, and CI/CD gates. | [Master Engineering Style Guide](/standards/engineering-style-guide) • [Simulation & Control Harnesses](/standards/testing-harness-patterns) • [Multi-Stage CI/CD Pipelines](/standards/ci-cd-pipelines) |
| **Polyglot Archetypes** | Complete stack blueprints across C#, Python, TypeScript, and C++. | [Archetypes Catalog](/archetypes/) • [Fullstack (.NET + React)](/archetypes/fullstack-dotnet-react) • [.NET Console & CLI](/archetypes/console-cli-dotnet) • [Python FastAPI & FastMCP](/archetypes/python-fastapi-mcp) • [React, TS & Vite UI](/archetypes/react-ts-vite-ui) • [C++ Native Algorithms](/archetypes/native-cpp-algorithms) |
| **Agent Rules & Skills** | Drop-in agent context files and executable skill manifests. | [Rules & Context Overview](/rules/) • [Universal Agent Rules (AGENTS.md)](/rules/agents) • [Executable Skills](/rules/skills) |
