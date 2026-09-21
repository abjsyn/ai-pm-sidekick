# Command: /create-documentation

>-

# 📚 Technical & User Documentation Skill

## Overview
The `create-documentation` skill creates clear, thorough documentation for both technical teams (engineers, architects, QA) and non-technical end users (customers, support agents, account managers).

---

## 🎯 Dual-Output Structure

1. **Technical Specifications (`tech-spec`)**:
   - **Architecture & Flow**: Mermaid.js sequence and entity relationship diagrams.
   - **API Schema**: OpenAPI 3.0 YAML/JSON specification format.
   - **Data Models**: Table schemas, data types, indexing, and primary/foreign keys.
   - **Security & Error Handling**: Authentication headers, rate limits, status code mappings.

2. **End-User / Customer Documentation (`user-guide`)**:
   - **Feature Overview**: What it does and why it helps the user.
   - **Step-by-Step Guide**: Numbered instructions with UI placeholder anchors (`[Screenshot: Dashboard Button]`).
   - **FAQs & Troubleshooting**: Solutions for common user mistakes or edge-case errors.

---

## 🛠️ Step-by-Step Execution Workflow

1. **Target Selection**:
   - Prompt user whether to generate Technical Spec, End-User Guide, or Both.
2. **Technical Spec Drafting**:
   - Write OpenAPI schemas and Mermaid diagrams for system interactions.
3. **User Guide Drafting**:
   - Write simple, friendly user instructions with step numbers and clear headings.
4. **Markdown Export & Flow Handling**:
   - Deliver documents formatted for GitBook, Readme.io, Notion, or GitHub Wiki.
   - Suggest next skills in the product release lifecycle.

---

## 🔄 Flow Handling & Suggested Next Skills
At the end of generating documentation, ALWAYS recommend the logical next steps:
- **Next Step 1 (Release Preparation)**: "Would you like to draft customer release notes and changelog announcements using `release-notes` (Backlog)?"
- **Next Step 2 (Analytics Tracking)**: "Would you like to write a telemetry & event tracking plan using `telemetry-plan` (Backlog)?"