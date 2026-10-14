---
id: shape-up
name: Shape Up (Basecamp Product Development)
category: operations
problem_signatures:
  - "Projects drag on indefinitely with continuous sprint rollovers and creeping scope"
  - "Engineers receive UI wireframes that are too rigid or PRDs that are too vague"
  - "Backlog grooming has degraded into an endless backlog management chore"
best_for_stage:
  - 0-to-1
  - growth
  - scale
data_maturity_required: low
when_not_to_use:
  - "Fixed-scope enterprise contractual deliverables with strict external deadlines"
  - "Pure maintenance, continuous firefighting, or infrastructure incident response teams"
paired_skills:
  - create-prd
  - create-design-brief
  - create-mockup
write_back_target: .context/conventions.md
---

# 🔨 Operational Framework: Shape Up (Shaped Pitches & Appetite Delivery)

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Developed by **Ryan Singer** and the **Basecamp (37signals)** team, **Shape Up** replaces rigid backlog estimation and unbounded sprints with a fixed-time, variable-scope product development operating system:
- **Shaping**: Work is shaped at the right level of abstraction (wireframes are too concrete; raw user stories are too abstract) before betting on it.
- **Appetite over Estimation**: Instead of asking *"How long will this take to build?"*, the team asks *"How much time do we want to spend on this problem?"* (Small Batch = 1–2 weeks, Big Batch = 6 weeks).
- **The Betting Table**: No rolling backlogs. Pitches compete cleanly at the betting table; unbet pitches are discarded rather than groomed indefinitely.
- **Circuit Breaker**: If a project does not finish within its appetite cycle, it is halted by default to prevent runaway sunk-cost traps.
- **Hill Charts**: Progress is measured not by completed task count, but by epistemic state: *Phase 1: Figuring it out (uphill)* vs. *Phase 2: Getting it done (downhill)*.

### Primary Purpose
To eliminate endless scope creep, eliminate backlog grooming debt, and empower autonomous cross-functional teams to deliver complete, polished features within bounded timeboxes.

### Trigger Conditions
Apply this framework when:
- Operating under `operating_model: shape-up` in `.context/harness-config.yaml`.
- Drafting executive pitches or scoping feature initiatives in `/create-prd`.
- Slicing UX flows into bounded appetites in `/create-design-brief` or `/create-mockup`.
- Mitigating high technical or UX uncertainty before assigning work to engineering.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Core problem statement, user personas, and strategic release goals.
- [`.context/conventions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/conventions.md): UI standards, appetite constraints, and Definition of Done.
- [`.context/harness-config.yaml`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/harness-config.yaml): Active operating model and deliverable tier.

### Socratic Inquiry
The AI agent must interrogate pitch proposals using these diagnostic tests:
1. **The Appetite Test**: *"Are we asking engineering how long this takes, or have business and product established an explicit appetite (e.g. 2 weeks vs 6 weeks)?"*
2. **The Fat Marker Test**: *"Is this solution specified with broad strokes (breadboards & fat-marker sketches) that leave UI agency to the team, or have we prematurely dictated pixel-level implementation details?"*
3. **The Rabbit Hole Audit**: *"What technical, edge-case, or third-party API rabbit holes are hidden in this pitch, and what explicit patches or trade-offs defuse them?"*
4. **The No-Gos Gate**: *"What adjacent features, customer edge cases, or bells-and-whistles are explicitly declared OUT OF BOUNDS (No-Gos) for this cycle?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Step 1: Set the Appetite
Define the maximum timebox the organization is willing to invest:
- **Small Batch**: 1–2 weeks (tactical enhancements, localized workflows, targeted UX improvements).
- **Big Batch**: 6 weeks (major net-new features, substantial architectural capabilities).

### Step 2: Breadboard the Interaction Flow
Map the system using 3 atomic components:
- **Places**: Navigable screens or dialogs (e.g., Invoicing Dashboard, Payment Modal).
- **Affordances**: Clickables, inputs, and interactive levers (e.g., "Add Line Item" button, "Tax Rate" field).
- **Connection Lines**: Navigational and state transitions linking affordances to places.

### Step 3: Identify Rabbit Holes & Explicitly Define No-Gos
- **Rabbit Holes**: Complex technical bottlenecks (e.g., legacy sync, asynchronous race conditions, localized currency conversion). For each, specify an explicit simplified mechanism.
- **No-Gos**: Clear, non-negotiable boundaries: *"We will NOT support multi-currency in this version."*

### Step 4: Map Scopes onto Hill Chart
Decompose the pitch into 3–5 cohesive, integrated **Scopes** (vertical slices of work, not horizontal layers). Track each scope along the hill:
- **Uphill (0%–50%)**: Unknowns remain; figuring out approaches, discovering edge cases.
- **Top of the Hill (50%)**: All unknowns solved; clear execution path forward.
- **Downhill (50%–100%)**: Pure execution, polishing, testing, merging.

---

## 4. 📊 Output Format (Markdown Table & Pitch Schema)

```markdown
# 🔨 Shaped Pitch: [Feature / Initiative Name]

### 1. Problem & Persona
- **Raw User Struggle**: [Exact customer frustration or workflow friction]
- **Persona**: [Target user persona from .context/product.md]

### 2. Appetite & Constraints
- **Appetite**: [Small Batch (1–2 weeks) | Big Batch (6 weeks)]
- **Circuit Breaker**: If uncompleted within appetite, project halts for review.

### 3. Breadboard Flow
[Place: Screen A]
  └── (Affordance: Action 1) ──> [Place: Modal B]
                                   └── (Affordance: Confirm) ──> [State: Updated]

### 4. Boundaries & No-Gos
- ❌ **No-Go 1**: [Explicit out-of-scope requirement]
- ❌ **No-Go 2**: [Deferred edge case]
- ⚠️ **Rabbit Hole Avoided**: [Potential technical trap and chosen simplification]

### 5. Hill Chart Scopes
| Scope Name | Description | Epistemic Status | Hill Position |
| :--- | :--- | :--- | :--- |
| **Scope 1: Core Flow** | [Basic happy path] | All unknowns resolved | Downhill (75%) |
| **Scope 2: Edge Handling** | [Validation & errors] | Figuring out edge states | Uphill (30%) |
| **Scope 3: Notifications** | [Webhook & alerts] | Scope clarified | Top of Hill (50%) |
```

---

## 5. ✍️ `.context/` Write-Back Target

- **Target File**: [`.context/conventions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/conventions.md)
- **Target Section**: `## 🔄 5. Operating Model Conventions`
- **Persistence Protocol**: Append shaped pitch conventions, active appetite constraints, and Hill Chart scope definitions to keep autonomous squads aligned.
