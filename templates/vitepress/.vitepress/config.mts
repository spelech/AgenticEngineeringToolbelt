import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(
  defineConfig({
    title: 'Project Documentation',
    description: 'Living architecture and engineering documentation site.',
    base: process.env.GITHUB_ACTIONS ? `/${process.env.GITHUB_REPOSITORY?.split('/')[1] || ''}/` : '/',
    themeConfig: {
      siteTitle: 'Project Docs',
      nav: [
        { text: 'Home', link: '/' },
        { text: 'Architecture', link: '/architecture' },
        { text: 'Requirements', link: '/requirements' }
      ],
      sidebar: [
        {
          text: 'Architecture & Design',
          items: [
            { text: 'System Overview', link: '/architecture' },
            { text: 'System Requirements', link: '/requirements' },
            { text: 'Changelog', link: '/changelog' }
          ]
        },
        {
          text: 'Standards & Quality',
          items: [
            { text: 'Style Guide & Conventions', link: '/standards/style-guide' },
            { text: 'Simulation & Control Harnesses', link: '/standards/simulation-harnesses' }
          ]
        }
      ],
      socialLinks: [
        { icon: 'github', link: 'https://github.com/' }
      ],
      footer: {
        message: 'Built with VitePress and AgenticEngineeringToolbelt.',
        copyright: 'Living Documentation Baseline'
      }
    },
    mermaid: {
      theme: 'default'
    }
  })
)
