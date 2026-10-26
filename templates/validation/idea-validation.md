# 🧪 Idea & Hypothesis Validation Report

**Idea Name:** [Project / Feature Concept Name]  
**Evaluator:** [PM Name] | **Date:** [YYYY-MM-DD]

---

## 1. Executive Concept Summary
Brief 2-3 sentence overview of the idea and the problem it attempts to solve.

---

## 2. Strategyzer 4-Risk Assessment Matrix

| Risk Dimension | Critical Assumptions | Severity (1-5) | Uncertainty (1-5) | Risk Score (S x U) |
| :--- | :--- | :---: | :---: | :---: |
| **1. Desirability** *(Do users actually want this?)* | [Assumption 1] | 5 | 4 | **20 (Critical)** |
| **2. Feasibility** *(Can we build this technically?)* | [Assumption 2] | 3 | 2 | **6 (Low)** |
| **3. Viability** *(Is the business model sustainable?)* | [Assumption 3] | 4 | 3 | **12 (Medium)** |
| **4. Usability** *(Can users figure out how to use it?)* | [Assumption 4] | 2 | 2 | **4 (Low)** |

---

## 3. The Mom Test — Customer Interview Framework
*Questions designed to avoid opinion bias and extract real past behavior:*
1. **Past Behavior Question:** "How do you currently handle [problem] today?"
2. **Cost / Friction Question:** "What has that cost you in time/money over the past month?"
3. **Workaround Question:** "What tools or workarounds have you tried to solve this?"

---

## 4. Market Sizing (TAM / SAM / SOM)
* **TAM (Total Addressable Market):** $[X]B (Total global market demand)
* **SAM (Serviceable Addressable Market):** $[Y]M (Target segment reached by our channel)
* **SOM (Serviceable Obtainable Market):** $[Z]M (Realistic capture in Year 1-2)

---

## 5. Pre-Mortem & Risky Assumptions
* **If this product fails in 12 months, why did it fail?**
  1. [Failure Mode 1: e.g., CAC too high]
  2. [Failure Mode 2: e.g., Low retention after week 2]

---

## 6. Recommended Validation Experiments (Osterwalder 44-Experiment Selector)
*Matched via `frameworks/discovery/experiment-selector.md` based on Risk Lens, B2B/B2C Market Fit, Cost/Time, and Evidence Strength:*

| Step / Priority | Experiment (#/44) | Risk & Market Fit | Evidence (1–5) | Cost & Duration | Target Metric / Kill Threshold | Paired Skill |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Step 1 (Discovery)** | #19 Datasheet / #21 Smoke Landing Page | Desirability (B2B/B2C) | 3/5 (Commit/CTA) | $0–$200 / 3 Days | > 8% CTA signup or >= 5/8 pilot requests; Kill if < 2% | `/create-mockup` |
| **Step 2 (Validation)** | #35 Concierge / #34 Wizard of Oz MVP | Desirability & Usability | 4/5 (What People Do) | $0 / 1–2 Weeks | >= 5 active weekly manual users completing core loop | `/validate-idea` |
| **Step 3 (Viability)** | #43 Letter of Intent (LOI) / #40 Mock Sale | Viability (Willingness to Pay) | 5/5 (Skin in the Game) | $0 / 5 Days | >= 2 signed B2B LOIs or > 3% checkout click rate | `/define-metrics-and-experiment` |

---

## 🚦 Final Recommendation Signal: [GO / PIVOT / NO-GO]
**Rationale:** Summary of why we should proceed, modify direction, or abandon.
