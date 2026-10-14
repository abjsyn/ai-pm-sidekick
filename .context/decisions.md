# 📜 Product Knowledge Core — Product Decision Log (`decisions.md`)

This file is an **append-only record** of all major product, architecture, and governance decisions made across the lifecycle of this product. Each entry follows the **Product Decision Record (PDR)** format.

---

## 📋 PDR Record Schema
When appending a new decision, adhere strictly to this schema:

```markdown
### PDR-[XXX]: [Short Decision Title]
- **Date**: YYYY-MM-DD
- **Status**: Proposed | Accepted | Superseded | Deprecated
- **Deciders / Stakeholders**: [Names and Roles]
- **Context & Problem Statement**: [What situation or friction required a decision?]
- **Decision Taken**: [What was decided?]
- **Alternatives Considered**: [What options were evaluated and rejected?]
- **Consequences & Trade-offs**:
  - *Positive*: [Benefits gained]
  - *Negative / Trade-offs*: [Costs, technical debt, or operational constraints accepted]
```

---

## 📚 Product Decision Records (PDRs)

### PDR-001: Physical Separation of Sidekick Harness UI from User Product Deliverables
- **Date**: 2026-10-14
- **Status**: **Accepted**
- **Deciders / Stakeholders**: AI Harness Architect, Lead PM
- **Context & Problem Statement**:
  Previously, internal Sidekick UI specifications (`PM_COMMAND_CENTER_PRD.md`, `sidepanel_*.md`) and web screens (`pm-command-center.html`, `user-profile-settings.html`, `stitch/*`) resided directly in `docs/` and `mockups/`. This caused severe context contamination: LLM prompts generating user PRDs frequently ingested the Sidekick's own internal UI specs as product requirements, and the UI Deliverable Hub listed internal tools as user work.
- **Decision Taken**:
  Move all internal Sidekick UI assets into a dedicated `ui/` directory (`ui/views/`, `ui/stitch/`, `ui/specs/`). Reserve `docs/` and `mockups/` exclusively for PM-generated product deliverables, protected by `.gitkeep` and descriptive `README.md` files.
- **Alternatives Considered**:
  - *Keep in root docs/ with naming prefixes (e.g., `_sidekick_prd.md`)*: Rejected because file globbing in LLMs and scripts frequently leaked internal content into prompt context.
  - *Package UI into a standalone python package/wheel*: Rejected because local customizability of Atelier views is a key user feature.
- **Consequences & Trade-offs**:
  - *Positive*: Complete elimination of context contamination; clean artifact scanning in `launch-ui.py`; explicit repository boundaries.
  - *Negative / Trade-offs*: Requires updating paths in `scripts/launch-ui.py` and `skills/gui-run/SKILL.md`.

---

### PDR-002: Establishment of `.context/` as the Single Source of Truth for Product Knowledge
- **Date**: 2026-10-14
- **Status**: **Accepted**
- **Deciders / Stakeholders**: AI Harness Architect, Product Team
- **Context & Problem Statement**:
  AI skills across disparate environments (AGY, Cursor, Claude Code) lacked a unified, persistent memory of product vision, active outcomes, technical stack, and quality conventions, leading to inconsistent outputs and repetitive prompt engineering.
- **Decision Taken**:
  Establish `.context/` as the canonical Product Knowledge Core with 7 structured files:
  1. `harness-config.yaml`: Operating mode, tier defaults, and tool configurations.
  2. `product.md`: High-level strategic vision, personas, value loops, North Star metric, and OKRs.
  3. `discovery.md`: Active outcomes, Opportunity Solution Tree (OST), Mom Test interviews, and JTBD canvases.
  4. `strategy-and-constraints.md`: Wardley Mapping value chain evolution, Theory of Constraints (ToC) bottleneck analysis, and business constraints.
  5. `architecture.md`: Technical stack, data models, and API interfaces (supports auto-scanning in embedded mode).
  6. `conventions.md`: Definition of Ready (DoR), Gherkin BDD criteria standards, and tier guidelines.
  7. `decisions.md`: This append-only record of architectural and product choices.
- **Alternatives Considered**:
  - *Monolithic single prompt or single markdown file*: Rejected because large documents exceed context limits and degrade instruction following.
  - *Database / SQLite storage*: Rejected because git-tracked markdown files are human-reviewable, branchable, and diffable.
- **Consequences & Trade-offs**:
  - *Positive*: Deterministic prompt grounding; zero LLM hallucination of core tech stack; consistent quality across all 14 skills.
  - *Negative / Trade-offs*: Team must maintain discipline to update `.context/` as strategic direction evolves.

---

### PDR-003: Three-Tier Artifact Convention (Lean, Standard Agile, Enterprise)
- **Date**: 2026-10-14
- **Status**: **Accepted**
- **Deciders / Stakeholders**: AI Harness Architect, Lead PM
- **Context & Problem Statement**:
  Early-stage MVPs need lightweight 1-page specs, while enterprise scaleups require rigorous compliance, traceability matrices, and audit logging. A one-size-fits-all approach causes either bureaucratic bloat for startups or unacceptable risk for enterprises.
- **Decision Taken**:
  Standardize all PRD and User Story generation skills around 3 selectable operational tiers (`lean`, `standard`, `enterprise`), configured via `.context/harness-config.yaml` or runtime CLI flags.
- **Alternatives Considered**:
  - *Single adaptive prompt*: Rejected because LLMs often produce unpredictable document lengths without explicit structural templates.
- **Consequences & Trade-offs**:
  - *Positive*: Perfect fit for every stage of product maturity; effortless transition as a product scales.
  - *Negative / Trade-offs*: Maintaining three separate template variations per artifact type in `templates/`.
