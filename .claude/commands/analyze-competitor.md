# Command: /analyze-competitor

Takes competitor URLs, release notes, or positioning dumps, compares them against .context/ product specs, and outputs a feature parity matrix, differentiation gaps, and a 1-page Sales/PM battlecard.

# ⚔️ Competitive Analysis & Battlecard Skill

## Overview
The `analyze-competitor` skill prevents teams from building in an echo chamber or panicking when competitors launch new features. It ingests competitor marketing materials, release notes, pricing pages, or raw teardowns, compares them objectively against the repository's `.context/` single source of truth, and produces a feature parity matrix, sustainable differentiation analysis, and a 1-page Sales/PM battlecard.

---

## ⚙️ Supported Analysis Modes
1. **🥊 1-Page Sales & PM Battlecard (`battlecard`)**:
   - Quick-reference sheet for Sales and PMs: competitor strengths, weaknesses, our "landmine" questions to plant with buyers, and objection responses.
2. **📊 Feature Parity & Gap Matrix (`parity-matrix`)**:
   - Side-by-side technical evaluation across core capabilities, architecture, pricing tiers, and compliance baselines.
3. **🏰 Defensibility & Moat Analysis (`defensibility`)**:
   - Evaluates whether competitor features represent defensible moats or easily copied commodities using Hamilton Helmer's 7 Powers framework (`frameworks/strategy/seven-powers-moats.md`).

---

## 📋 Best Practices & Standards Enforced
- **Objectivity over Wishful Thinking**: Acknowledge where the competitor is genuinely superior; never sugarcoat competitor strengths.
- **Rooted in Customer Value**: Avoid "check-box feature matrix" superficiality; analyze *how well* each tool actually solves the user's underlying job.
- **Landmine Questions**: Equip sales teams with questions that expose the competitor's architectural compromises without appearing hostile.
- **Continuous Grounding**: Compare against real capabilities documented in `.context/product.md` and `.context/architecture.md`.

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
1. Ingest [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) for target personas, product vision, unique differentiators, and pricing tiers.
2. Ingest [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) for strategic moats, technology constraints, and known gaps.
3. Ingest competitor data provided in the prompt (URL summary, feature dump, or text).

### Stage 2: Socratic Clarifying Gate
1. Check if competitor information was provided. If missing, prompt:
   > *"Which competitor are we analyzing? Please provide their name, website URL, or paste their recent launch notes/positioning text."*
2. Clarify primary purpose: Sales enablement battlecard vs Product roadmap gap analysis.

### Stage 3: Grounded Generation
Generate the Competitive Battlecard & Parity Deliverable:

```markdown
# ⚔️ Competitive Battlecard: [Competitor Name] vs. [Our Product]

**Last Updated**: [YYYY-MM-DD]  
**Primary Competitor Profile**: [Incumbent enterprise tool | VC-funded agile startup | Open-source project]

---

## ⚡ Quick Positioning Summary
| Dimension | [Our Product] | [Competitor Name] |
| :--- | :--- | :--- |
| **Core Value Pitch** | Air-gapped local AI PM harness grounded in code | Cloud-hosted collaborative PM web portal |
| **Target Customer** | Security-conscious PMs & technical product teams | General business PMs & marketing squads |
| **Hosting & Privacy** | 100% Local / Zero API key cloud logging | Multi-tenant public SaaS cloud |
| **Pricing Model** | Open-source core + Developer license | $25/user/month seat-based SaaS |

---

## 📊 Feature Parity & Capability Matrix

| Capability / Workflow | [Our Product] | [Competitor] | Competitive Assessment & Reality |
| :--- | :---: | :---: | :--- |
| **Local CLI Auto-Detection** | 🟢 Native | 🔴 Missing | We have total privacy; competitor requires cloud account. |
| **INVEST Gherkin Linting** | 🟢 Automated | 🟡 Basic | Our linting checks edge cases; competitor generates raw markdown. |
| **Real-time Web UI Canvas** | 🟡 Single-user | 🟢 Multiplayer | Competitor is superior for live multi-user whiteboarding. |
| **Custom Framework Engine** | 🟢 Modular (23) | 🔴 Hardcoded | We allow drop-in markdown frameworks; competitor is fixed. |

---

## 🥊 How to Win & Plant Landmines

### 🟢 When We Win
- Prospects with strict IT security, SOC2/GDPR constraints, or proprietary repos.
- Technical PMs who want specifications that match real code schemas and architecture.
- Teams tired of copy-pasting between ChatGPT tabs and Jira.

### 🔴 When They Win
- Non-technical teams who need heavy visual marketing templates and non-code Gantt charts.
- Organizations that demand a single monolithic vendor across sales, HR, and product.

### 💣 Landmine Questions to Plant with Prospects
1. *"Ask Competitor how their cloud AI model ensures your proprietary architecture specs and code aren't logged on multi-tenant servers."*
2. *"Ask them if their user story generator can parse your actual git repo and lint against Gherkin edge cases before grooming."*

---

## 🛡️ Response to Competitor's Common FUD
- **Competitor Claim**: *"A local command-line tool is too technical for non-engineer PMs."*
  - **Our Counter**: *"Our PM Command Center launches a full visual browser GUI with one command (`/gui-run`), giving you a beautiful graphical workspace with local zero-config security."*
```

### Stage 4: Knowledge Compounding (Write-Back)
1. Save the battlecard to `docs/competitive/battlecard_[competitor].md`.
2. Offer to update [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) with newly identified competitive moats or parity gaps.

---

## 🔄 Flow Handling & Suggested Next Skills
- **Update Positioning**: Refine launch messaging with `frameworks/strategy/product-positioning.md`.
- **Analyze Strategic Moats**: Evaluate defensibility with `frameworks/strategy/seven-powers-moats.md`.
- **Address Feature Gaps**: Scope competitive responses with `create-prd`.