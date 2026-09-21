---
name: sync-jira
description: >-
  Syncs user stories, acceptance criteria (Gherkin BDD), story points, and epics directly to Jira via Atlassian MCP integration.
---

# 🎟️ Jira Backlog Sync Skill

## Overview
The `sync-jira` skill connects AI PM Sidekick output directly with Atlassian Jira via Model Context Protocol (MCP). It parses Gherkin user stories, Fibonacci story points, and Definition of Done, creating Jira Epics, Stories, and Sub-tasks automatically.

---

## 🛠️ Step-by-Step Execution Workflow

1. **Verify Jira MCP Connection**:
   - Check if Atlassian MCP server is available (`@modelcontextprotocol/server-atlassian`).
   - If missing, guide user to run `/connect-mcp` or `python3 scripts/setup-mcp.py`.

2. **Collect Target Project Details**:
   - Ask for **Jira Project Key** (e.g. `PROJ`, `CORE`, `MOBILE`).
   - Ask for **Epic Link / Parent Key** (optional).
   - Confirm target issue type (`Story`, `Epic`, `Task`).

3. **Map Story Fields to Jira Schema**:
   - **Summary**: `[US-01] User Story Title`
   - **Description**: 
     - User Persona & Need (`As a... I want... So that...`)
     - Gherkin Acceptance Criteria (`Given / When / Then`)
     - Definition of Done Checklist
   - **Story Points**: Map Fibonacci estimate (e.g., `3`, `5`, `8`).
   - **Labels**: `ai-pm-sidekick`, `generated-story`, operational mode (`lean`/`agile`/`enterprise`).

4. **Execute MCP Calls**:
   - Invoke `jira_create_issue` or `jira_update_issue` tool.
   - Return created issue keys (e.g., `PROJ-142`, `PROJ-143`) with direct URLs.

---

## 🔄 Flow Handling & Next Skill Suggestions
- **Next Step 1 (Publish Confluence Spec)**: "Would you like to publish the overarching PRD to Confluence using `sync-confluence`?"
- **Next Step 2 (Audit Readiness)**: "Would you like to check remaining story grooming scores using `refine-user-stories`?"
