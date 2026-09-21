# Command: /sync-figma

>-

# 🎨 Figma Design Sync Skill

## Overview
The `sync-figma` skill links product management specifications with live Figma design files via Model Context Protocol (MCP). It can inspect component specs, pull layout trees, and attach UI/UX requirements directly as comments on Figma frames.

---

## 🛠️ Step-by-Step Execution Workflow

1. **Verify Figma MCP Connection**:
   - Ensure `FIGMA_ACCESS_TOKEN` is set.
   - If missing, guide user to run `/connect-mcp` or `python3 scripts/setup-mcp.py`.

2. **Select Action Mode**:
   - **Mode A: Inspect Figma File / Component**:
     - Input: Figma File Key (from URL `https://figma.com/file/<file_key>/...`)
     - MCP Call: `figma_get_file` or `figma_get_file_nodes`
     - Action: Extract color styles, typography, component names, layout hierarchy. Use data to enrich `create-design-brief` or `create-mockup`.
   - **Mode B: Post Design Brief Comments**:
     - Input: Figma File Key & Node ID
     - Action: Attach WCAG 2.1 AA accessibility guidelines and state specs (Hover/Active/Disabled/Error) directly onto design nodes via `figma_post_comment`.

3. **Deliver Summary**:
   - Present component hierarchy or confirm comments attached to Figma nodes.

---

## 🔄 Flow Handling & Next Skill Suggestions
- **Next Step 1 (Build HTML Mockup)**: "Would you like to build an interactive HTML wireframe prototype based on these Figma components using `create-mockup`?"
- **Next Step 2 (Write User Stories)**: "Would you like to write Gherkin user stories for these design states using `create-user-stories`?"