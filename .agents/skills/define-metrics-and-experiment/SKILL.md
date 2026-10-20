---
name: define-metrics-and-experiment
description: >-
  Defines feature success metrics (North Star, Primary, Guardrail), event tracking taxonomy
  (events + properties), and A/B test or rollout hypotheses before engineering begins building.
---

# 📈 Define Metrics & Experiment Plan Skill

## Overview
The `define-metrics-and-experiment` skill ensures that no feature is shipped without a measurable definition of success and a concrete instrumentation spec. It establishes the metric hierarchy (North Star impact, primary adoption metric, guardrail/counter-metrics), designs telemetry event dictionaries, and specifies A/B testing or staged rollout criteria before engineering writes frontend or backend code.

---

## ⚙️ Supported Measurement Scopes
1. **🧪 Quantitative A/B Experimentation**:
   - Sample size calculation, minimum detectable effect (MDE), null/alternative hypotheses, variant definitions, and statistical significance threshold (95% confidence).
2. **🚀 Phased Rollout / Canary Gate**:
   - For 0-to-1 features or B2B platforms where traffic volume is insufficient for statistical A/B tests; defines 10% ➔ 50% ➔ 100% rollout gates based on health metrics.
3. **📊 Telemetry & Event Tracking Taxonomy**:
   - Complete dictionary of analytics events, triggers, object properties, and payload schemas ready for Amplitude, PostHog, Mixpanel, or Segment.

---

## 📋 Best Practices & Standards Enforced
- **Mandatory Guardrail Metrics**: Every positive optimization metric must be paired with a counter-metric (e.g., *Optimize signup conversion* must guard against *drop in 30-day retention or surge in spam accounts*).
- **No Vanity Metrics**: Pageviews, registered users, and total clicks are rejected; metrics must measure completed customer value actions.
- **Instrumented Before Shipping**: Event tracking must be defined as acceptance criteria in the PRD and user stories (`create-user-stories`).
- **Pre-Determined Decision Rules**: Explicitly define what happens if the experiment is positive, flat, or negative before launching.

---

## 🛠️ Standardized 4-Stage Execution Protocol

### Stage 1: Context Hydration
1. Ingest [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) for overarching North Star metrics, current OKRs, and baseline KPIs.
2. Ingest [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) for data infrastructure limits, privacy/telemetry constraints, and compliance boundaries.
3. Ingest the target PRD from `docs/` or the feature description to anchor metrics in real functionality.

### Stage 2: Socratic Clarifying Gate
Audit whether the measurement criteria are sound:
1. **Primary Metric**: What is the single measurable action indicating the customer experienced value?
2. **Counter-Metric**: What could break, slow down, or degrade if this feature succeeds wildly?
3. **Traffic Reality**: Does the product have sufficient traffic ($\ge 1,000$ weekly conversions) for an A/B test, or should this be a phased cohort rollout?
4. If ambiguous, ask 2 targeted clarifying questions before generating.

### Stage 3: Grounded Generation
Generate the complete Metrics & Instrumentation Plan:

```markdown
# 📈 Measurement & Experimentation Plan: [Feature Name]

## 1. 🎯 Metric Hierarchy
| Level | Metric Name | Definition & Formula | Baseline | Target Goal | Source / Tool |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **North Star Link** | Weekly Active Creators (WAC) | Users who publish $\ge 1$ artifact / week | 1,200 | +8% | PostHog / Snowflake |
| **Primary Metric** | Feature Completion Rate | $\frac{\text{Completed Workflows}}{\text{Initiated Workflows}}$ | 34% | 55% | Amplitude |
| **Secondary Metric** | Time-to-First-Result | Median seconds from modal open to output | 85s | $< 30\text{s}$ | Datadog / RUM |
| **🛡️ Guardrail 1** | Pipeline Error Rate | $\frac{\text{5xx Server Failures}}{\text{Total API Requests}}$ | $< 0.1\%$ | $< 0.1\%$ | Datadog APM |
| **🛡️ Guardrail 2** | User Churn / Unsubscribe | Weekly opt-out rate | $1.2\%$ | $\le 1.2\%$ | Stripe / CRM |

---

## 2. 📡 Event Tracking & Telemetry Dictionary
| Event Name | Trigger Moment | Properties / Payload | Data Type | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `feature_started` | User clicks CTA in studio | `source_page`: string<br>`tier`: string<br>`preset_id`: string | Schema | Fire on click |
| `step_completed` | User finishes step 1 or 2 | `step_number`: int<br>`duration_ms`: int | Schema | Timing metric |
| `feature_completed` | Artifact successfully saved | `artifact_type`: string<br>`token_count`: int<br>`status`: "success" | Schema | Primary conversion |
| `feature_abandoned` | User closes tab or modal | `exit_step`: int<br>`has_dirty_input`: bool | Schema | Drop-off analysis |

---

## 3. 🧪 Experiment & Rollout Strategy
- **Rollout Mechanism**: [A/B Split Test | Phased Canary Rollout (10% -> 50% -> 100%)]
- **Hypothesis**: *"Providing pre-filled templates in the modal will increase feature completion from 34% to 55% without increasing support ticket volume."*
- **Sample Size & Duration**: Minimum 4,000 unique users per variant over 14 calendar days.
- **Decision Matrix**:
  - **Ship**: Primary metric $+10\%$ with $p < 0.05$ and all guardrails green.
  - **Iterate**: Primary metric flat ($[-2\%, +4\%]$) with high qualitative engagement; inspect drop-off telemetry.
  - **Rollback / Kill**: Primary metric negative or any guardrail violated ($> 0.5\%$ error rate).
```

### Stage 4: Knowledge Compounding (Write-Back)
1. Save the experiment spec to `docs/specs/metrics_[feature].md` or append directly to the active PRD in `docs/`.
2. Offer to update [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md) with newly established metric baselines and tracking targets.

---

## 🔄 Flow Handling & Suggested Next Skills
- **Embed into PRD**: Add metrics directly into the active PRD with `create-prd`.
- **Generate Analytics Stories**: Break telemetry requirements into INVEST developer stories with `create-user-stories`.
- **Post-Launch Retrospective**: After the rollout period concludes, run `evaluate-launch` to evaluate performance.
