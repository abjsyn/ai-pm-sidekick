---
id: assumption-mapping
name: Assumption Mapping & Riskiest Assumption Test (RAT)
category: discovery
problem_signatures:
  - "Team is preparing to build a major feature based on unverified team opinions rather than customer evidence"
  - "Unclear which risk (desirability, feasibility, viability, usability) could kill the product first"
  - "Over-investing in high-fidelity prototypes when a simple landing page or customer inquiry test would suffice"
best_for_stage:
  - 0-to-1
  - growth
data_maturity_required: low
when_not_to_use:
  - "Standard maintenance tasks, refactoring, or compliance mandates with known solutions and zero user uncertainty"
  - "Optimizing high-traffic checkout funnels where quantitative multivariate A/B testing is already active"
paired_skills:
  - validate-idea
  - prepare-user-interview
  - define-metrics-and-experiment
write_back_target: .context/discovery.md
---

# 🎯 Discovery Framework: Assumption Mapping & Riskiest Assumption Test (RAT)

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Synthesized by **David Bland** and **Alexander Osterwalder** in *Testing Business Ideas*, Assumption Mapping decomposes product hypotheses across four fundamental risk lenses:
- **Desirability**: Do customers actually want this? Does it address a real, burning pain point?
- **Viability**: Can we build a sustainable business model around this? Will users pay or retain?
- **Feasibility**: Can we technically build, scale, and maintain this with our team and architecture?
- **Usability / Responsibility**: Can users figure out how to use it intuitively? Are there ethical, privacy, or regulatory tripwires?

Assumptions are then plotted on a **2x2 Matrix**: **Importance (High vs Low)** on the vertical axis and **Evidence (Unknown / Low Evidence vs Known / High Evidence)** on the horizontal axis.

```
                          ▲ High Importance
                          │
         ZONE 2: MONITOR  │  ZONE 1: EXPERIMENT FIRST (RAT)
         (Important, but  │  (Critical leap-of-faith,
         already proven)  │   untested assumptions)
    ──────────────────────┼──────────────────────▶ High Evidence
                          │
         ZONE 4: IGNORE   │  ZONE 3: SECONDARY SPIKES
         (Low value,      │  (Low impact,
         proven truth)    │   untested trivia)
                          │
```

The top-right quadrant (**High Importance + Low/No Evidence**) contains the **Riskiest Assumptions**. The team must design a **Riskiest Assumption Test (RAT)** for these before writing production code.

### Primary Purpose
To eliminate leap-of-faith failures and prevent engineering teams from spending months building products or features that nobody wants, cannot be monetized, or hit insurmountable technical roadblocks.

### Trigger Conditions
Apply this framework when:
- Evaluating raw ideas in `/validate-idea` or preparing user discovery in `/prepare-user-interview`.
- A PM or stakeholder proposes a high-effort feature requiring significant architectural investment.
- Slicing an MVP or deciding whether to build a prototype vs conduct smoke tests.
- Defining success metrics and experiment gates in `/define-metrics-and-experiment`.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Target customer segment, core value proposition, and business model assumptions.
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): Strategic boundaries, budget, and architectural constraints.
- [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md): Historical customer interview signals, unvalidated hypotheses, and competitor observations.

### Socratic Inquiry
1. **The Fatal Flaw Test**: *"If this single assumption is proven false next Tuesday, does the entire project get cancelled immediately?"* (If yes, Importance = High).
2. **The Evidence Interrogation**: *"What first-party behavioral data (not opinions or polite interview compliments) proves this assumption today?"* (If none, Evidence = Low).
3. **The Fastest Experiment Test**: *"What is the absolute cheapest, fastest test (e.g., fake door test, 5 customer interviews, paper prototype, manual concierge) we can run in under 48 hours to falsify this assumption?"*
4. **The Four-Lens Balance**: *"Have we only focused on technical feasibility while ignoring whether customers will change their existing workflow (desirability/habit)?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Phase 1: Assumption Generation Across 4 Lenses
Prompt the team to state all assumptions using the phrasing: *"We assume that [Target Persona] will [Specific Behavior / Acceptance] because [Underlying Reason]."*
- **Desirability**: Customers actively seek a solution and are dissatisfied with workarounds.
- **Viability**: Customers will pay $\$X$ or CAC will remain below $\$Y$.
- **Feasibility**: 3rd-party APIs provide required sub-second latency and data guarantees.
- **Usability**: Users can complete setup without requiring dedicated customer success onboarding.

### Phase 2: Quadrant Plotting
Score each assumption:
- **Importance (1 to 10)**: $10 = \text{Feature is dead if false}$; $1 = \text{Cosmetic preference}$.
- **Evidence (1 to 10)**: $1 = \text{Pure speculation / team opinion}$; $10 = \text{Proven by live customer usage data}$.
- Assumptions with $\text{Importance} \ge 7$ and $\text{Evidence} \le 4$ enter the **RAT Zone (Zone 1)**.

### Phase 3: Riskiest Assumption Test (RAT) Design
For every Zone 1 assumption, construct an experiment card:
1. **Hypothesis**: Specific falsifiable statement.
2. **Experiment Mechanism**: Discovery interview, clickable prototype, Concierge/Wizard-of-Oz, Fake door button, or Technical proof-of-concept.
3. **Success / Kill Metric**: Concrete quantitative threshold (e.g., *"At least 6 out of 10 interviewed prospects commit a deposit or agree to share confidential files"*).
4. **Timebox**: Maximum duration (typically 2 to 5 business days).

---

## 4. 📊 Output Format

### Assumption Mapping Ledger

| ID | Lens | Assumption Statement | Importance (1-10) | Evidence (1-10) | Quadrant Zone | RAT Experiment Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ASM-01** | Desirability | PMs will connect Jira API keys to an AI agent rather than copy-pasting | 9 | 2 | **Zone 1: RAT** | 5 Customer Mom Test Interviews |
| **ASM-02** | Feasibility | Third-party REST API allows fetching 500 tickets without rate-limiting | 8 | 3 | **Zone 1: RAT** | 1-hour Python SPIKE script |
| **ASM-03** | Viability | Teams will upgrade from Free to $49/mo for automated backlog triage | 7 | 2 | **Zone 1: RAT** | Pricing smoke-test landing page |
| **ASM-04** | Usability | Developers understand Gherkin syntax without additional onboarding docs | 5 | 8 | Zone 2: Monitor | In-app tooltip guidance |

### RAT Experiment Card Template

```markdown
#### 🧪 RAT Card: [ASM-01] Jira API Connection Friction
- **Primary Hypothesis**: At least 70% of enterprise PMs are permitted by IT security to connect read-only API tokens.
- **Test Method**: 8 target enterprise customer discovery calls with IT compliance screening questions.
- **Kill Threshold**: If $> 3$ prospects state that connecting API tokens requires a 6-month SOC2 audit, pivot immediately to manual markdown export/import mode.
- **Owner & Timeline**: PM Sidekick lead, 3-day turnaround.
```

---

## 5. ✍️ `.context/` Write-Back Target

- **Primary Target File**: [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md) (under `## 🔬 Active Hypotheses & Assumption Mapping (RAT)`).
- **Secondary Target**: [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) if critical technical or business model constraints are discovered.
