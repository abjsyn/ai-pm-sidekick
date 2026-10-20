---
id: north-star-metric-tree
name: North Star Metric & Input Metric Tree
category: strategy
problem_signatures:
  - "Team is optimizing fragmented vanity metrics that do not roll up to sustainable customer value"
  - "Different squads or engineers pull in opposing directions without a unified equation of growth"
  - "Leadership tracks lagging revenue numbers without actionable leading input metrics for product teams"
best_for_stage:
  - 0-to-1
  - growth
  - scale
  - enterprise
data_maturity_required: medium
when_not_to_use:
  - "Early customer discovery phase before any initial product value loop or prototype exists"
  - "Ad-hoc consulting or custom bespoke software projects with zero recurring usage loops"
paired_skills:
  - define-metrics-and-experiment
  - create-prd
  - create-roadmap
write_back_target: .context/product.md
---

# 🌟 Strategic Framework: North Star Metric & Input Metric Tree

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Developed and popularized by **Amplitude** (*The North Star Playbook*) and **John Cutler**, the North Star Framework aligns product teams around a single key metric that expresses the core value delivered to customers while predicting long-term, sustainable business outcomes.

Because a North Star Metric is often a lagging or high-level indicator, it must be decomposed into an **Input Metric Tree** spanning 4 complementary dimensions:
1. **Breadth**: How many active users or accounts are experiencing the core value?
2. **Depth**: How deeply or frequently are they engaged in each session?
3. **Frequency**: How regularly do users return within a standard cycle (daily/weekly/monthly)?
4. **Efficiency / Speed**: How fast and friction-free is the user journey to value?

```
                       [ Lagging Business Goal: ARR / LTV ]
                                       │
                    [ 🌟 NORTH STAR METRIC (Customer Value) ]
                                       │
         ┌───────────────────┬─────────┴─────────┬───────────────────┐
         ▼                   ▼                   ▼                   ▼
    [ 1. Breadth ]      [ 2. Depth ]      [ 3. Frequency ]    [ 4. Efficiency ]
    Active Teams        Specs Generated   Days Active/Week    Time to 1st Draft
         │                   │                   │                   │
         └─────────────┬─────┴───────────────────┴─────────────┬─────┘
                       ▼                                       ▼
             [ 🛡️ Guardrail Metric 1 ]               [ 🛡️ Guardrail Metric 2 ]
             Spec Rejection / Error Rate             Churn / Slipped Sprints
```

### Primary Purpose
To establish a clear causal equation between day-to-day feature development and overall company success, ensuring squads optimize actionable leading indicators without gaming the system.

### Trigger Conditions
Apply this framework when:
- Establishing product goals or quarterly OKRs in `/define-metrics-and-experiment`.
- Defining company context or updating [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md).
- Structuring themes for an outcome-based product roadmap in `/create-roadmap`.
- Evaluating whether a proposed feature in `/create-prd` moves an input lever or is merely cosmetic.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Product vision, value loop, target customer segments, and quarterly OKRs.
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): Strategic constraints and business model fundamentals.

### Socratic Inquiry
1. **The Customer Value Test**: *"If our North Star Metric goes up, does the customer definitively experience more value, or could this be an optical illusion caused by spammy notifications or price cuts?"*
2. **The Leading Indicator Test**: *"Does this input metric move within 2 to 7 days of an engineering release, or does it take 6 months to measure?"*
3. **The Gameability Check**: *"How could a malicious or desperate team inflate this input metric without actually helping the customer?"*
4. **The Dimension Balance**: *"Are we over-indexing on Breadth (acquisition) while our Frequency (retention) and Efficiency metrics are bleeding?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Phase 1: Define the North Star Metric (NSM)
Select a metric meeting the 3 Golden Rules:
1. **Measures Value Delivery**: Represents the "Aha!" moment realized (e.g. *Weekly Validated Stories Groomed*, not *Total Logins*).
2. **Represents Strategy**: Aligns with whether the game is Attention, Transaction, Productivity, or Network.
3. **Leading Indicator of Revenue**: Correlates directly with retention, renewal, and expansion.

### Phase 2: Construct the 4 Input Levers
Deconstruct the NSM into mutually supporting input drivers:
- **Breadth Lever**: e.g., *Number of weekly active product managers initiating $\ge 1$ skill*.
- **Depth Lever**: e.g., *Number of accepted user stories or frameworks run per active session*.
- **Frequency Lever**: e.g., *Percentage of users returning 3+ days per work week*.
- **Efficiency Lever**: e.g., *Median time from prompt submission to accepted deliverable*.

### Phase 3: Establish Guardrail & Counter-Metrics
Define 2 mandatory counter-metrics to prevent gaming or quality degradation:
- Quality Guardrail: *Rate of generated stories rejected during sprint review*.
- Trust Guardrail: *Unsubscribe or tool abandonment rate*.

---

## 4. 📊 Output Format

### North Star & Input Metric Tree Table

| Level | Dimension | Metric Name | Operational Definition | Current Baseline | Q4 Target | Paired Squad / Epic |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **🌟 NSM** | Customer Value | **Weekly Validated Deliverables (WVD)** | Unique PRDs & INVEST stories committed to Git/Jira | 420 | 1,200 | All Squads |
| **Input 1** | Breadth | Active PM Workspaces | Teams with $\ge 1$ deliverable created this week | 85 | 220 | Growth / Onboarding |
| **Input 2** | Depth | Framework Runs / Session | Median frameworks applied per feature spec | 1.2 | 2.5 | Core Intelligence |
| **Input 3** | Frequency | Multi-Day Retention (W3) | Users active $\ge 3$ days per week | 28% | 45% | Workflow & Habit |
| **Input 4** | Efficiency | Spec Generation Latency | Median seconds to full PRD draft | 45s | $< 20\text{s}$ | Platform & Infra |
| **🛡️ Guard 1** | Quality | Regeneration Rate | % of outputs immediately discarded | 18% | $< 8\%$ | Prompt Architecture |
| **🛡️ Guard 2** | Reliability | Pipeline Uptime | Error-free tool execution rate | 99.4% | $\ge 99.9\%$ | DevOps |

---

## 5. ✍️ `.context/` Write-Back Target

- **Primary Target File**: [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) (under `## 🌟 North Star Metric & Input Metric Tree`).
- **Write-Back Content**:
  1. Record the formal North Star definition and formula.
  2. Document the 4 input metrics and their target owners.
  3. Update quarterly OKR targets accordingly.
