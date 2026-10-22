---
name: compact-context
description: Merges staged .context/.inbox/ patches after human review and compacts bloated .context/*.md files using Anchored Incremental Summarization without losing foundational decisions.
paths:
  - ".context/*.md"
  - ".context/.inbox/*.md"
requires:
  context_files:
    - ".context/harness-config.yaml"
---

# Compact Context & Memory Inbox Manager

## Purpose

Prevent context rot and silent strategy drift across long-running product lifecycles. This skill performs two deterministic operations:

1. **Inbox Review & Merge (`--apply-inbox`):** Lists pending memory patches in `.context/.inbox/`, asks the PM for explicit approval per patch, and merges approved diffs into `.context/product.md`, `.context/strategy-and-constraints.md`, or `.context/decisions.md`.

2. **Anchored Incremental Compaction (`--compact`):** When any `.context/*.md` file exceeds `max_tokens_per_file` (default: 4,000 tokens / ~16,000 characters), compacts historical entries into anchored sections while preserving the 5 most recent entries verbatim.

## Required Inputs

Always read before acting:

- `.context/harness-config.yaml`
- All files in `.context/.inbox/*.md` (excluding `README.md`)
- Target `.context/*.md` file(s) being compacted (`discovery.md`, `decisions.md`, `strategy-and-constraints.md`, `product.md`)

## Interactive Workflow

### Phase 1: Inbox Triage

1. Scan `.context/.inbox/` for any `.md` files (ignoring `README.md`).
2. If pending patches exist, display a numbered summary table:
   - `Patch File` | `Target Context File` | `Originating Skill` | `1-Sentence Summary of Change`
3. Ask the user: *"Which patches should I merge, edit, or discard? (e.g., 'merge 1, discard 2')"*
4. **STOP and wait for user confirmation.** Never merge a patch into `product.md`, `strategy-and-constraints.md`, or `decisions.md` without explicit user approval.
5. Upon approval, apply the update to the target `.context/*.md` file and delete the consumed patch file from `.context/.inbox/`.

### Phase 2: Anchored Incremental Compaction

1. Estimate token count of each `.context/*.md` file using `len(text) // 4`.
2. Report any file exceeding `4,000` tokens (or `16,000` characters).
3. When compacting a file, **NEVER summarize from scratch**. Use the **Anchored Incremental Merge** structure below:
   - Read the existing anchored summary block (if present) in `<previous-summary>` and merge older entries into these exact 5 Markdown sections:
     1. `## 1. Active Product Bet & Core Constraints` (Preserve still-true strategic guardrails)
     2. `## 2. Validated Discovery Insights` (High-signal user/market facts with evidence)
     3. `## 3. Invalidated Hypotheses & Dead Ends` (Prevent re-litigating failed ideas)
     4. `## 4. Committed Decisions (ADRs / PDRs)` (Immutable trade-offs with date and rationale)
     5. `## 5. Verbatim Recent Log (Last 5 Entries)` (Keep the 5 newest entries untouched at the bottom)
4. Show a before/after token count diff and write the compacted file back to `.context/<filename>.md`.
