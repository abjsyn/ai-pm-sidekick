# Command: /sync-github-issues

Bi-directionally syncs GitHub Issues, labels, and milestones. Pulls issues into BACKLOG.md and .context/discovery.md, or exports refined user stories as structured GitHub Issues.

# 🐙 GitHub Issues & Backlog Sync Skill

## Overview
The `sync-github-issues` skill connects AI PM Sidekick directly with GitHub repositories via Model Context Protocol (MCP) using `@modelcontextprotocol/server-github`. It provides true bi-directional synchronization between engineering GitHub Issues and Product Management artifacts in `BACKLOG.md`, `.context/`, and `docs/`.

---

## ⚙️ Prerequisites & MCP Credentials
Ensure credentials are configured in `.env` (or via `python3 scripts/setup-mcp.py --tool github --interactive`):
```env
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token_here
GITHUB_OWNER=your-org-or-username
GITHUB_REPO=your-repository-name
```
Active MCP Server: `github` (`@modelcontextprotocol/server-github`).

---

## 🔄 Dual Bi-Directional Synchronization Flows

### Flow 1: PULL (GitHub ➔ PM Workspace)
Pulls issues, bugs, customer feedback, and milestones from GitHub into the PM workspace:
1. **Backlog Ingestion**: Fetches open issues and categorizes them into [`BACKLOG.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/BACKLOG.md) by milestone and priority.
2. **Customer Pain Discovery**: Extracts issue descriptions flagged with `bug`, `customer-request`, or `feedback` directly into [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md) under Customer Opportunities and The Mom Test interview evidence.
3. **Milestone Progress Tracking**: Reads milestone due dates and completion ratios to update delivery projections.

### Flow 2: PUSH (PM Workspace ➔ GitHub)
Pushes refined user stories and acceptance criteria from `docs/` to GitHub Issues:
1. **Story Formatting**: Converts user stories into GitHub Markdown format:
   - **Issue Title**: `[US-XX] Feature / User Story Title`
   - **Description**:
     - *User Persona & Intent*: `As a [persona], I want [action], So that [outcome]`
     - *Gherkin Acceptance Criteria*: `Given / When / Then` scenarios (Happy path, error states, boundaries)
     - *Definition of Done*: Markdown checklist
     - *Story Points*: Fibonacci tag (`points:1`, `points:2`, `points:3`, `points:5`, `points:8`)
2. **Labels & Milestones**:
   - Automatically applies labels: `user-story`, `ready-for-dev`, tier (`lean`, `agile`, `enterprise`).
   - Links issues to the active GitHub Milestone.

---

## 🛠️ Step-by-Step Execution Workflow

### Step 1: Verify MCP Connection Readiness
- Check if GitHub MCP tools are available (`create_issue`, `list_issues`, `get_issue`, `search_issues`, `update_issue`).
- Verify `GITHUB_OWNER` and `GITHUB_REPO` are defined in `.env`.

### Step 2: Select Sync Direction & Scope
Prompt user for synchronization action:
> *"What GitHub sync operation would you like to run?*
> 1. **Pull**: Fetch open issues from `owner/repo` into `BACKLOG.md` and `.context/discovery.md`.
> 2. **Push**: Export user stories from `docs/<feature>_user_stories.md` as new GitHub Issues.
> 3. **Status Check**: Inspect active milestones and issue counts."*

### Step 3: Payload Construction & Preview
- For **Pull**: Display extracted issues with title, state, and target context section.
- For **Push**: Display the preview table of issues to be created with labels, milestone, and title.

### Step 4: User Confirmation Gate
- **STOP** and ask for confirmation before modifying GitHub or workspace files:
  > *"Review the payload above. Would you like me to proceed with creating/pulling these issues?"*

### Step 5: Execute MCP Tool Calls & Report URLs
- Invoke `create_issue` or fetch issues via MCP.
- Return direct GitHub URLs (e.g. `https://github.com/owner/repo/issues/104`) and confirmation status.

---

## 🔄 Flow Handling & Next Skill Suggestions
At the end of synchronizing GitHub Issues, ALWAYS recommend the logical next steps:
- **Next Step 1 (Story Grooming)**: "Would you like to audit these stories for edge cases using `refine-user-stories`?"
- **Next Step 2 (Technical Documentation)**: "Would you like to generate technical API schemas for these issues using `create-documentation`?"
- **Next Step 3 (Sync to Jira)**: "Would you like to cross-sync these tickets into Jira Cloud using `sync-jira`?"