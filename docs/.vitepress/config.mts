import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(
  defineConfig({
    title: 'Agentic Engineering Toolbelt',
    description: 'Engineering standards, archetypes, simulation harnesses, and agent rules for high-reliability systems.',
    base: process.env.GITHUB_ACTIONS ? '/AgenticEngineeringToolbelt/' : '/',
    themeConfig: {
      siteTitle: 'Agentic Engineering Toolbelt',
      nav: [
        { text: 'Home', link: '/' },
        { text: 'Standards', link: '/standards/engineering-style-guide' },
        { text: 'Archetypes', link: '/archetypes/' },
        { text: 'Rules & Skills', link: '/rules/' }
      ],
      sidebar: [
        {
          text: 'Standards',
          items: [
            { text: 'Engineering Style Guide', link: '/standards/engineering-style-guide' },
            { text: 'Simulation & Control Harnesses', link: '/standards/testing-harness-patterns' },
            { text: 'CI/CD Pipelines', link: '/standards/ci-cd-pipelines' },
            { text: 'ASD-STE100 Writing Rules', link: '/standards/asd-ste100' }
          ]
        },
        {
          text: 'Archetypes',
          items: [
            { text: 'Catalog Overview', link: '/archetypes/' },
            { text: '.NET Console & CLI', link: '/archetypes/console-cli-dotnet' },
            { text: 'Controls Fullstack (.NET + React)', link: '/archetypes/controls-fullstack-dotnet-react' },
            { text: 'C++ Native Algorithms', link: '/archetypes/native-cpp-algorithms' },
            { text: 'Python FastAPI & MCP', link: '/archetypes/python-fastapi-mcp' },
            { text: 'React TS Vite UI', link: '/archetypes/react-ts-vite-ui' }
          ]
        },
        {
          text: 'Rules & Skills',
          items: [
            { text: 'Context Overview', link: '/rules/' },
            { text: 'Universal Agent Rules (AGENTS.md)', link: '/rules/agents' },
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
