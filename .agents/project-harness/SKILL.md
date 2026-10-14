---
name: project-harness
description: >-
  Core AI PM Sidekick operational router. Hydrates product context from .context/, enforces strict separation between internal UI and user deliverables, applies Socratic inquiry, and compounds knowledge.
---

# 🚀 AI PM Sidekick — Project Harness Router

This is the primary harness router skill for the AI PM Sidekick. It governs how agentic models interact with the workspace, consult product context, and generate production-grade PM deliverables.

## 1. Operating Principles

1. **Context Hydration**: Always read relevant files from `.context/` before initiating work:
   - Configuration: `.context/harness-config.yaml`
   - Vision & Personas: `.context/product.md`
   - Conventions & Standards: `.context/conventions.md`
   - Discovery & Outcomes: `.context/discovery.md`
   - Strategy & Bottlenecks: `.context/strategy-and-constraints.md`
   - Architecture & Schemas: `.context/architecture.md`
   - Decision Log: `.context/decisions.md`

2. **Prevent Context Contamination**:
   - `ui/specs/` and `ui/views/` are strictly internal Sidekick assets. Never treat them as user product documentation.
   - User PRDs, specs, and stories MUST be created in `docs/`.
   - User HTML prototypes and mockups MUST be created in `mockups/`.

3. **Socratic Clarifying Gate**:
   - Never hallucinate critical business constraints or user pain points.
   - If user requirements lack necessary context for the requested deliverable tier, pause and ask 2–4 targeted clarifying questions.
   - If the user prefers fast iteration, document explicit assumptions in the output.

4. **Knowledge Compounding**:
   - When a session yields validated assumptions, architectural decisions, or user insights, propose updating the `.context/*.md` files and logging decisions in `.context/decisions.md`.

## 2. Dynamic Skill & Framework Routing

- Match user requests to skills in `skills/` or invoke via slash commands (`/create-prd`, `/create-user-stories`, `/apply-framework`, etc.).
- Strategic, discovery, and prioritization frameworks are available in `frameworks/strategy/`, `frameworks/discovery/`, and `frameworks/prioritization/`.
- Refer to `dist/harness-manifest.json` for live metadata and triggers.
