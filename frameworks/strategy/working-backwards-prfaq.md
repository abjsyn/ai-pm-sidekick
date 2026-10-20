---
id: working-backwards-prfaq
name: Working Backwards (Amazon PR/FAQ)
category: strategy
problem_signatures:
  - "Feature concept is heavily engineering-led or architecture-driven without a clear customer value narrative"
  - "Product vision is diffuse and executive stakeholders disagree on the core customer experience being built"
  - "Team writes massive 30-page spec documents that bury the real customer problem under implementation minutiae"
best_for_stage:
  - 0-to-1
  - growth
  - enterprise
data_maturity_required: low
when_not_to_use:
  - "Incremental bug fixing, tech debt reduction, or internal pipeline refactoring"
  - "Continuous UI polish sprints where the core value proposition is already proven and unchanged"
paired_skills:
  - create-prd
  - validate-idea
  - audit-spec
  - plan-launch
write_back_target: .context/strategy-and-constraints.md
---

# 📰 Strategic Framework: Working Backwards (Amazon PR/FAQ)

## 1. 🧠 Mental Model & Trigger Conditions

### Theoretical Foundation
Pioneered by **Amazon**, the **Working Backwards** product methodology demands that before a team writes a single line of functional specification or architecture code, they must draft the future launch assets from the customer's perspective:
1. **The Press Release (PR)**: A 1-page announcement dated on the hypothetical launch day. Written in clear, non-jargon language, it describes the customer problem, why existing solutions failed, how the new product solves it elegantly, and features a simulated customer testimonial quote.
2. **The Customer FAQ**: Answers real, practical end-user questions (e.g., pricing, onboarding friction, data migration, privacy, platform support).
3. **The Internal Stakeholder FAQ**: Confronts hard technical, architectural, operational, and financial realities (e.g., unit economics, scalability bottlenecks, competitor reaction, rollback plan, legal constraints).

```
                      [ Future Customer Launch Reality ]
                                       │
                ┌──────────────────────┴──────────────────────┐
                ▼                                             ▼
     [ 1. Future Press Release ]                 [ 2. Customer & Internal FAQs ]
     • Customer pain & current workarounds       • End-user onboarding & costs
     • Hero capability & how it feels            • Architecture limits & unit economics
     • Hypothetical customer quote               • Trade-offs, risks & kill criteria
                │                                             │
                └──────────────────────┬──────────────────────┘
                                       ▼
                     [ Grounded Functional PRD & Backlog ]
```

### Primary Purpose
To enforce extreme customer-centric clarity, prevent technical solipsism, align cross-functional leaders around the core value proposition, and expose unaddressed trade-offs long before development begins.

### Trigger Conditions
Apply this framework when:
- Kicking off a major 0-to-1 product or strategic platform pivot in `/create-prd`.
- A proposed initiative is technologically sophisticated but the customer value narrative is muddy or missing.
- Preparing an executive defense or strategic initiative brief in `/prep-meeting`.
- Aligning engineering and business teams before writing detailed functional requirements.

---

## 2. 📥 Required `.context/` Inputs & Socratic Questions

### Mandatory Context Inputs
- [`.context/product.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/product.md): Target audience profile, brand voice, North Star metric, and core value loops.
- [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md): Strategic boundaries, competitive landscape, and regulatory constraints.
- [`.context/discovery.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/discovery.md): Customer verbatims describing the visceral friction of current alternatives.

### Socratic Inquiry
1. **The Non-Jargon Test**: *"Can an average non-technical user or executive understand this press release without understanding our database schema or API acronyms?"*
2. **The Testimonial Authenticity Check**: *"Does the customer quote sound like words a real human would say to their peer, or like a corporate marketing brochure?"*
3. **The Hard Internal Questions**: *"What is the single most terrifying architectural, financial, or legal risk detailed in the Internal FAQ that everyone is afraid to bring up?"*
4. **The 'So What?' Litmus Test**: *"If a customer reads this headline on TechCrunch or Hacker News, do they immediately understand why their daily workflow gets 10x better?"*

---

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric

### Phase 1: Drafting the Press Release (One Page Max)
1. **Heading**: Product Name + One-sentence headline capturing customer outcome (not feature list).
2. **Sub-heading**: Target customer + immediate benefit.
3. **Summary Paragraph**: City, Launch Date — High-level summary of the announcement.
4. **Problem Statement**: 1–2 paragraphs detailing the painful problem and why existing alternatives are inadequate.
5. **Solution & Core Value**: How the product effortlessly solves the problem without introducing new friction.
6. **Leader Quote**: Internal executive quote explaining company vision and conviction.
7. **Customer Quote**: Fictional but realistic verbatim testimonial from an early beta user describing their concrete transformation.
8. **Call to Action & Getting Started**: Exactly where and how customers access it today.

### Phase 2: Drafting the Customer FAQ (External)
Focus on usability, friction, and economics:
- *How much does this cost?*
- *What happens to my existing data/workflows?*
- *How long does onboarding take?*
- *What if something breaks or I need human help?*

### Phase 3: Drafting the Internal FAQ (Tough Reality)
Confront the elephants in the room:
- *What is the total estimated engineering appetite (weeks/sprints)?*
- *What are the primary technical scaling bottlenecks or architectural dependencies?*
- *How could our chief competitor neutralize or copy this announcement in 30 days?*
- *What is our explicit kill/rollback condition if adoption fails?*

---

## 4. 📊 Output Format

### Working Backwards PR/FAQ Document Structure

```markdown
# 📰 [DRAFT] Press Release: [Product / Major Feature Name]

**FOR IMMEDIATE RELEASE — [Hypothetical Launch Date]**

### [Headline: Action-oriented customer outcome, e.g. "Acme Corp Unveils AI PM Sidekick: Turning Raw Customer Feedback into INVEST User Stories in 60 Seconds"]

**SAN FRANCISCO, CA** — Today, [Company] announced [Product/Feature], enabling [Target Persona] to [Primary Job to be Done] without [Primary Pain Point/Friction].

For years, product managers and engineering leads have struggled with [Visceral Problem Statement]. While existing tools like [Competitor/Old Way] offer [Inadequate Solution], they force teams to spend up to 40% of their working hours manually copy-pasting notes and reformatting tickets.

[Product/Feature] eliminates this overhead entirely by [Core Solution Mechanism]. Users simply connect their repository, and the system automatically [Key Differentiator].

> *"Before [Product], our sprint grooming dragged on for three grueling hours every other Tuesday,"* said Sarah Jenkins, VP of Product at FinScale. *"Now, our stories arrive with pre-validated Gherkin criteria and edge cases already tested. Our cycle time dropped by 35% in our first month."*

Starting today, [Product/Feature] is available to all customers at [URL / Command].

---

## 👥 Customer FAQ (External)
1. **Q: How does this integrate with our existing Jira or Linear setup?**
   - **A:** [Concise, non-technical explanation].
2. **Q: Is our proprietary product data used to train public AI models?**
   - **A:** [Direct security and compliance guarantee].

---

## 🏢 Internal Stakeholder FAQ (Cross-Functional Reality)
1. **Q: What is our estimated cloud infrastructure cost per active monthly user?**
   - **A:** [Unit economic breakdown].
2. **Q: If our primary LLM provider suffers an outage, how does the system fail gracefully?**
   - **A:** [Fallback mechanisms and local model cache].
```

---

## 5. ✍️ `.context/` Write-Back Target

- **Primary Target File**: [`.context/strategy-and-constraints.md`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/strategy-and-constraints.md) (under `## 📰 Working Backwards (PR/FAQ) Strategic Narratives`) or saved to `docs/prds/prfaq_<feature>.md`.
- **Write-Back Content**:
  1. Record the agreed headline, core value narrative, and customer promise.
  2. Embed key trade-offs and non-negotiables discovered during the Internal FAQ into strategy constraints.
