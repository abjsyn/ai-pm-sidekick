---
name: evaluate-launch
description: >-
  Evaluates post-launch performance data against the PRD's original success metrics,
  logs whether the bet succeeded/failed/iterated, and writes lessons learned back to .context/decisions.md.
---

# 📊 Post-Launch Impact Retrospective Skill

## Overview
The `evaluate-launch` skill closes the learning loop. In typical feature-factory teams, features are shipped and instantly forgotten. This skill forces rigorous post-launch accountability: it compares observed analytics telemetry against the original success targets defined in the PRD and `define-metrics-and-experiment`, determines whether the product bet succeeded, underperformed, or failed, and documents immutable lessons learned into [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md).

---

## ⚙️ Supported Evaluation Horizons
1. **⚡ Initial 14-Day Canary / Smoke Check (`day-14`)**:
   - Evaluates initial adoption velocity, error rates, critical support tickets, and early drop-off points.
2. **📈 Full 60-Day OKR Impact Retrospective (`day-60`)**:
   - Evaluates sustained cohort retention, North Star metric lift, unit economic changes, and revenue expansion.

---

## 📋 Best Practices & Standards Enforced
- **Intellectual Honesty**: Celebrate failures that produced clear learnings; reject rationalizations or shifting goalposts after launch.
- **Traceability to Original PRD**: Benchmark strictly against the hypotheses and baseline targets established *before* development began.
- **Root Cause Attribution**: Distinguish between **Problem Failure** (customers didn't care about the problem) vs **Execution Failure** (the solution was too confusing or buggy).
- **Compounding Memory**: Every retrospective must produce at least one permanent institutional learning logged to `.context/decisions.md`.

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
1. Ingest the original PRD in `docs/prds/` or the experimentation spec created by `define-metrics-and-experiment`.
2. Ingest [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) for target OKR numbers and North Star baselines.
3. Ingest [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md) to inspect past retrospective records.
4. Ingest post-launch telemetry numbers or qualitative feedback provided by the user.

### Stage 2: Socratic Clarifying Gate
1. Inspect the reported post-launch numbers against PRD baselines.
2. If data is incomplete, ask 2 concise questions:
   - *"What were the observed values for your Primary Metric and Guardrail Metrics over the evaluation window?"*
   - *"Were there unexpected spikes in customer support tickets, rollback events, or negative qualitative feedback?"*

### Stage 3: Grounded Generation
Generate the comprehensive Post-Launch Impact Retrospective:

```markdown
# 📊 Post-Launch Impact Retrospective: [Feature Name]

**Evaluation Window**: [e.g. 30 Days Post-Launch (YYYY-MM-DD to YYYY-MM-DD)]  
**Original PRD Reference**: `docs/prds/[feature]_prd.md`  
**Product Lead**: [PM Name]

---

## 🎯 Target vs. Actual Metric Scorecard

| Metric Level | Target Metric | Pre-Launch Baseline | PRD Target Goal | Observed Actual | Variance | Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Primary Metric** | Feature Completion Rate | 34% | 55% | **61.4%** | **+6.4%** | 🟢 **Exceeded** |
| **North Star Link**| Weekly Active Creators | 1,200 | +8% (1,296) | **1,340** | **+3.4%** | 🟢 **Achieved** |
| **Efficiency** | Time-to-First-Result | 85s | $< 30\text{s}$ | **42s** | +12s | 🟡 Partial |
| **🛡️ Guardrail 1** | Server 5xx Error Rate | $< 0.1\%$ | $< 0.1\%$ | **0.04%** | -0.06% | 🟢 Healthy |
| **🛡️ Guardrail 2** | User Churn / Unsubscribes| $1.2\%$ | $\le 1.2\%$ | **1.15%** | -0.05% | 🟢 Healthy |

**Overall Bet Outcome**: 🏆 **SUCCESS (Ship & Iterate)**  
*(Alternatives: 🟢 SUCCESS \| 🟡 PARTIAL / ITERATE \| 🔴 FAILED / ROLLBACK)*

---

## 🔍 Root-Cause Analysis & Surprises

### 1. What Went Better Than Expected?
- Enterprise PMs adopted the feature within 48 hours of release without requiring sales enablement calls.
- Word-of-mouth referral on internal Slack channels drove 35% of initial feature activations.

### 2. Where Did We Miss or Underestimate?
- Time-to-First-Result fell short of the 30-second target (achieved 42s) due to cold-start model latency on Linux environments.
- 12 users reported confusion over the "Export" button placement on mobile screens.

---

## 🧠 Institutional Lessons Learned (For `.context/decisions.md`)
1. **Hypothesis Validation**: Pre-filling template forms is 2x more effective at driving completion than blank textareas.
2. **Process Learning**: Including the Staff Engineer in the Socratic Clarifying Gate (`audit-spec`) prevented a high-severity database migration failure on Day 1.

---

## 🚀 Follow-Up Action Commitments
- [ ] Log verified hypothesis to `.context/decisions.md` (PDR-XX).
- [ ] Open optimization story in `BACKLOG.md` for cold-start latency reduction (`refine-user-stories`).
- [ ] Share executive summary with leadership via `create-stakeholder-update`.
```

### Stage 4: Knowledge Compounding (Write-Back)
1. Save the retrospective document to `docs/retrospectives/retro_[feature]_[date].md`.
2. Append a new **Product Decision Record (PDR)** to [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md) recording the validated outcome and key takeaway.
3. Update [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) with newly established metric baselines.

---

## 🔄 Flow Handling & Suggested Next Skills
- **Share Learnings**: Broadcast retrospective findings with `create-stakeholder-update`.
- **Iterate Feature**: Groom follow-up optimization stories with `refine-user-stories`.
- **Update Roadmap**: Adjust future outcome bets in `create-roadmap`.
