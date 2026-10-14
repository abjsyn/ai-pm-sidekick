---
name: gui-run
description: >-
  Launches the PM Command Center visual web application (GUI) locally on port 3000 and automatically opens it in your default web browser.
---

# 🚀 Launch PM Command Center Web GUI

## Overview
The `gui-run` skill starts the AI PM Sidekick PM Command Center local web server (`http://localhost:3000`) and automatically opens the interactive Atelier Workspace dashboard in your default web browser tab.

---

## 🛠️ Step-by-Step Execution Instructions

1. **Launch Local Web Server & Open Browser**:
   Run the zero-dependency Python launcher script:
   ```bash
   python3 scripts/launch-ui.py --open
   ```

2. **Access URL**:
   If your environment does not automatically pop up a browser tab, open your web browser manually to:
   👉 **http://localhost:3000** (or `http://127.0.0.1:3000`)

3. **Features Available in GUI**:
   - **⭐ Pinned Favorites Sidepanel**: Star your favorite skills for 1-click execution.
   - **Skill Wizard**: Interactive forms with live dual-pane Markdown previewer.
   - **Deliverable Hub**: Real-time disk file explorer for generated PRDs, stories, and wireframes.
   - **MCP Manager**: Configure Atlassian (Jira/Confluence), Figma, and Miro API credentials in `.env`.

---

## 🏛️ Architecture & UI Asset Structure
To prevent context contamination between harness tools and user product artifacts, Sidekick's internal UI files are isolated in `ui/`:
- **Main View Screen**: `ui/views/pm-command-center.html`
- **Navigation Panel**: `ui/views/sidepanel-skills-navigation.html`
- **Settings View**: `ui/views/user-profile-settings.html`
- **Atelier Design & Stitch Assets**: `ui/stitch/` (design system tokens, reference screen)
- **Sidekick UI Specifications**: `ui/specs/` (internal UI PRD & component specs)
- **User Deliverables**: PM-generated PRDs and specs are written to `docs/`; generated interactive prototypes are written to `mockups/`.

---

## 🔄 Flow Handling & Suggested Next Skills
Once the GUI is running:
- **Next Step 1 (PRD Generation)**: Use `create-prd` from the sidepanel or wizard to generate product specs.
- **Next Step 2 (INVEST Stories)**: Use `create-user-stories` to decompose PRDs into Gherkin BDD user stories.
- **Next Step 3 (Sync to Jira)**: Use `sync-jira` to push sprint stories directly to Jira Cloud.
