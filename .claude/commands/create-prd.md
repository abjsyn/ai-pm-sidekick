# Command: /create-prd

>-

# 📝 Product Requirements Document (PRD) Skill

## Overview
The `create-prd` skill creates industry-standard PRDs adapted to the user's specific operational context. It translates raw ideas and requirements into clear, unambiguous product specifications that align stakeholders, designers, and engineering teams.

---

## ⚙️ Supported Operational Modes
When initiating this skill, prompt the user or detect their mode choice:
1. **⚡ Lean Mode (`lean`)**:
   - Best for startup MVPs, hackathons, or fast spikes.
   - Output: 1-page PRD focusing on problem, persona, key features, and metrics.
   - Template: `templates/prd/lean.md`
2. **🎯 Standard Agile Mode (`standard`)** *(Default)*:
   - Best for mid-size teams, growth products, and standard sprints.
   - Output: Full PRD with OKRs, End-to-End flows, Functional Reqs, Non-Functional Reqs, and Edge Cases.
   - Template: `templates/prd/standard.md`
3. **🏢 Enterprise Mode (`enterprise`)**:
   - Best for regulated industries, SOC2/GDPR compliance, enterprise software.
   - Output: Deep PRD with Security matrix, RBAC, Data Governance, SLA targets, and Sign-off section.
   - Template: `templates/prd/enterprise.md`

---

## 📋 Best Practices Applied
- **Unambiguous Functional Requirements**: Every requirement is numbered (`FR-01`, `EFR-01`) and assigned a priority (Must/Should/Could).
- **Measurable Goals**: All success metrics include baseline, target, and measurement tool.
- **Edge Case Rigor**: Explicit inclusion of error states, network disconnects, empty states, and invalid input handling.

---

## 🛠️ Step-by-Step Execution Workflow

1. **Mode Selection & Inputs**:
   - Ask user for: Feature Name, Target Mode (`lean`, `standard`, `enterprise`), Core Goal, Target Persona, Key Features.
2. **Drafting PRD**:
   - Load the corresponding template from `templates/prd/<mode>.md`.
   - Populating sections thoroughly without placeholders where user information is provided.
3. **Quality & Completeness Audit**:
   - Verify that all functional requirements have priority tags and out-of-scope boundaries are crystal clear.
4. **Final Deliverable & Flow Handling**:
   - Deliver clean Markdown PRD formatted for GitHub/Notion/Confluence.
   - Prompt the user with recommended next skills in the product pipeline.

---

## 🔄 Flow Handling & Suggested Next Skills
At the end of generating the PRD, ALWAYS recommend the logical next steps:
- **Next Step 1 (Publish to Confluence via MCP)**: "Would you like to publish this PRD to Confluence using `sync-confluence`?"
- **Next Step 2 (Backlog & Jira Sync)**: "Would you like me to break down these requirements into INVEST User Stories using `create-user-stories` or push to Jira via `sync-jira`?"
- **Next Step 3 (Design Specification & Figma)**: "Would you like to draft a UI/UX Design Brief using `create-design-brief` or sync with Figma via `sync-figma`?"
- **Next Step 4 (Interactive Prototype)**: "Would you like to build an interactive HTML wireframe mockup using `create-mockup`?"