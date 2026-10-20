---
id: pre-mortem-tigers
name: Pre-Mortem (Tigers, Paper Tigers & Elephants)
category: operations
problem_signatures:
  - "Teams experience catastrophic launch-day surprises that could easily have been anticipated"
  - "Engineering and business teams waste excessive energy debating vocal but harmless minor worries"
  - "Nobody on the team feels safe speaking up about known fatal architectural or organizational flaws"
best_for_stage:
  - 0-to-1
  - growth
  - scale
  - enterprise
data_maturity_required: low
when_not_to_use:
  - "Low-risk, reversible routine bug fixes or internal copy changes"
  - "Teams where psychological safety is so damaged that risk identification is weaponized"
paired_skills:
  - audit-spec
  - create-prd
  - plan-launch
  - prep-meeting
write_back_target: .context/decisions.md
---

# 🐅 Operational Framework: Pre-Mortem (Tigers, Paper Tigers & Elephants)

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Synthesized by **Shreyas Doshi** (former Stripe, Twitter, Google PM leader) and grounded in Gary Klein's cognitive pre-mortem technique, this framework conducts a structured failure simulation before committing to build or launch.

The core insight is that teams suffer from three distinct categories of risks, which are routinely conflated:
1. 🐅 **Tigers (Real Existential Threats)**: Probable, fatal risks that will kill the product, break customer trust, or cause catastrophic outages if unmitigated.
2. 🐯 **Paper Tigers (Harmless Noise)**: Highly visible, vocal concerns that cause endless debate and anxiety among stakeholders, but have minimal actual impact if they occur.
3. 🐘 **Elephants in the Room (Unspoken Truths)**: Known structural flaws, missing competencies, or painful organizational realities that everyone recognizes privately but avoids voicing out of political politeness or fear.

```
                           [ Launch Day Simulation: Total Failure ]
                                              │
         ┌────────────────────────────────────┼────────────────────────────────────┐
         ▼                                    ▼                                    ▼
  🐅 TIGERS (Real Threats)            🐯 PAPER TIGERS (Noise)             🐘 ELEPHANTS (Taboos)
  • Single point of failure           • Theoretical competitor tweet      • Team lacks required skill
  • Unscalable DB query               • Minor edge-case aesthetic         • Upstream team won't deliver
  • Fatal compliance tripwire         • One customer vocal complaint      • Target deadline is a fantasy
         │                                    │                                    │
  [ Mitigate with Top Priority ]      [ Dismiss / Acknowledge & Move On ]  [ Confront & Escalated Now ]
```

### Primary Purpose
To normalize the voice of dissent, prevent preventable launch disasters, clear away unproductive anxiety over minor edge cases, and confront taboo blockers while there is still time to adjust scope.

### Trigger Conditions
Apply this framework when:
- Reviewing a completed PRD or backlog before sprint kickoff in `/audit-spec`.
- Preparing a Go-To-Market rollout plan in `/plan-launch`.
- Defending a strategic roadmap or product trade-off before executives in `/prep-meeting`.
- A major cross-functional release involves multiple interdependent teams or platforms.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): Core system constraints, budget, team capacity, and external dependencies.
- [`.context/architecture.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/architecture.md): Technical architecture, database schemas, and integration boundaries.
- [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md): Past decisions, trade-offs, and historical pivots.

### Socratic Inquiry
1. **The Time-Travel Failure Test**: *"It is 6 months from today, and this feature has been completely decommissioned after being a public embarrassment. What exact technical or customer failure killed it?"*
2. **The Paper Tiger Filter**: *"If this feared event happens, will the business lose $>1\%$ of users or revenue, or will it just feel mildly uncomfortable for an afternoon?"*
3. **The Elephant Confrontation**: *"What is the single biggest fact that everyone on this team knows is broken, but nobody wants to say out loud to leadership?"*
4. **The Mitigation Accountability**: *"Who is personally responsible for taming each identified Tiger before the release candidate is cut?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Phase 1: Failure Brainstorming (The Premise)
Frame the premise unambiguously: *"Imagine we shipped on time, but the release was a complete disaster: customers are furious, systems crashed, and we missed our OKR entirely."*

### Phase 2: Triaging Risks into Three Buckets
Evaluate each stated risk against strict criteria:
- **🐅 Tigers**: High Probability $\times$ Catastrophic Severity. (e.g., *API rate limits block 90% of syncing; DB table locks during migration; customer security violation*).
- **🐯 Paper Tigers**: Low Probability or Trivial Severity. (e.g., *A customer might want a custom hex color code in v1; competitor might announce a blog post*).
- **🐘 Elephants**: High Severity + Known Reality + Low Psychological Safety. (e.g., *The designated engineer has never written Rust; the dependency team has ignored our tickets for 2 months*).

### Phase 3: Action Protocol
1. **Tigers**: Generate a mandatory engineering mitigation task or circuit-breaker before code freeze.
2. **Paper Tigers**: Explicitly log as "Accepted Risk / Out of Scope" and prohibit further meeting debate.
3. **Elephants**: Frame as an objective product risk and escalate directly to leadership in `/create-stakeholder-update` or `/prep-meeting`.

---

## 4. 📊 Output Format

### Pre-Mortem Risk Matrix

| Type | Risk Name | Root Cause & Failure Mechanism | Severity | Action & Mitigation Protocol | Owner |
| :---: | :--- | :--- | :---: | :--- | :--- |
| 🐅 **Tiger** | API Rate Expiry | Linear sync makes 1 request per ticket, hitting 1,500 req/min limit | Critical | Implement batch GraphQL endpoint + Redis rate-limiting queue | Tech Lead |
| 🐅 **Tiger** | Schema Drift | User uploads corrupt CSV crashing Python parser | High | Add Pydantic validation gate with error boundary | Lead Eng |
| 🐯 **Paper Tiger** | Single Dark Mode Dislike | A user complains about yellow accent color | Low | **Dismiss**: Default theme is accessible WCAG AA; postpone | Design |
| 🐘 **Elephant** | Unrealistic Go-Live Date | Target Nov 1 date was promised to Sales before architecture was vetted | Fatal | **Escalate**: Re-scope to Walking Skeleton or push date by 3 weeks | Head of Product |

---

## 5. ✍️ `.context/` Write-Back Target

- **Primary Target File**: [`.context/decisions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/decisions.md) (under `## 🐅 Pre-Mortem Risk Log & Mitigations`) or [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md).
- **Write-Back Content**:
  1. Record identified Tigers and their verified mitigations.
  2. Document Elephants raised and leadership escalations.
  3. Archive Paper Tigers to prevent scope creep.
