# Command: /sync-jira

Bi-directionally syncs Jira epics, stories, and sprint issues. Pulls issues into BACKLOG.md and .context/discovery.md, or exports INVEST user stories from docs/ to Jira via Atlassian MCP.

# 🎟️ Jira Backlog & Issue Sync Skill

## Overview
The `sync-jira` skill establishes bi-directional synchronization between Atlassian Jira and the AI PM Sidekick workspace via Model Context Protocol (MCP) using `@modelcontextprotocol/server-atlassian`. It routes sprint backlogs, epics, and bug reports into `BACKLOG.md` and `.context/`, and pushes refined user stories, Gherkin acceptance criteria, and story points from `docs/` directly into Jira.

---

## ⚙️ Prerequisites & MCP Credentials
Ensure credentials are configured in `.env` (or via `python3 scripts/setup-mcp.py --tool atlassian --interactive`):
```env
ATLASSIAN_HOST=https://your-domain.atlassian.net
ATLASSIAN_EMAIL=your-email@domain.com
ATLASSIAN_API_TOKEN=your_atlassian_api_token
JIRA_PROJECT_KEY=PROJ
```
Active MCP Server: `atlassian` (`@modelcontextprotocol/server-atlassian`).

---

## 🔄 Dual Bi-Directional Synchronization Flows

### Flow 1: PULL (Jira ➔ PM Workspace)
Pulls active sprints, backlog issues, bugs, and epics from Jira into the PM workspace:
1. **Backlog Ingestion**: Queries open Jira issues via JQL (`jira_search_issues`) and organizes them into [`BACKLOG.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/BACKLOG.md) grouped by Epic, Sprint, and Priority.
2. **Customer Pain & Bug Discovery**: Ingests bug reports, production incidents, and customer escalations directly into [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md) under Customer Opportunities and Mom Test behavioral evidence (or delegates to [`skills/ingest-context/SKILL.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/skills/ingest-context/SKILL.md)).
3. **Execution Constraints & Velocity**: Pulls sprint velocity, blocker tags, and capacity constraints into [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md).

### Flow 2: PUSH (PM Workspace ➔ Jira)
Pushes refined user stories and epics from `docs/` to Jira Cloud:
1. **Mandatory Context Hydration Gate**:
   Before constructing payloads or creating tickets, **MUST** read:
   - [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) — validates persona definitions, product goals, and target release alignment.
   - [`.context/conventions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/conventions.md) — adheres to ticket naming conventions, Gherkin syntax standards, and Definition of Done (DoD).
   - [`.context/harness-config.yaml`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/harness-config.yaml) — ensures deliverable tier standards (`lean`, `agile`, `enterprise`).
2. **Story Decomposition & Field Mapping**:
   - **Summary**: `[US-XX] Feature / User Story Title`
   - **Issue Type**: `Epic`, `Story`, `Bug`, or `Task`
   - **Description**:
     - *User Persona & Intent*: `As a [persona], I want [action], So that [outcome]`
     - *Gherkin Acceptance Criteria*: `Given / When / Then` testable scenarios (happy path, edge cases, error states)
     - *Definition of Done (DoD)*: Quality and verification checklist
   - **Story Points**: Fibonacci sequence points (`1, 2, 3, 5, 8, 13`)
   - **Labels & Links**: Maps operational tags (`ai-pm-sidekick`, tier, sprint) and links to parent Epic.

---

## 🛠️ Step-by-Step Execution Workflow

### Step 1: Verify MCP Connection Readiness
- Check Atlassian MCP tools availability (`jira_create_issue`, `jira_search_issues`, `jira_get_issue`, `jira_update_issue`).
- Verify `ATLASSIAN_HOST`, `ATLASSIAN_EMAIL`, `ATLASSIAN_API_TOKEN`, and `JIRA_PROJECT_KEY`.

### Step 2: Context Hydration
- Read `.context/product.md`, `.context/conventions.md`, and `.context/harness-config.yaml`.
- Extract target personas, project key defaults, and DoD criteria.

### Step 3: Select Sync Direction & Scope
Prompt user for synchronization action:
> *"What Jira sync operation would you like to run?*
> 1. **Pull**: Fetch active sprint issues and bugs into `BACKLOG.md` and `.context/discovery.md`.
> 2. **Push**: Export user stories from `docs/<feature>_user_stories.md` into Jira project tickets.
> 3. **Status Check**: Inspect Jira sprint board status, epics, and unestimated backlog items."*

### Step 4: Payload Construction & Preview
- For **Pull**: Display table of issues to ingest, showing summary, status, and target section in `BACKLOG.md` or `.context/discovery.md`.
- For **Push**: Display formatted Jira payload table showing Issue Type, Summary, Story Points, Epic Link, and Labels.

### Step 5: User Confirmation Gate
- **STOP** and ask for confirmation before modifying Jira or workspace files:
  > *"Review the Jira payload above. Would you like me to proceed with creating/pulling these issues?"*

### Step 6: Execute MCP Tool Calls & Deliver Ticket URLs
- Call `jira_create_issue` or fetch issues via `jira_search_issues`.
- Return direct Jira URLs (e.g. `https://your-domain.atlassian.net/browse/PROJ-142`) and synchronization summary.

---

## 🔄 Flow Handling & Next Skill Suggestions
At the end of synchronizing Jira issues, ALWAYS recommend the logical next steps:
- **Next Step 1 (Confluence Spec Sync)**: "Would you like to publish the overarching PRD to Confluence using `sync-confluence`?"
- **Next Step 2 (Readiness Audit)**: "Would you like to audit remaining stories for edge cases using `refine-user-stories`?"
- **Next Step 3 (Technical Schemas)**: "Would you like to generate OpenAPI schemas or technical documentation for these tickets using `create-documentation`?"