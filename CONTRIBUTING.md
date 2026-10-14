# 🤝 Contributing to AI PM Sidekick

Welcome to the **AI PM Sidekick** contributor community! This repository provides an extensible, local-first product management command center and multi-agent harness for Google Antigravity (AGY), Claude Code, and Cursor IDE.

We welcome contributions of new **modular frameworks** (`frameworks/`) and **AI skills** (`skills/`).

---

## 🏛️ Core Architectural Principles

1. **Strict Asset Separation**:
   - Internal Sidekick application assets (HTML views, Stitch design tokens, internal specs) reside strictly in `ui/`.
   - Never write internal harness documentation into `docs/` or `mockups/` — those directories are reserved exclusively for PM user deliverables.
2. **Zero External Python Dependencies**:
   - All build and exporter scripts in `scripts/` must run on Python standard library only (`os`, `sys`, `re`, `json`, `pathlib`, `shutil`, `urllib`, `http.server`). Do not introduce `pip` dependencies.
3. **Multi-Tool Adaptation via Canonical Source**:
   - Never edit files in `.agents/skills/`, `.cursor/rules/`, or `.claude/commands/` directly. Always edit the canonical files in `skills/` or `frameworks/`, and run `python3 scripts/export-skills.py` to compile adapters.

---

## 🧠 1. Contributing a New Framework (`frameworks/<category>/<name>.md`)

All frameworks live under `frameworks/` inside one of four categories:
- `frameworks/strategy/`: Value chain evolution, competitive moats, system constraints.
- `frameworks/discovery/`: Continuous customer discovery, interview evidence, problem validation.
- `frameworks/prioritization/`: Quantitative and qualitative trade-off models.
- `frameworks/operations/`: Delivery cycles, sprint pacing, appetite budgeting, planning layers.

### Required YAML Frontmatter Schema
Every framework file **must start with YAML frontmatter** containing these diagnostic fields:

```yaml
---
id: [kebab-case-identifier, e.g. wardley-mapping]
name: [Human Readable Name, e.g. Wardley Value Chain Evolution Mapping]
category: strategy | discovery | prioritization | operations
problem_signatures:
  - "[Real-world PM pain point 1 that triggers this framework]"
  - "[Real-world PM pain point 2 that triggers this framework]"
best_for_stage:
  - 0-to-1     # Include applicable stages
  - growth
  - scale
  - enterprise
data_maturity_required: low | medium | high
when_not_to_use:
  - "[Explicit anti-pattern 1: Where this framework causes waste or false precision]"
  - "[Explicit anti-pattern 2: Circumstance where an alternative is better]"
paired_skills:
  - [skill-name-1, e.g. create-prd]
  - [skill-name-2, e.g. validate-idea]
write_back_target: .context/[target-file].md
---
```

### Required 5-Section Markdown Body
The body must strictly implement the standard 5-part specification:

1. `## 1. 🧠 Mental Model & Trigger Conditions`
   - Theoretical foundation, author origin, core thesis.
   - Primary PM problem solved.
   - Explicit trigger conditions.
2. `## 2. 📥 Required .context/ Inputs & Socratic Questions`
   - Mandatory `.context/*.md` files read prior to execution.
   - 3–4 provocative diagnostic questions the AI must ask the PM to challenge assumptions.
3. `## 3. ⚙️ Step-by-Step Execution & Scoring Rubric`
   - Concrete phased algorithm, formulas, or classification matrices.
   - Explicit anti-gaming rules to prevent inflated scoring or cognitive bias.
4. `## 4. 📊 Output Format (Markdown Table / Mermaid Diagram)`
   - Concrete sample deliverable (Mermaid diagram, Gherkin blocks, or Markdown tables).
5. `## 5. ✍️ .context/ Write-Back Target`
   - Exact path and section in `.context/` updated upon completion.

---

## ⚡ 2. Contributing a New Skill (`skills/<name>/SKILL.md`)

Each AI skill lives in its own canonical folder: `skills/<name>/SKILL.md`.

### Required Skill YAML Frontmatter
```yaml
---
name: [kebab-case-name, matching folder name]
description: >-
  [Action-oriented summary explaining what the skill accomplishes, input sources, and output deliverables.]
---
```

### The 4-Stage Execution Protocol
Every skill must implement the standard 4-Stage Protocol:

1. **Stage 1: Context Hydration**:
   - Instruct the agent to read relevant files from `.context/` (`harness-config.yaml`, `product.md`, `conventions.md`, etc.).
2. **Stage 2: Socratic Clarifying Gate**:
   - If user requirements lack necessary context for the requested deliverable tier, the agent must pause and ask 2–4 targeted clarifying questions.
3. **Stage 3: Generation & Formatting**:
   - Save user deliverables to `docs/` (`.md` specs) or `mockups/` (`.html` prototypes).
   - Follow the deliverable tier (`lean`, `standard`, `enterprise`) defined in `.context/harness-config.yaml`.
4. **Stage 4: Knowledge Compounding Write-Back**:
   - Propose syncing newly derived decisions or user insights back into `.context/` and `BACKLOG.md`.
   - Recommend 2–3 logical next skills to continue the product workflow.

---

## 🤖 3. AI Contributor Prompt Template

Contributors can copy and paste this prompt to their AI agent to author a compliant framework from any methodology, article, or book:

```markdown
Act as a Principal Product Architect for the `ai-pm-sidekick` repository.
Read CONTRIBUTING.md, frameworks/README.md, and frameworks/strategy/wardley-mapping.md.

Convert the following methodology into a fully compliant framework file:
[PASTE METHODOLOGY / BOOK SUMMARY / ARTICLE HERE]

Requirements:
1. Target path: `frameworks/<category>/<framework-id>.md`
   (category must be one of: strategy, discovery, prioritization, operations).
2. Include complete YAML frontmatter:
   - id, name, category
   - problem_signatures (2-3 real-world PM pain points)
   - best_for_stage (subset of [0-to-1, growth, scale, enterprise])
   - data_maturity_required (low | medium | high)
   - when_not_to_use (2-3 explicit anti-patterns)
   - paired_skills (skills in skills/)
   - write_back_target (target file in .context/)
3. Strictly implement all 5 standard sections:
   - ## 1. 🧠 Mental Model & Trigger Conditions
   - ## 2. 📥 Required .context/ Inputs & Socratic Questions
   - ## 3. ⚙️ Step-by-Step Execution & Scoring Rubric (with anti-gaming checks)
   - ## 4. 📊 Output Format (Markdown Table & Mermaid diagram)
   - ## 5. ✍️ .context/ Write-Back Target
```

---

## 🧪 4. Linting & Validation

Before submitting a Pull Request, validate that all skills and frameworks conform to schemas:

```bash
# Run schema and frontmatter validator
python3 scripts/export-skills.py --validate

# Compile multi-tool adapters
python3 scripts/export-skills.py
```

Check `git status` to verify that `.agents/skills/`, `.cursor/rules/`, `.claude/commands/`, and `dist/` have been cleanly regenerated.
