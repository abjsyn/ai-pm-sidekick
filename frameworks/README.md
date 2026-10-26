# 🧠 AI PM Sidekick — Modular Framework Engine (`frameworks/`)

The `frameworks/` directory provides a modular, extensible library of strategic, continuous discovery, and prioritization frameworks. By separating framework logic from individual AI skills (`skills/`), skills can dynamically orchestrate and apply structured product thinking without hardcoding heuristics into individual skill prompts.

---

## 🏛️ Framework Directory Structure

```
frameworks/
├── README.md                      # Schema specification & execution protocol
├── strategy/                      # High-level positioning, value chains, and system constraints
│   ├── wardley-mapping.md         # Value chain evolution & build-vs-buy doctrine
│   ├── theory-of-constraints.md   # 5 Focusing Steps & bottleneck throughput optimization
│   ├── working-backwards-prfaq.md # Amazon Press Release & Customer/Internal FAQ
│   ├── north-star-metric-tree.md  # North Star decomposition into Breadth/Depth/Frequency/Efficiency
│   ├── product-positioning.md     # April Dunford 5-component positioning engine
│   ├── seven-powers-moats.md      # Hamilton Helmer structural defensibility analysis
│   └── pricing-and-packaging.md   # Van Westendorp PSM & Good-Better-Best tiering
├── discovery/                     # Continuous discovery, user pains, and customer validation
│   ├── opportunity-solution-tree.md # Outcome -> Opportunity -> Solution -> Test hierarchy
│   ├── jtbd-and-mom-test.md       # Jobs to Be Done & non-leading interview synthesis
│   ├── assumption-mapping.md      # 4 lenses (Desirability, Feasibility, Viability, Usability) + RAT
│   ├── experiment-selector.md     # Osterwalder 44-Experiment Selector & Discovery-to-Validation sequencing
│   └── aarrr-and-growth-loops.md  # Pirate metrics funnel diagnostics & compounding growth loops
├── prioritization/                # Quantitative & qualitative trade-off scoring
│   ├── rice.md                    # Reach, Impact, Confidence (anti-gaming), Effort
│   ├── wsjf-cost-of-delay.md      # Weighted Shortest Job First economic scheduling
│   ├── kano-model.md              # Must-be, Performance, and Delighter categorization
│   ├── ice-and-value-effort.md    # ICE scoring (Impact, Confidence, Ease) + 2x2 Value/Effort
│   ├── opportunity-scoring.md     # Ulwick / Dan Olsen Opportunity formula (Importance vs Satisfaction)
│   └── moscow-scope-negotiation.md# Must/Should/Could/Won't boundaries & Buy-a-Feature budget games
└── operations/                    # Delivery execution, cadence, and operational models
    ├── shape-up.md                # Shaped Pitches, Appetite, Rabbit Holes, Hill Charts
    ├── scrum-sprint-delivery.md   # Sprint Goal, INVEST Stories, Gherkin ACs, Velocity slicing
    ├── gist-planning.md           # Goals, Ideas, Step-projects, Tasks
    ├── user-story-mapping.md      # Jeff Patton narrative backbone & Walking Skeleton release slices
    ├── pre-mortem-tigers.md       # Shreyas Doshi failure simulation: Tigers, Paper Tigers, Elephants
    └── kanban-continuous-flow.md  # Little's Law continuous flow, WIP limits, and Service Level Expectations
```

---

## 📋 Standard Diagnostic Frontmatter & 5-Part Specification Schema

Every framework file in this directory **must strictly implement** the following YAML frontmatter and 5-part body schema to ensure deterministic execution by AI agents and seamless bidirectional synchronization with the `.context/` Product Knowledge Core:

```markdown
---
id: [framework-id]
name: [Human Readable Name]
category: [strategy | discovery | prioritization | operations]
problem_signatures:
  - "[Signature 1: Real-world pain point]"
  - "[Signature 2: Real-world pain point]"
best_for_stage:
  - [0-to-1 | growth | scale | enterprise]
data_maturity_required: [low | medium | high]
when_not_to_use:
  - "[Anti-pattern 1: Where this framework fails]"
  - "[Anti-pattern 2: Where this framework fails]"
paired_skills:
  - [skill-1]
  - [skill-2]
write_back_target: [.context/target-file.md]
---
# [Framework Name]

## 1. 🧠 Mental Model & Trigger Conditions
- **Theoretical Foundation**: Core philosophy, origin, and author.
- **Primary Purpose**: The specific product management problem this framework solves.
- **Trigger Conditions**: Explicit scenarios and skill invocations that trigger this framework 
  (e.g., during idea validation, PRD drafting, story grooming, roadmap sequencing, build-vs-buy analysis).

## 2. 📥 Required `.context/` Inputs & Socratic Questions
- **Mandatory Input Files**: Specific `.context/` files to read before execution 
  (`.context/product.md`, `.context/strategy-and-constraints.md`, `.context/discovery.md`, `.context/architecture.md`, `.context/conventions.md`).
- **Socratic Inquiry**: Provocative diagnostic questions the AI agent must ask the PM 
  or answer using repository context to interrogate assumptions and challenge biases.

## 3. ⚙️ Step-by-Step Execution & Scoring Rubric
- **Phased Algorithm**: Concrete, step-by-step instructions for executing the framework.
- **Formulas & Mathematical Logic**: Specific formulas (e.g., RICE, WSJF, Kano matrices).
- **Anti-Gaming Rules & Failure Modes**: Strict boundary rules to prevent cognitive bias, 
  inflated confidence scores, or superficial feature prioritization.

## 4. 📊 Output Format (Markdown Table / Mermaid Diagram)
- **Standard Deliverable Artifact**: Canonical Markdown tables, Gherkin blocks, or Mermaid diagrams 
  ready for embedding into PRDs (`docs/`), backlog tickets, or design briefs.

## 5. ✍️ `.context/` Write-Back Target
- **Target File & Section**: Exact path and section in `.context/` updated upon framework completion.
- **Persistence Protocol**: Append, replace, or merge instructions to maintain the Product Knowledge Core 
  as the single source of truth.
```

---

## 🔄 How AI Skills Invoke Frameworks

When an agent executes a canonical skill (e.g. `/validate-idea`, `/create-prd`, `/create-user-stories`, `/refine-user-stories`):
1. **Detect Framework Need**: Check `.context/harness-config.yaml` (`active_frameworks`) and the task objectives.
2. **Ingest Framework Spec**: Read the corresponding `frameworks/<category>/<framework>.md`.
3. **Load Context**: Ingest the specified `.context/` dependency files.
4. **Execute & Render**: Generate the framework deliverable (Mermaid diagram, scoring matrix, or table) into the target product document in `docs/`.
5. **Write Back**: Update `.context/` with newly derived strategic insights, bottlenecks, or opportunities to keep memory synchronized across all future skill executions.
