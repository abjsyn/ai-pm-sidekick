# 🎯 PM Command Center UI — Product Requirements Document (PRD)

**Author:** AI PM Sidekick | **Date:** 2026-09-20 | **Status:** Approved / Ready for Engineering | **Mode:** Standard Agile  
**Target Release:** MVP Sprint 1 | **Tech Lead:** Antigravity AI | **Design Lead:** UI/UX Sidekick

---

## 1. Executive Summary & Context
* **Summary:** The **PM Command Center UI** is a lightweight, locally hosted web application (`http://localhost:3000`) that wraps AI PM Sidekick's terminal skills, automation scripts, and MCP integrations (Atlassian Jira/Confluence, Figma, Miro) into a sleek, visual dashboard designed specifically for non-technical Product Managers.
* **Strategic Alignment:** Directly supports the product objective of expanding AI PM Sidekick adoption beyond technical CLI power-users to 100% of product team members, eliminating terminal friction while preserving full underlying script capability.

---

## 2. Problem Statement & User Persona

### 🎯 The Problem
Non-technical Product Managers often find command-line interfaces (`npx`, slash commands, terminal flags) intimidating or tedious to configure. While they desire AI-assisted PRD generation, story breakdown, and MCP syncing (Jira, Confluence, Figma, Miro), missing visual feedback and CLI barriers prevent daily active usage.

### 👤 Target Audience
* **Primary Persona:** *Paula (Product Manager)* — Non-technical PM who wants guided visual forms, instant previewing of PRDs/mockups, and 1-click export buttons to Jira and Confluence without touching a terminal prompt.
* **Secondary Persona:** *Dave (Engineering Lead)* — Wants a quick visual dashboard to verify MCP server connectivity (Jira/Confluence/Figma/Miro) and review generated Gherkin acceptance criteria before tickets are created.

### 💎 User Value Proposition
Reduces the time to generate, review, and export a complete product package (PRD + Wireframe + Jira Stories) from **15 minutes to under 3 minutes** via a zero-code, visual web interface.

---

## 3. Goals & Success Metrics (OKRs/KPIs)

| Goal | Metric / Indicator | Baseline | Target | Measurement Tool |
| :--- | :--- | :--- | :--- | :--- |
| **User Adoption** | Non-CLI PM Active Usage Rate | 0% | 85% within 14 days | Local telemetry / usage log |
| **Workflow Velocity** | Avg Time to Generate & Sync PRD/Stories | 15.0 mins | < 3.0 mins | Web UI session timer |
| **Integration Reliability** | 1-Click MCP Sync Success Rate | N/A | > 99.0% | Setup status API logger |
| **User Satisfaction** | Ease of Use CSAT Score | 3.2 / 5.0 | > 4.7 / 5.0 | In-app feedback rating |

---

## 4. User Journeys & End-to-End Workflow

```
[Launch UI / Localhost:3000] ──> [Select Skill Wizard] ──> [Fill Guided Form & Generate] ──> [Live Preview & 1-Click MCP Sync]
```

1. **Trigger:** PM launches local server (`python3 scripts/setup-mcp.py --ui` or double-clicks desktop app shortcut) and opens `http://localhost:3000`.
2. **Action (Skill Wizard):** PM selects a capability (e.g. `create-prd`), fills out the 3-step visual wizard (*Feature Name*, *Operational Mode*, *Persona*, *Goal*), and clicks **"Generate Deliverable"**.
3. **Live Preview:** Real-time dual-pane view opens: left pane retains form parameters, right pane streams live rendered Markdown PRD and interactive Tailwind wireframe.
4. **Outcome (MCP Sync):** PM reviews output and clicks **"1-Click Sync to Confluence"** or **"Break down into Jira Stories"**. Server executes underlying MCP tools silently and displays a green confirmation toast with direct web link.

---

## 5. Functional Requirements

| ID | Requirement / User Story | Priority | Complexity | Notes / Technical Ref |
| :--- | :--- | :--- | :--- | :--- |
| **FR-01** | **Visual Skill Selector & Wizard**: UI must provide visual card launchers for all 13 canonical skills (`create-prd`, `create-user-stories`, `create-mockup`, `brainstorm`, etc.) with guided form inputs. | Must Have | Medium | Parses skill templates dynamically |
| **FR-02** | **Real-Time Dual Pane Live Preview**: UI must render live Markdown, Gherkin tables, and interactive HTML mockups in an iframe preview panel. | Must Have | Medium | Uses `marked.js` + iframe wrapper |
| **FR-03** | **1-Click MCP Connection Manager**: Visual dashboard showing status of Jira, Confluence, Figma, and Miro MCP servers with inline `.env` credential configuration modal. | Must Have | Medium | Interacts with `scripts/setup-mcp.py` REST API |
| **FR-04** | **1-Click MCP Sync Execution**: One-click action buttons on deliverables to push user stories to Jira (`sync-jira`), docs to Confluence (`sync-confluence`), comments to Figma (`sync-figma`), and stickies to Miro (`sync-miro`). | Must Have | Medium | Wraps MCP tool calls via local server |
| **FR-05** | **Collapsible Terminal Log Drawer**: Live output stream showing stdout/stderr logs from background CLI processes for transparency and debugging. | Should Have | Low | WebSockets / Server-Sent Events (SSE) |
| **FR-06** | **Artifact Library & Search**: Local file explorer listing past PRDs, Design Briefs, Mockups, and User Stories with search and download features. | Should Have | Low | Reads `.agents/skills` and output dirs |
| **FR-07** | **Dark / Light Mode & Responsive UI**: Clean, modern Tailwind UI supporting dark/light themes and responsive screen sizes. | Could Have | Low | Tailwind CSS + Lucide icons |

---

## 6. Non-Functional & Quality Requirements

* **Performance:** 
  - Local web server startup time < 1.0s.
  - Initial page load latency < 150ms.
  - Live markdown preview rendering delay < 50ms.
* **Architecture & Decoupling:**
  - 100% decoupled from underlying CLI: the UI acts strictly as a web wrapper. CLI tools, slash commands, and scripts continue operating independently.
* **Security & Privacy:**
  - Localhost binding only (`127.0.0.1:3000`). No external telemetry or cloud data leakage.
  - Sensitive API tokens stored exclusively in local `.env` file.

---

## 7. Edge Cases & Error Handling

* **Missing MCP Credentials:** When a user clicks "Sync to Jira" without credentials configured, UI opens a friendly credential modal pre-filled with `.env.example` guidance.
* **CLI Subprocess Failure:** If a script fails or times out, the UI displays a clean error banner with an expandable "View Execution Log" toggle and a "Retry Action" button.
* **Unsaved Form Progress:** Displays a confirmation prompt if user attempts to navigate away from an active wizard before generating the deliverable.

---

## 8. Out of Scope (Non-Goals)

* ❌ **Multi-User Cloud Hosting / SaaS**: MVP is strictly local-first (`localhost`). No cloud user authentication or multi-tenant database required.
* ❌ **Custom Skill Builder Code Editor**: Users edit `SKILL.md` files in their IDE or via terminal scripts, not inside the web app code editor.

---

## 9. Dependencies & Risks

| Dependency / Risk | Impact | Mitigation Strategy |
| :--- | :--- | :--- |
| **Python FastAPI / Node Backend Runtime** | Required to launch local web server | Package setup script with zero-config launcher (`python3 scripts/launch-ui.py`) |
| **Long-Running Generation Processes** | Potential UI freeze during deep skill execution | Stream subprocess output asynchronously using Server-Sent Events (SSE) |
| **Browser Mockup Security Restrictions** | Cross-Origin / Sandbox issues with iframe mockups | Serve interactive HTML wireframes from local origin endpoint (`/preview/mockup.html`) |

---

## 🔄 Flow Handling & Suggested Next Skills

Now that the **PM Command Center UI PRD** is defined, here are the logical next steps in the PM pipeline:

- **Next Step 1 (Jira Sync)**: "Would you like to sync these PRD requirements & tickets directly to Jira using `sync-jira`?"
- **Next Step 2 (Confluence Publish)**: "Would you like to publish this PRD to Confluence using `sync-confluence`?"
- **Next Step 3 (User Stories)**: "Would you like me to break down this PRD into INVEST user stories using `create-user-stories`?"
- **Next Step 4 (Interactive Wireframe)**: "Would you like to build an interactive HTML wireframe prototype of the Command Center UI using `create-mockup`?"
