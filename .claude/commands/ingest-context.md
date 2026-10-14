# Command: /ingest-context

Ingests raw unstructured inputs (meeting notes, customer interview transcripts, Slack dumps, existing PRDs, codebase READMEs, or MCP pages) and routes structured updates into .context/ product knowledge files.

# 📥 Ingest Context Skill

## Overview
The `ingest-context` skill is the intelligence gateway of the AI PM Sidekick. It absorbs raw, messy, or unstructured information from real-world product workflows—such as customer interview transcripts, stakeholder meeting minutes, Slack threads, existing legacy PRDs, codebase READMEs, or pages fetched via MCP—and systematically distills them into the `.context/` Product Knowledge Core.

---

## 🎯 Supported Input Sources
1. **Raw Text Pastes**:
   - Customer interview transcripts, user call notes, feedback surveys.
   - Executive strategy meeting minutes, sprint retrospective notes, Slack threads.
2. **Local Workspace Files**:
   - Legacy PRDs, Google Docs exports, competitor teardowns, codebase `README.md` files.
3. **MCP-Fetched External Data**:
   - Confluence pages (via Atlassian MCP `confluence_get_page`).
   - Jira epics and story backlogs (via Atlassian MCP `jira_search_issues`).
   - Figma design review comments (via Figma MCP `figma_get_comments`).
   - Miro brainstorm boards (via Miro MCP).

---

## 🧭 Intelligent Context Routing Map

The skill parses and categorizes extracted insights, automatically routing them to their designated `.context/` home:

| Ingested Signal / Insight | Primary Target File | Target Section |
| :--- | :--- | :--- |
| **High-level Vision, Mission, Personas, North Star Metric, OKRs** | [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) | `## 1. Vision`, `## 2. Personas`, `## 4. North Star`, `## 5. OKRs` |
| **Customer Pains, Desired Gains, Interview Facts, JTBD, OST Opportunities** | [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md) | `## 2. OST`, `## 3. The Mom Test Evidence`, `## 4. JTBD Canvas` |
| **Value Chain Components, System Bottlenecks, ToC Friction, Compliance Limits** | [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) | `## 1. Wardley Map`, `## 2. Theory of Constraints`, `## 3. Constraints` |
| **Tech Stack, Languages, Frameworks, DBs, Data Models, API Boundaries** | [`.context/architecture.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/architecture.md) | `## 2. Tech Stack`, `## 3. Data Models`, `## 4. API Boundaries` |
| **Architectural Choices, Strategic Trade-offs, Go/Pivot Decisions** | [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md) | `## 📚 Product Decision Records (PDRs)` |
| **Tier Defaults, Active Frameworks, Pinned Skills** | [`.context/harness-config.yaml`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/harness-config.yaml) | Root YAML configuration |

---

## 🛠️ Step-by-Step Execution Workflow

### 1. Ingestion & Pre-Processing
- Accept raw text input, a file path (e.g. `docs/legacy_spec.md`), or an MCP source URL.
- Strip irrelevant formatting noise while preserving verbatim quotes, specific quantitative metrics, dates, and names.

### 2. Entity & Insight Extraction (Mom Test Filtering)
- **Separate Facts from Fluff**: Filter customer feedback using `frameworks/discovery/jtbd-and-mom-test.md` (retain Tier 1 behavioral evidence; discard polite praise).
- **Identify Architectural Anchors**: Extract technical frameworks, database schemas, and integration endpoints.
- **Isolate Strategic Decisions**: Flag explicit trade-offs and decisions that warrant a formal Product Decision Record (PDR).

### 3. Structured Diff Generation & Preview
- Format the extracted insights strictly according to the target file's schema.
- Present a clear, human-readable preview of proposed changes:
  ```markdown
  ### Proposed Context Updates:
  - 📄 .context/discovery.md: Add 2 Mom Test interview quotes from PM customer call.
  - 📄 .context/strategy-and-constraints.md: Add Stripe payment gateway as Stage III Product in Wardley map.
  - 📄 .context/decisions.md: Append PDR-004: Migration to PostgreSQL for audit logging.
  ```

### 4. Explicit User Confirmation Gate
- **STOP** and ask the user for permission before modifying any file on disk:
  > *"Review the proposed updates above. Would you like me to apply these updates to your `.context/` Knowledge Core?"*

### 5. Safe Persistence & Verification
- On user approval, update the corresponding `.context/` files cleanly (merging sections and preserving existing comments).
- Report confirmation with the updated file paths.

---

## 🔄 Flow Handling & Suggested Next Skills
Once context ingestion is complete, ALWAYS recommend the logical next action:
- **Next Step 1 (Validate Fresh Ideas)**: "Would you like to evaluate newly discovered assumptions using `validate-idea`?"
- **Next Step 2 (Draft PRD Grounded in New Context)**: "Would you like to start drafting a PRD incorporating this updated context using `create-prd`?"
- **Next Step 3 (Run Strategic Analysis)**: "Would you like to evaluate newly identified bottlenecks using `apply-framework` (Theory of Constraints)?"