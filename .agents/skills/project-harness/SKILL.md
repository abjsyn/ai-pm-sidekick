---
name: project-harness
description: >-
  Core AI PM Sidekick operational router. Hydrates product context from .context/, enforces strict separation between internal UI and user deliverables, applies Socratic inquiry, and compounds knowledge.
---

# 🚀 AI PM Sidekick — Project Harness Router

This is the primary harness router skill for the AI PM Sidekick. It governs how agentic models interact with the workspace, consult product context, and generate production-grade PM deliverables.

## 🧭 1. Operating Principles & 4-Stage Execution Protocol

For any deliverable generation, refinement, or strategic analysis, execute in 4 strict stages:

1. **Stage 1: Context Hydration First**: Always read relevant files from `.context/` before initiating work:
   - Configuration & Operating Model: `.context/harness-config.yaml` (reads `mode`, `default_tier`, and `operating_model`)
   - Conventions & Standards: `.context/conventions.md` (DoR, DoD, Gherkin BDD, and Operating Model cadences)
   - Vision & Personas: `.context/product.md`
   - Discovery & Outcomes: `.context/discovery.md`
   - Strategy & Bottlenecks: `.context/strategy-and-constraints.md`
   - Architecture & Schemas: `.context/architecture.md` (plus repo package manifests in embedded mode)
   - Decision Log: `.context/decisions.md`

2. **Absolute Separation of Concerns (Zero Context Contamination)**:
   - `ui/specs/`, `ui/views/`, and `ui/stitch/` are strictly internal Sidekick web application assets. Never treat them as user product documentation.
   - User PRDs, specs, user stories, and technical documentation MUST be created in `docs/`.
   - User HTML prototypes, wireframes, and mockups MUST be created in `mockups/`.

3. **Stage 2: Socratic Clarifying Gate**:
   - Never hallucinate critical business constraints, user pain points, or architecture.
   - If user requirements lack necessary context for the requested deliverable tier, pause and ask 2–4 targeted clarifying questions.
   - If the user prefers fast iteration, document explicit working assumptions in the output.

4. **Stage 3: Grounded Generation**:
   - Produce deliverables matching the active tier (`lean` for MVPs, `standard` for Agile squads, `enterprise` for compliance and scale).
   - Apply relevant frameworks from `frameworks/` or use `/recommend-framework` to diagnose bottlenecks.
   - Adhere to Given/When/Then Gherkin acceptance criteria and INVEST guidelines for user stories.

5. **Stage 4: Knowledge Compounding (Write-Back)**:
   - When a session yields validated assumptions, architectural decisions, or user insights, propose updating the `.context/*.md` files and logging decisions in `.context/decisions.md`.

---

## ⚡ 2. Active Skills Catalog (19 Skills)

| Command / Trigger | Skill Name | Category | Primary Purpose |
| :--- | :--- | :--- | :--- |
| `/apply-framework` | **Modular Framework Runner** | `knowledge` | Executes modular strategic, discovery, or prioritization frameworks from frameworks/ over an idea, backlog, or PRD, and synchronizes results back to .context/. |
| `/brainstorm` | **Opportunity Brainstorm** | `ideation` | Facilitates structured product & feature brainstorming using SCAMPER, How Might We (HMW), 6 Thinking Hats, and Value vs. Effort matrix. |
| `/connect-mcp` | **MCP Integration Manager** | `sync` | Establishes, tests, and manages Model Context Protocol (MCP) integrations for external PM tools: Atlassian (Jira & Confluence), GitHub Issues, Figma, Miro, Notion, and Google Stitch across AGY, Claude Code, and Cursor IDEs. |
| `/create-design-brief` | **UI/UX Design Brief** | `specification` | Creates comprehensive UI/UX Design Briefs including design objectives, user context, step-by-step user flows, component specs, WCAG 2.1 AA accessibility guidelines, and Figma handoff criteria. |
| `/create-documentation` | **Technical & User Docs** | `specification` | Generates dual-purpose technical and end-user documentation. Produces API schemas (OpenAPI format), Mermaid sequence diagrams, architecture specs, and step-by-step end-user manuals. |
| `/create-mockup` | **HTML Wireframe & Prototype** | `specification` | Generates clickable, interactive UI mockups and prototypes as self-contained HTML files styled with Tailwind CSS, supporting interactive tabs, modals, forms, and responsive device views. |
| `/create-prd` | **PRD Generator** | `specification` | Generates comprehensive Product Requirements Documents (PRDs) across 3 modes: Lean (Startup/MVP), Standard Agile (Growth/Mid-size), and Enterprise (Compliance/Scale). |
| `/create-user-stories` | **INVEST User Stories** | `specification` | Generates user stories adhering to INVEST criteria, Concur format (As a/I want/So that), Gherkin Given-When-Then Acceptance Criteria, Fibonacci story points, and Definition of Done across Lean, Standard Agile, and Enterprise modes. |
| `/gui-run` | **PM Command Center GUI** | `gui` | Launches the PM Command Center visual web application (GUI) locally on port 3000 and automatically opens it in your default web browser. |
| `/ingest-context` | **Context Ingestion Router** | `knowledge` | Ingests raw unstructured inputs (meeting notes, customer interview transcripts, Slack dumps, existing PRDs, codebase READMEs, or MCP pages) and routes structured updates into .context/ product knowledge files. |
| `/recommend-framework` | **Framework Dispatcher** | `knowledge` | Diagnoses PM bottlenecks, uncertainty, or prioritization challenges, recommends the optimal framework & skill with a lightweight alternative and anti-pattern warning, and guides execution. |
| `/refine-user-stories` | **Story Refinement & SPIDR** | `specification` | Grooms and refines existing user stories. Detects ambiguity, splits large stories using the SPIDR framework, adds missing Gherkin edge cases, and calculates a Grooming Readiness Score (0-100%). |
| `/sync-confluence` | **Confluence Wiki Sync** | `sync` | Bi-directionally syncs Confluence product wikis and specs. Pulls company knowledge into .context/ and BACKLOG.md, or publishes PRDs, design briefs, and technical specs to Confluence via Atlassian MCP. |
| `/sync-figma` | **Figma Specs Sync** | `sync` | Bi-directionally syncs Figma design tokens, components, and brief annotations. Pulls design context into .context/ and BACKLOG.md, or posts UX specs to Figma nodes via Figma MCP. |
| `/sync-github-issues` | **GitHub Issues Sync** | `sync` | Bi-directionally syncs GitHub Issues, labels, and milestones. Pulls issues into BACKLOG.md and .context/discovery.md, or exports refined user stories as structured GitHub Issues. |
| `/sync-jira` | **Jira Epics & Stories Sync** | `sync` | Bi-directionally syncs Jira epics, stories, and sprint issues. Pulls issues into BACKLOG.md and .context/discovery.md, or exports INVEST user stories from docs/ to Jira via Atlassian MCP. |
| `/sync-miro` | **Miro Whiteboards Sync** | `sync` | Bi-directionally syncs Miro whiteboards, brainstorm sticky notes, and roadmaps. Pulls visual ideation into .context/ and BACKLOG.md, or exports brainstorms/roadmaps to Miro via Miro MCP. |
| `/sync-notion` | **Notion Databases Sync** | `sync` | Bi-directionally syncs Notion product wikis, databases, and pages. Pulls research into .context/, or publishes PRDs, design briefs, and decision logs to Notion. |
| `/validate-idea` | **Idea & Hypothesis Validator** | `ideation` | Validates product ideas, feature concepts, and business hypotheses using Strategyzer 4-Risk Analysis, The Mom Test customer interview framework, TAM/SAM/SOM market sizing, and Pre-mortem risk identification. |

---

## 🗺️ 3. Modular Product Frameworks (10 Frameworks across 4 Categories)

Frameworks are organized into 4 strategic categories and invoked via `/apply-framework <id>` or diagnosed via `/recommend-framework`:

### 📈 Strategy Frameworks
- **Theory of Constraints (ToC) & CRT Mapping** (`theory-of-constraints`): To pinpoint the operational bottleneck choking product delivery, maximize throughput at that specific point, and align all upstream discovery and downstream execution to eliminate waste.
  - *Target*: `.context/strategy-and-constraints.md` | *Data Maturity*: `medium` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Engineering delivery velocity stalls despite adding headcount or running more syncs; Backlog grows exponentially while deployment throughput remains completely flat
- **Wardley Value Chain Evolution Mapping** (`wardley-mapping`): To prevent catastrophic resource misallocation (e.g., custom-building commoditized components) and explicitly identify where a product's true competitive differentiation resides.
  - *Target*: `.context/strategy-and-constraints.md` | *Data Maturity*: `low` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Team debates custom-building infrastructure vs buying SaaS or using cloud utilities; Unclear where durable competitive advantage lies in the technology architecture

### 🔍 Discovery Frameworks
- **Jobs-to-be-Done (JTBD) & The Mom Test** (`jtbd-and-mom-test`): To uncover genuine customer demand by systematically filtering out false validation, identifying real customer struggle, and structuring value propositions around the forces that drive adoption.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `low` | *Stages*: `0-to-1, growth, scale`
  - *Solves*: Customers give polite compliments in interviews but never buy, activate, or retain; Feature specifications anchor on opinions and generic hypothetical promises
- **Opportunity Solution Tree (OST)** (`opportunity-solution-tree`): To break the "feature factory" anti-pattern by ensuring teams explore the problem space thoroughly, evaluate multiple competing solutions for each customer pain point, and test assumptions before committing engineering resources.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `medium` | *Stages*: `0-to-1, growth, scale, enterprise`
  - *Solves*: Team operates as a feature factory shipping random stakeholder solution requests; Features lack direct traceability to measurable business outcomes

### ⚖️ Prioritization Frameworks
- **The Kano Model & Customer Delight** (`kano-model`): To construct balanced product releases that satisfy table-stakes baseline requirements, compete effectively on performance, and incorporate distinct delighters while aggressively pruning indifferent bloat.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `medium` | *Stages*: `0-to-1, growth, scale`
  - *Solves*: MVP scope suffers from feature creep and lacks differentiation from competitors; Unclear distinction between table-stakes basic features and true delighters
- **RICE Scoring Matrix** (`rice`): To eliminate cognitive bias, loud-stakeholder lobbying, and "pet project" syndrome by anchoring prioritization to empirical reach, measurable business impact, defensible confidence, and engineering effort.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `medium` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Backlog is prioritized by who speaks the loudest or highest-paid person's opinion (HiPPO); Low-impact pet projects consistently displace high-reach core features
- **Weighted Shortest Job First (WSJF) & Cost of Delay** (`wsjf-cost-of-delay`): To maximize economic flow by scheduling high-value, time-critical, risk-reducing features that can be delivered quickly, preventing the common failure mode of tying up engineering squads on monolithic, slow-moving projects.
  - *Target*: `.context/strategy-and-constraints.md` | *Data Maturity*: `high` | *Stages*: `scale, enterprise`
  - *Solves*: Slow-moving massive initiatives block fast, high-impact tactical releases; Time-sensitive market opportunities or regulatory deadlines missed due to poor sequencing

### 🚀 Operations & Delivery Frameworks
- **GIST Planning (Goals, Ideas, Step-projects, Tasks)** (`gist-planning`): To drastically reduce product waste by testing ideas through tiny step-projects before committing full engineering squads to building multi-month feature implementations.
  - *Target*: `.context/product.md` | *Data Maturity*: `low` | *Stages*: `0-to-1, growth, scale`
  - *Solves*: Annual or quarterly roadmaps become obsolete within weeks of leadership sign-off; Teams commit to multi-month solutions before validating whether the core concept works
- **Scrum Sprint Delivery & INVEST Execution** (`scrum-sprint-delivery`): To provide predictable, sustainable, cross-functional engineering throughput with continuous delivery of shippable software increments.
  - *Target*: `.context/conventions.md` | *Data Maturity*: `medium` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Sprints fail repeatedly because stories are too large, ambiguous, or unestimated; Engineers build literal ticket text rather than solving the real customer need
- **Shape Up (Basecamp Product Development)** (`shape-up`): To eliminate endless scope creep, eliminate backlog grooming debt, and empower autonomous cross-functional teams to deliver complete, polished features within bounded timeboxes.
  - *Target*: `.context/conventions.md` | *Data Maturity*: `low` | *Stages*: `0-to-1, growth, scale`
  - *Solves*: Projects drag on indefinitely with continuous sprint rollovers and creeping scope; Engineers receive UI wireframes that are too rigid or PRDs that are too vague

---

## 🔄 4. Delivery Operating Models (`operating_model`)

Configured via `operating_model` in `.context/harness-config.yaml` and detailed in Section 5 of `.context/conventions.md`:
- **`scrum`** *(Default)*: 1–2 week sprints, INVEST stories, Fibonacci points (<= 5 pts), sprint velocity and DoD sign-off.
- **`shape-up`**: 6-week cycles + 2-week cooldown, shaped pitches, fixed appetite budgeting, hill charts, and circuit breaker.
- **`kanban`**: Continuous pull flow, WIP limits, cycle-time optimization, backlog queue triage.
- **`gist`**: Iterative experiment loops, step-projects (<= 2 weeks), ICE scoring, outcome tracking.

---

## 🛠️ 5. Integration & Tooling Reference

- **Model Context Protocol (MCP)**: Use `/connect-mcp` or tool-specific sync skills (`/sync-jira`, `/sync-confluence`, `/sync-github-issues`, `/sync-figma`, `/sync-miro`, `/sync-notion`).
- **GUI Command Center**: Launch the local visual dashboard on port 3000 via `/gui-run` (`python3 scripts/launch-ui.py --open`).
- **Machine-Readable Manifest**: Consult `dist/harness-manifest.json` for live schema definitions, triggers, and framework metadata.
