# 🚀 AI PM Sidekick

**AI PM Sidekick** is a local-first, privacy-respecting, tool-agnostic AI assistant framework and harness built for Product Managers, Technical PMs, and Engineering Leads. It bridges the gap between chaotic customer discovery and engineering execution—powering idea validation, PRDs, user stories, interactive HTML wireframes, design briefs, technical documentation, the **PM Command Center Web GUI**, and **live bi-directional MCP integrations with Atlassian (Jira & Confluence), GitHub Issues, Figma, Miro, Notion, and Google Stitch**.

> 📖 **Looking for the complete operational guide?**  
> Read the [📘 AI-SDLC Playbook (AI_SDLC.md)](AI_SDLC.md) for step-by-step walkthroughs of **Workflow A (Standalone PM Command Center)**, **Workflow B (Embedded Codebase Harness)**, adding custom frameworks in 2 minutes, and context hygiene rules.

---

## 🌟 Core Capabilities & 18 Canonical Skills

| Skill / Integration | Slash Command | Category | Description | Primary Output Target | Next Skill Suggestion |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PM Command Center** | `/gui-run` | `gui` | Web GUI dashboard & REST API on `localhost:3000` | Google Stitch Atelier UI | `create-prd`, `connect-mcp` |
| **Context Ingestion** | `/ingest-context` | `knowledge` | Distills raw notes, calls, & Slack dumps into `.context/` | `.context/*.md`, `decisions.md` | `apply-framework`, `create-prd` |
| **Apply Framework** | `/apply-framework` | `knowledge` | Runs strategic, discovery, & prioritization models | `.context/`, `BACKLOG.md`, `docs/` | `create-prd`, `create-user-stories` |
| **Idea Validation** | `/validate-idea` | `ideation` | Evaluates raw concepts & hypotheses (4-Risk, Mom Test, Pre-mortem) | 4-Risk Brief in `docs/` | `brainstorm`, `create-prd` |
| **Brainstorming** | `/brainstorm` | `ideation` | Generates innovative solution angles (SCAMPER, HMW, 6 Hats) | Opportunity doc in `docs/` | `sync-miro`, `create-prd` |
| **PRD Generation** | `/create-prd` | `specification` | Generates structured PRDs across Lean, Standard, and Enterprise tiers | PRD in `docs/` | `create-mockup`, `create-user-stories` |
| **Clickable Mockups** | `/create-mockup` | `specification` | Generates self-contained, interactive Tailwind HTML wireframes | HTML prototype in `mockups/` | `create-design-brief`, `create-user-stories` |
| **Design Briefs** | `/create-design-brief` | `specification` | Bridges PM and UI/UX design specs with WCAG 2.1 AA accessibility | UI/UX Brief in `docs/` | `sync-figma`, `create-mockup` |
| **User Stories** | `/create-user-stories` | `specification` | Breaks down features into INVEST stories + Gherkin BDD AC | User Stories in `docs/` | `refine-user-stories`, `sync-jira` |
| **Story Grooming** | `/refine-user-stories` | `specification` | Refines & splits stories using SPIDR with Readiness Score | Refined Stories in `docs/` | `sync-jira`, `sync-github-issues` |
| **Documentation** | `/create-documentation` | `specification` | Dual tech spec & user guide generator (OpenAPI 3.0, Mermaid) | Tech Docs & Manuals in `docs/` | `sync-confluence`, `sync-notion` |
| **MCP Manager** | `/connect-mcp` | `sync` | Connects & verifies external PM tools across IDEs | `mcp.json` & `.env` | `sync-jira`, `sync-github-issues` |
| **Jira Backlog Sync** | `/sync-jira` | `sync` | Exports stories/epics directly to Jira via Atlassian MCP | Jira Issues & Epics | `sync-confluence`, `refine-user-stories` |
| **Confluence Doc Sync**| `/sync-confluence` | `sync` | Publishes PRDs/specs straight to Confluence spaces | Confluence Wiki Pages | `sync-jira`, `create-documentation` |
| **GitHub Issues Sync** | `/sync-github-issues` | `sync` | Bi-directional GitHub Issues, milestones, and label sync | GitHub Issues & Milestones | `refine-user-stories`, `sync-jira` |
| **Figma Design Sync** | `/sync-figma` | `sync` | Inspects components & posts design feedback to Figma nodes | Figma Comments & Specs | `create-mockup`, `create-design-brief` |
| **Miro Whiteboard Sync**| `/sync-miro` | `sync` | Exports brainstorm stickies, OSTs, and roadmaps to Miro | Miro Visual Boards | `validate-idea`, `apply-framework` |
| **Notion Wiki Sync** | `/sync-notion` | `sync` | Bi-directional Notion research databases and PRD wiki sync | Notion Pages & Databases | `create-prd`, `ingest-context` |

---

## 🧠 The `.context/` Product Knowledge Core

At the center of AI PM Sidekick is a persistent, version-controlled **single source of truth** in `.context/`. Instead of stuffing massive prompts into ephemeral chat windows, agents continuously hydrate from and compound knowledge back into these structured files:

- [`.context/harness-config.yaml`](.context/harness-config.yaml): Workspace mode (`standalone` vs `embedded`), default tier (`lean`, `standard`, `enterprise`), active frameworks, and enabled MCP integrations.
- [`.context/product.md`](.context/product.md): High-level strategic vision, primary personas, core value loops, North Star metric, and quarterly OKRs.
- [`.context/discovery.md`](.context/discovery.md): Teresa Torres Opportunity Solution Trees (OST), active customer opportunities, and verified Mom Test insights.
- [`.context/strategy-and-constraints.md`](.context/strategy-and-constraints.md): Wardley Map value chain evolution table, Theory of Constraints system bottleneck, and business/regulatory constraints.
- [`.context/architecture.md`](.context/architecture.md): Live tech stack, entity data models, API boundaries, security constraints, and codebase directory layout.
- [`.context/conventions.md`](.context/conventions.md): Team Definition of Ready (DoR), Given/When/Then Gherkin acceptance criteria standards, and tier rules.
- [`.context/decisions.md`](.context/decisions.md): Append-only immutable Product Decision Log (PDR/ADR) tracking historical trade-offs, rationale, and rejected alternatives.

### 🚫 Strict Asset Separation (Zero Context Contamination)
To eliminate AI hallucinations:
- **Internal Sidekick UI Specs & Views (`ui/specs/`, `ui/views/`)**: Reserved strictly for the Sidekick's own web UI.
- **User Product Deliverables (`docs/`, `mockups/`)**: All PRDs, user stories, and specs belong exclusively in `docs/`; all wireframes belong in `mockups/`.

---

## 🗺️ Modular Framework Engine (`frameworks/`)

AI PM Sidekick includes a decoupled library of industry-standard strategic, discovery, and prioritization frameworks:

### 1. Strategic Frameworks ([`frameworks/strategy/`](frameworks/strategy/))
- **`wardley-mapping`**: Plots value chain components along Visibility vs. Evolution (Genesis ➔ Custom ➔ Product ➔ Commodity) to enforce disciplined Build-vs-Buy decisions.
- **`theory-of-constraints`**: Executes Goldratt's 5 Focusing Steps to exploit the primary system bottleneck choking sprint throughput, backed by Current Reality Trees (CRT).

### 2. Discovery Frameworks ([`frameworks/discovery/`](frameworks/discovery/))
- **`opportunity-solution-tree`**: Teresa Torres OST framework connecting Desired Business Outcomes $\rightarrow$ Customer Opportunities (unmet needs) $\rightarrow$ Candidate Solutions $\rightarrow$ Fastest Assumption Tests.
- **`jtbd-and-mom-test`**: Maps Functional, Emotional, and Social jobs across the Four Forces of Progress ($\text{Push} + \text{Pull} > \text{Anxiety} + \text{Habit}$) and filters customer interviews for behavioral facts over empty compliments.

### 3. Prioritization Frameworks ([`frameworks/prioritization/`](frameworks/prioritization/))
- **`rice`**: Quantitative score ($\frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort}}$) featuring strict anti-gaming confidence thresholds ($100\%, 80\%, 50\%, 20\%$).
- **`wsjf-cost-of-delay`**: Weighted Shortest Job First economic scheduling ($\frac{\text{User Value} + \text{Time Criticality} + \text{Risk Reduction}}{\text{Job Size}}$).
- **`kano-model`**: Non-linear customer satisfaction classification (Must-be, One-dimensional, Attractive, Indifferent) using functional/dysfunctional question pairs.

> 💡 **Add your own custom framework in under 2 minutes!** Follow the standardized 5-part schema in [`frameworks/README.md`](frameworks/README.md) and run `python3 scripts/export-skills.py`.

---

## 🔌 6 Live MCP Tool Integrations

Connect the Sidekick directly to your team's production tool stack using the Model Context Protocol (MCP):

| Tool | Supported Workflows | MCP Server Package |
| :--- | :--- | :--- |
| **Atlassian (Jira)** | Backlog sync, epic generation, ticket creation, status updates | `npx -y @atlassian/mcp` |
| **Atlassian (Confluence)**| PRD publishing, engineering spec updates, space page creation | `npx -y @atlassian/mcp` |
| **GitHub Issues** | Bi-directional issue sync, milestone mapping, label assignment | `npx -y @modelcontextprotocol/server-github` |
| **Figma** | Design file inspection, component discovery, canvas comments | `npx -y @figma/mcp` |
| **Miro** | Sticky note brainstorming, OST visual maps, roadmap exports | `npx -y @miro/mcp` |
| **Notion** | Research database syncing, product wiki publishing, PDR logs | `npx -y @notionhq/notion-mcp-server` |

---

## 🚀 Quick Start Guide

### 1. Initialize Workspace
```bash
# Standalone mode (launches local web GUI & PM Command Center):
python3 scripts/init-workspace.py --mode standalone --open

# Embedded mode (scans existing codebase & pre-populates .context/architecture.md):
python3 scripts/init-workspace.py --mode embedded --tier standard
```

### 2. Configure MCP Credentials
```bash
# Run interactive setup wizard for Jira, Confluence, GitHub, Figma, Miro, Notion:
python3 scripts/setup-mcp.py --interactive

# Audit readiness and verify credentials:
python3 scripts/setup-mcp.py --check
```

### 3. Compile Skills & Multi-Tool Adapters
```bash
python3 scripts/export-skills.py
```
This generates native configurations for:
- **AGY / Gemini**: `.agents/skills/` and `.agents/project-harness/SKILL.md`
- **Cursor IDE**: `.cursor/rules/*.mdc` and `.cursorrules`
- **Claude Code**: `.claude/commands/*.md` and `CLAUDE.md`
- **ChatGPT / Custom GPTs**: `dist/pm_sidekick_system_prompt.md`
- **Web GUI Sidepanel**: `dist/harness-manifest.json`

---

## 🎯 3 Operational Deliverable Tiers

When generating PRDs or User Stories, choose your compliance and detail tier:
1. **⚡ Lean Mode (Startup / MVP)**: 1-page PRDs, rapid bullet acceptance criteria, minimal overhead.
2. **🎯 Standard Agile Mode (Default / Growth)**: Full INVEST criteria, Gherkin BDD (`Given/When/Then`), Fibonacci story points, and Definition of Done.
3. **🏢 Enterprise Mode (Compliance / Scale)**: Traceability matrices, SOC2/GDPR compliance tags, security assertions, SLA targets, and audit log specifications.

---

## 📚 Complete Documentation & Playbook

- **Operational Playbook**: [📘 AI-SDLC Playbook (AI_SDLC.md)](AI_SDLC.md)
- **Framework Guide**: [🗺️ Frameworks Architecture (frameworks/README.md)](frameworks/README.md)
- **MCP Connection Guide**: [🔌 MCP Connect Guide (skills/connect-mcp/SKILL.md)](skills/connect-mcp/SKILL.md)
- **Backlog**: [📋 Product Backlog (BACKLOG.md)](BACKLOG.md)

---

*AI PM Sidekick — Built with ❤️ for Product Managers who demand strategic rigor, architectural grounding, and zero busywork.*
