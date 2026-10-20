# 📋 AI PM Sidekick — Extended Backlog & Roadmap

This document outlines prioritized future capabilities ("Product Manager Must-Haves") planned for AI PM Sidekick.

---

## ✅ Completed Capabilities & Canonical Skills

### 🔌 Model Context Protocol (MCP) Integrations
* **`connect-mcp`**: Unified MCP connection & verification wizard for Atlassian, GitHub, Linear, Figma, Miro, Notion across AGY, Claude, and Cursor.
* **`sync-jira`**: Atlassian MCP integration to export user stories, epics, and Gherkin BDD criteria directly to Jira backlogs.
* **`sync-confluence`**: Atlassian MCP integration to publish PRDs, technical documentation, and design briefs to Confluence spaces.
* **`sync-github-issues`**: Bi-directional GitHub Issues, milestones, and label sync via GitHub MCP.
* **`sync-linear`**: Bi-directional Linear cycles, projects, issues, and triage queues sync via Linear MCP.
* **`sync-figma`**: Figma MCP integration to inspect design component structures and attach PM criteria as comments on Figma nodes.
* **`sync-miro`**: Miro MCP integration to transform SCAMPER/HMW brainstorms into visual sticky notes on Miro whiteboards.
* **`sync-notion`**: Notion MCP integration for product wikis, research databases, and PDR logs.

### 🚀 Core PM Workflow Skills (30 Total Skills)
* **`create-stakeholder-update`**: Synthesizes git & backlog into Executive digests, team updates, or release notes.
* **`prepare-user-interview`**: Non-leading Mom Test guides, screener questions, & assumption probes.
* **`define-metrics-and-experiment`**: Defines North Star hierarchies, event telemetry schemas, & A/B rollout gates.
* **`audit-spec`**: VP Product + Staff Eng review auditing scope creep, edge cases, & architecture.
* **`plan-launch`**: Tier 1/2/3 launch playbook with positioning copy, enablement FAQ, & kill switches.
* **`create-roadmap`**: Transforms backlog into Now/Next/Later or Quarterly OKR outcome horizons.
* **`prep-meeting`**: 1-page defense brief with decision history, hostile questions, & trade-off boxes.
* **`analyze-competitor`**: Feature parity matrix, positioning teardowns, & Sales/PM battlecards.
* **`triage-feedback`**: Clusters raw support/NPS/transcript feedback by frequency & severity.
* **`evaluate-launch`**: Evaluates telemetry against PRD targets and logs lessons to decisions.md.
* **`create-prd`**: Generates structured PRDs across Lean, Standard, and Enterprise tiers.
* **`create-user-stories`**: Breaks down features into INVEST stories + Gherkin BDD AC.
* **`refine-user-stories`**: Refines & splits stories using SPIDR with Readiness Score.
* **`create-mockup`**: Generates self-contained, interactive Tailwind HTML wireframes.
* **`create-design-brief`**: Bridges PM and UI/UX design specs with WCAG 2.1 AA accessibility.
* **`create-documentation`**: Dual tech spec & user guide generator (OpenAPI 3.0, Mermaid).
* **`validate-idea`**: Evaluates raw concepts & hypotheses (4-Risk, Mom Test, Pre-mortem).
* **`brainstorm`**: Generates innovative solution angles (SCAMPER, HMW, 6 Hats).
* **`ingest-context`**: Distills raw notes, calls, & Slack dumps into `.context/`.
* **`apply-framework`**: Runs 23 strategic, discovery, prioritization, & operational models.
* **`recommend-framework`**: Diagnoses bottlenecks & uncertainty, recommends the optimal framework & skill.
* **`gui-run`**: SaaS web studio, Product Brain manager, & REST server on `localhost:3000`.

---

## 🎯 Next Horizon / Future Capabilities

### B1. `competitor-analysis` — Competitive Teardowns & Matrix
* **Goal:** Benchmark feature sets against primary and secondary competitors.
* **Outputs:**
  * SWOT Analysis Matrix (Strengths, Weaknesses, Opportunities, Threats)
  * Feature Comparison Table (Direct competitors vs. product)
  * Market Positioning Map (2x2 Price vs. Value or Speed vs. Customization)

### B2. `prioritize-backlog` — Feature Prioritization Engine
* **Goal:** Evaluate and score competing feature requests objectively.
* **Frameworks Supported:**
  * **RICE Scoring**: Reach x Impact x Confidence / Effort
  * **Kano Model**: Must-Haves, Performance Features, Delighters
  * **Eisenhower / Value vs. Effort**: 2x2 Matrix mapping
* **Output:** Ranked feature priority queue with justification scores.

### B3. `synthesize-feedback` — Customer Interview & Feedback Synthesizer
* **Goal:** Process unstructured customer interview transcripts, Zendesk tickets, or NPS comments.
* **Outputs:**
  * Sentiment tag clusters (Positive, Pain Point, Feature Request)
  * Direct verbatim user quotes mapped to underlying product needs
  * Frequency heatmap of requested capabilities

---

## 🚀 Medium Priority Backlog

### B4. `telemetry-plan` — Analytics & Event Tracking Specification
* **Goal:** Create precise event tracking schemas before feature development starts.
* **Outputs:**
  * Product Analytics Plan (Mixpanel, PostHog, Amplitude, Segment compatible)
  * Event Naming Spec (`[object]_[action]` syntax e.g. `checkout_button_clicked`)
  * Required Event Properties & Trigger Conditions

### B5. `release-notes` — Multi-Audience Release Announcements
* **Goal:** Generate tailored release documentation from commits, PRs, or sprint items.
* **Outputs:**
  * Technical Changelog (for engineering & devops)
  * Customer Release Notes (friendly, value-oriented highlight list)
  * Marketing & Sales Enablement Annoucement Copy

### B6. `gtm-strategy` — Go-To-Market & Launch Checklist
* **Goal:** Plan product launch campaigns and cross-functional alignment.
* **Outputs:**
  * Messaging Hierarchy (Value proposition, elevator pitch, key pillars)
  * Cross-functional Launch Checklist (Product, Marketing, Sales, Support enablement)
  * Launch Timeline & Tiering (Tier 1 major launch vs Tier 3 quiet release)

---

## 🛠️ Advanced / Future Backlog

### B7. `roadmap-generator` — Outcome-Based Roadmap Visualizer
* **Goal:** Transform unstructured backlog items into visual, outcome-focused roadmaps.
* **Outputs:**
  * Now / Next / Later Roadmap format (Mermaid Gantt or visual markdown cards)
  * Objective-linked theme mapping

### B8. `bug-triage` — Bug Severity & RCA Processor
* **Goal:** Triage inbound bug reports and analyze system root causes.
* **Outputs:**
  * Bug Severity Classifier (P0 Critical, P1 High, P2 Medium, P3 Low)
  * Customer Blast Radius & Impact Estimate
  * Root Cause Analysis (RCA) draft template
