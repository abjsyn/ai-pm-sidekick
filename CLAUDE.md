# AI PM Sidekick — Claude Code Workspace Guide

Welcome to **AI PM Sidekick**, a local-first product management command center and AI harness.

## 🧭 Core Workflow & The 4-Stage Protocol

When assisting product managers, technical PMs, or engineering leads, always follow this protocol:

1. **Stage 1: Context Hydration**
   - Check `.context/harness-config.yaml` to know the workspace mode (`standalone` vs `embedded`), deliverable tier (`lean`, `standard`, `enterprise`), and delivery operating model (`scrum`, `shape-up`, `kanban`, `gist`).
   - Hydrate core knowledge from `.context/product.md`, `.context/conventions.md`, `.context/discovery.md`, `.context/strategy-and-constraints.md`, and `.context/architecture.md`.
   - In `embedded` mode, check repository package manifests and structure.

2. **Stage 2: Socratic Clarifying Gate**
   - Identify ambiguities or missing requirements in the user's prompt.
   - If critical information is absent, pause and ask 2–4 concise questions before drafting.
   - If the user instructs to proceed with assumptions, explicitly document those assumptions in the output.

3. **Stage 3: Grounded Generation**
   - Use the appropriate template from `templates/` and tier conventions from `.context/conventions.md`.
   - Reference frameworks in `frameworks/` or diagnose via `/recommend-framework`.
   - Ensure user stories meet INVEST criteria and Given/When/Then Gherkin acceptance criteria.

4. **Stage 4: Knowledge Compounding (Write-Back)**
   - Offer to record new product discoveries, technical facts, and validated assumptions in `.context/*.md`.
   - Append major product decisions to `.context/decisions.md`.

## 🚫 Critical Guardrail: Zero Context Contamination

- **Internal UI vs User Product**:
  - `ui/specs/`, `ui/views/`, and `ui/stitch/` are internal assets for the Sidekick's own web UI. **DO NOT** read them as product requirements for the user's product.
  - All user-facing PRDs, stories, and technical specs belong in `docs/`.
  - All user-facing UI wireframes and HTML mockups belong in `mockups/`.

## ⚡ Slash Commands & Skills (19 Skills)

| Command | Purpose |
|---------|---------|
| `/apply-framework` | Executes modular strategic, discovery, or prioritization frameworks from frameworks/ over an idea, backlog, or PRD, and synchronizes results back to .context/. |
| `/brainstorm` | Facilitates structured product & feature brainstorming using SCAMPER, How Might We (HMW), 6 Thinking Hats, and Value vs. Effort matrix. |
| `/connect-mcp` | Establishes, tests, and manages Model Context Protocol (MCP) integrations for external PM tools: Atlassian (Jira & Confluence), GitHub Issues, Figma, Miro, Notion, and Google Stitch across AGY, Claude Code, and Cursor IDEs. |
| `/create-design-brief` | Creates comprehensive UI/UX Design Briefs including design objectives, user context, step-by-step user flows, component specs, WCAG 2.1 AA accessibility guidelines, and Figma handoff criteria. |
| `/create-documentation` | Generates dual-purpose technical and end-user documentation. Produces API schemas (OpenAPI format), Mermaid sequence diagrams, architecture specs, and step-by-step end-user manuals. |
| `/create-mockup` | Generates clickable, interactive UI mockups and prototypes as self-contained HTML files styled with Tailwind CSS, supporting interactive tabs, modals, forms, and responsive device views. |
| `/create-prd` | Generates comprehensive Product Requirements Documents (PRDs) across 3 modes: Lean (Startup/MVP), Standard Agile (Growth/Mid-size), and Enterprise (Compliance/Scale). |
| `/create-user-stories` | Generates user stories adhering to INVEST criteria, Concur format (As a/I want/So that), Gherkin Given-When-Then Acceptance Criteria, Fibonacci story points, and Definition of Done across Lean, Standard Agile, and Enterprise modes. |
| `/gui-run` | Launches the PM Command Center visual web application (GUI) locally on port 3000 and automatically opens it in your default web browser. |
| `/ingest-context` | Ingests raw unstructured inputs (meeting notes, customer interview transcripts, Slack dumps, existing PRDs, codebase READMEs, or MCP pages) and routes structured updates into .context/ product knowledge files. |
| `/recommend-framework` | Diagnoses PM bottlenecks, uncertainty, or prioritization challenges, recommends the optimal framework & skill with a lightweight alternative and anti-pattern warning, and guides execution. |
| `/refine-user-stories` | Grooms and refines existing user stories. Detects ambiguity, splits large stories using the SPIDR framework, adds missing Gherkin edge cases, and calculates a Grooming Readiness Score (0-100%). |
| `/sync-confluence` | Bi-directionally syncs Confluence product wikis and specs. Pulls company knowledge into .context/ and BACKLOG.md, or publishes PRDs, design briefs, and technical specs to Confluence via Atlassian MCP. |
| `/sync-figma` | Bi-directionally syncs Figma design tokens, components, and brief annotations. Pulls design context into .context/ and BACKLOG.md, or posts UX specs to Figma nodes via Figma MCP. |
| `/sync-github-issues` | Bi-directionally syncs GitHub Issues, labels, and milestones. Pulls issues into BACKLOG.md and .context/discovery.md, or exports refined user stories as structured GitHub Issues. |
| `/sync-jira` | Bi-directionally syncs Jira epics, stories, and sprint issues. Pulls issues into BACKLOG.md and .context/discovery.md, or exports INVEST user stories from docs/ to Jira via Atlassian MCP. |
| `/sync-miro` | Bi-directionally syncs Miro whiteboards, brainstorm sticky notes, and roadmaps. Pulls visual ideation into .context/ and BACKLOG.md, or exports brainstorms/roadmaps to Miro via Miro MCP. |
| `/sync-notion` | Bi-directionally syncs Notion product wikis, databases, and pages. Pulls research into .context/, or publishes PRDs, design briefs, and decision logs to Notion. |
| `/validate-idea` | Validates product ideas, feature concepts, and business hypotheses using Strategyzer 4-Risk Analysis, The Mom Test customer interview framework, TAM/SAM/SOM market sizing, and Pre-mortem risk identification. |

## 🗺️ Modular Product Frameworks (10 Frameworks across 4 Categories)

Organized across 4 categories in `frameworks/`:
### Strategy
- **Theory of Constraints (ToC) & CRT Mapping** (`theory-of-constraints`): To pinpoint the operational bottleneck choking product delivery, maximize throughput at that specific point, and align all upstream discovery and downstream execution to eliminate waste.
- **Wardley Value Chain Evolution Mapping** (`wardley-mapping`): To prevent catastrophic resource misallocation (e.g., custom-building commoditized components) and explicitly identify where a product's true competitive differentiation resides.

### Discovery
- **Jobs-to-be-Done (JTBD) & The Mom Test** (`jtbd-and-mom-test`): To uncover genuine customer demand by systematically filtering out false validation, identifying real customer struggle, and structuring value propositions around the forces that drive adoption.
- **Opportunity Solution Tree (OST)** (`opportunity-solution-tree`): To break the "feature factory" anti-pattern by ensuring teams explore the problem space thoroughly, evaluate multiple competing solutions for each customer pain point, and test assumptions before committing engineering resources.

### Prioritization
- **The Kano Model & Customer Delight** (`kano-model`): To construct balanced product releases that satisfy table-stakes baseline requirements, compete effectively on performance, and incorporate distinct delighters while aggressively pruning indifferent bloat.
- **RICE Scoring Matrix** (`rice`): To eliminate cognitive bias, loud-stakeholder lobbying, and "pet project" syndrome by anchoring prioritization to empirical reach, measurable business impact, defensible confidence, and engineering effort.
- **Weighted Shortest Job First (WSJF) & Cost of Delay** (`wsjf-cost-of-delay`): To maximize economic flow by scheduling high-value, time-critical, risk-reducing features that can be delivered quickly, preventing the common failure mode of tying up engineering squads on monolithic, slow-moving projects.

### Operations & Delivery
- **GIST Planning (Goals, Ideas, Step-projects, Tasks)** (`gist-planning`): To drastically reduce product waste by testing ideas through tiny step-projects before committing full engineering squads to building multi-month feature implementations.
- **Scrum Sprint Delivery & INVEST Execution** (`scrum-sprint-delivery`): To provide predictable, sustainable, cross-functional engineering throughput with continuous delivery of shippable software increments.
- **Shape Up (Basecamp Product Development)** (`shape-up`): To eliminate endless scope creep, eliminate backlog grooming debt, and empower autonomous cross-functional teams to deliver complete, polished features within bounded timeboxes.

## 🔄 Delivery Operating Models (`operating_model`)

Configured via `operating_model` in `.context/harness-config.yaml`:
- `scrum`: Iterative sprints, INVEST user stories, Fibonacci points, DoD sign-off (Default)
- `shape-up`: 6-week cycles, shaped pitches, appetite budgeting, hill charts, circuit breaker
- `kanban`: Continuous pull flow, WIP limits, cycle-time optimization
- `gist`: Goals, Ideas (ICE scored), Step-projects (<= 2 wks), Tasks for high-uncertainty planning

## 📦 Architecture & Conventions

- **Python Scripts**: Standard library only (Python 3.10+). No external dependencies.
- **Manifest**: Live metadata is in `dist/harness-manifest.json`.
- **Frameworks**: Located in `frameworks/strategy/`, `frameworks/discovery/`, `frameworks/prioritization/`, and `frameworks/operations/`.
