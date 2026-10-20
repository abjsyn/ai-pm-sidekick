# Command: /recommend-framework

Diagnoses PM bottlenecks, uncertainty, or prioritization challenges, recommends the optimal framework & skill with a lightweight alternative and anti-pattern warning, and guides execution.

# 🧭 Framework Dispatcher & Recommendation Skill

## Overview
The `recommend-framework` skill acts as an intelligent product advisor. When a Product Manager describes a challenge, dilemma, bottleneck, or goal without knowing which methodology or skill to use, this skill analyzes the workspace context (`.context/harness-config.yaml`, `.context/product.md`) and the diagnostic frontmatter of all available frameworks in `frameworks/*/*.md` to prescribe the exact best-fit framework, a 15-minute lightweight alternative, and an explicit anti-pattern warning.

---

## ⚙️ Diagnostic Decision Engine

The dispatcher matches problem signatures against the four framework categories:

```
                          ┌─────────────────────────────┐
                          │   What is the core issue?   │
                          └──────────────┬──────────────┘
                                         │
       ┌──────────────────┬──────────────┴──────────────┬──────────────────┐
       ▼                  ▼                             ▼                  ▼
┌──────────────┐   ┌──────────────┐              ┌──────────────┐   ┌──────────────┐
│  Strategy &  │   │  Continuous  │              │ Quantitative │   │  Delivery &  │
│  Defensibility   │  Discovery   │              │ Prioritize   │   │  Operations  │
└──────┬───────┘   └──────┬───────┘              └──────┬───────┘   └──────┬───────┘
       │                  │                             │                  │
   [Wardley]          [JTBD / Mom]                   [RICE]            [Shape Up]
   Build vs Buy       Past Behavior              Reach x Impact      Fixed Appetite
       │                  │                             │                  │
    [ToC]               [OST]                        [WSJF]             [Scrum]
  Bottlenecks       Outcomes/Opps                Cost of Delay       INVEST Sprints
       │                  │                             │                  │
    [PR/FAQ]           [Assumptions]                 [Kano]             [GIST]
 Customer Vision      RAT Risk Matrix              Delighters       Step-Projects
       │                  │                             │                  │
  [North Star]         [AARRR]                       [ICE]           [Story Mapping]
  Metric Tree        Growth Loops                 Speed Heuristic    Walking Skeleton
       │                                                │                  │
 [Positioning]                                      [Opp Score]      [Pre-Mortem]
 April Dunford                                    ODI Satisfaction   Tigers & Elephants
       │                                                │                  │
  [7 Powers]                                         [MoSCoW]           [Kanban]
 Moat Defense                                      Scope Budget      Flow WIP & SLE
       │
   [Pricing]
 Van Westendorp
```

---

## 🛠️ Step-by-Step Diagnostic Protocol

### Step 1: Ingest Context & Diagnostic Metadata
1. Read [`.context/harness-config.yaml`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/harness-config.yaml) to identify `mode`, `default_tier`, `operating_model`, and `active_frameworks`.
2. Read [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) to determine current company stage (0-to-1, growth, scale, enterprise) and target outcomes.
3. Parse YAML frontmatter across all files in [`frameworks/`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/frameworks/) (`problem_signatures`, `best_for_stage`, `data_maturity_required`, `when_not_to_use`, `paired_skills`, `write_back_target`).

### Step 2: Diagnostic Clarification Gate
If the user's inquiry is ambiguous across:
- **(a) Product Stage**: Is this a brand-new hypothesis (0-to-1) or an established feature (growth/scale)?
- **(b) Available Data/Evidence**: Do you have quantitative telemetry and interview facts, or pure qualitative intuition?
- **(c) Time Horizon**: Do you need a decision for tomorrow's sprint or quarterly strategic planning?

Ask at most **1–2 targeted multiple-choice diagnostic questions** before recommending.

### Step 3: Formulate the Diagnostic Prescription
Synthesize findings into the standardized 4-part **Diagnostic Prescription**:

1. **🏆 Best-Fit Framework & Skill**:
   - Framework name and path in `frameworks/`.
   - Paired execution skill in `skills/`.
   - **Why It Fits**: Concrete rationale linking the user's specific problem signature to the framework's mathematical/qualitative model.
   - **Exact Command**: The copy-pasteable command to run (e.g., `/apply-framework framework=shape-up` or `/validate-idea`).

2. **⚡ Lightweight Alternative (15-Minute Version)**:
   - A faster, low-friction heuristic if the PM has immediate deadlines (e.g., 2x2 Value vs. Effort matrix, ICE scoring, or 5-question Mom Test quick scan).

3. **⚠️ Anti-Pattern Warning**:
   - A widely-used framework that **must be avoided** in this specific situation (referencing `when_not_to_use`).
   - Explanation of the cognitive trap, false precision, or process overhead it would cause.

4. **Interactive Action Gate**:
   End with the exact prompt:
   > *"Reply **'1'** to run the Best-Fit Framework now, or **'2'** for the Lightweight Alternative."*

---

## 📊 Sample Diagnostic Prescription Output

```markdown
### 🩺 Product Diagnostic Prescription

#### 1. 🏆 Best-Fit Recommendation: Shape Up (Pitches & Appetite Delivery)
- **Framework**: `frameworks/operations/shape-up.md`
- **Paired Skill**: `/create-prd` or `/apply-framework framework=shape-up`
- **Why It Fits**: You mentioned that your 2-week sprints keep rolling over and your developers feel constrained by premature wireframes. Shape Up solves this by fixing appetite (e.g. 6 weeks) and using breadboarding to define boundaries without dictating pixels.
- **Exact Command**: `/apply-framework framework=shape-up`

#### 2. ⚡ Lightweight Alternative: GIST Step-Project Slicing (15 mins)
- **Framework**: `frameworks/operations/gist-planning.md`
- **Alternative**: Slice the feature into a 1-week prototype step-project before doing a full 6-week shaped pitch.

#### 3. ⚠️ Anti-Pattern Warning: Do NOT use RICE Scoring here
- **Why Avoid**: RICE requires reliable Reach and Impact estimates. For this early-stage feature, assigning numerical Reach and 100% Confidence creates an illusion of mathematical certainty over pure guesswork.

---
👉 **Reply '1' to run Shape Up now, or '2' for the GIST Step-Project Alternative.**
```

---

## 🔄 Dynamic Skill Routing & Execution
When the user replies:
- **If '1'**: Immediately invoke the best-fit framework using `apply-framework` or its paired skill.
- **If '2'**: Immediately execute the lightweight alternative.