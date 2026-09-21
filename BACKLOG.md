# 📋 AI PM Sidekick — Extended Backlog & Roadmap

This document outlines prioritized future capabilities ("Product Manager Must-Haves") planned for AI PM Sidekick.

---

## ✅ Completed Capabilities (MCP Tool Integrations)

* **`connect-mcp`**: Unified MCP connection & verification wizard for Atlassian, Figma, and Miro across AGY, Claude, and Cursor.
* **`sync-jira`**: Atlassian MCP integration to export user stories, epics, and Gherkin BDD criteria directly to Jira backlogs.
* **`sync-confluence`**: Atlassian MCP integration to publish PRDs, technical documentation, and design briefs to Confluence spaces.
* **`sync-figma`**: Figma MCP integration to inspect design component structures and attach PM criteria as comments on Figma nodes.
* **`sync-miro`**: Miro MCP integration to transform SCAMPER/HMW brainstorms into visual sticky notes on Miro whiteboards.

---

## 🎯 High Priority Backlog (Next Iteration)

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
