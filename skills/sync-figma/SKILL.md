---
name: sync-figma
description: >-
  Bi-directionally syncs Figma design tokens, components, and brief annotations. Pulls design context into .context/ and BACKLOG.md, or posts UX specs to Figma nodes via Figma MCP.
---

# 🎨 Figma Design & Specification Sync Skill

## Overview
The `sync-figma` skill links AI PM Sidekick directly with Figma design files via Model Context Protocol (MCP) using `@modelcontextprotocol/server-figma`. It provides bi-directional collaboration between product and design: inspecting layout hierarchies, design tokens, and review feedback to hydrate `.context/` and `BACKLOG.md`, and pushing structured UI/UX Design Brief specs, state requirements, and accessibility criteria from `docs/` directly as comments onto Figma frames.

---

## ⚙️ Prerequisites & MCP Credentials
Ensure credentials are configured in `.env` (or via `python3 scripts/setup-mcp.py --tool figma --interactive`):
```env
FIGMA_ACCESS_TOKEN=figd_your_access_token_here
FIGMA_FILE_KEY=your_figma_file_key_here
```
Active MCP Server: `figma` (`@modelcontextprotocol/server-figma`).

---

## 🔄 Dual Bi-Directional Synchronization Flows

### Flow 1: PULL (Figma ➔ PM Workspace)
Pulls design tokens, component hierarchies, and design critique comments into the PM workspace:
1. **Design Tokens & UI Styles**: Inspects Figma files (`figma_get_file`, `figma_get_file_nodes`) to extract color palettes, typography styles, spacing rules, and component definitions into [`.context/conventions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/conventions.md) and [`.context/architecture.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/architecture.md).
2. **Design Critique & Review Comments**: Fetches design comments (`figma_get_comments`) and extracts feedback, UX gaps, and edge cases into [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md) (or delegates to [`skills/ingest-context/SKILL.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/skills/ingest-context/SKILL.md)).
3. **UX Debt & Missing States**: Flags unresolved Figma discussion threads and missing UI states directly into [`BACKLOG.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/BACKLOG.md).

### Flow 2: PUSH (PM Workspace ➔ Figma)
Annotates Figma canvas frames and components with rigorous PM specifications from `docs/`:
1. **Mandatory Context Hydration Gate**:
   Before annotating Figma designs, **MUST** read:
   - [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) — extracts target user personas, mental models, and primary user journeys.
   - [`.context/conventions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/conventions.md) — aligns with WCAG 2.1 AA accessibility standards, component naming rules, and responsive breakpoints.
   - [`.context/harness-config.yaml`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/harness-config.yaml) — ensures deliverable tier rigor (`lean`, `agile`, `enterprise`).
2. **Design Brief & Acceptance Annotation**:
   - Reads UI/UX Design Briefs from `docs/*_design_brief.md`.
   - Posts targeted comments onto specific Figma node IDs (`figma_post_comment`):
     - **Component State Matrix**: Hover, Active, Focus, Disabled, Loading, and Error states.
     - **Accessibility Rules**: Minimum 4.5:1 contrast ratios, screen-reader labels, keyboard navigation order.
     - **Business Logic & Validation**: Form error rules, input masks, and edge-case behaviors.

---

## 🛠️ Step-by-Step Execution Workflow

### Step 1: Verify MCP Connection Readiness
- Check Figma MCP tools availability (`figma_get_file`, `figma_get_file_nodes`, `figma_get_comments`, `figma_post_comment`).
- Validate `FIGMA_ACCESS_TOKEN` and `FIGMA_FILE_KEY`.

### Step 2: Context Hydration
- Read `.context/product.md`, `.context/conventions.md`, and `.context/harness-config.yaml`.
- Extract accessibility thresholds, persona context, and project tier.

### Step 3: Select Sync Direction & Scope
Prompt user for synchronization action:
> *"What Figma sync operation would you like to run?*
> 1. **Pull Design Context**: Extract design tokens, component hierarchy, and review comments into `.context/` and `BACKLOG.md`.
> 2. **Push Design Brief**: Annotate Figma frames with specs from `docs/<feature>_design_brief.md`.
> 3. **Inspect Frame**: Inspect node details and layout properties for a specific Figma Frame ID."*

### Step 4: Payload Construction & Preview
- For **Pull**: Display discovered components, typography tokens, and comments with target destinations in `.context/conventions.md`, `.context/discovery.md`, or `BACKLOG.md`.
- For **Push**: Display table mapping Figma Node IDs to proposed specification comments.

### Step 5: User Confirmation Gate
- **STOP** and ask for confirmation before writing comments to Figma or workspace files:
  > *"Review the Figma payload above. Would you like me to proceed with attaching/pulling this design context?"*

### Step 6: Execute MCP Tool Calls & Deliver Status
- Call `figma_post_comment` or `figma_get_file`.
- Return direct Figma frame URLs (e.g. `https://www.figma.com/design/<file_key>?node-id=12%3A34`) and confirmation summary.

---

## 🔄 Flow Handling & Next Skill Suggestions
At the end of synchronizing Figma designs, ALWAYS recommend the logical next steps:
- **Next Step 1 (Build HTML Prototype)**: "Would you like to build an interactive HTML prototype matching these Figma components using `create-mockup`?"
- **Next Step 2 (INVEST User Stories)**: "Would you like to generate Gherkin user stories for these design states using `create-user-stories`?"
- **Next Step 3 (Sync to Jira)**: "Would you like to push the resulting frontend user stories to Jira using `sync-jira`?"
