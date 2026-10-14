# Command: /brainstorm

Facilitates structured product & feature brainstorming using SCAMPER, How Might We (HMW), 6 Thinking Hats, and Value vs. Effort matrix.

# 💡 Product & Feature Brainstorming Skill

## Overview
The `brainstorm` skill helps Product Managers break through creative blocks, discover alternative solution angles, explore edge-case features, and prioritize creative ideas using battle-tested ideation frameworks grounded in `.context/`.

---

## 🎯 When to Use
Use this skill when:
- Kicking off a new product feature or product line exploration.
- Seeking innovative solutions to a persistent user pain point identified in `.context/discovery.md`.
- Addressing an operational constraint or bottleneck flagged in `.context/strategy-and-constraints.md`.
- Re-imagining a stagnant or low-adoption feature.

---

## 📋 Best Practices & Frameworks Applied
1. **SCAMPER Framework**:
   - **Substitute**: What materials, steps, protocols, or people can we substitute?
   - **Combine**: Can we merge this feature with an adjacent workflow?
   - **Adapt**: What existing pattern from another domain or tool can we adapt?
   - **Modify/Magnify**: What happens if we remove or double a core constraint?
   - **Put to another use**: How else can this data or service be utilized?
   - **Eliminate**: What is the simplest version if we strip 80% of the UI/steps?
   - **Reverse**: What if we flipped the user journey or ownership backwards?
2. **How Might We (HMW) Statements**:
   - Framing raw user friction into open-ended opportunity questions.
3. **Value vs. Effort Matrix**:
   - Categorizing ideas into Quick Wins, Major Projects, Fill-ins, and Time Sinks.
4. **Opportunity Solution Tree (OST)**:
   - Branching multiple distinct solution candidates from a shared customer opportunity (`frameworks/discovery/opportunity-solution-tree.md`).

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
Before launching the ideation session, absorb the organizational and product context:
1. **Read Core Context**:
   - Ingest `.context/harness-config.yaml` to detect operating mode and active frameworks.
   - Ingest `.context/product.md` to ground concepts in target personas, core value loops, and North Star metrics.
   - Ingest `.context/conventions.md` to respect delivery tier constraints (`lean`, `standard`, `enterprise`).
   - Ingest `.context/discovery.md` (Active Outcomes & Opportunity Solution Tree) and `.context/strategy-and-constraints.md` (Current system bottlenecks & Theory of Constraints focus).
2. **Embedded Codebase Inspection** *(if `mode: embedded`)*:
   - Read `.context/architecture.md` and scan repository modules to ensure brainstormed concepts are technically viable on the existing stack.

### Stage 2: Socratic Clarifying Gate
Evaluate whether the ideation target is well-defined:
1. **Problem Boundary Check**: Verify whether the user has specified the target persona, the specific friction point, and any hard non-negotiable constraints (budget, timeline, regulatory).
2. **Socratic Inquiry**: If the problem is overly broad or ambiguous, **STOP** and ask the user **2 to 4 sharp, concrete clarifying questions**:
   - *"Is the primary goal of this session to eliminate a friction bottleneck for existing power users, or to attract an entirely new persona?"*
   - *"Which constraints (e.g., tech stack, compliance, sprint budget) are absolute boundaries vs. open to challenge?"*
   - *"What existing solutions or competitors have attempted this, and where did they fail?"*
3. **Fast-Draft Escape Hatch**: If the user says *"proceed with assumptions"* or wants rapid divergent concepts, proceed immediately to Stage 3, explicitly listing assumed problem boundaries and persona needs under `## Working Assumptions`.

### Stage 3: Grounded Generation
Generate structured ideation concepts adhering to the workspace deliverable tier:
1. **Multi-Angle Generation**:
   - Apply SCAMPER to generate 8–12 distinct solution concepts.
   - Formulate 3–5 HMW opportunity cards tied to `.context/discovery.md`.
2. **Prioritization Mapping**:
   - Map each concept onto a 2x2 Value vs. Effort matrix (calibrated against `.context/architecture.md` complexity).
3. **Actionable Recommendations**:
   - Highlight the top 3 winning concepts with immediate low-cost prototype experiments (smoke test, clickable mockup, script).

### Stage 4: Knowledge Compounding (Write-Back)
Capture newly created strategic concepts back into the Product Knowledge Core:
1. **Propose Write-Back Updates**:
   - Formulate candidate solutions to link under the target opportunity in `.context/discovery.md` (OST section).
2. **Prompt for Permission**:
   - *"Would you like me to update `.context/discovery.md` with these candidate solutions and link them to our active Opportunity Solution Tree?"*
3. **Persist on Approval**: Append or update the context files upon confirmation.

---

## 🔄 Flow Handling & Suggested Next Skills
At the end of generating brainstorming concepts, ALWAYS recommend the logical next steps:
- **Next Step 1 (Visual Whiteboard via MCP)**: "Would you like to export these sticky notes and matrix to Miro using `sync-miro`?"
- **Next Step 2 (Product Requirements)**: "Would you like to capture the winning concept into a structured PRD using `create-prd`?"
- **Next Step 3 (Interactive Prototype)**: "Would you like to generate a clickable HTML mockup for the top idea using `create-mockup`?"