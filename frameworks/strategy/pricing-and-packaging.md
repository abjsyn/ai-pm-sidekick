---
id: pricing-and-packaging
name: Van Westendorp & Packaging/Tiering Matrix
category: strategy
problem_signatures:
  - "Pricing strategy is based on internal team guesswork rather than empirical customer willingness-to-pay"
  - "Feature tiering is confusing and customers resist upgrading between Free, Pro, and Enterprise"
  - "Team packages 'killer' core value features into lower tiers, starving higher tiers of upgrade incentives"
best_for_stage:
  - growth
  - scale
  - enterprise
data_maturity_required: medium
when_not_to_use:
  - "Pure open-source software with zero commercial, monetization, or paid tier ambitions"
  - "Early 0-to-1 discovery where customers haven't validated the core value proposition"
paired_skills:
  - validate-idea
  - plan-launch
  - create-prd
  - apply-framework
write_back_target: .context/strategy-and-constraints.md
---

# 💰 Strategic Framework: Van Westendorp & Packaging/Tiering Matrix

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Synthesized from **Peter van Westendorp's Price Sensitivity Meter (PSM)** and the Good-Better-Best packaging doctrine from Madhavan Ramanujam (*Monetizing Innovation*), this framework prevents the catastrophic mistake of treating monetization as an afterthought.

1. **Van Westendorp PSM**: Asks prospective buyers 4 price threshold questions:
   - **Too Cheap**: At what price is the product so cheap that you would question its quality?
   - **Bargain / Cheap**: At what price is the product a great deal?
   - **Expensive**: At what price is it starting to get expensive, but you would still consider it?
   - **Too Expensive**: At what price is it prohibitively expensive, beyond consideration?
   The intersections define the **Point of Marginal Cheapness (PMC)**, **Point of Marginal Expensiveness (PME)**, and the **Optimal Price Point (OPP)**.

2. **Good-Better-Best Feature Packaging**:
   Classifies candidate capabilities across three monetization roles:
   - **Leaders (Core Value)**: High-value, high-frequency features that drive customer acquisition and retention. Present in all tiers.
   - **Fillers (Commodities)**: Standard table stakes; bundled into lower tiers to round out the offering.
   - **Killers (Monetization Hooks)**: Specialized, high-willingness-to-pay capabilities (e.g. SOC2 compliance, SSO/SAML, audit logs, unlimited seats) that force enterprise upgrades.

```
                           [ Good-Better-Best Packaging ]
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
   [ Tier 1: Free / Community ]     [ Tier 2: Pro / Team ]           [ Tier 3: Enterprise ]
   • Leaders (Core Value)           • Everything in Free             • Everything in Pro
   • Standard Fillers               • Advanced Leaders (Automation)  • Killers: SSO/SAML, SOC2
   • Community support              • Priority support               • Dedicated Air-Gapped SLA
```

### Primary Purpose
To establish data-backed pricing boundaries, eliminate monetization guesswork, and package features into clear, high-converting tier boundaries.

### Trigger Conditions
Apply this framework when:
- Designing or adjusting pricing tiers in `/validate-idea` or `/plan-launch`.
- Deciding which tier a new feature in `/create-prd` belongs to (Free vs Pro vs Enterprise).
- Evaluating customer feedback regarding price sensitivity in `/prepare-user-interview`.
- Crafting competitive sales battlecards in `/analyze-competitor`.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Target customer profiles, core value propositions, and current tier definitions (`lean`, `standard`, `enterprise`).
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): Unit economics, margin targets, and competitor pricing baselines.

### Socratic Inquiry
1. **The Killer Gating Test**: *"Did we put an Enterprise 'Killer' feature (like SAML SSO or audit logs) into our Free tier, destroying our primary reason for enterprise deals to upgrade?"*
2. **The Willingness-to-Pay Reality**: *"Did we ask customers 'Would you pay for this?' (polite false positive) or did we ask Van Westendorp price boundaries?"*
3. **The Value Metric Alignment**: *"Does our pricing scale with customer value (e.g., active projects, seats, synced repositories) or an arbitrary artificial cap that annoys users?"*
4. **The Too-Cheap Risk**: *"If we price this at $5/mo, will enterprise CPOs dismiss us as an unvetted hobby toy that cannot be trusted with company IP?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Phase 1: Van Westendorp Survey Analysis
Plot cumulative survey curves from target customers:
- **Optimal Price Point (OPP)**: Intersection of "Too Cheap" and "Too Expensive".
- **Indifference Price Point (IPP)**: Intersection of "Cheap" and "Expensive".
- **Acceptable Price Range**: Bound between Point of Marginal Cheapness (PMC) and Point of Marginal Expensiveness (PME).

### Phase 2: Feature Packaging Audit (Good-Better-Best)
Audit every feature against the 3 packaging categories:
- **Leader**: Must be included in Starter/Pro to create habit and activation.
- **Filler**: Standard hygiene features that do not motivate upgrades on their own.
- **Killer**: Gated strictly behind higher tiers (e.g. Enterprise / Team).

---

## 4. 📊 Output Format

### Packaging & Feature Tiering Matrix

| Feature / Capability | Packaging Role | Free / Community | Pro ($29/mo) | Enterprise (Custom) | Upgrade Incentive Rationale |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Local CLI Auto-Detection** | Leader | ✅ Included | ✅ Included | ✅ Included | Core activation loop; frictionless install. |
| **INVEST Gherkin PRD Generator** | Leader | ✅ Included | ✅ Included | ✅ Included | Primary customer value driver. |
| **All 23 Modular Frameworks** | Leader | ✅ Included | ✅ Included | ✅ Included | Product differentiation. |
| **Bi-directional MCP Sync** | Killer | ❌ 1 Sync / wk | ✅ Unlimited | ✅ Unlimited | Drives power-user upgrade to Pro. |
| **Air-Gapped Enterprise Audit Log** | Killer | ❌ Excluded | ❌ Excluded | ✅ Included | **Enterprise Gating**: Mandated by SOC2 / IT compliance. |
| **Custom Framework White-Labeling** | Killer | ❌ Excluded | ❌ Excluded | ✅ Included | Corporate governance hook. |

### Van Westendorp Price Sensitivity Range
- **Too Cheap Threshold**: $< \$15/\text{user/month}$ (Signals toy / unreliable security).
- **Optimal Price Point (OPP)**: **$\$29/\text{user/month}$** (Maximizes adoption and margin).
- **Point of Marginal Expensiveness**: $\$69/\text{user/month}$ (Resistance begins for mid-market).
- **Enterprise Floor**: $\$5,000/\text{year}$ base license.

---

## 5. ✍️ `.context/` Write-Back Target

- **Primary Target File**: [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) (under `## 💰 Pricing, Packaging & Tiering Rules`) and [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md).
- **Write-Back Content**:
  1. Record the feature gating rules across Free, Pro, and Enterprise tiers.
  2. Document the accepted pricing ranges and upgrade triggers.
