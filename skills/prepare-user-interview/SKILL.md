---
name: prepare-user-interview
description: >-
  Generates non-leading Mom Test interview guides, screener questions, and assumption probes tailored
  to a specific target persona and hypothesis before user discovery sessions.
paths:
  - ".context/product.md"
  - ".context/discovery.md"
  - "templates/validation/*.md"
requires:
  context_files:
    - ".context/product.md"
---

# 🎙️ User Interview Script & Research Guide Skill

## Overview
The `prepare-user-interview` skill prepares product managers, founders, and UX researchers for discovery calls. Grounded in Rob Fitzpatrick's *The Mom Test* and Jobs-to-be-Done (JTBD), it generates objective, non-leading interview guides, participant screener criteria, and tactical follow-up probes designed to uncover ground truth rather than polite false praise.

---

## ⚙️ Supported Research Objectives
1. **🔍 Problem Discovery (0-to-1 / Early Discovery)**:
   - Deep-dive into customer workflows, current workarounds, frustrations, and economic costs of the problem without pitching any solution.
2. **🧪 Solution & Concept Feedback (Prototype / Wireframe Testing)**:
   - Evaluates user reactions to a workflow or mockup (`create-mockup`) while actively preventing leading questions (*"Do you like this button?"*).
3. **💔 Churn & Win/Loss Interviews (Growth / Retention)**:
   - Unpacks why a prospect chose a competitor or why a paying customer cancelled.

---

## 📋 Best Practices & Standards Enforced
- **The Mom Test Rule**: Never ask *"Would you use/buy a feature that does X?"*. Only ask about past, real behaviors (*"Tell me about the last time you..."*).
- **Workaround Focus**: If the user hasn't actively tried to solve the problem with existing tools/spreadsheets, it is not a real problem.
- **Quantify Friction**: Probe for exact time spent, money lost, or emotional stress caused by the current status quo.
- **Strict Anti-Pitch Isolation**: Keep the interviewer's mouth shut 80% of the call; listen and take behavioral notes.

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
1. Ingest [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) for target personas, value proposition, and customer problem statements.
2. Ingest [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md) for existing interview notes, open customer outcomes (`OUT-XX`), and past user quotes.
3. Ingest [`frameworks/discovery/jtbd-and-mom-test.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/frameworks/discovery/jtbd-and-mom-test.md) and [`frameworks/discovery/assumption-mapping.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/frameworks/discovery/assumption-mapping.md) for behavioral question patterns and high-risk assumption targets.

### Stage 2: Socratic Clarifying Gate
Audit whether the research goals are clear:
1. **Target Persona**: Who is the specific interview candidate (e.g., Senior DevOps Engineer at a 500-person company, Solo Freelancer)?
2. **Core Hypothesis / Assumption**: What specific leap-of-faith assumption (from assumption mapping) are we testing?
3. If ambiguous, ask 2 concise questions:
   - *"What specific customer persona or role are you scheduling calls with?"*
   - *"What core assumption or unknown behavior do you most urgently need to validate or falsify?"*

### Stage 3: Grounded Generation
Draft a comprehensive, ready-to-use 30-minute interview script:

```markdown
# 🎙️ Customer Discovery Research Guide: [Feature / Topic]

## 🎯 Target Persona & Screener Criteria
- **Ideal Profile**: [Role, company size, tooling ecosystem].
- **Disqualifiers**: [Users who don't face the problem frequently, users who don't control the budget/workflow].
- **Screener Survey Question**: *"How often do you [perform task]?"* (Must be at least 2x/week).

---

## ⏱️ 30-Minute Interview Agenda & Script

### 1. Warm-Up & Context (3 mins)
- *"Thanks for taking the time. We're researching how teams handle [domain] to see where the real headaches are. I'm not here to sell you anything or demo software—just want to hear about your daily reality."*

### 2. Past Behavioral Exploration (15 mins)
- *"Tell me about the last time you had to [perform core task]?"*
- *"Walk me through step-by-step: what tool did you open first? What did you do next?"*
- *"What was the most frustrating part of that process?"*
- *"How are you solving or working around that today? How much does that workaround cost or take in hours?"*

### 3. Digging into the Pain & Economics (7 mins)
- *"Why haven't you solved this already with [common alternative/tool]?"*
- *"What happened the last time this process failed or broke?"*
- *"Who else at your company feels the impact when this goes wrong?"*

### 4. Assumption Stress-Test (3 mins)
- Probe candidate-specific risks: *"When you last evaluated tools for this, what stopped you from adopting them?"*

### 5. Wrap-Up & Referral (2 mins)
- *"What question should I have asked you today that I completely missed?"*
- *"Who else on your team or in your network struggles with this that I should speak with?"*
```

### Stage 4: Knowledge Compounding (Write-Back)
1. Save the generated guide to `docs/research/interview_guide_[topic].md`.
2. Provide a reminder on post-interview transcription:
   > *"After completing your interviews, use `ingest-context` to automatically process raw transcripts or notes and update `.context/discovery.md` with verified insights and Mom Test quotes."*

---

## 🔄 Flow Handling & Suggested Next Skills
- **Post-Interview Ingestion**: Use `ingest-context` to parse interview recordings, transcripts, or notes.
- **Run Assumption Mapping**: Use `apply-framework framework=assumption-mapping` to re-score evidence levels.
- **Synthesize Backlog**: Use `create-prd` or `validate-idea` to convert validated pains into PRD requirements.
