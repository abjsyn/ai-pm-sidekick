---
id: rice
name: RICE Scoring Matrix
category: prioritization
problem_signatures:
  - "Backlog is prioritized by who speaks the loudest or highest-paid person's opinion (HiPPO)"
  - "Low-impact pet projects consistently displace high-reach core features"
  - "Teams lack an objective numerical basis to resolve stakeholder feature debates"
best_for_stage:
  - growth
  - scale
  - enterprise
data_maturity_required: medium
when_not_to_use:
  - "Early 0-to-1 discovery where Reach and Impact numbers are completely speculative"
  - "Hard-deadline regulatory or compliance mandates that must be built regardless of reach"
paired_skills:
  - refine-user-stories
  - create-prd
  - sync-jira
write_back_target: .context/discovery.md
---

# ⚖️ Prioritization Framework: RICE Scoring Matrix

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Developed by **Sean McBride** at **Intercom**, RICE is a four-factor quantitative scoring model designed to prioritize competing product ideas, feature requests, and engineering initiatives:

$$\mathbf{RICE\ Score} = \frac{\mathbf{Reach} \times \mathbf{Impact} \times \mathbf{Confidence}}{\mathbf{Effort}}$$

### Primary Purpose
To eliminate cognitive bias, loud-stakeholder lobbying, and "pet project" syndrome by anchoring prioritization to empirical reach, measurable business impact, defensible confidence, and engineering effort.

### Trigger Conditions
Apply this framework when:
- Evaluating candidate initiatives during quarterly roadmap planning.
- Deciding which features from the OST should be written into full PRDs in `/create-prd`.
- Prioritizing backlog epics or user stories in `/refine-user-stories`.
- Resolving conflicting opinions between sales, customer success, and engineering.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): North Star metric, target personas, and active OKRs.
- [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md): Mom Test customer interview evidence (to validate Confidence).
- [`.context/architecture.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/architecture.md): Known tech stack and integration boundaries (to ground Effort).

### Socratic Inquiry
The AI agent must challenge PM inputs using these diagnostic checks:
1. **The Reach Boundary**: *"Over what exact time window (e.g., 90-day quarter) are we measuring Reach, and does this double-count repeat user actions?"*
2. **The Impact Calibration**: *"Is this truly a Massive (3.0) impact that directly moves our North Star metric, or an incremental UX polish item (0.5)?"*
3. **The Anti-Gaming Confidence Check**: *"What verifiable evidence justifies your Confidence score? If this is based on intuition or a single executive request, it cannot exceed 20%."*
4. **The Comprehensive Effort Check**: *"Does this Effort estimate include QA testing, edge-case handling, documentation, telemetry, and migration scripts, or just raw backend coding time?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### 1. Reach (R): Number of Users / Events per Quarter
Estimated number of unique users or accounts who will directly encounter and benefit from this feature within a standard 90-day evaluation window.

### 2. Impact (I): Per-User Impact on North Star Metric
| Impact Multiplier | Level | Definition |
| :--- | :--- | :--- |
| **3.0** | Massive | Fundamentally transforms the user workflow; directly moves the primary North Star metric. |
| **2.0** | High | Significantly enhances core efficiency or resolves a severe blocker for the majority of users. |
| **1.0** | Medium | Noticeable improvement; measurable positive effect on engagement or speed. |
| **0.5** | Low | Minor improvement or convenience enhancement. |
| **0.25**| Minimal | Superficial polish or cosmetic adjustment with negligible behavioral shift. |

### 3. Confidence (C): Strict Anti-Gaming Rubric
To prevent score inflation, Confidence is capped based strictly on demonstrable evidence:

| Confidence % | Permitted Level | Mandatory Verification Criteria |
| :--- | :--- | :--- |
| **100% (1.0)** | High Confidence | Quantitative product analytics funnel data **AND** $\ge 3$ Tier 1 Mom Test interview transcripts **AND** completed technical feasibility spike. |
| **80% (0.8)** | Medium Confidence | Strong quantitative user telemetry **OR** validated qualitative user testing prototype, with zero major technical unknowns. |
| **50% (0.5)** | Low Confidence | Qualitative customer quotes only, competitor feature parity, or preliminary user survey data. |
| **$\le 20\%$ (0.2)** | Moonshot / Speculative | Gut feel, unvalidated executive requests, or hypothetical survey responses (*"I would pay for this"*). |

> [!CAUTION]
> **Anti-Gaming Rule**: Any feature assigned $\ge 80\%$ confidence MUST link to specific telemetry data or interview evidence in `.context/discovery.md`. Without citations, the score is automatically downgraded to 50% or 20%.

### 4. Effort (E): Person-Sprints or Person-Weeks
The total estimated engineering, design, and PM work in person-weeks (minimum $0.5$). Typical values follow Fibonacci: $0.5, 1, 2, 3, 5, 8$.

---

## 4. 📊 Output Format (Markdown Table)

### Canonical RICE Prioritization Table
```markdown
| Rank | Feature / Initiative | Reach (Q) | Impact | Confidence | Effort (wks) | RICE Score | Evidence Citation (Anti-Gaming) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | Automated Gherkin Generator | 1,200 | 2.0 (High) | 100% (1.0) | 2.0 | **1,200.0** | Telemetry: 75% story grooming rework + 4 Mom Test logs |
| **2** | 1-Click Jira MCP Export | 850 | 2.0 (High) | 80% (0.8) | 1.5 | **906.7** | Confluence/Jira sync survey + tested MCP protocol |
| **3** | Dark Mode Theme Palette | 2,400 | 0.25 (Min) | 80% (0.8) | 1.0 | **480.0** | Analytics: 35% user setting toggle rate |
| **4** | AI Voice Prompt Input | 400 | 1.0 (Med) | 20% (Spec) | 3.0 | **26.7** | Gut feel assumption; no user interview evidence |
```

---

## 5. ✍️ `.context/` Write-Back Target

- **Target File**: [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md)
- **Target Section**: Append as a new **Product Decision Record (PDR)** documenting the quarterly prioritization trade-offs.
- **Artifact Embedding**: Embed the completed RICE table directly into parent PRDs in [`docs/`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/docs/) under `## 3. Prioritization & Roadmap Alignment`.
