---
name: refine-user-stories
description: >-
  Grooms and refines existing user stories. Detects ambiguity, splits large stories using the SPIDR framework, adds missing Gherkin edge cases, and calculates a Grooming Readiness Score (0-100%).
paths:
  - ".context/*.md"
  - "templates/prd/*.md"
  - "templates/user-stories/*.md"
  - "templates/design/*.md"
requires:
  context_files:
    - ".context/product.md"
    - ".context/discovery.md"
    - ".context/strategy-and-constraints.md"
---

# 🔍 User Story Grooming & Refinement Skill

## Overview
The `refine-user-stories` skill takes existing draft user stories or backlog tickets and audits them for sprint readiness. It eliminates ambiguity, adds missing edge cases, validates against the workspace Definition of Ready (DoR), and splits oversized stories using SPIDR.

---

## 🎯 Key Capabilities & Frameworks Applied
1. **Grooming Readiness Score (0–100%)**:
   - Evaluates each story against 5 objective parameters (20 pts each):
     - **Clear User Value Statement** (Concur format with valid persona).
     - **Complete Gherkin BDD Criteria** (Proper `Given/When/Then` syntax).
     - **Edge Cases & Error Scenarios** (Network, null states, boundaries).
     - **Technical Dependencies & NFRs** (API endpoints, latency, security).
     - **Testability & DoD Clarity** (Unambiguous pass/fail verifiability).
2. **SPIDR Story Splitting Framework**:
   - **Spikes**: Research unknown technical algorithms before committing.
   - **Paths**: Separate alternative user flows (e.g., credit card vs PayPal vs Apple Pay).
   - **Interfaces**: Split by platform/device (Desktop vs Mobile, Web vs Native).
   - **Data**: Handle simple data types first, complex binary/file uploads in a second story.
   - **Rules**: Relax complex business constraints for v1; enforce full rule matrix in v2.
3. **Theory of Constraints (ToC) Alignment**:
   - Directly addresses the system bottleneck in `.context/strategy-and-constraints.md` by preventing defective, ungroomed stories from starving engineering.

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
Before auditing tickets, ground the agent in organizational standards:
1. **Read Core Context**:
   - Ingest `.context/conventions.md` to load the exact Definition of Ready (DoR) checklist, Gherkin syntax requirements, and tier rules (`lean`, `standard`, `enterprise`).
   - Ingest `.context/architecture.md` to verify whether referenced components, APIs, and data models exist.
   - Ingest `.context/strategy-and-constraints.md` (Theory of Constraints section) to align with current sprint bottleneck policies.
2. **Embedded Codebase Inspection** *(if `mode: embedded`)*:
   - Verify file and service references directly against the codebase.

### Stage 2: Socratic Clarifying Gate
Evaluate whether the draft story contains unresolvable architectural ambiguities or missing business rules:
1. **Ambiguity Audit**: Identify missing validation rules, ambiguous terms (*"system should be fast"*), or unhandled negative paths.
2. **Socratic Inquiry**: If critical inputs are missing, **STOP** and ask the user **2 to 4 sharp, concrete clarifying questions**:
   - *"The story estimates 13 story points—should we split it using SPIDR by alternative payment Paths or by Data complexity?"*
   - *"What should happen when an external API service returns an HTTP 504 gateway timeout?"*
   - *"Are there concurrent session rules if a user logs in from multiple devices simultaneously?"*
3. **Fast-Draft Escape Hatch**: If the user replies *"proceed with assumptions"* (or requests an instant grooming pass), proceed directly to Stage 3, applying industry-standard defaults and explicitly highlighting all assumptions in a dedicated callout block.

### Stage 3: Grounded Generation
Refine the user stories according to the workspace deliverable tier:
1. **Calculate Grooming Readiness Score**:
   - Output an itemized scorecard (0–100%) highlighting missing criteria.
2. **Apply SPIDR Splitting**:
   - If story points $> 8$ or score $< 70\%$, provide concrete split recommendations decomposing the item into $\le 5$-point tickets.
3. **Deliver Strengthened Gherkin Scenarios**:
   - Provide complete, drop-in replacement Markdown text with expanded happy path, negative path, and boundary conditions.
4. **Persist Artifact**:
   - Save or update the deliverable in `docs/<feature-name>_groomed_stories.md`.

### Stage 4: Knowledge Compounding (Write-Back)
Capture newly refined acceptance rules and DoR scores back into `.context/`:
1. **Propose Write-Back Updates**:
   - Summarize recurring edge-case patterns or architectural assumptions that should be permanently codified in `.context/conventions.md`.
2. **Prompt for Permission**:
   - *"Would you like me to update `.context/conventions.md` with these newly codified edge-case conventions and log this refinement in `.context/decisions.md`?"*
3. **Persist on Approval**: Update the targeted `.context/` files upon user confirmation.

---

## 🔄 Flow Handling & Suggested Next Skills
At the end of story grooming, ALWAYS recommend the logical next steps:
- **Next Step 1 (Sync to Jira Backlog via MCP)**: "Would you like to push these groomed stories directly to Jira Cloud using `sync-jira`?"
- **Next Step 2 (Technical Documentation)**: "Now that the story is groomed, would you like to generate technical API specs & sequence diagrams using `create-documentation`?"
- **Next Step 3 (UI Design Handoff)**: "Would you like to generate a UI Design Brief for this story using `create-design-brief`?"
