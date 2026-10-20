---
id: product-positioning
name: Product Positioning (April Dunford)
category: strategy
problem_signatures:
  - "Prospects and customers say 'So what?' or misunderstand what the product actually does"
  - "Sales team struggles to close deals without extensive discounting or custom development"
  - "The product competes head-on against entrenched incumbents in the wrong market category"
best_for_stage:
  - 0-to-1
  - growth
  - scale
data_maturity_required: medium
when_not_to_use:
  - "Internal platform tools with zero external customer or market positioning considerations"
  - "Routine patch releases or minor bug fix updates"
paired_skills:
  - plan-launch
  - analyze-competitor
  - create-prd
  - prep-meeting
write_back_target: .context/strategy-and-constraints.md
---

# 🧭 Strategic Framework: Product Positioning (April Dunford)

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Originated by **April Dunford** in *Obviously Awesome*, this framework posits that product positioning is not clever copy, taglines, or messaging—it is the deliberate act of establishing **context** for your product so that your target customers can quickly understand why it is exceptionally valuable to them.

Dunford defines the 5 interconnected components of positioning that must be solved in strict sequential order:
1. **Competitive Alternatives**: What would customers do or buy if our product did not exist? (Often Excel, manual junior labor, or status quo, rather than direct software competitors).
2. **Unique Differentiating Attributes**: What technical, design, or business model capabilities do we have that the alternatives lack?
3. **Value & Proof**: What concrete value or business outcome do those unique capabilities enable for customers?
4. **Target Customer Characteristics**: What specific segment of customers cares deeply about this value?
5. **Market Category**: What context frame makes your value obvious and your competitors irrelevant?

```
 [ 1. Competitive Alternatives ]  ──▶  What customers use today (e.g., Spreadsheets, Jira)
              │
              ▼
 [ 2. Unique Attributes ]         ──▶  What we have that they lack (e.g., Local CLI auto-detect)
              │
              ▼
 [ 3. Value & Proof ]             ──▶  The concrete benefit (e.g., Zero API key setup friction)
              │
              ▼
 [ 4. Target Customer Segment ]   ──▶  Who cares the most (e.g., Security-conscious enterprise PMs)
              │
              ▼
 [ 5. Market Category ]           ──▶  The frame of reference (e.g., "Air-Gapped AI PM Command Center")
```

### Primary Purpose
To eliminate positioning confusion, elevate differentiation above incumbent competitors, and guide GTM launch messaging, sales battlecards, and PRD scope.

### Trigger Conditions
Apply this framework when:
- Designing a Go-To-Market launch plan in `/plan-launch`.
- Crafting competitive sales battlecards in `/analyze-competitor`.
- Defining company positioning or value propositions in [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md).
- Prospects routinely confuse your product with an unrelated SaaS category.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Target personas, core product capabilities, and value loops.
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): Strategic differentiation pillars, competitive landscape, and pricing tier.
- [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md): Customer interview quotes describing current alternative tools.

### Socratic Inquiry
1. **The True Alternative Test**: *"If our tool vanished tomorrow, what would users ACTUALLY do? Would they buy Competitor X, or would they just use a hacky Python script or Google Docs?"*
2. **The 'So What?' Test**: *"We have Feature Y. So what? What does Feature Y allow the user to do that makes their boss promote them or saves their team $50k/year?"*
3. **The Disqualification Test**: *"What customer characteristic makes someone a terrible fit for this product, and how do we actively filter them out?"*
4. **The Category Frame**: *"Are we positioning as an 'AI tool' (crowded, low-trust) or an 'Embedded Engineering Harness' (specialized, high-conviction)?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Phase 1: Identify Real Competitive Alternatives
List the top 3 alternatives customers actually use today (e.g., Status Quo, Excel, Atlassian Jira, Linear, ChatGPT web UI).

### Phase 2: Isolate Unique Capabilities
Identify only the features that are **provably true and unique** to our solution (e.g., *Runs locally on developer machine with zero cloud API key exposure; generates full INVEST Gherkin stories in 3 seconds*).

### Phase 3: Translate Capabilities into Proven Value
Map each unique attribute to a measurable business outcome:
- *Capability* ➔ *So What? (Value)* ➔ *Proof Point*.

### Phase 4: Define the Best-Fit Customer Profile
Identify the firmographic, technographic, or behavioral traits that make a customer care 10x more about this value than average buyers.

### Phase 5: Select Market Category
Choose between:
- **Head to Head**: Win the established market category (e.g., "The best Jira alternative").
- **Big Fish / Small Pond (Sub-segment)**: Dominate a specific niche (e.g., "The AI Backlog Groomer for Regulated Fintech").
- **Create New Category**: Reframe the market around a new paradigm (e.g., "AI-SDLC Command Center").

---

## 4. 📊 Output Format

### April Dunford 5-Component Positioning Canvas

| Component | Concrete Product Definition | Strategic Rationale |
| :--- | :--- | :--- |
| **1. Competitive Alternatives** | 1. Manual Jira typing<br>2. Copy-pasting ChatGPT prompts<br>3. Fragile custom Python scripts | Customers default to manual drudgery because enterprise IT blocks sending proprietary IP to cloud LLM tools. |
| **2. Unique Attributes** | • Zero-config local CLI engine detection (`agy`, `gemini`, `claude`)<br>• Bidirectional `.context/` grounding<br>• Pre-built INVEST & Gherkin linter | No other PM tool operates entirely within the developer's local repo without requiring third-party SaaS cloud accounts. |
| **3. Value & Proof** | • Cuts sprint prep time from 4 hours to 15 mins<br>• 100% data privacy (zero cloud logging)<br>• Eliminates hallucinations | Stories reference verified schemas and endpoints in `.context/architecture.md`. |
| **4. Target Customer** | Mid-to-Enterprise Software PMs working in regulated industries (Fintech, Health, Defense) | They have strict compliance policies banning public SaaS AI assistants but urgent sprint delivery backlogs. |
| **5. Market Category** | **Autonomous AI-SDLC Harness & Command Center** | Reframes away from "generic AI wrapper" into specialized developer infrastructure. |

---

## 5. ✍️ `.context/` Write-Back Target

- **Primary Target File**: [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) (under `## 🧭 Product Positioning & Differentiation Canvas`) and [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md).
- **Write-Back Content**:
  1. Record the 5 positioning components.
  2. Embed differentiated messaging into launch plans and battlecards.
