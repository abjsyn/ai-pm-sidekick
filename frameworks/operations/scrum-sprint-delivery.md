---
id: scrum-sprint-delivery
name: Scrum Sprint Delivery & INVEST Execution
category: operations
problem_signatures:
  - "Sprints fail repeatedly because stories are too large, ambiguous, or unestimated"
  - "Engineers build literal ticket text rather than solving the real customer need"
  - "Lack of clear Definition of Ready (DoR) causes continuous mid-sprint scope churn"
best_for_stage:
  - growth
  - scale
  - enterprise
data_maturity_required: medium
when_not_to_use:
  - "Tiny 1-2 person exploratory teams where meeting ceremonies create pure overhead"
  - "High-uncertainty innovation spikes where scope cannot be estimated into 2-week commitments"
paired_skills:
  - create-user-stories
  - refine-user-stories
  - sync-jira
  - sync-github-issues
write_back_target: .context/conventions.md
---

# 🏃 Operational Framework: Scrum Sprint Delivery & INVEST Slicing

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Based on the **Scrum Guide** (Ken Schwaber, Jeff Sutherland) and **Extreme Programming (XP)** engineering practices, Scrum Sprint Delivery structures execution into fixed 1–2 week sprints governed by:
- **Sprint Goal**: A single, unifying business outcome that anchors the sprint commitment (not just a random bag of tickets).
- **INVEST Criteria**: Ensuring user stories are Independent, Negotiable, Valuable, Estimable, Small ($\le 5$ story points), and Testable.
- **Gherkin Acceptance Criteria**: Explicit `Given/When/Then` behavioral specifications eliminating ambiguity.
- **Empirical Velocity & Capacity Slicing**: Committing only to work matching historical velocity discounted for team availability.

### Primary Purpose
To provide predictable, sustainable, cross-functional engineering throughput with continuous delivery of shippable software increments.

### Trigger Conditions
Apply this framework when:
- Operating under `operating_model: scrum` in `.context/harness-config.yaml`.
- Preparing sprint planning backlogs in `/create-user-stories` or `/sync-jira`.
- Grooming and splitting large epics into right-sized stories in `/refine-user-stories`.
- Auditing user stories against Definition of Ready (DoR) thresholds ($\ge 85\%$).

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/conventions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/conventions.md): Definition of Ready (DoR), Gherkin standard, and Definition of Done (DoD).
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Target personas, quarterly OKRs, and North Star metric.
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): Team sprint velocity, current capacity limits, and architectural bottlenecks.

### Socratic Inquiry
The AI agent must interrogate sprint backlog candidates using these diagnostic questions:
1. **The Sprint Goal Cohesion Test**: *"Do these 8 stories collectively deliver one clear user capability, or is this sprint an unconnected grab-bag of disparate tasks?"*
2. **The 5-Point Slicing Rule**: *"Is any candidate story estimated at $> 5$ Fibonacci points? If so, which SPIDR dimension (Spike, Path, Interface, Data, Rule) can split it into two independent stories?"*
3. **The Gherkin Testability Check**: *"Are all edge cases and error states written in testable Given/When/Then format, or did the PM write vague acceptance notes like 'Must be user-friendly'?"*
4. **The Capacity Reality Check**: *"Does the total committed point count exceed our trailing 3-sprint rolling average velocity after subtracting holidays, on-call duty, and PTO?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Step 1: Craft the Single Sprint Goal
Synthesize sprint objectives into a 1-sentence value proposition:
> *"Enable [Target Persona] to successfully [Action/Capability] in order to improve [Key Metric] without [Constraint/Risk]."*

### Step 2: Slice Stories via the SPIDR Protocol
Split any story exceeding 5 points along one of 5 dimensions:
1. **Spike**: Research unknown tech or third-party APIs in a timeboxed 1–2 point spike first.
2. **Path**: Split alternative user paths (Happy Path Story vs. Exception/Error Recovery Story).
3. **Interface**: Split by UI complexity (Basic web form story vs. rich drag-and-drop modal story).
4. **Data**: Split by data scope (Standard CSV data story vs. large multi-GB dataset support).
5. **Rules**: Relax business constraints initially (Strict regulatory validation story vs. standard validation).

### Step 3: Enforce Definition of Ready (DoR) Scoring
Audit each story across the 6 INVEST dimensions (0–100% score). Only stories scoring $\ge 85\%$ qualify for sprint entry.

### Step 4: Map Capacity & Forecast Commitments
Calculate sprint capacity:
$$\mathbf{Committed\ Points} \le \mathbf{Rolling\ Average\ Velocity} \times \left(1 - \frac{\mathbf{Absence\ Days}}{\mathbf{Total\ Available\ Days}}\right)$$

---

## 4. 📊 Output Format (Sprint Backlog & Story Schema)

```markdown
# 🏃 Sprint Delivery Plan: Sprint [XX]

### 🎯 Sprint Goal
> **Goal**: [1-sentence unifying user capability and business outcome]

### 📊 Capacity & Velocity Slicing
- **Rolling Velocity (Trailing 3 Sprints)**: [XX] pts
- **Adjusted Sprint Capacity**: [XX] pts
- **Committed Scope**: [XX] pts ([X] Stories)

### 📋 Committed Sprint Stories
| Story ID | Story Title | Persona | Pts | Gherkin Scenarios | DoR Score | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **US-101** | [Feature Title] | [Persona] | 3 | Happy + Boundary + Error | 95% | Ready |
| **US-102** | [Edge Flow Title] | [Persona] | 2 | Auth + Timeout | 90% | Ready |

### 🧪 Sample Gherkin Specification
```gherkin
Scenario: Successful form submission with valid inputs
  Given an authenticated user on the checkout view
  When they submit valid payment details
  Then a 200 confirmation modal is displayed
  And an order receipt is queued for email dispatch
```
```

---

## 5. ✍️ `.context/` Write-Back Target

- **Target File**: [`.context/conventions.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/conventions.md)
- **Target Section**: `## 🎯 1. Definition of Ready (DoR)` and `## 🔄 5. Operating Model Conventions`
- **Persistence Protocol**: Maintain updated sprint velocity thresholds, grooming standards, and INVEST slicing guidelines.
