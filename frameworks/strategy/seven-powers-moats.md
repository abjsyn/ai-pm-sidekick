---
id: seven-powers-moats
name: 7 Powers (Hamilton Helmer) Moat Analysis
category: strategy
problem_signatures:
  - "Features are easily copied by well-funded incumbents within weeks of launching"
  - "The product lacks durable structural defensibility or pricing power as it scales"
  - "Team confuses temporary operational excellence or speed with long-term strategic moats"
best_for_stage:
  - growth
  - scale
  - enterprise
data_maturity_required: medium
when_not_to_use:
  - "Early 0-to-1 exploratory spikes where product-market fit has not yet been demonstrated"
  - "Internal developer tooling with no commercial or competitive market dynamics"
paired_skills:
  - analyze-competitor
  - validate-idea
  - apply-framework
  - create-prd
write_back_target: .context/strategy-and-constraints.md
---

# 🏰 Strategic Framework: 7 Powers (Hamilton Helmer) Moat Analysis

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Synthesized by **Hamilton Helmer** in *7 Powers: Foundations of Business Strategy*, this framework defines Strategy as the route to creating **Power**: a set of conditions that simultaneously generates **Differential Returns** (higher profits/value than competitors) and creates a durable **Barrier** that prevents competitors from neutralizing them.

Helmer proves that there are only **Seven Powers** in business:
1. **Scale Economies**: Per-unit production cost declines as volume increases (Barrier: prohibitive capital cost for entrants).
2. **Network Economies**: Value of service increases with each additional user (Barrier: multi-homing friction, negative network effects of leaving).
3. **Counter-Positioning**: A newcomer adopts a superior business model that incumbents cannot copy without destroying their existing cash-cow business.
4. **Switching Costs**: Loss of time, money, or emotional comfort a customer incurs by migrating to an alternative (Barrier: incompatibility, workflow embedding).
5. **Branding**: An objective consumer willingness to pay a premium based on accumulated historical trust (Barrier: requires decades and massive capital).
6. **Cornered Resource**: Preferential access to a scarce asset (patent, unique talent, proprietary training data) that competitors cannot obtain.
7. **Process Power**: Embedded, highly complex organizational habits and systems developed over years that cannot be easily copied by reverse-engineering.

```
                           [ Hamilton Helmer 7 Powers ]
                                        │
         ┌──────────────────┬───────────┴───────────┬──────────────────┐
         ▼                  ▼                       ▼                  ▼
    [ Economics ]     [ Network & Data ]      [ Structural ]     [ Operational ]
    • Scale Econ      • Network Econ          • Counter-Pos      • Process Power
    • Switching Cost  • Cornered Resource     • Branding
```

### Primary Purpose
To force product managers to distinguish between temporary "features" (easily copied commodities) and structural "powers" that generate enduring enterprise value.

### Trigger Conditions
Apply this framework when:
- Conducting competitor teardowns in `/analyze-competitor`.
- Validating long-term defensibility of a new product concept in `/validate-idea`.
- Prioritizing foundational architectural investments versus superficial UI tweaks in `/create-prd`.
- Defending strategic positioning during executive reviews in `/prep-meeting`.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Target market, value propositions, and monetization models.
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): Strategic pillars, architectural boundaries, and competitive landscape.

### Socratic Inquiry
1. **The Fast-Follower Test**: *"If Microsoft, Google, or Atlassian puts 15 engineers on copying this feature next month, what structural barrier prevents them from rendering us obsolete?"*
2. **The Counter-Positioning Test**: *"Does our local, air-gapped architecture force cloud SaaS incumbents into a dilemma where copying us would cannibalize their multi-tenant cloud subscription revenues?"*
3. **The Switching Cost Reality**: *"How embedded is our `.context/` Product Knowledge Core in the team's daily git workflow? Does moving away cause immense friction or is it a trivial 1-click migration?"*
4. **The Operational Excellence Trap**: *"Are we assuming our 'fast execution speed' is a moat, forgetting that execution speed is a temporary advantage, not a durable Power?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Phase 1: Audit Across the 7 Powers
Score candidate powers on a scale from **0 (None) to 5 (Formidable Fortress)**:
1. **Scale Economies**: Does marginal cost decrease with usage?
2. **Network Economies**: Does user B benefit when user A adopts?
3. **Counter-Positioning**: Does our approach attack the incumbent's revenue model?
4. **Switching Costs**: How painful is it to export context and retrain developers?
5. **Branding**: Do users trust our specific reputation for privacy and engineering rigor?
6. **Cornered Resource**: Do we have unique proprietary algorithms or datasets?
7. **Process Power**: Is our multi-agent harness too intricate to copy quickly?

### Phase 2: Identify Active vs Candidate Powers
- **Active Powers (Score $\ge 4$)**: Defensible today; anchor all marketing and sales messaging here.
- **Nascent Powers (Score 2–3)**: Focus product roadmaps on deepening the barrier before competitors notice.
- **Illusions (Score 0–1)**: Commodities; do not over-invest.

---

## 4. 📊 Output Format

### 7 Powers Moat Evaluation Ledger

| Power Type | Score (0-5) | Status | Specific Company Capability | Competitor Barrier / Incumbent Dilemma |
| :--- | :---: | :---: | :--- | :--- |
| **Counter-Positioning** | 5 / 5 | 🟢 **Active Power** | Local repository execution with zero cloud storage of user IP | Incumbent cloud PM tools (Jira/Asana) cannot offer 100% local air-gapped execution without dismantling their multi-tenant SaaS business model. |
| **Switching Costs** | 4 / 5 | 🟢 **Active Power** | `.context/` knowledge core compounding git history and PDRs | Once a team has 6 months of architectural rules and decision records in `.context/`, switching to another tool causes massive knowledge loss. |
| **Process Power** | 3 / 5 | 🟡 Nascent | Diagnostic framework engine + INVEST linter linter architecture | Difficult to reproduce with basic system prompts; requires deep agent harness integration. |
| **Network Economies** | 2 / 5 | 🟡 Nascent | Shared team workspace presets and custom framework shares | Value currently accrues primarily to individual PMs and local pods. |
| **Scale Economies** | 1 / 5 | 🔴 Weak | Local compute utilizes user's machine | Marginal cost is zero, but scale economies do not create an entrant barrier. |
| **Cornered Resource** | 1 / 5 | 🔴 Weak | Open-source foundation | LLM models are public commodities; no proprietary closed weights. |
| **Branding** | 2 / 5 | 🟡 Nascent | "AI-SDLC Engineering Rigor" reputation | Growing developer mindshare in developer tools. |

---

## 5. ✍️ `.context/` Write-Back Target

- **Primary Target File**: [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) (under `## 🏰 7 Powers Strategic Defensibility Analysis`).
- **Write-Back Content**:
  1. Record the scores and barriers across the 7 Powers.
  2. Embed Counter-Positioning talking points into Sales Battlecards (`analyze-competitor`).
