# Command: /plan-launch

Generates a tiered launch plan (Tier 1 Major, Tier 2 Standard, Tier 3 Silent) from a PRD, including positioning messaging, internal enablement FAQs, rollout checklists, and rollback triggers.

# 🚀 Plan Go-To-Market (GTM) Launch Skill

## Overview
The `plan-launch` skill bridges the gap between engineering completion and real-world market adoption. Grounded in the active PRD in `docs/` and April Dunford's product positioning framework, it creates a tiered Go-To-Market (GTM) rollout plan tailored to the impact level of the release, complete with positioning copy, internal Sales/Support enablement FAQs, a cross-functional launch checklist, and automated rollback/kill triggers.

---

## ⚙️ Supported Launch Tiers
1. **🌟 Tier 1: Major Strategic Launch**:
   - Company-wide priority, new product category, or major monetization shift. Full external press release, dedicated landing page, webinar, sales certification, and customer success training.
2. **🎯 Tier 2: Standard Feature Launch**:
   - Significant feature addition within existing product. In-app announcement modal, customer changelog post, support knowledge base update, and social media blast.
3. **🤫 Tier 3: Silent / Technical Rollout**:
   - Backend migration, performance enhancement, or minor UI polish. Internal release notes, dark-launch feature flags, and canary telemetry monitoring with zero external marketing noise.

---

## 📋 Best Practices & Standards Enforced
- **Positioning Alignment**: Messaging must answer *"Why now?"* and *"So what?"* using April Dunford's 5 components.
- **Support & Sales Preparedness**: Mandatory internal FAQ addressing edge cases, pricing changes, and customer objections before external launch.
- **Clear Rollback Triggers**: Concrete, quantifiable thresholds (e.g. error rate $> 0.5\%$ or latency $> 500\text{ms}$) that automatically abort the launch.
- **Definition of Launch-Ready**: Pre-launch verification across analytics, docs, legal, and operational runbooks.

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
1. Ingest [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) for target audience profiles, value propositions, and brand voice.
2. Ingest [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) for positioning pillars and competitive landscape.
3. Ingest the target PRD in `docs/` to ground the launch plan in verified feature capabilities.

### Stage 2: Socratic Clarifying Gate
1. Determine the appropriate Launch Tier:
   - Ask the user: *"What tier of launch is this release?*  
     *1. 🌟 **Tier 1 (Major Strategic)** — New product/monetization, full GTM campaign*  
     *2. 🎯 **Tier 2 (Standard Agile)** — High-impact feature, in-app changelog & enablement*  
     *3. 🤫 **Tier 3 (Silent/Canary)** — Operational rollout, dark launch & monitoring*"
2. Clarify key dates and release dependencies if not specified in the PRD.

### Stage 3: Grounded Generation
Generate the comprehensive GTM Launch Plan deliverable:

```markdown
# 🚀 Go-To-Market Launch Plan: [Feature / Product Name]

### 🏷️ Launch Tier: [Tier 1 | Tier 2 | Tier 3]
- **Target Launch Date**: [YYYY-MM-DD]
- **Target Audience**: [Specific customer segment from product.md]
- **GTM Lead**: [PM / Product Marketing Lead]

---

## 1. 🧭 Positioning & Core Messaging
- **Headline (The Hook)**: [Customer-centric outcome statement].
- **The Value Proposition**: [Why this is 10x better than existing alternatives].
- **Key Customer Proof Points**:
  - [Proof Point 1: Quantitative time saved or error reduced]
  - [Proof Point 2: Security or convenience benefit]

---

## 2. 👥 Internal Enablement FAQ (Sales & Support)
- **Q: What should Sales say when a prospect asks if this costs extra?**
  - **A:** [Direct pricing and tier gating response].
- **Q: What is the most common customer question or error expected on Day 1?**
  - **A:** [Support triage guide and troubleshooting link].
- **Q: How does this compare to [Main Competitor]'s offering?**
  - **A:** [Key differentiation talking point from battlecard].

---

## 3. 🗓️ Cross-Functional Launch Checklist

### T-Minus 2 Weeks (Preparation)
- [ ] Feature passes all staging QA and end-to-end tests.
- [ ] Analytics telemetry and dashboards verified (`define-metrics-and-experiment`).
- [ ] Support team briefed and internal documentation published.

### Launch Day (Execution)
- [ ] Flip feature flag to 10% canary cohort; monitor APM error rates.
- [ ] Expand rollout to 100% after 2 hours of healthy metrics.
- [ ] Publish public release notes and in-app banner (`create-stakeholder-update`).

### T-Plus 1 Week (Retro)
- [ ] Review adoption against primary metric targets.
- [ ] Run post-launch retrospective with `evaluate-launch`.

---

## 4. 🛑 Circuit Breakers & Rollback Triggers
Immediately toggle feature flag OFF and roll back if any of the following occur:
- 🚨 Server error rate (HTTP 5xx) exceeds $0.2\%$ for more than 5 minutes.
- 🚨 P95 latency degrades by $> 250\text{ms}$.
- 🚨 More than 3 customer support tickets report data loss or permission leaks.
```

### Stage 4: Knowledge Compounding (Write-Back)
1. Save the launch plan to `docs/gtm/launch_plan_[feature].md`.
2. Offer to append launch dates, positioning copy, and rollback criteria to [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md).

---

## 🔄 Flow Handling & Suggested Next Skills
- **Release Notes**: Generate the customer announcement with `create-stakeholder-update`.
- **Pre-Mortem**: Run a pre-launch stress test with `apply-framework framework=pre-mortem-tigers`.
- **Post-Launch Retro**: Once shipped, evaluate performance with `evaluate-launch`.