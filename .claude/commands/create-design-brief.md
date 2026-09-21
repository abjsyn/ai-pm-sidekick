# Command: /create-design-brief

>-

# 🎨 UI/UX Design Brief Skill

## Overview
The `create-design-brief` skill bridges the gap between Product Management and Product Design. It converts PRD specs into designer-friendly project briefs that clearly define user emotions, key screen flows, design system alignment, and accessibility standards.

---

## 🎯 Key Elements Included

1. **User Context & Emotion**:
   - Defining the user's environment, mindset, and urgency during the feature interaction.
2. **Step-by-Step UX Flows**:
   - Visualizing entry points, primary CTAs, loading states, and exit paths.
3. **Accessibility (WCAG 2.1 AA Checklist)**:
   - Color contrast requirements (4.5:1 minimum).
   - Touch target sizing (minimum 44x44px).
   - Screen reader ARIA roles and keyboard focus indicator guidelines.
4. **Figma Handoff Criteria**:
   - Specification of required UI states (Empty, Loading, Error, Hover, Active, Disabled).

---

## 🛠️ Step-by-Step Execution Workflow

1. **Gather Design Scope**:
   - Review PRD or feature requirement text.
2. **Draft Brief**:
   - Populate sections using template `templates/design/design-brief.md`.
3. **Audit Accessibility Specs**:
   - Verify WCAG 2.1 AA requirements are explicitly stated.
4. **Deliver Brief & Flow Handling**:
   - Present markdown document ready for design handoff in Figma / Notion.
   - Suggest next skills in the pipeline.

---

## 🔄 Flow Handling & Suggested Next Skills
At the end of generating a design brief, ALWAYS recommend the logical next steps:
- **Next Step 1 (Sync with Figma via MCP)**: "Would you like to sync or inspect components in Figma using `sync-figma`?"
- **Next Step 2 (Clickable Wireframe)**: "Would you like to build an interactive HTML wireframe prototype from this brief using `create-mockup`?"
- **Next Step 3 (User Stories)**: "Would you like to write engineering user stories for these design components using `create-user-stories`?"