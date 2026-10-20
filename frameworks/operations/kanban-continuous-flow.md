---
id: kanban-continuous-flow
name: Continuous Kanban & Service Level Expectations (SLE)
category: operations
problem_signatures:
  - "Teams struggle with sprint batching friction and artificial 2-week boundary overhead"
  - "Work-in-progress (WIP) bloat causes lead times and cycle times to blow out unpredictably"
  - "High-priority production bugs and urgent customer requests constantly disrupt sprint commitments"
best_for_stage:
  - growth
  - scale
  - enterprise
data_maturity_required: medium
when_not_to_use:
  - "Early 0-to-1 exploratory spikes where workflows have no distinct linear stages"
  - "Contract-driven waterfall releases requiring fixed-scope, fixed-date milestone sign-offs"
paired_skills:
  - refine-user-stories
  - apply-framework
  - create-stakeholder-update
write_back_target: .context/conventions.md
---

# 📊 Operational Framework: Continuous Kanban & Service Level Expectations (SLE)

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Rooted in the Toyota Production System and formalized for knowledge work by **David J. Anderson** and **Daniel Vacanti** (*Actionable Agile Metrics for Predictability*), **Continuous Flow Kanban** treats software delivery not as batched sprints, but as a continuous pull system.

The methodology relies on three mathematical pillars governed by **Little's Law**:

$$\text{Average Cycle Time} = \frac{\text{Work in Progress (WIP)}}{\text{Average Throughput}}$$

1. **WIP Limits**: Explicit constraints on how many items can simultaneously occupy each workflow state.
2. **Service Level Expectations (SLE)**: A statistical forecast of cycle time based on historical percentiles (e.g., *"85% of standard stories are completed in $\le 6$ days"*).
3. **Classes of Service**: Explicit policies prioritizing work based on Cost of Delay:
   - **Expedite**: Urgent production outage or critical vulnerability; bypasses WIP limits; max 1 item in system.
   - **Fixed Date**: Regulatory or contractual deadline; tracked against burn-down.
   - **Standard**: Routine feature work pulled according to FIFO or opportunity rank.
   - **Intangible**: Technical debt or internal refactoring; low immediate Cost of Delay.

```
       [ Upstream Ready Buffer ]  (WIP: 5)
                  │
                  ▼
          [ In Development ]      (WIP: 3)
                  │
                  ▼
              [ In QA ]           (WIP: 2)
                  │
                  ▼
             [ Shipped ]          (Continuous Flow)
```

### Primary Purpose
To eliminate sprint-end crunch and rollover anxiety, stabilize flow predictability, shorten lead time from idea to production, and ensure operational readiness when `operating_model: kanban` is active in `.context/harness-config.yaml`.

### Trigger Conditions
Apply this framework when:
- Operating in a continuous delivery environment or configuring `operating_model: kanban`.
- Grooming stories in `/refine-user-stories` and setting Definition of Ready WIP policies.
- Lead times and cycle times are ballooning despite team working harder.
- Managing mixed workloads of feature development, maintenance, and ad-hoc client requests.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/conventions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/conventions.md): Definition of Ready, Definition of Done, and team cadence rules.
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): Team capacity limits and engineering bottleneck points.
- [`BACKLOG.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/BACKLOG.md): Current backlog items, column queues, and WIP counts.

### Socratic Inquiry
1. **The Little's Law Test**: *"If we want to cut our cycle time in half, why are we attempting to increase developer speed instead of cutting our active WIP in half?"*
2. **The Aging Item Trap**: *"Which active card has spent the most days idling in 'In Review' or 'In QA', and why has the team pulled new work instead of swarming to unblock it?"*
3. **The Stop Starting Rule**: *"Are we actively enforcing 'Stop Starting, Start Finishing' when a column hits its WIP limit?"*
4. **The Expedite Discipline**: *"Is this new bug truly an Expedite item with catastrophic Cost of Delay, or is a loud stakeholder trying to jump the standard queue?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Phase 1: Establish Workflow Columns & Strict WIP Limits
Rule of thumb: **$\text{WIP Limit per column} = \text{Number of dedicated contributors} \times 1.5$** (rounded down).
- **Ready for Dev**: Max 5 cards (prevents stale backlog buffering).
- **In Development**: Max 3 cards for a 3-engineer pod.
- **Code Review & QA**: Max 2 cards (forces engineers to review peer PRs before opening new tickets).
- **Deploy / Monitor**: Continuous.

### Phase 2: Compute Service Level Expectations (SLE)
Using historical percentile analysis:
- **50th Percentile**: Median turnaround (e.g. 3 days).
- **85th Percentile (Standard SLE)**: Target commitment to stakeholders (e.g. 6 days).
- **95th Percentile**: Outlier threshold (e.g. 11 days). Any card exceeding this is flagged as blocked.

### Phase 3: Enforce Pull Policies & Swarming
1. If "Code Review & QA" reaches its WIP limit of 2, developers **cannot** pull new cards from "Ready for Dev". They must swarm on reviewing or testing the existing items.
2. Work is pulled strictly from left to right.

---

## 4. 📊 Output Format

### Kanban Flow & Service Level Ledger

| Column / Workflow Stage | Active WIP Limit | Current Card Count | Health Status | Pull Policy / Swarming Trigger |
| :--- | :---: | :---: | :---: | :--- |
| **1. Ready for Dev (Buffer)** | 5 | 3 | 🟢 Healthy | Cards must satisfy INVEST & Gherkin DoR (`refine-user-stories`). |
| **2. In Development** | 3 | 3 | 🟢 At Limit | Pull highest opportunity score when slot opens. |
| **3. Code Review & Testing** | 2 | 2 | 🟡 Warning | **WIP Full**: Developers must swarm on PR reviews before starting new work. |
| **4. Done / Released** | $\infty$ | 18 | 🟢 Complete | Deployed continuously behind feature flags. |

### Service Level Expectations (SLE) Summary
- **Target SLE**: 85% of standard user stories ship in $\le 6$ business days from pull.
- **Blocked Flag**: Any ticket exceeding 8 days in progress triggers an automatic Socratic review.

---

## 5. ✍️ `.context/` Write-Back Target

- **Primary Target File**: [`.context/conventions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/conventions.md) (under `## 📊 Continuous Kanban Policies & WIP Limits`).
- **Write-Back Content**:
  1. Record the agreed column WIP limits and policies.
  2. Document the official 85th percentile SLE for stakeholder communication.
