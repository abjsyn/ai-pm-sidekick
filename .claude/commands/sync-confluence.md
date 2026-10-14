# Command: /sync-confluence

Publishes PRDs, Technical Specs, Design Briefs, and User Manuals directly into Confluence spaces using Atlassian MCP integration.

# 📄 Confluence Documentation Sync Skill

## Overview
The `sync-confluence` skill converts generated PRDs (`create-prd`), Design Briefs (`create-design-brief`), and Technical Specs (`create-documentation`) into structured Confluence pages using Atlassian MCP.

---

## 🛠️ Step-by-Step Execution Workflow

1. **Verify Confluence MCP Connection**:
   - Check Atlassian MCP server readiness (`ATLASSIAN_HOST`, `ATLASSIAN_EMAIL`, `ATLASSIAN_API_TOKEN`).
   - If missing, prompt user to run `/connect-mcp`.

2. **Gather Target Confluence Parameters**:
   - **Space Key**: (e.g., `PROD`, `ENG`, `DESIGN`).
   - **Parent Page ID**: (optional, to nest under epic or product hierarchy).
   - **Page Title**: Auto-populated from PRD or spec header.

3. **Format & Publish Document**:
   - Convert Markdown content into Confluence Storage Format (XHTML / standard HTML markdown).
   - Render Mermaid sequence diagrams into Confluence-compatible macro or image callouts.
   - Invoke `confluence_create_page` or `confluence_update_page` via MCP.

4. **Deliver URL & Summary**:
   - Return direct link to created Confluence page.

---

## 🔄 Flow Handling & Next Skill Suggestions
- **Next Step 1 (Export Jira Backlog)**: "Would you like to break this PRD down into Jira tickets using `sync-jira`?"
- **Next Step 2 (Design Specs)**: "Would you like to sync design components with Figma using `sync-figma`?"