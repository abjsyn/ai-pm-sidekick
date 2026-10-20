---
id: opportunity-scoring
name: Opportunity Scoring (Importance vs. Satisfaction)
category: prioritization
problem_signatures:
  - "Team is over-investing in features where customer satisfaction is already high (over-served market)"
  - "Critical customer needs are severely underserved, but ignored because no vocal stakeholder advocates for them"
  - "Prioritization relies on subjective HIPPO opinions rather than quantitative customer satisfaction gaps"
best_for_stage:
  - growth
  - scale
  - enterprise
data_maturity_required: medium
when_not_to_use:
  - "Early 0-to-1 concept phase where customers have never experienced a candidate solution"
  - "Internal devops pipelines where customer satisfaction surveys cannot be administered"
paired_skills:
  - apply-framework
  - validate-idea
  - create-roadmap
  - create-prd
write_back_target: .context/discovery.md
---

# 🎯 Prioritization Framework: Opportunity Scoring (Importance vs. Satisfaction)

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Originated by **Anthony Ulwick** (Strategyn / Outcome-Driven Innovation) and popularized by **Dan Olsen** (*The Lean Product Playbook*), **Opportunity Scoring** identifies market opportunities by measuring the mathematical gap between customer **Importance** and current customer **Satisfaction**.

Customers are asked two fundamental 1-to-10 scale questions for each outcome or task:
1. **Importance ($I$)**: How important is it to you that you can successfully achieve [Outcome]? (1 = Not at all, 10 = Critically important).
2. **Satisfaction ($S$)**: How satisfied are you with how your current tools/methods achieve [Outcome]? (1 = Extremely dissatisfied, 10 = Completely satisfied).

$$\text{Opportunity Score} = \text{Importance} + \max(\text{Importance} - \text{Satisfaction}, 0)$$

```
                               ▲ High Importance
                               │
            APPROPRIATELY      │      UNDERSERVED / HIGH OPPORTUNITY
            SERVED             │      (High Importance, Low Satisfaction)
            (Maintain quality) │      🔥 PRIME PRODUCT TARGETS
      ─────────────────────────┼─────────────────────────▶ High Satisfaction
                               │
            NON-FACTOR         │      OVER-SERVED
            (Low Importance,   │      (High Satisfaction, Low Importance)
            Low Satisfaction)  │      ⚠️ DANGER: Wasteful Gold-Plating
                               │
```

### Primary Purpose
To eliminate the wasteful "feature trap" of improving capabilities that customers already find "good enough", and redirect resources toward high-importance jobs where customers remain acutely dissatisfied.

### Trigger Conditions
Apply this framework when:
- Analyzing survey results or user feedback in `/triage-feedback` or `/apply-framework`.
- Prioritizing major themes for an outcome roadmap in `/create-roadmap`.
- Validating whether a proposed PRD addresses an underserved need in `/create-prd`.
- Defending strategic focus areas against stakeholder pet features in `/prep-meeting`.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Target customer segments, core value propositions, and competitor alternatives.
- [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md): Customer interview signals, survey feedback, and active customer outcomes.

### Socratic Inquiry
1. **The Over-Serving Test**: *"Are we spending another sprint optimizing a feature where customers are already 8/10 satisfied, when our core onboarding is sitting at 3/10?"*
2. **The Table Stakes Check**: *"Is this outcome high importance (9/10) and high satisfaction (9/10)? If so, it is table stakes: maintain it, but do not market it as a differentiator."*
3. **The Gold-Plating Trap**: *"Is this feature idea in an area with low importance to users? If so, why is it on our roadmap?"*
4. **The Formula Result**: *"Does the Opportunity Score exceed 10.0 (indicating an attractive market opportunity) or 12.0+ (indicating an urgent underserved goldmine)?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Phase 1: Survey / Telemetry Ingestion
Measure median ratings (1–10) across a representative sample of target users:
- **Importance ($I$)**: Scaled from 1 to 10.
- **Satisfaction ($S$)**: Scaled from 1 to 10.

### Phase 2: Compute Opportunity Scores
Apply the Ulwick formula:
$$\text{Opportunity Score} = I + \max(I - S, 0)$$

### Phase 3: Segment into Strategic Quadrants
- **Underserved Opportunity ($\text{Score} \ge 12.0$)**: Severe customer dissatisfaction on a critical job. **Allocate 70% of feature capacity here.**
- **Appropriately Served ($I \ge 7.0, S \ge 7.0$)**: Competitive parity. Keep stable, automate, do not over-engineer.
- **Over-Served ($I < 6.0, S \ge 7.0$)**: Ripe for disruption by simpler/cheaper alternatives or candidates for scope pruning.
- **Irrelevant ($I < 5.0, S < 5.0$)**: Low importance trivia. Ignore.

---

## 4. 📊 Output Format

### Opportunity Scoring Ledger

| Rank | Customer Job / Outcome | Importance ($I$) | Satisfaction ($S$) | Opp Score ($I + \max(I-S, 0)$) | Opportunity Classification | Action Protocol |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **1** | Turn meeting notes into Jira tickets | 9.2 | 3.1 | **15.3** | 🔥 **Severely Underserved** | Prioritize in Q1 Sprint 1 |
| **2** | Detect architectural drift from PRDs | 8.8 | 4.2 | **13.4** | 🔥 **Severely Underserved** | High-priority epic |
| **3** | Dark mode theme customization | 4.1 | 7.8 | **4.1** | ⚠️ **Over-Served** | Deprioritize / Freeze |
| **4** | Export markdown to PDF | 7.2 | 7.5 | **7.2** | 🟢 **Appropriately Served** | Maintain status quo |
| **5** | Custom emoji reactions on stories | 2.5 | 3.0 | **2.5** | ⚪ **Irrelevant** | Drop completely |

```mermaid
quadrantChart
    title Dan Olsen / Ulwick Opportunity Matrix
    x-axis Low Satisfaction --> High Satisfaction
    y-axis Low Importance --> High Importance
    quadrant-1 Appropriately Served (Table Stakes)
    quadrant-2 Underserved (High Opportunity)
    quadrant-3 Irrelevant (Ignore)
    quadrant-4 Over-Served (Prune / Simplify)
    "Notes to Jira": [0.31, 0.92]
    "Detect Spec Drift": [0.42, 0.88]
    "PDF Export": [0.75, 0.72]
    "Dark Mode": [0.78, 0.41]
    "Emoji Reactions": [0.30, 0.25]
```

---

## 5. ✍️ `.context/` Write-Back Target

- **Primary Target File**: [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md) (under `## 🎯 Opportunity Scoring & Outcome Prioritization`).
- **Write-Back Content**:
  1. Record the scored list of customer outcomes.
  2. Embed top opportunities ($\text{Score} \ge 12.0$) into active discovery epics.
