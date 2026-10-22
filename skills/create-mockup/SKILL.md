---
name: create-mockup
description: >-
  Generates clickable, interactive UI mockups and prototypes as self-contained HTML files styled with Tailwind CSS, supporting interactive tabs, modals, forms, and responsive device views.
paths:
  - ".context/*.md"
  - "templates/prd/*.md"
  - "templates/user-stories/*.md"
  - "templates/design/*.md"
requires:
  context_files:
    - ".context/product.md"
    - ".context/discovery.md"
    - ".context/strategy-and-constraints.md"
---

# 🎨 Clickable Wireframe & Mockup Skill

## Overview
The `create-mockup` skill generates functional, responsive, and clickable HTML wireframes directly from user stories, PRDs, or design briefs. Generated files are self-contained with Tailwind CSS (CDN) and vanilla JavaScript, allowing immediate browser testing while remaining strictly isolated in `mockups/`.

---

## 🎯 Key Features & UX Standards
1. **Self-Contained & Zero-Dependency**:
   - Single `.html` file outputs requiring zero build tools, node modules, or local servers.
2. **Modern Styling System**:
   - Styled with Tailwind CSS CDN (`https://cdn.tailwindcss.com`) and Inter typography.
3. **Interactive JavaScript Components**:
   - Tab switching, modal dialog triggers, multi-step wizards, interactive dropdowns, and toast alerts.
4. **Strict Asset Isolation**:
   - All user feature mockups are saved exclusively to `mockups/<feature-name>.html`, keeping internal Sidekick application screens in `ui/views/` completely unpolluted.

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
Before generating UI code, ingest workspace context:
1. **Read Core Context**:
   - Ingest `.context/product.md` to identify target personas and primary user journeys.
   - Ingest `.context/conventions.md` to review deliverable tier expectations.
   - Ingest `.context/architecture.md` to align UI styling patterns with existing project conventions.
2. **Read Source Specs**:
   - Ingest relevant PRDs or User Stories from `docs/` to extract screen states, CTAs, and data fields.
3. **Embedded Codebase Inspection** *(if `mode: embedded`)*:
   - Inspect existing frontend components to reuse familiar layout structures and visual hierarchies.

### Stage 2: Socratic Clarifying Gate
Evaluate whether screen interaction details and component states are sufficiently defined:
1. **Interaction Audit**: Check if modal triggers, form validation rules, active tabs, and realistic mock data records are clear.
2. **Socratic Inquiry**: If critical details are missing, **STOP** and ask the user **2 to 4 sharp, concrete clarifying questions**:
   - *"What specific interactive components (e.g., slide-over panel, confirmation modal, multi-tab table) should be clickable in this prototype?"*
   - *"What realistic mock data (e.g., 3–5 sample customer rows) should populate the initial view?"*
   - *"Should the primary CTA trigger a success toast notification, a page state switch, or a modal dialog?"*
3. **Fast-Draft Escape Hatch**: If the user replies *"proceed with assumptions"* (or requests an instant prototype), proceed immediately to Stage 3, populating realistic industry mock data and standard interactive modal behaviors automatically.

### Stage 3: Grounded Generation
Construct the self-contained HTML prototype:
1. **HTML Layout & Boilerplate**:
   - Set up HTML5 boilerplate loading Tailwind CSS CDN and Google Inter fonts.
   - Ensure responsive layout (Desktop, Tablet, Mobile container widths).
2. **Vanilla JavaScript Interactivity**:
   - Implement modular JS functions for opening/closing modals, toggling tabs, and simulating form submission feedback.
3. **Persist Deliverable**:
   - Write the output file directly to `mockups/<feature-name>.html` (leaving `ui/views/` and `ui/stitch/` completely untouched).

### Stage 4: Knowledge Compounding (Write-Back)
Capture newly established UI components and user interaction workflows back into `.context/`:
1. **Propose Write-Back Updates**:
   - Summarize interactive component states, form validation workflows, or modal flows established in the prototype.
2. **Prompt for Permission**:
   - *"Would you like me to update `.context/architecture.md` with these newly established UI interaction components and record the mockup in `.context/decisions.md`?"*
3. **Persist on Approval**: Update the targeted `.context/` files upon user confirmation.

---

## 🔄 Flow Handling & Suggested Next Skills
At the end of generating a mockup, ALWAYS recommend the logical next steps:
- **Next Step 1 (Design Handoff)**: "Would you like to draft a formal UI/UX Design Brief based on this mockup using `create-design-brief`?"
- **Next Step 2 (User Stories)**: "Would you like to generate INVEST engineering user stories for the interactions shown in this mockup using `create-user-stories`?"
- **Next Step 3 (Figma Inspection via MCP)**: "Would you like to compare this wireframe against live Figma designs using `sync-figma`?"
