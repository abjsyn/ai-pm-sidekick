---
id: moscow-scope-negotiation
name: MoSCoW & Buy-a-Feature Scope Negotiation
category: prioritization
problem_signatures:
  - "Stakeholders treat every feature request as an absolute P0 must-have"
  - "Release deadlines are fixed by contractual commitments but scope keeps ballooning"
  - "Scope cutting meetings devolve into political turf wars without clear budget boundaries"
best_for_stage:
  - growth
  - scale
  - enterprise
data_maturity_required: low
when_not_to_use:
  - "Early 0-to-1 exploratory spikes where user problem discovery is still fluid"
  - "Teams running small, continuous single-piece flow without batch milestone releases"
paired_skills:
  - create-prd
  - refine-user-stories
  - apply-framework
  - prep-meeting
write_back_target: .context/strategy-and-constraints.md
---

# 🎯 Prioritization Framework: MoSCoW & Buy-a-Feature Scope Negotiation

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Developed by **Dai Clegg** (DSDM / Agile Project Framework) and complemented by Luke Hohmann's *Innovation Games* ("Buy a Feature"), this framework forces brutal clarity on scope boundaries during high-stakes release negotiations.

The framework enforces four distinct, mutually exclusive buckets:
- **Must Have (M)**: Non-negotiable baseline. Without these, the product cannot launch legally, securely, or functionally. The Walking Skeleton. (Target: **$\le 60\%$ of total release effort**).
- **Should Have (S)**: High-impact features that are essential for competitive success, but have acceptable temporary workarounds if delayed. (Target: **$\sim 20\%$ of release effort**).
- **Could Have (C)**: Desirable enhancements and minor delighters implemented only if time and budget permit. Primary candidates for scope cutting. (Target: **$\sim 20\%$ of release effort**).
- **Won't Have This Time (W)**: Explicitly agreed out-of-scope items for this specific release window, preserved for future discovery.

```
       [ 100% Total Engineering Capacity / Budget ]
 ┌─────────────────────────────────────────────────────────────┐
 │  MUST HAVES (Max 60% Capacity)                              │
 │  Non-negotiable core; release fails without these           │
 ├──────────────────────────────┬──────────────────────────────┤
 │  SHOULD HAVES (~20% Capacity)│  COULD HAVES (~20% Buffer)   │
 │  Important; has workaround   │  First to cut if time slips  │
 └──────────────────────────────┴──────────────────────────────┘
                         [ WON'T HAVES ]
             Explicitly rejected / postponed to next cycle
```

### Primary Purpose
To establish enforceable release boundaries, protect developers from burnout, and prevent the "everything is high priority" trap during fixed-date enterprise deliveries.

### Trigger Conditions
Apply this framework when:
- Negotiating scope boundaries in `/create-prd` or trimming backlogs in `/refine-user-stories`.
- Managing fixed-date enterprise releases or regulatory compliance deadlines.
- Facilitating scope trade-offs in `/prep-meeting` before executive steering committees.
- Budgeting engineering capacity across competing stakeholder wishlists.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Target audience, primary value proposition, and release goals.
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): Fixed milestone dates, team capacity, and regulatory constraints.
- [`BACKLOG.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/BACKLOG.md): Candidate user stories and estimated Fibonacci story points.

### Socratic Inquiry
1. **The Cancellation Test**: *"If we ship on the promised date without this specific requirement, will we be sued, shut down by regulators, or suffer immediate mass churn?"* (If no, it is a Should Have, not a Must Have).
2. **The 60% Capacity Rule**: *"Do our Must Haves consume more than 60% of our available sprint capacity? If yes, we have zero contingency buffer for inevitable surprises."*
3. **The Workaround Challenge**: *"What manual script, spreadsheet, or support concierge process can we use for 30 days to downgrade this from Must to Should?"*
4. **The Explicit Won't Have**: *"What popular stakeholder request are we brave enough to put in the 'Won't Have' column right now to protect team focus?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Phase 1: Effort Estimation & Capacity Budgeting
1. Calculate total sprint/cycle capacity in Story Points (e.g. 100 points).
2. Cap Must Haves at a maximum of **60 points (60%)**.
3. Allocate Should Haves up to **20 points (20%)**.
4. Reserve Could Haves at **20 points (20%)** as the sacrificial buffer.

### Phase 2: MoSCoW Categorization Audit
Classify candidate requirements using strict criteria:
- **Must**: Core workflow continuity, legal/security mandates, system integrity.
- **Should**: Significant usability, core competitive hygiene; manual workaround exists.
- **Could**: Cosmetic tweaks, nice-to-have filters, convenience exports.
- **Won't**: Documented out of scope; explicitly communicated to stakeholders.

### Phase 3: The Buy-a-Feature Scope Negotiation Game
When stakeholders dispute classifications, allocate each stakeholder a fixed currency budget ($100 play money) priced according to story points. Let them pool funds to "purchase" features, exposing real value preferences.

---

## 4. 📊 Output Format

### MoSCoW Release Allocation Ledger

| Priority Category | Feature / Requirement ID | Story Points | Cumulative Points | Capacity Allocation | Contingency / Risk Plan |
| :--- | :--- | :---: | :---: | :---: | :--- |
| 🔴 **MUST HAVE** | Local CLI Engine Detection | 13 | 13 | 13% | Non-negotiable; zero-config security foundation. |
| 🔴 **MUST HAVE** | Basic INVEST Gherkin Exporter | 21 | 34 | 34% | Non-negotiable; core product value loop. |
| 🔴 **MUST HAVE** | Local Repo File System Polling | 13 | 47 | 47% | **Within 60% Cap** (Healthy contingency buffer). |
| 🟡 **SHOULD HAVE** | Linear MCP Bi-directional Sync | 13 | 60 | 60% | Important; temporary workaround is manual CSV. |
| 🟡 **SHOULD HAVE** | Slack Digest Notification | 8 | 68 | 68% | High convenience; workaround is email digest. |
| 🟢 **COULD HAVE** | Multi-theme Dark/Light Toggle | 5 | 73 | 73% | **Sacrificial Buffer**: Drop if sprint slips $> 2$ days. |
| 🟢 **COULD HAVE** | Audio Voice Note Transcription | 13 | 86 | 86% | **Sacrificial Buffer**: Postpone to next cycle. |
| ⚪ **WON'T HAVE** | Custom AI Model Fine-Tuning | — | — | 0% | **Explicitly Out of Scope** for this release window. |

---

## 5. ✍️ `.context/` Write-Back Target

- **Primary Target File**: [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) (under `## 🎯 MoSCoW Release Scope & Boundary Agreements`) and [`BACKLOG.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/BACKLOG.md).
- **Write-Back Content**:
  1. Record agreed Must/Should/Could/Won't boundaries.
  2. Document the official Won't Have backlog to prevent scope creep.
