---
name: refine-user-stories
description: >-
  Grooms and refines existing user stories. Detects ambiguity, splits large stories using the SPIDR framework, adds missing Gherkin edge cases, and calculates a Grooming Readiness Score (0-100%).
---

# 🔍 User Story Grooming & Refinement Skill

## Overview
The `refine-user-stories` skill takes existing draft user stories or backlog items and reviews them for sprint readiness. It identifies ambiguities, missing edge cases, security gaps, and story sizing risks.

---

## 🎯 Key Capabilities & Frameworks

1. **Grooming Readiness Score (0–100%)**:
   - Scores the story based on 5 parameters:
     - Clear User Value Statement (20 pts)
     - Complete Gherkin Acceptance Criteria (20 pts)
     - Edge Cases & Error Scenarios Covered (20 pts)
     - Technical Dependencies Identified (20 pts)
     - Testability & DoD Clarity (20 pts)
2. **SPIDR Story Splitting Framework**:
   - **S**pikes, **P**aths, **I**nterfaces, **D**ata, **R**ules.

---

## 🛠️ Step-by-Step Execution Workflow

1. **Audit Existing Story**:
   - Analyze input story text against INVEST criteria and Gherkin completeness.
2. **Calculate Readiness Score**:
   - Output detailed scorecard with breakdown and missing elements.
3. **Apply SPIDR Splitting (If Story Points > 8 or Score < 70%)**:
   - Provide concrete recommendations on how to split the story into 2-3 smaller tickets.
4. **Deliver Refined Version & Flow Handling**:
   - Return updated story text with strengthened Gherkin scenarios, edge cases, and technical notes.
   - Conclude with next skill suggestions.

---

## 🔄 Flow Handling & Suggested Next Skills
At the end of story grooming, ALWAYS recommend the logical next steps:
- **Next Step 1 (Documentation)**: "Now that the story is groomed, would you like to generate technical API specs & end-user guides using `create-documentation`?"
- **Next Step 2 (UI Handoff)**: "Would you like to generate a UI Design Brief for this story using `create-design-brief`?"
