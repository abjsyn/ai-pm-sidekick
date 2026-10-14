# AI PM Sidekick — Claude Code Workspace Guide

Welcome to **AI PM Sidekick**, a local-first product management command center and AI harness.

## 🧭 Core Workflow & The 4-Stage Protocol

When assisting product managers, technical PMs, or engineering leads, always follow this protocol:

1. **Stage 1: Context Hydration**
   - Check `.context/harness-config.yaml` to know the workspace mode (`standalone` vs `embedded`) and deliverable tier (`lean`, `standard`, `enterprise`).
   - Hydrate core knowledge from `.context/product.md`, `.context/conventions.md`, `.context/discovery.md`, `.context/strategy-and-constraints.md`, and `.context/architecture.md`.
   - In `embedded` mode, check repository package manifests and structure.

2. **Stage 2: Socratic Clarifying Gate**
   - Identify ambiguities or missing requirements in the user's prompt.
   - If critical information is absent, pause and ask 2–4 concise questions before drafting.
   - If the user instructs to proceed with assumptions, explicitly document those assumptions in the output.

3. **Stage 3: Grounded Generation**
   - Use the appropriate template from `templates/` and tier conventions from `.context/conventions.md`.
   - Reference frameworks in `frameworks/` (Wardley mapping, Theory of Constraints, OST, JTBD, RICE, WSJF, Kano).
   - Ensure user stories meet INVEST criteria and Given/When/Then Gherkin acceptance criteria.

4. **Stage 4: Knowledge Compounding (Write-Back)**
   - Offer to record new product discoveries, technical facts, and validated assumptions in `.context/*.md`.
   - Append major product decisions to `.context/decisions.md`.

## 🚫 Critical Guardrail: Zero Context Contamination

- **Internal UI vs User Product**:
  - `ui/specs/` and `ui/views/` are internal assets for the Sidekick's own web UI. **DO NOT** read them as product requirements for the user's product.
  - All user-facing PRDs, stories, and technical specs belong in `docs/`.
  - All user-facing UI wireframes and HTML mockups belong in `mockups/`.

## ⚡ Slash Commands & Skills

| Command | Purpose |
|---------|---------|
| `/create-prd` | Generate PRD (Lean, Standard, or Enterprise) |
| `/create-user-stories` | Break down features into INVEST stories + Gherkin AC |
| `/refine-user-stories` | Groom stories, SPIDR split, readiness score |
| `/create-mockup` | Interactive Tailwind HTML wireframe |
| `/create-design-brief` | UI/UX design brief with WCAG guidelines |
| `/create-documentation` | OpenAPI specs, Mermaid diagrams, user guides |
| `/brainstorm` | SCAMPER, HMW, 6 Hats feature ideation |
| `/validate-idea` | Strategyzer 4-Risk & Mom Test validation |
| `/apply-framework` | Execute framework from `frameworks/` |
| `/ingest-context` | Ingest notes/interviews into `.context/` |
| `/connect-mcp` | Configure Jira, Confluence, GitHub, Figma, Miro, Notion |
| `/sync-jira` | Export stories and epics to Jira |
| `/sync-confluence` | Publish docs to Confluence spaces |
| `/sync-github-issues` | Bi-directionally sync GitHub Issues and milestones |
| `/sync-figma` | Inspect designs and push specs to Figma |
| `/sync-miro` | Export brainstorms and roadmaps to Miro |
| `/sync-notion` | Bi-directionally sync Notion databases and wikis |
| `/gui-run` | Launch PM Command Center GUI on port 3000 |

## 📦 Architecture & Conventions

- **Python Scripts**: Standard library only (Python 3.10+). No external dependencies.
- **Manifest**: Live metadata is in `dist/harness-manifest.json`.
- **Frameworks**: Located in `frameworks/strategy/`, `frameworks/discovery/`, and `frameworks/prioritization/`.
