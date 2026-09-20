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
      text: Browse Archetypes
      link: /archetypes/
    - theme: alt
      text: GitHub
      link: https://github.com/spelech/AgenticEngineeringToolbelt

features:
  - title: Living Documentation (ASD-STE100)
    details: Clear, concise technical writing with active voice and under 25 words per sentence. Native Mermaid diagrams visualize system architecture.
  - title: Observable Systems & Simulation Harnesses
    details: Dynamic control loops with diagnostic tap points, parameter sweeps, and standardized 6-part feedback envelopes for developers and AI.
  - title: Traditional Git Flow Automation
    details: Deterministic branch topology with develop, main, and release branches. GitHub Actions workflows automate verification and publishing.
  - title: APIs First, MCP Later
    details: Encapsulate domain logic in typed, self-contained libraries and APIs. Expose Model Context Protocol tools strictly as thin wrapper adapters.
---

## 🏛️ System Architecture Topology

The following diagram illustrates how autonomous agents and consumer software repositories consume the **AgenticEngineeringToolbelt**:

```mermaid
flowchart TD
    subgraph Toolbelt["AgenticEngineeringToolbelt Repository"]
        Standards["standards/<br>• Style Guide<br>• Simulation Harnesses<br>• CI/CD Pipelines<br>• ASD-STE100 Rules"]
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

## 🚀 Quickstart Guide

Install the toolbelt as a submodule in any software repository:

```bash
# Add the toolbelt as a git submodule
git submodule add https://github.com/spelech/AgenticEngineeringToolbelt.git .toolbelt
git submodule update --init --recursive

# Run the installation script to link agent skills
bash .toolbelt/scripts/install.sh
```

### Local Documentation Development

Launch the VitePress live documentation development server:

```bash
# Install dependencies
npm install

# Start local dev server
npm run docs:dev

# Build static assets
npm run docs:build
```

---

## 📐 Core Engineering Standards

1. [Engineering Style Guide](/standards/engineering-style-guide): Architecture principles, language matrix, and solid conventions.
2. [Simulation & Control Harnesses](/standards/testing-harness-patterns): Observation, diagnostic tap points, and 6-part feedback envelopes.
3. [CI/CD Pipelines](/standards/ci-cd-pipelines): 4-stage GitHub Actions automation and quality gates.
4. [ASD-STE100 Writing Rules](/standards/asd-ste100): Simplified Technical English standards for documentation.
