---
name: prep-meeting
description: >-
  Prepares a 1-page briefing doc before a tough stakeholder review, board meeting, or customer call,
  pulling past decisions, anticipated objections, trade-off options, and talking points.
paths:
  - ".context/*.md"
  - "docs/**/*.md"
requires:
  context_files:
    - ".context/product.md"
    - ".context/decisions.md"
    - ".context/strategy-and-constraints.md"
---

# 🛡️ Meeting Prep & Stakeholder Defense Brief Skill

## Overview
The `prep-meeting` skill arms product managers before high-stakes meetings—executive reviews, architecture reviews, board presentations, customer negotiations, or sprint commitments. It synthesizes past decisions from `.context/decisions.md`, maps anticipated stakeholder objections, articulates ironclad trade-off rationale, and provides bulletproof talking points so the PM controls the room.

---

## ⚙️ Supported Meeting Contexts
1. **👔 Executive / Board Review (`executive`)**:
   - Focuses on ROI, OKR alignment, strategic defensibility, resource allocation, and market timing.
2. **🏗️ Engineering Architecture Review (`architecture`)**:
   - Focuses on technical debt, scalability limits, schema migrations, API contracts, and delivery feasibility.
3. **🤝 Customer / Sales Deal Review (`sales-customer`)**:
   - Focuses on enterprise contract commitments, delivery timelines, feature gating, and custom scope requests.

---

## 📋 Best Practices & Standards Enforced
- **Anticipate Tough Objections**: Proactively formulate answers to the 3 hardest, most hostile questions stakeholders could ask.
- **Rooted in Historical Decisions**: Reference specific Product Decision Records (PDRs) from `.context/decisions.md` to prevent rehashing settled debates.
- **Explicit Trade-Off Matrices**: Frame choices as clear trade-offs (*"We can ship Option A in 2 weeks, or Option B in 6 weeks; which risk do we accept?"*) rather than passive defensiveness.
- **1-Page Discipline**: Briefing document must fit on a single page for rapid pre-meeting review.

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
1. Ingest [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) for overarching North Star metrics, current OKRs, and strategic pillars.
2. Ingest [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md) to inspect past decision history, discarded alternatives, and rationale.
3. Ingest [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) for known capacity limits, bottlenecks, and compliance constraints.

### Stage 2: Socratic Clarifying Gate
1. **Stakeholder Identification**: Who is in the room? (e.g. Skeptical VP of Engineering, Cost-conscious CFO, Impatient Sales Director).
2. **Core Agenda & Friction Point**: What is the primary proposal or point of contention? (e.g. Cutting scope from Q1 release; pushing back a custom enterprise feature).
3. If not stated, ask 1–2 sharp clarifying questions to calibrate tone and arguments.

### Stage 3: Grounded Generation
Generate the 1-Page Meeting Defense Brief:

```markdown
# 🛡️ Stakeholder Defense Brief: [Meeting Title / Topic]

**Meeting Date**: [YYYY-MM-DD]  
**Key Stakeholders**: [Names / Roles]  
**Objective**: [Clear single goal, e.g. Secure approval to defer Custom Export feature to Q2]

---

## ⚡ 60-Second Opening Statement
*"Thanks everyone. Today we are aligning on our Q1 release scope. Our primary commitment is to protect our core North Star metric (Onboarding Completion) by shipping a rock-solid Walking Skeleton on Nov 15. To guarantee that date without burning out the team or shipping fragile code, we have evaluated three trade-off paths and recommend Path A."*

---

## 🥊 Anticipated Hostile Questions & Battle-Tested Answers

### 1. "Why can't we just work overtime and ship both features by Nov 15?"
- **The Core Flaw**: Mythical man-month fallacy; conflates effort with throughput.
- **The Scripted Answer**: *"We modeled this in our Pre-Mortem analysis (`pre-mortem-tigers`). Working overtime on parallel tracks increases context switching by 40% and directly threatens our P95 latency guardrail. As decided in PDR-03, we protect quality and delivery predictability over scope bloat."*

### 2. "Our enterprise prospect Acme Corp won't sign without Custom Export!"
- **The Core Flaw**: Distorting company-wide roadmap for a single uncommitted lead.
- **The Scripted Answer**: *"Acme's core security requirement is air-gapped local execution, which is fully delivered in Slice 1. We can provide a manual CSV export script on Day 1 while automated sync queues for Slice 2. Trading our primary release date for custom export puts $200k in pipeline at risk across 15 other accounts."*

---

## ⚖️ The 3 Trade-Off Options (The Decision Box)

| Option | Scope & Deliverable | Delivery Date | Risk & Strategic Cost |
| :--- | :--- | :---: | :--- |
| **Option A (Recommended)** | Walking Skeleton + Core Security | **Nov 15 (On Time)** | Deferred custom UI; manual CSV fallback. |
| **Option B** | Include Custom Export | Dec 20 (+5 weeks) | Misses holiday season; team fatigue. |
| **Option C** | Outsource to Contractors | Dec 01 (+2 weeks) | $45k unbudgeted spend; onboarding drag. |

---

## 🎯 The Ask & Closing Close
*"I need a firm decision today: do we confirm Option A to hit Nov 15, or accept Option B and push the date to Dec 20? Option A protects our OKRs."*
```

### Stage 4: Knowledge Compounding (Write-Back)
1. Save the brief to `docs/meetings/defense_brief_[meeting_name].md`.
2. Post-meeting: Offer to record outcomes and agreed trade-offs directly into [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md).

---

## 🔄 Flow Handling & Suggested Next Skills
- **Post-Meeting Decisions**: Log approvals and pivots in `.context/decisions.md`.
- **Stakeholder Update**: Send the meeting digest using `create-stakeholder-update`.
- **Adjust Scope**: Update sprint backlogs with `refine-user-stories`.
