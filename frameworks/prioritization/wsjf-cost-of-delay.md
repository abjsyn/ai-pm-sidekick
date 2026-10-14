# ⏱️ Prioritization Framework: Weighted Shortest Job First (WSJF) & Cost of Delay

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Formulated by **Donald G. Reinertsen** in *The Principles of Product Development Flow* and popularized by **SAFe**, **Weighted Shortest Job First (WSJF)** is an economic scheduling model that prioritizes jobs based on the **Cost of Delay (CoD)** divided by **Job Duration (Size)**:

$$\mathbf{WSJF} = \frac{\mathbf{Cost\ of\ Delay\ (CoD)}}{\mathbf{Job\ Size}} = \frac{\mathbf{User\text{-}Business\ Value} + \mathbf{Time\ Criticality} + \mathbf{Risk\ Reduction\ /\ Opportunity\ Enablement}}{\mathbf{Job\ Size}}$$

### Primary Purpose
To maximize economic flow by scheduling high-value, time-critical, risk-reducing features that can be delivered quickly, preventing the common failure mode of tying up engineering squads on monolithic, slow-moving projects.

### Trigger Conditions
Apply this framework when:
- Sequencing epics or high-level initiatives in quarterly roadmaps.
- Deciding between building a fast tactical feature vs. embarking on a multi-sprint architectural refactor.
- Features have hard external deadlines (e.g., regulatory compliance dates, customer renewal milestones, seasonal launch windows).
- Operating in **Standard Agile** or **Enterprise** mode in `/create-prd` or `/refine-user-stories`.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Business outcomes, North Star metric, and revenue drivers.
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): System bottlenecks, team capacity limits, and regulatory constraints.
- [`.context/conventions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/conventions.md): Definition of Ready (DoR) and story sizing scales.

### Socratic Inquiry
The AI agent must probe economic trade-offs using these questions:
1. **The Cost of Delay Test**: *"What is the financial, customer churn, or competitive penalty if this release is delayed by 30 days?"*
2. **The Time Decay Test**: *"Does the business value decay rapidly over time (high time criticality), or is the value steady regardless of when it ships?"*
3. **The Unlocking Factor**: *"Does completing this job enable multiple other teams to move faster (Opportunity Enablement) or retire a major architectural vulnerability (Risk Reduction)?"*
4. **The Job Slicing Test**: *"Can we decompose this 13-point initiative using SPIDR to isolate a 3-point core slice that captures 80% of the Cost of Delay, achieving an exponentially higher WSJF score?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

Evaluate all candidate jobs in a shared backlog using a normalized relative Fibonacci scale ($1, 2, 3, 5, 8, 13, 20$).

### Component 1: User / Business Value (UBV)
- **1–2**: Minor convenience or internal workflow polish.
- **3–5**: Noticeable customer benefit; improves retention or reduces operational overhead.
- **8–13**: Core revenue driver, primary conversion factor, or major competitive differentiator.
- **20**: Existential product capability required for market viability.

### Component 2: Time Criticality (TC)
- **1–2**: Steady value over time; zero penalty if delayed 2 quarters.
- **3–5**: Value decays moderately; competitor release expected within 6 months.
- **8–13**: High urgency; customer contract renewal contingent on delivery this quarter.
- **20**: Hard deadline (e.g. legal regulation deadline, fixed enterprise contract date) after which value drops to zero or incurs legal fines.

### Component 3: Risk Reduction / Opportunity Enablement (RR/OE)
- **1–2**: Zero architectural risk reduction; unlocks no subsequent work.
- **3–5**: Refactors localized technical debt or simplifies a single subsystem.
- **8–13**: Unlocks multiple dependent product teams or mitigates a high-probability security/compliance risk.
- **20**: Foundational architectural platform required before any other roadmap initiatives can proceed.

### Component 4: Job Size / Duration (JS)
Relative implementation effort and complexity estimated using the standard Fibonacci sequence ($1, 2, 3, 5, 8, 13, 20$).

---

## 4. 📊 Output Format (Markdown Table)

### Canonical WSJF Scoring Table
```markdown
| Priority Rank | Epic / Feature Name | User-Business Value (UBV) | Time Criticality (TC) | Risk Red / Opp Enab (RR/OE) | Cost of Delay (CoD) | Job Size (JS) | WSJF Score | Execution Order |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | SOC2 Audit Log Compliance | 8 | 20 | 13 | **41** | 3 | **13.67** | Sprint 1 (Immediate) |
| **2** | 1-Click Jira MCP Exporter | 13 | 5 | 8 | **26** | 2 | **13.00** | Sprint 1 (Fast Follow) |
| **3** | Core Database Migration | 8 | 3 | 20 | **31** | 8 | **3.88** | Sprint 2 (Planned Slice) |
| **4** | Custom Theme Builder | 3 | 1 | 1 | **5** | 5 | **1.00** | Backlog Deferred |
```

---

## 5. ✍️ `.context/` Write-Back Target

- **Target File**: [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md)
- **Target Section**: Append as a new **Product Decision Record (PDR)** documenting sprint or epic execution sequencing.
- **Roadmap Artifacts**: Embed the WSJF table directly into roadmap PRDs in [`docs/`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/docs/) under `## 2. Release Sequencing & Economic Prioritization`.
