---
name: apply-framework
description: >-
  Executes modular strategic, discovery, or prioritization frameworks from frameworks/ over an idea, backlog, or PRD, and synchronizes results back to .context/.
---

# 🧠 Apply Framework Skill

## Overview
The `apply-framework` skill executes any strategic, continuous discovery, or prioritization framework defined in the `frameworks/` directory against an idea, backlog (`BACKLOG.md`), PRD (`docs/`), or architectural dilemma. It enforces structured thinking, calculates mathematical or qualitative scores, and compounds newly derived strategic insights back into the `.context/` Product Knowledge Core.

---

## 📚 Supported Framework Library

The skill dynamically orchestrates any methodology from [`frameworks/`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/frameworks/):

### 1. Strategic Frameworks ([`frameworks/strategy/`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/frameworks/strategy/))
- **`wardley-mapping`**: Plots value chain components along Visibility vs Evolution (Genesis ➔ Custom ➔ Product ➔ Commodity) and applies build-vs-buy doctrine.
- **`theory-of-constraints`**: Executes the 5 Focusing Steps to identify and exploit the single bottleneck choking sprint delivery; constructs Current Reality Trees (CRTs).

### 2. Discovery Frameworks ([`frameworks/discovery/`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/frameworks/discovery/))
- **`opportunity-solution-tree`**: Teresa Torres OST decoupling Desired Outcomes from candidate Solutions via verified Customer Opportunities and assumption tests.
- **`jtbd-and-mom-test`**: Maps Functional, Emotional, and Social jobs across the Four Forces of Progress ($\text{Push} + \text{Pull} > \text{Anxiety} + \text{Habit}$) and filters out false praise using The Mom Test.

### 3. Prioritization Frameworks ([`frameworks/prioritization/`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/frameworks/prioritization/))
- **`rice`**: Quantitative ranking ($\frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort}}$) with strict anti-gaming confidence thresholds ($100\%, 80\%, 50\%, 20\%$).
- **`wsjf-cost-of-delay`**: Weighted Shortest Job First economic scheduling ($\frac{\text{User-Business Value} + \text{Time Criticality} + \text{RR/OE}}{\text{Job Size}}$).
- **`kano-model`**: Non-linear satisfaction classification (Must-Be, Performance, Attractive, Indifferent) using functional/dysfunctional question pairs.

### 4. Operational & Delivery Frameworks ([`frameworks/operations/`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/frameworks/operations/))
- **`shape-up`**: Fixed-time, variable-scope product development (Shaped Pitches, Appetite budgeting, Breadboards, No-Gos, Hill Charts).
- **`scrum-sprint-delivery`**: Predictable sprint execution (Sprint Goal, INVEST slicing via SPIDR, Gherkin acceptance criteria, DoR gating).
- **`gist-planning`**: Iterative high-uncertainty outcome execution (Goals, Ideas backlog, lightweight Step-projects $\le 2$ weeks, Tasks).

---

## 🎯 Target Inputs
Run this skill over any of the following targets:
1. **Backlog Items**: Prioritize items in [`BACKLOG.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/BACKLOG.md) or sprint tickets using RICE or WSJF.
2. **Product Requirements**: Evaluate a PRD in [`docs/`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/docs/) using Kano feature classification or Wardley value chain mapping.
3. **Raw Concepts & Pitches**: Interrogate raw ideas with OST, The Mom Test, or Shape Up breadboards.
4. **Engineering / Process Bottlenecks**: Run Theory of Constraints over sprint velocity or grooming friction.

---

## 🛠️ Step-by-Step Execution Workflow

### 1. Framework Selection & Target Ingestion
- **No Specific Framework Named? Delegate to Dispatcher**:
  If the user describes a problem, bottleneck, or goal without specifying an exact framework name, **immediately invoke [`skills/recommend-framework/SKILL.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/skills/recommend-framework/SKILL.md)** to generate a 4-part Diagnostic Prescription.
- If a framework is specified, prompt user to confirm or select:
  > *"Running framework: `<framework-id>`. Available frameworks: `rice`, `wsjf-cost-of-delay`, `kano-model`, `opportunity-solution-tree`, `jtbd-and-mom-test`, `wardley-mapping`, `theory-of-constraints`, `shape-up`, `scrum-sprint-delivery`, `gist-planning`."*
- Ingest the target content: raw text, a file in `docs/`, `BACKLOG.md`, or user prompt.

### 2. Context Hydration
- Read the framework definition file in `frameworks/<category>/<framework>.md`.
- Ingest required `.context/` dependency files (e.g., `product.md`, `discovery.md`, `strategy-and-constraints.md`, `architecture.md`, `conventions.md`).

### 3. Socratic Interrogation Gate
- Interrogate the target using the framework's specific Socratic Questions:
  - If anti-gaming checks fail (e.g. 100% RICE confidence without quantitative data, or an OST opportunity that is actually a feature in disguise), **STOP** and challenge the PM.
  - Allow the user to adjust inputs or proceed with explicitly documented assumptions.

### 4. Methodological Execution & Output Generation
- Execute the framework's mathematical formulas, matrix cross-tabulations, or diagnostic algorithms.
- Render the deliverable using the canonical output format specified in the framework:
  - Mermaid diagrams (Wardley value chains, Current Reality Trees, OST flowcharts, Four Forces).
  - Canonical Markdown tables (RICE scoring, WSJF economic scheduling, Kano classification).

### 5. Knowledge Compounding Write-Back
- Propose syncing newly derived insights back into the designated `.context/` write-back target.
- Ask for explicit user permission:
  > *"Would you like me to update `.context/<target_file>.md` with these strategic findings?"*
- Apply changes upon confirmation.

---

## 🔄 Flow Handling & Suggested Next Skills
At the end of running a framework, ALWAYS recommend the logical next steps:
- **Next Step 1 (Incorporate into PRD)**: "Would you like to draft a PRD reflecting these prioritized features using `create-prd`?"
- **Next Step 2 (Break Down into Stories)**: "Would you like to generate user stories for the top-ranked initiatives using `create-user-stories`?"
- **Next Step 3 (Sync to Jira Backlog via MCP)**: "Would you like to export these prioritized tickets directly to Jira using `sync-jira`?"
