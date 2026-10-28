---
name: mermaid-live
description: Use when generating, formatting, or rendering Mermaid diagrams to ensure proper syntax sanitization, pako-compressed state generation, URL shortening, and clickable Mermaid Live links.
---

# Mermaid Live Skill

This skill provides an automated workflow and helper CLI for generating interactive, shareable Mermaid Live Editor links (`https://mermaid.live/edit#pako:...`) and shortened URLs (`https://tinyurl.com/...`) from Mermaid diagram sources.

## Why This Skill Exists

1. **Terminal & Mobile Truncation**: Large Mermaid diagrams rendered in Markdown can be truncated or difficult to explore in CLI chat clients or mobile devices.
2. **Mermaid Parser Edge Cases**: Unquoted parentheses `(...)`, brackets, or colons inside edge labels (e.g. `-->|Task (direct :8032)|`) cause fatal Mermaid syntax errors (`Parse error: Expecting ... got 'PS'`).
3. **URL Bloat**: Pako-compressed state strings can exceed several hundred characters, cluttering markdown responses. Employing an automated shortener provides a clean, compact link alongside the direct link.

---

## Tooling & Command Line Interface

The repository includes a dedicated generator utility: `mermaid-live` (or `/containers/scripts/mermaid_live.py`).

### Quick Usage

```bash
# From inline string (outputs markdown block with shortened and direct links):
mermaid-live -s "flowchart TD; A[Start] --> B[End]"

# From a file or heredoc:
mermaid-live << 'EOF'
flowchart LR
    A -->|"Step (1)"| B
    B --> C
EOF

# Get URL only:
mermaid-live -s "graph TD; A --> B" --url-only

# Output as JSON:
mermaid-live -f my_diagram.mmd --json

# Output direct pako link (default):
mermaid-live -s "graph TD; A --> B"

# Publish directly to owned Agent Preview Hub (short, private domain, zero enterprise blocks):
mermaid-live -s "graph TD; A --> B" --preview my-diagram --title "My Diagram"

# Explicitly shorten via da.gd (optional):
mermaid-live -s "graph TD; A --> B" --shorten
```

---

## Formatting Convention for Agent Responses

When outputting diagrams in chat turns, artifacts, or living documentation:

1. Always wrap the diagram in ````mermaid ... ```` code fences.
2. Provide a clean direct clickable link using standard Markdown hyperlink syntax directly below the diagram block:
   ```markdown
   🔍 **[Open in Mermaid Live (Interactive Full View)](https://mermaid.live/edit#pako:<compressed_token>)**
   ```
   *Note: Standard Markdown anchor text hides the long URL completely. Third-party URL shorteners are avoided by default to prevent enterprise security proxy blocks.*

---

## Syntax Rules & Automated Sanitization

The `mermaid-live` tool automatically sanitizes common pitfalls, but agents should adhere to the following rules:

- **Edge Labels with Special Characters**:
  - ❌ `A -->|Dispatch (Direct :8032)| B` (breaks Mermaid parser)
  - ✅ `A -->|"Dispatch (Direct :8032)"| B` (quotes protect special characters)
- **Node Labels**:
  - Prefer `id["Label (Extra Info)"]` over unquoted parentheses inside node delimiters.
- **Subgraphs**:
  - Quote subgraph titles with spaces or brackets: `subgraph Group["My Service Group (LAN)"]`.

---

## Technical Details

- **Direct Link (Default)**: Produces unblockable `https://mermaid.live/edit#pako:...` links.
- **Enterprise Firewall Safety**: Avoids third-party shortener domains (`tinyurl`, `da.gd`) that corporate proxies frequently flag as anonymizers or suspicious redirects.
- **Compression**: The state object `{"code": "...", "mermaid": "{\"theme\": \"default\"}", "autoSync": true, "updateDiagram": true}` is JSON-encoded, compressed using `zlib.compress(json_bytes, level=9)`, and base64url-encoded without padding `=` to match Mermaid Live Editor's `serde.ts` specification (`js-base64` / `pako`).
- **Shortener**: Calls TinyURL API (`https://tinyurl.com/api-create.php?url=...`). TinyURL preserves URL fragment hashes (`#pako:...`) in HTTP 301 `Location` response headers.
