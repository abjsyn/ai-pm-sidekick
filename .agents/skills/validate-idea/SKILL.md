---
name: validate-idea
description: >-
  Validates product ideas, feature concepts, and business hypotheses using
  Strategyzer 4-Risk Analysis, Osterwalder's 44-Experiment Selector, The Mom Test
  customer interview framework, TAM/SAM/SOM market sizing, and Pre-mortem risk identification.
paths:
  - ".context/product.md"
  - ".context/discovery.md"
  - "frameworks/discovery/experiment-selector.md"
  - "frameworks/discovery/assumption-mapping.md"
  - "templates/validation/*.md"
requires:
  context_files:
    - ".context/product.md"
---

# 🧪 Idea & Hypothesis Validation Skill

## Overview
The `validate-idea` skill evaluates raw product ideas, market opportunities, or feature requests. It guides the Product Manager through structured hypothesis testing, identifies high-risk assumptions, matches them to optimal experiments from Bland & Osterwalder's 44-experiment catalog, calculates market opportunity, and outputs an actionable Go/Pivot/No-Go validation report grounded in `.context/`.

---

## 🎯 When to Use
Use this skill when:
- Evaluating a new product concept, startup idea, or unvetted feature request.
- Deciding whether to invest engineering effort into a proposed opportunity from `.context/discovery.md`.
- Selecting the fastest, highest-evidence validation experiment from Osterwalder's 44-experiment taxonomy (`frameworks/discovery/experiment-selector.md`).
- Preparing for executive pitch meetings or investment committee reviews.
- Identifying critical assumptions that require fast, empirical customer validation.

---

## 📋 Best Practices & Frameworks Applied
1. **Strategyzer 4-Risk Framework & Assumption Mapping (`frameworks/discovery/assumption-mapping.md`)**:
   - **Desirability Risk**: Do customers actually want this? Will they change habits?
   - **Feasibility Risk**: Can we build and scale this within our architecture?
   - **Viability Risk**: Is the unit economics / financial model sustainable?
   - **Usability Risk**: Can users intuitively navigate and adopt the solution?
2. **Osterwalder 44-Experiment Selector (`frameworks/discovery/experiment-selector.md`)**:
   - Matching Zone 1 risky assumptions to the optimal Discovery and Validation experiments across Risk Type (`D/V/F/U`), Market Fit (`B2B` vs. `B2C`), Cost/Time, and Evidence Strength (`Say` vs. `Do/Pay`).
   - Prescribing a 2-to-3 step Experiment Sequencing Chain (Discovery ➔ Behavioral Validation ➔ Viability Proof).
3. **The Mom Test (Rob Fitzpatrick)**:
   - Formulating non-leading questions focused on past behaviors rather than hypothetical opinions.
   - Filtering out compliments and false positives using `frameworks/discovery/jtbd-and-mom-test.md`.
4. **Pre-Mortem Analysis**:
   - Projecting 12 months into the future assuming project failure, identifying failure modes early.
5. **TAM / SAM / SOM Market Estimation**:
   - Structuring top-down and bottom-up market sizing.

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
Before evaluating the idea, actively ingest the workspace context:
1. **Read Core Context**:
   - Ingest `.context/harness-config.yaml` to detect operating mode (`standalone` vs `embedded`) and `default_tier`.
   - Ingest `.context/product.md` to ground the evaluation in target personas, core value loops, and North Star metrics.
   - Ingest `.context/conventions.md` to align with organizational risk thresholds and tier standards.
   - Ingest `.context/discovery.md` (Active Outcomes & past Mom Test interview logs) and `.context/strategy-and-constraints.md` (Hard business/market constraints & Wardley evolution stage).
2. **Embedded Codebase Inspection** *(if `mode: embedded`)*:
   - Read `.context/architecture.md` and inspect key repo directories to verify technical feasibility against real stack capabilities.

### Stage 2: Socratic Clarifying Gate
Evaluate whether the input idea contains critical ambiguities or missing dimensions:
1. **Gap Audit**: Check if the problem statement, primary persona, trigger situation, or existing customer workarounds are vague or unsubstantiated.
2. **Socratic Inquiry**: If critical gaps exist, **STOP** and ask the user **2 to 4 sharp, concrete clarifying questions** before generating the full document:
   - *"What specific observable past behavior or customer struggle prompted this idea?"*
   - *"What are target customers currently doing or spending (workarounds/hacks) to address this today?"*
   - *"Which dimension represents the greatest fatal risk: customer desirability or technical feasibility?"*
3. **Fast-Draft Escape Hatch**: If the user responds with *"proceed with assumptions"* (or requests an instant draft), proceed immediately to Stage 3 and explicitly document all working assumptions under a dedicated `## Documented Assumptions` section.

### Stage 3: Grounded Generation
Produce the comprehensive validation report using the tier specified in `.context/conventions.md` (`lean`, `standard`, or `enterprise`):
1. **Apply Framework Lenses**:
   - Ingest and execute `frameworks/discovery/jtbd-and-mom-test.md` to evaluate customer struggle vs compliments.
   - Score risks across Desirability, Feasibility, Viability, and Usability (1–5 scale). Flag scores $\ge 15$ as "Dealbreaker Assumptions".
2. **Formulate Experiment Blueprints via Osterwalder 44-Experiment Selector**:
   - Ingest and execute `frameworks/discovery/experiment-selector.md` to match the highest-risk assumptions against the 44-experiment catalog based on **Risk Type (`D/V/F/U`)**, **Market Fit (`B2B` vs. `B2C`)**, **Resource Budget (`Cost/Time`)**, and **Evidence Strength (`Say` vs. `Do/Pay`)**.
   - Select the **Top 2–3 Matched Experiments** and construct a **2-to-3 step Experiment Sequencing Chain** (Discovery ➔ Validation) with explicit target metrics, kill thresholds, and paired Sidekick skills. Never dump all 44 experiments into the report.
3. **Issue Strategic Signal**:
   - Conclude with a decisive **GO**, **PIVOT**, or **NO-GO** recommendation backed by evidence.
4. **Persist Artifact**:
   - Write the completed report to `docs/<feature-name>_idea_validation.md`.

### Stage 4: Knowledge Compounding (Write-Back)
Conclude the session by synthesizing newly derived truths to keep workspace memory fresh:
1. **Propose Write-Back Updates**:
   - Present a concise summary of newly validated/killed assumptions, interview insights, or pivot vectors.
2. **Prompt for Permission**:
   - *"Would you like me to record these insights in `.context/discovery.md` (Mom Test & OST) and stage a Go/Pivot decision patch in `.context/.inbox/` for `.context/decisions.md`?"*
3. **Persist on Approval**: Update the targeted `.context/` files upon user confirmation following the Context Write-Back Governance below.

## Context Write-Back Governance

- **Additive Discovery Logs:** Append new interview notes or hypothesis test results directly to `.context/discovery.md`.
- **Protected Strategy & Decision Files:** Do NOT overwrite `.context/product.md`, `.context/strategy-and-constraints.md`, or `.context/decisions.md` directly. Write proposed updates as a timestamped patch file to `.context/.inbox/YYYYMMDD-HHMM-<skill-name>.md` with frontmatter `target: .context/<filename>.md` and instruct the user to review via `/compact-context` or the UI Command Center.
- **Optional Pre-Completion Adversarial Review (`pm-critic`):** Before finalizing the validation report, you may delegate an isolated review to the read-only `pm-critic` sub-agent (`agents/pm-critic.md`) to audit the hypothesis and evidence against `.context/strategy-and-constraints.md` and `.context/discovery.md`.

---

## 🔄 Flow Handling & Suggested Next Skills
At the end of generating the validation report, ALWAYS recommend the logical next steps:
- **If GO**: "Would you like to explore alternative solution angles using `brainstorm` or draft a full PRD using `create-prd`?"
- **If PIVOT**: "Would you like to run `brainstorm` to explore alternative angles for this problem, or evaluate value chain shifts with `apply-framework` (Wardley Mapping)?"
- **If NO-GO**: "Would you like to archive this hypothesis in `.context/decisions.md` and evaluate another opportunity from `.context/discovery.md`?"
