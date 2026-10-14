---
name: create-documentation
description: >-
  Generates dual-purpose technical and end-user documentation. Produces API schemas (OpenAPI format), Mermaid sequence diagrams, architecture specs, and step-by-step end-user manuals.
---

# 📚 Technical & User Documentation Skill

## Overview
The `create-documentation` skill creates clear, thorough documentation for both technical teams (engineers, architects, QA) and non-technical end users (customers, support teams, product operations), fully grounded in `.context/`.

---

## 🎯 Dual-Output Structure
1. **Technical Specifications (`tech-spec`)**:
   - **Architecture & Flow**: Mermaid.js sequence and entity relationship diagrams.
   - **API Schemas**: OpenAPI 3.0 YAML/JSON specification format.
   - **Data Models**: Table schemas, field types, constraints, and primary/foreign keys.
   - **Security & Error Handling**: Authentication headers, rate limits, status code mappings.
2. **End-User / Customer Documentation (`user-guide`)**:
   - **Feature Overview**: Business value proposition and user benefit.
   - **Step-by-Step Guide**: Numbered instructions with visual anchor callouts (`[Screenshot: Action Area]`).
   - **FAQs & Troubleshooting**: Practical solutions for common user mistakes and edge-case errors.

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
Before drafting documentation, absorb system architecture and product context:
1. **Read Core Context**:
   - Ingest `.context/architecture.md` to identify known tech stack, database models, and existing API interfaces.
   - Ingest `.context/product.md` for target personas and user workflows.
   - Ingest `.context/conventions.md` to align with organizational documentation standards.
2. **Read Source Specs**:
   - Ingest corresponding PRDs or User Stories from `docs/` to extract functional workflows.
3. **Embedded Codebase Inspection** *(if `mode: embedded`)*:
   - Inspect controller routes, ORM schemas, and API handlers in the repository to guarantee 100% technical accuracy.

### Stage 2: Socratic Clarifying Gate
Evaluate whether documentation targets and technical details are complete:
1. **Scope Audit**: Determine whether the output should be a Technical Spec, an End-User Manual, or both. Check if API payload formats, auth scopes, or user onboarding steps are missing.
2. **Socratic Inquiry**: If critical inputs are missing, **STOP** and ask the user **2 to 4 sharp, concrete clarifying questions**:
   - *"Is this documentation primarily intended for internal engineers (API spec / Mermaid diagrams) or customer-facing operations (user manual / troubleshooting guide)?"*
   - *"What authentication mechanism (e.g., Bearer JWT, API key header) and error codes (400, 401, 404, 500) should be documented for this API?"*
   - *"What are the top 2 failure scenarios or edge cases users are likely to encounter?"*
3. **Fast-Draft Escape Hatch**: If the user replies *"proceed with assumptions"* (or requests an instant guide), proceed directly to Stage 3, applying standard RESTful/OpenAPI conventions and standard user guide structures.

### Stage 3: Grounded Generation
Generate the complete documentation deliverable:
1. **Draft Technical Specification**:
   - Render Mermaid sequence diagrams illustrating client-server interaction.
   - Write standard OpenAPI 3.0 YAML endpoint schemas with sample request/response payloads.
2. **Draft End-User Manual**:
   - Write clear, jargon-free step-by-step instructions with numbered headings and visual placeholder anchors.
   - Provide a structured FAQ & Troubleshooting table.
3. **Persist Deliverable**:
   - Save the documentation to `docs/<feature-name>_documentation.md`.

### Stage 4: Knowledge Compounding (Write-Back)
Capture newly documented technical interfaces and system models back into `.context/`:
1. **Propose Write-Back Updates**:
   - Summarize newly documented REST endpoints, data entity schemas, or security boundaries.
2. **Prompt for Permission**:
   - *"Would you like me to update `.context/architecture.md` with these newly documented API endpoints and schemas, and log a release record in `.context/decisions.md`?"*
3. **Persist on Approval**: Update the targeted `.context/` files upon user confirmation.

---

## 🔄 Flow Handling & Suggested Next Skills
At the end of generating documentation, ALWAYS recommend the logical next steps:
- **Next Step 1 (Publish to Confluence via MCP)**: "Would you like to publish this documentation directly to a Confluence space using `sync-confluence`?"
- **Next Step 2 (Release Planning)**: "Would you like to draft customer release notes and changelog announcements based on this guide?"
