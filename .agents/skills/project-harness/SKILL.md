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

## ⚡ 2. Active Skills Catalog (30 Skills)

| Command / Trigger | Skill Name | Category | Primary Purpose |
| :--- | :--- | :--- | :--- |
| `/analyze-competitor` | **Competitor Analysis & Battlecard** | `strategy` | Takes competitor URLs, release notes, or positioning dumps, compares them against .context/ product specs, and outputs a feature parity matrix, differentiation gaps, and a 1-page Sales/PM battlecard. |
| `/apply-framework` | **Modular Framework Runner** | `knowledge` | Executes modular strategic, discovery, or prioritization frameworks from frameworks/ over an idea, backlog, or PRD, and synchronizes results back to .context/. |
| `/audit-spec` | **Spec Auditor & Pre-Mortem Critique** | `specification` | Audits draft PRDs and User Stories against .context/ single source of truth, flagging scope creep, missing edge cases, unvalidated assumptions, and architectural conflicts. |
| `/brainstorm` | **Opportunity Brainstorm** | `ideation` | Facilitates structured product & feature brainstorming using SCAMPER, How Might We (HMW), 6 Thinking Hats, and Value vs. Effort matrix. |
| `/connect-mcp` | **MCP Integration Manager** | `sync` | Establishes, tests, and manages Model Context Protocol (MCP) integrations for external PM tools: Atlassian (Jira & Confluence), GitHub Issues, Figma, Miro, Notion, and Google Stitch across AGY, Claude Code, and Cursor IDEs. |
| `/create-design-brief` | **UI/UX Design Brief** | `specification` | Creates comprehensive UI/UX Design Briefs including design objectives, user context, step-by-step user flows, component specs, WCAG 2.1 AA accessibility guidelines, and Figma handoff criteria. |
| `/create-documentation` | **Technical & User Docs** | `specification` | Generates dual-purpose technical and end-user documentation. Produces API schemas (OpenAPI format), Mermaid sequence diagrams, architecture specs, and step-by-step end-user manuals. |
| `/create-mockup` | **HTML Wireframe & Prototype** | `specification` | Generates clickable, interactive UI mockups and prototypes as self-contained HTML files styled with Tailwind CSS, supporting interactive tabs, modals, forms, and responsive device views. |
| `/create-prd` | **PRD Generator** | `specification` | Generates comprehensive Product Requirements Documents (PRDs) across 3 modes: Lean (Startup/MVP), Standard Agile (Growth/Mid-size), and Enterprise (Compliance/Scale). |
| `/create-roadmap` | **Outcome Roadmap Generator** | `strategy` | Transforms BACKLOG.md, .context/discovery.md, and prioritization scores into a stakeholder-ready Now / Next / Later or Quarterly OKR Outcome Roadmap. |
| `/create-stakeholder-update` | **Stakeholder Update & Release Notes** | `communication` | Synthesizes recent changes in BACKLOG.md, .context/decisions.md, and docs/ into tailored communications: Executive Weekly Digest, Engineering/Cross-Functional Update, or Customer-Facing Release Notes. |
| `/create-user-stories` | **INVEST User Stories** | `specification` | Generates user stories adhering to INVEST criteria, Concur format (As a/I want/So that), Gherkin Given-When-Then Acceptance Criteria, Fibonacci story points, and Definition of Done across Lean, Standard Agile, and Enterprise modes. |
| `/define-metrics-and-experiment` | **Metrics & Experiment Plan** | `specification` | Defines feature success metrics (North Star, Primary, Guardrail), event tracking taxonomy (events + properties), and A/B test or rollout hypotheses before engineering begins building. |
| `/evaluate-launch` | **Post-Launch Retrospective** | `operations` | Evaluates post-launch performance data against the PRD's original success metrics, logs whether the bet succeeded/failed/iterated, and writes lessons learned back to .context/decisions.md. |
| `/gui-run` | **PM Command Center GUI** | `gui` | Launches the PM Command Center visual web application (GUI) locally on port 3000 and automatically opens it in your default web browser. |
| `/ingest-context` | **Context Ingestion Router** | `knowledge` | Ingests raw unstructured inputs (meeting notes, customer interview transcripts, Slack dumps, existing PRDs, codebase READMEs, or MCP pages) and routes structured updates into .context/ product knowledge files. |
| `/plan-launch` | **GTM Launch Plan** | `operations` | Generates a tiered launch plan (Tier 1 Major, Tier 2 Standard, Tier 3 Silent) from a PRD, including positioning messaging, internal enablement FAQs, rollout checklists, and rollback triggers. |
| `/prep-meeting` | **Meeting Prep & Defense Brief** | `communication` | Prepares a 1-page briefing doc before a tough stakeholder review, board meeting, or customer call, pulling past decisions, anticipated objections, trade-off options, and talking points. |
| `/prepare-user-interview` | **User Interview Script & Guide** | `discovery` | Generates non-leading Mom Test interview guides, screener questions, and assumption probes tailored to a specific target persona and hypothesis before user discovery sessions. |
| `/recommend-framework` | **Framework Dispatcher** | `knowledge` | Diagnoses PM bottlenecks, uncertainty, or prioritization challenges, recommends the optimal framework & skill with a lightweight alternative and anti-pattern warning, and guides execution. |
| `/refine-user-stories` | **Story Refinement & SPIDR** | `specification` | Grooms and refines existing user stories. Detects ambiguity, splits large stories using the SPIDR framework, adds missing Gherkin edge cases, and calculates a Grooming Readiness Score (0-100%). |
| `/sync-confluence` | **Confluence Wiki Sync** | `sync` | Bi-directionally syncs Confluence product wikis and specs. Pulls company knowledge into .context/ and BACKLOG.md, or publishes PRDs, design briefs, and technical specs to Confluence via Atlassian MCP. |
| `/sync-figma` | **Figma Specs Sync** | `sync` | Bi-directionally syncs Figma design tokens, components, and brief annotations. Pulls design context into .context/ and BACKLOG.md, or posts UX specs to Figma nodes via Figma MCP. |
| `/sync-github-issues` | **GitHub Issues Sync** | `sync` | Bi-directionally syncs GitHub Issues, labels, and milestones. Pulls issues into BACKLOG.md and .context/discovery.md, or exports refined user stories as structured GitHub Issues. |
| `/sync-jira` | **Jira Epics & Stories Sync** | `sync` | Bi-directionally syncs Jira epics, stories, and sprint issues. Pulls issues into BACKLOG.md and .context/discovery.md, or exports INVEST user stories from docs/ to Jira via Atlassian MCP. |
| `/sync-linear` | **Linear Issues & Cycles Sync** | `sync` | Bi-directionally syncs Linear issues, cycles, projects, and triage queues via Model Context Protocol (MCP). Imports Linear issues into BACKLOG.md and .context/discovery.md, or exports INVEST user stories to Linear. |
| `/sync-miro` | **Miro Whiteboards Sync** | `sync` | Bi-directionally syncs Miro whiteboards, brainstorm sticky notes, and roadmaps. Pulls visual ideation into .context/ and BACKLOG.md, or exports brainstorms/roadmaps to Miro via Miro MCP. |
| `/sync-notion` | **Notion Databases Sync** | `sync` | Bi-directionally syncs Notion product wikis, databases, and pages. Pulls research into .context/, or publishes PRDs, design briefs, and decision logs to Notion. |
| `/triage-feedback` | **Customer Feedback Triage** | `discovery` | Batch-processes raw customer feedback, support tickets, NPS verbatims, or sales call notes, clustering them by frequency and severity, and mapping them to opportunities in .context/discovery.md. |
| `/validate-idea` | **Idea & Hypothesis Validator** | `ideation` | Validates product ideas, feature concepts, and business hypotheses using Strategyzer 4-Risk Analysis, The Mom Test customer interview framework, TAM/SAM/SOM market sizing, and Pre-mortem risk identification. |

---

## 🗺️ 3. Modular Product Frameworks (23 Frameworks across 4 Categories)

Frameworks are organized into 4 strategic categories and invoked via `/apply-framework <id>` or diagnosed via `/recommend-framework`:

### 📈 Strategy Frameworks
- **North Star Metric & Input Metric Tree** (`north-star-metric-tree`): To establish a clear causal equation between day-to-day feature development and overall company success, ensuring squads optimize actionable leading indicators without gaming the system.
  - *Target*: `.context/product.md` | *Data Maturity*: `medium` | *Stages*: `0-to-1, growth, scale, enterprise`
  - *Solves*: Team is optimizing fragmented vanity metrics that do not roll up to sustainable customer value; Different squads or engineers pull in opposing directions without a unified equation of growth
- **Van Westendorp & Packaging/Tiering Matrix** (`pricing-and-packaging`): To establish data-backed pricing boundaries, eliminate monetization guesswork, and package features into clear, high-converting tier boundaries.
  - *Target*: `.context/strategy-and-constraints.md` | *Data Maturity*: `medium` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Pricing strategy is based on internal team guesswork rather than empirical customer willingness-to-pay; Feature tiering is confusing and customers resist upgrading between Free, Pro, and Enterprise
- **Product Positioning (April Dunford)** (`product-positioning`): To eliminate positioning confusion, elevate differentiation above incumbent competitors, and guide GTM launch messaging, sales battlecards, and PRD scope.
  - *Target*: `.context/strategy-and-constraints.md` | *Data Maturity*: `medium` | *Stages*: `0-to-1, growth, scale`
  - *Solves*: Prospects and customers say 'So what?' or misunderstand what the product actually does; Sales team struggles to close deals without extensive discounting or custom development
- **7 Powers (Hamilton Helmer) Moat Analysis** (`seven-powers-moats`): To force product managers to distinguish between temporary "features" (easily copied commodities) and structural "powers" that generate enduring enterprise value.
  - *Target*: `.context/strategy-and-constraints.md` | *Data Maturity*: `medium` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Features are easily copied by well-funded incumbents within weeks of launching; The product lacks durable structural defensibility or pricing power as it scales
- **Theory of Constraints (ToC) & CRT Mapping** (`theory-of-constraints`): To pinpoint the operational bottleneck choking product delivery, maximize throughput at that specific point, and align all upstream discovery and downstream execution to eliminate waste.
  - *Target*: `.context/strategy-and-constraints.md` | *Data Maturity*: `medium` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Engineering delivery velocity stalls despite adding headcount or running more syncs; Backlog grows exponentially while deployment throughput remains completely flat
- **Wardley Value Chain Evolution Mapping** (`wardley-mapping`): To prevent catastrophic resource misallocation (e.g., custom-building commoditized components) and explicitly identify where a product's true competitive differentiation resides.
  - *Target*: `.context/strategy-and-constraints.md` | *Data Maturity*: `low` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Team debates custom-building infrastructure vs buying SaaS or using cloud utilities; Unclear where durable competitive advantage lies in the technology architecture
- **Working Backwards (Amazon PR/FAQ)** (`working-backwards-prfaq`): To enforce extreme customer-centric clarity, prevent technical solipsism, align cross-functional leaders around the core value proposition, and expose unaddressed trade-offs long before development begins.
  - *Target*: `.context/strategy-and-constraints.md` | *Data Maturity*: `low` | *Stages*: `0-to-1, growth, enterprise`
  - *Solves*: Feature concept is heavily engineering-led or architecture-driven without a clear customer value narrative; Product vision is diffuse and executive stakeholders disagree on the core customer experience being built

### 🔍 Discovery Frameworks
- **AARRR Pirate Metrics & Growth Loops** (`aarrr-and-growth-loops`): To diagnose exactly where the user conversion leaks occur, fix the "leaky bucket" before spending money on acquisition, and architect compounding, product-led distribution loops.
  - *Target*: `.context/product.md` | *Data Maturity*: `medium` | *Stages*: `growth, scale`
  - *Solves*: User acquisition is growing but revenue or retention is flatlining (leaky bucket syndrome); Growth model relies entirely on paid linear ads rather than compounding self-reinforcing product loops
- **Assumption Mapping & Riskiest Assumption Test (RAT)** (`assumption-mapping`): To eliminate leap-of-faith failures and prevent engineering teams from spending months building products or features that nobody wants, cannot be monetized, or hit insurmountable technical roadblocks.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `low` | *Stages*: `0-to-1, growth`
  - *Solves*: Team is preparing to build a major feature based on unverified team opinions rather than customer evidence; Unclear which risk (desirability, feasibility, viability, usability) could kill the product first
- **Jobs-to-be-Done (JTBD) & The Mom Test** (`jtbd-and-mom-test`): To uncover genuine customer demand by systematically filtering out false validation, identifying real customer struggle, and structuring value propositions around the forces that drive adoption.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `low` | *Stages*: `0-to-1, growth, scale`
  - *Solves*: Customers give polite compliments in interviews but never buy, activate, or retain; Feature specifications anchor on opinions and generic hypothetical promises
- **Opportunity Solution Tree (OST)** (`opportunity-solution-tree`): To break the "feature factory" anti-pattern by ensuring teams explore the problem space thoroughly, evaluate multiple competing solutions for each customer pain point, and test assumptions before committing engineering resources.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `medium` | *Stages*: `0-to-1, growth, scale, enterprise`
  - *Solves*: Team operates as a feature factory shipping random stakeholder solution requests; Features lack direct traceability to measurable business outcomes

### ⚖️ Prioritization Frameworks
- **ICE & Value vs. Effort Prioritization** (`ice-and-value-effort`): To deliver rapid, transparent prioritization when teams are in early stages, lack large-scale statistical telemetry for RICE, or need to unblock backlog paralysis in under 15 minutes.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `low` | *Stages*: `0-to-1, growth`
  - *Solves*: Team lacks quantitative reach and conversion telemetry required to run RICE without guessing; Need a fast, 15-minute consensus scoring method to rank a brainstormed backlog of 15+ ideas
- **The Kano Model & Customer Delight** (`kano-model`): To construct balanced product releases that satisfy table-stakes baseline requirements, compete effectively on performance, and incorporate distinct delighters while aggressively pruning indifferent bloat.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `medium` | *Stages*: `0-to-1, growth, scale`
  - *Solves*: MVP scope suffers from feature creep and lacks differentiation from competitors; Unclear distinction between table-stakes basic features and true delighters
- **MoSCoW & Buy-a-Feature Scope Negotiation** (`moscow-scope-negotiation`): To establish enforceable release boundaries, protect developers from burnout, and prevent the "everything is high priority" trap during fixed-date enterprise deliveries.
  - *Target*: `.context/strategy-and-constraints.md` | *Data Maturity*: `low` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Stakeholders treat every feature request as an absolute P0 must-have; Release deadlines are fixed by contractual commitments but scope keeps ballooning
- **Opportunity Scoring (Importance vs. Satisfaction)** (`opportunity-scoring`): To eliminate the wasteful "feature trap" of improving capabilities that customers already find "good enough", and redirect resources toward high-importance jobs where customers remain acutely dissatisfied.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `medium` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Team is over-investing in features where customer satisfaction is already high (over-served market); Critical customer needs are severely underserved, but ignored because no vocal stakeholder advocates for them
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
- **Continuous Kanban & Service Level Expectations (SLE)** (`kanban-continuous-flow`): To eliminate sprint-end crunch and rollover anxiety, stabilize flow predictability, shorten lead time from idea to production, and ensure operational readiness when `operating_model: kanban` is active in `.context/harness-config.yaml`.
  - *Target*: `.context/conventions.md` | *Data Maturity*: `medium` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Teams struggle with sprint batching friction and artificial 2-week boundary overhead; Work-in-progress (WIP) bloat causes lead times and cycle times to blow out unpredictably
- **Pre-Mortem (Tigers, Paper Tigers & Elephants)** (`pre-mortem-tigers`): To normalize the voice of dissent, prevent preventable launch disasters, clear away unproductive anxiety over minor edge cases, and confront taboo blockers while there is still time to adjust scope.
  - *Target*: `.context/decisions.md` | *Data Maturity*: `low` | *Stages*: `0-to-1, growth, scale, enterprise`
  - *Solves*: Teams experience catastrophic launch-day surprises that could easily have been anticipated; Engineering and business teams waste excessive energy debating vocal but harmless minor worries
- **Scrum Sprint Delivery & INVEST Execution** (`scrum-sprint-delivery`): To provide predictable, sustainable, cross-functional engineering throughput with continuous delivery of shippable software increments.
  - *Target*: `.context/conventions.md` | *Data Maturity*: `medium` | *Stages*: `growth, scale, enterprise`
  - *Solves*: Sprints fail repeatedly because stories are too large, ambiguous, or unestimated; Engineers build literal ticket text rather than solving the real customer need
- **Shape Up (Basecamp Product Development)** (`shape-up`): To eliminate endless scope creep, eliminate backlog grooming debt, and empower autonomous cross-functional teams to deliver complete, polished features within bounded timeboxes.
  - *Target*: `.context/conventions.md` | *Data Maturity*: `low` | *Stages*: `0-to-1, growth, scale`
  - *Solves*: Projects drag on indefinitely with continuous sprint rollovers and creeping scope; Engineers receive UI wireframes that are too rigid or PRDs that are too vague
- **User Story Mapping (Jeff Patton)** (`user-story-mapping`): To eliminate "flat backlog blindness", ensure teams ship complete, coherent end-to-end user journeys rather than disconnected vertical feature fragments, and establish clear release boundaries based on value increments.
  - *Target*: `.context/discovery.md` | *Data Maturity*: `low` | *Stages*: `0-to-1, growth, scale`
  - *Solves*: Backlog is a flat, unprioritized list of tickets with no visibility into the end-to-end customer journey; Teams struggle to carve out a true Walking Skeleton MVP without scope creeping into a monolithic release

---

## 🔄 4. Delivery Operating Models (`operating_model`)

Configured via `operating_model` in `.context/harness-config.yaml` and detailed in Section 5 of `.context/conventions.md`:
- **`scrum`** *(Default)*: 1–2 week sprints, INVEST stories, Fibonacci points (<= 5 pts), sprint velocity and DoD sign-off.
- **`shape-up`**: 6-week cycles + 2-week cooldown, shaped pitches, fixed appetite budgeting, hill charts, and circuit breaker.
- **`kanban`**: Continuous pull flow, WIP limits, cycle-time optimization, backlog queue triage.
- **`gist`**: Iterative experiment loops, step-projects (<= 2 weeks), ICE scoring, outcome tracking.

---

## 🛠️ 5. Integration & Tooling Reference

- **Model Context Protocol (MCP)**: Use `/connect-mcp` or tool-specific sync skills (`/sync-jira`, `/sync-confluence`, `/sync-github-issues`, `/sync-linear`, `/sync-figma`, `/sync-miro`, `/sync-notion`).
- **GUI Command Center**: Launch the local visual dashboard on port 3000 via `/gui-run` (`python3 scripts/launch-ui.py --open`).
- **Machine-Readable Manifest**: Consult `dist/harness-manifest.json` for live schema definitions, triggers, and framework metadata.
