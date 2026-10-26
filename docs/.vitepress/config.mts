import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(
  defineConfig({
    title: 'Agentic Engineering Toolbelt',
    description: 'Engineering standards, archetypes, simulation harnesses, and agent rules for high-reliability systems.',
    base: process.env.GITHUB_ACTIONS ? '/AgenticEngineeringToolbelt/' : '/',
    themeConfig: {
      siteTitle: 'Agentic Engineering Toolbelt',
      outline: {
        level: [2, 3],
        label: 'On this page'
      },
      search: {
        provider: 'local'
      },
      nav: [
        { text: 'Home', link: '/' },
        { text: 'Architecture', link: '/architecture' },
        { text: 'Standards', link: '/standards/engineering-style-guide' },
        { text: 'Archetypes', link: '/archetypes/' },
        { text: 'Rules & Skills', link: '/rules/' }
      ],
      sidebar: [
        {
          text: 'Overview & Architecture',
          collapsed: false,
          items: [
            { text: 'Toolbelt Overview', link: '/' },
            {
              text: 'System Architecture & Map',
              link: '/architecture',
              collapsed: true,
              items: [
                { text: 'Consumption Topology', link: '/architecture#system-overview-and-consumption-topology' },
                { text: 'Subsystem Breakdown', link: '/architecture#subsystem-breakdown' },
                { text: 'Git Flow Release Model', link: '/architecture#traditional-git-flow-and-release-model' },
                { text: 'Testing Cadence', link: '/architecture#simulation-and-controls-testing-cadence' },
                { text: 'Documentation & Link Map', link: '/architecture#documentation-and-cross-linking-map' }
              ]
            }
          ]
        },
        {
          text: 'Engineering Standards',
          collapsed: false,
          items: [
            {
              text: 'Master Style Guide',
              link: '/standards/engineering-style-guide',
              collapsed: true,
              items: [
                { text: 'Collaboration & Git Flow', link: '/standards/engineering-style-guide#collaboration-and-iterative-design-model' },
                { text: 'Foundational Principles', link: '/standards/engineering-style-guide#foundational-engineering-principles' },
                { text: 'Language & Archetype Matrix', link: '/standards/engineering-style-guide#polyglot-language-and-archetype-standards' },
                { text: 'Backend & Persistence', link: '/standards/engineering-style-guide#backend-architecture-and-persistence' },
                { text: 'Frontend Architecture', link: '/standards/engineering-style-guide#frontend-architecture' },
                { text: 'Testing & Harnesses', link: '/standards/engineering-style-guide#testing-and-simulation-harnesses' },
                { text: 'Documentation & CI/CD', link: '/standards/engineering-style-guide#living-documentation-and-automation' }
              ]
            },
            {
              text: 'Simulation & Control Harnesses',
              link: '/standards/testing-harness-patterns',
              collapsed: true,
              items: [
                { text: 'Four Pillars of Verification', link: '/standards/testing-harness-patterns#observable-dynamic-systems-and-the-four-pillars' },
                { text: 'Banned vs. Mandated Matrix', link: '/standards/testing-harness-patterns#banned-and-mandated-patterns-matrix' },
                { text: 'Deterministic Agent Protocols', link: '/standards/testing-harness-patterns#deterministic-testing-protocols-for-ai-agents' },
                { text: 'Tiered Testing Cadence', link: '/standards/testing-harness-patterns#tiered-testing-cadence' },
                { text: 'Harness Types & Tap Points', link: '/standards/testing-harness-patterns#harness-types-and-simulation-patterns' },
                { text: 'UI Layout Auditing', link: '/standards/testing-harness-patterns#ui-layout-stability-and-ergonomics-auditing' },
                { text: 'Six-Part Feedback Envelope', link: '/standards/testing-harness-patterns#the-six-part-agent-feedback-envelope' },
                { text: 'Polyglot Harness Recipes', link: '/standards/testing-harness-patterns#polyglot-archetype-test-harness-recipes' }
              ]
            },
            {
              text: 'Multi-Stage CI/CD Pipelines',
              link: '/standards/ci-cd-pipelines',
              collapsed: true,
              items: [
                { text: 'Pipeline Topology', link: '/standards/ci-cd-pipelines#pipeline-topology' },
                { text: 'Git Flow Trigger Matrix', link: '/standards/ci-cd-pipelines#git-flow-trigger-matrix' },
                { text: 'Stage Descriptions', link: '/standards/ci-cd-pipelines#stage-descriptions' }
              ]
            },
            {
              text: 'Code Review & Guardrails',
              link: '/standards/code-review-and-guardrails',
              collapsed: true,
              items: [
                { text: 'The Six Reviewer Foci', link: '/standards/code-review-and-guardrails#multi-lens-code-review-and-the-six-reviewer-foci' },
                { text: 'Requirements Traceability', link: '/standards/code-review-and-guardrails#requirements-traceability-and-living-srs-catalogs' },
                { text: 'Operational Guardrails', link: '/standards/code-review-and-guardrails#operational-context-and-deployment-guardrails' }
              ]
            },
            {
              text: 'Technical Writing Standards',
              link: '/standards/asd-ste100',
              collapsed: true,
              items: [
                { text: 'Purpose & Style Foundations', link: '/standards/asd-ste100#purpose-and-style-foundations' },
                { text: 'Core Writing Rules', link: '/standards/asd-ste100#core-writing-rules' },
                { text: 'Structure, Links & Symbols', link: '/standards/asd-ste100#structural-and-formatting-rules' },
                { text: 'Verification Checklist', link: '/standards/asd-ste100#verification-checklist' }
              ]
            }
          ]
        },
        {
          text: 'Polyglot Archetypes',
          collapsed: false,
          items: [
            { text: 'Catalog Overview', link: '/archetypes/' },
            {
              text: 'Fullstack (.NET + React)',
              link: '/archetypes/fullstack-dotnet-react',
              collapsed: true,
              items: [
                { text: 'Core Architectural Tenets', link: '/archetypes/fullstack-dotnet-react#core-architectural-tenets' },
                { text: 'Backend Architecture', link: '/archetypes/fullstack-dotnet-react#backend-architecture' },
                { text: 'Frontend Architecture', link: '/archetypes/fullstack-dotnet-react#frontend-architecture' },
                { text: 'Testing & Harnesses', link: '/archetypes/fullstack-dotnet-react#testing-and-simulation-harnesses' }
              ]
            },
            {
              text: '.NET Console & CLI',
              link: '/archetypes/console-cli-dotnet',
              collapsed: true,
              items: [
                { text: 'Technology Stack', link: '/archetypes/console-cli-dotnet#technology-stack' },
                { text: 'Implementation Patterns', link: '/archetypes/console-cli-dotnet#core-implementation-patterns' },
                { text: 'Subprocess Test Harness', link: '/archetypes/console-cli-dotnet#representative-subprocess-test-harness' }
              ]
            },
            {
              text: 'Python FastAPI & FastMCP',
              link: '/archetypes/python-fastapi-mcp',
              collapsed: true,
              items: [
                { text: 'APIs First, MCP Later', link: '/archetypes/python-fastapi-mcp#architectural-philosophy-apis-first-mcp-later' },
                { text: 'FastMCP Integration', link: '/archetypes/python-fastapi-mcp#fastmcp-integration-pattern' },
                { text: 'Testing & Recipes', link: '/archetypes/python-fastapi-mcp#testing-cadence-and-representative-recipes' }
              ]
            },
            {
              text: 'React, TS & Vite UI',
              link: '/archetypes/react-ts-vite-ui',
              collapsed: true,
              items: [
                { text: 'Technology Stack', link: '/archetypes/react-ts-vite-ui#technology-stack' },
                { text: 'Zustand Selector Discipline', link: '/archetypes/react-ts-vite-ui#zustand-store-with-granular-selector-discipline' },
                { text: 'Playwright Layout Audit', link: '/archetypes/react-ts-vite-ui#representative-test-harness-playwright-and-layout-audit' }
              ]
            },
            {
              text: 'C++ Native Algorithms',
              link: '/archetypes/native-cpp-algorithms',
              collapsed: true,
              items: [
                { text: 'Technology Stack', link: '/archetypes/native-cpp-algorithms#technology-stack' },
                { text: 'C-ABI Interop Pattern', link: '/archetypes/native-cpp-algorithms#c-abi-interop-pattern-for-csharp-and-python' },
                { text: 'Parameter Sweep Harness', link: '/archetypes/native-cpp-algorithms#representative-test-harness-parameter-sweeps' }
              ]
            }
          ]
        },
        {
          text: 'Rules & Skills',
          collapsed: false,
          items: [
            { text: 'Context Overview', link: '/rules/' },
            {
              text: 'Universal Agent Rules (AGENTS.md)',
              link: '/rules/agents',
              collapsed: true,
              items: [
                { text: 'Collaboration & Workflow', link: '/rules/agents#collaboration-and-workflow-discipline' },
                { text: 'Code & Architecture', link: '/rules/agents#core-code-and-architectural-discipline' },
                { text: 'Polyglot Matrix', link: '/rules/agents#polyglot-language-matrix' },
                { text: 'Testing & Verification', link: '/rules/agents#testing-and-agent-verification-protocol' },
                { text: 'Code Review & Guardrails', link: '/rules/agents#multi-lens-code-review-and-operational-guardrails' }
              ]
            },
            { text: 'Claude Code (CLAUDE.md)', link: '/rules/claude' },
            { text: 'Antigravity / Gemini (GEMINI.md)', link: '/rules/gemini' },
            { text: 'Toolbelt Skills Manifests', link: '/rules/skills' }
          ]
        }
      ],
      socialLinks: [
        { icon: 'github', link: 'https://github.com/spelech/AgenticEngineeringToolbelt' }
      ],
      footer: {
        message: 'Released under the MIT License.',
        copyright: 'Copyright © 2026 Steven T. Pelech'
      }
    },
    mermaid: {
      theme: 'default'
    }
  })
)
