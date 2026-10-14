#!/usr/bin/env python3
"""
AI PM Sidekick — Cross-Tool Skill & Framework Exporter + Harness Manifest Generator

Compiles canonical skills (`skills/`) and modular frameworks (`frameworks/`) into:
  - AGY Native Skills (`.agents/skills/`) & Root Harness (`.agents/project-harness/SKILL.md`)
  - Cursor Rules (`.cursor/rules/*.mdc`) & Root Instructions (`.cursorrules`)
  - Claude Code Commands (`.claude/commands/*.md`) & Workspace Guide (`CLAUDE.md`)
  - Universal Prompt Bundle (`dist/pm_sidekick_system_prompt.md`)
  - Machine-Readable Harness Manifest (`dist/harness-manifest.json`)
"""

import os
import shutil
import re
import json
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).parent.parent.resolve()
SKILLS_DIR = ROOT_DIR / "skills"
FRAMEWORKS_DIR = ROOT_DIR / "frameworks"
CONTEXT_DIR = ROOT_DIR / ".context"
TEMPLATES_DIR = ROOT_DIR / "templates"
DIST_DIR = ROOT_DIR / "dist"

# Metadata enrichment for skills: categories, display names, context dependencies, and UI assets
SKILL_CONFIG = {
    "brainstorm": {
        "name": "Opportunity Brainstorm",
        "category": "ideation",
        "icon": "psychology_alt",
        "color": "text-amber-500",
        "required_context_files": [".context/product.md", ".context/discovery.md"]
    },
    "validate-idea": {
        "name": "Idea & Hypothesis Validator",
        "category": "ideation",
        "icon": "fact_check",
        "color": "text-red-400",
        "required_context_files": [".context/product.md", ".context/discovery.md", ".context/strategy-and-constraints.md"]
    },
    "create-prd": {
        "name": "PRD Generator",
        "category": "specification",
        "icon": "description",
        "color": "text-amber-500",
        "required_context_files": [".context/product.md", ".context/discovery.md", ".context/strategy-and-constraints.md", ".context/conventions.md"]
    },
    "create-user-stories": {
        "name": "INVEST User Stories",
        "category": "specification",
        "icon": "splitscreen",
        "color": "text-blue-400",
        "required_context_files": [".context/product.md", ".context/conventions.md", ".context/architecture.md"]
    },
    "refine-user-stories": {
        "name": "Story Refinement & SPIDR",
        "category": "specification",
        "icon": "tune",
        "color": "text-blue-400",
        "required_context_files": [".context/conventions.md", ".context/architecture.md"]
    },
    "create-mockup": {
        "name": "HTML Wireframe & Prototype",
        "category": "specification",
        "icon": "web",
        "color": "text-teal-400",
        "required_context_files": [".context/product.md", ".context/conventions.md"]
    },
    "create-design-brief": {
        "name": "UI/UX Design Brief",
        "category": "specification",
        "icon": "palette",
        "color": "text-teal-400",
        "required_context_files": [".context/product.md", ".context/conventions.md"]
    },
    "create-documentation": {
        "name": "Technical & User Docs",
        "category": "specification",
        "icon": "menu_book",
        "color": "text-zinc-400",
        "required_context_files": [".context/product.md", ".context/architecture.md"]
    },
    "ingest-context": {
        "name": "Context Ingestion Router",
        "category": "knowledge",
        "icon": "input",
        "color": "text-purple-400",
        "required_context_files": [".context/product.md", ".context/discovery.md", ".context/strategy-and-constraints.md", ".context/architecture.md", ".context/decisions.md"]
    },
    "apply-framework": {
        "name": "Modular Framework Runner",
        "category": "knowledge",
        "icon": "hub",
        "color": "text-indigo-400",
        "required_context_files": [".context/harness-config.yaml", ".context/discovery.md", ".context/strategy-and-constraints.md"]
    },
    "connect-mcp": {
        "name": "MCP Integration Manager",
        "category": "sync",
        "icon": "cable",
        "color": "text-emerald-400",
        "required_context_files": [".context/harness-config.yaml"]
    },
    "sync-jira": {
        "name": "Jira Epics & Stories Sync",
        "category": "sync",
        "icon": "task_alt",
        "color": "text-blue-500",
        "required_context_files": [".context/conventions.md"]
    },
    "sync-confluence": {
        "name": "Confluence Wiki Sync",
        "category": "sync",
        "icon": "library_books",
        "color": "text-blue-400",
        "required_context_files": [".context/product.md"]
    },
    "sync-github-issues": {
        "name": "GitHub Issues Sync",
        "category": "sync",
        "icon": "code",
        "color": "text-zinc-200",
        "required_context_files": [".context/discovery.md", ".context/conventions.md"]
    },
    "sync-figma": {
        "name": "Figma Specs Sync",
        "category": "sync",
        "icon": "design_services",
        "color": "text-violet-400",
        "required_context_files": [".context/conventions.md"]
    },
    "sync-miro": {
        "name": "Miro Whiteboards Sync",
        "category": "sync",
        "icon": "dashboard_customize",
        "color": "text-yellow-400",
        "required_context_files": [".context/discovery.md"]
    },
    "sync-notion": {
        "name": "Notion Databases Sync",
        "category": "sync",
        "icon": "sticky_note_2",
        "color": "text-orange-400",
        "required_context_files": [".context/product.md", ".context/decisions.md"]
    },
    "gui-run": {
        "name": "PM Command Center GUI",
        "category": "gui",
        "icon": "open_in_browser",
        "color": "text-amber-500",
        "required_context_files": [".context/harness-config.yaml"]
    }
}

CONTEXT_METADATA = {
    "harness-config.yaml": {
        "title": "Harness Configuration",
        "description": "Defines operating mode (standalone or embedded), deliverable tier, active frameworks, and enabled MCP servers."
    },
    "product.md": {
        "title": "Product Vision, Personas & OKRs",
        "description": "Core product identity, target user personas, primary value loops, North Star metric, and strategic OKRs."
    },
    "discovery.md": {
        "title": "Discovery, Opportunities & Insights",
        "description": "Active outcomes, Opportunity Solution Trees (OST), user interview takeaways, and JTBD insights."
    },
    "strategy-and-constraints.md": {
        "title": "Strategy, Bottlenecks & Constraints",
        "description": "Wardley mapping value chains, Theory of Constraints system bottleneck, and business/technical constraints."
    },
    "architecture.md": {
        "title": "Architecture & Technical Constraints",
        "description": "Tech stack overview, core data models, API boundaries, security constraints, and codebase layout."
    },
    "conventions.md": {
        "title": "Product Conventions & Definition of Ready",
        "description": "Deliverable tier rules (Lean, Standard Agile, Enterprise), Definition of Ready (DoR), and Given/When/Then AC standards."
    },
    "decisions.md": {
        "title": "Product Decision Log (PDR)",
        "description": "Append-only audit trail of strategic product decisions, trade-offs, and rationale."
    }
}

def parse_skill_file(skill_path):
    content = skill_path.read_text(encoding="utf-8")
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    skill_id = skill_path.parent.name
    
    if not frontmatter_match:
        cfg = SKILL_CONFIG.get(skill_id, {})
        return {
            "id": skill_id,
            "name": cfg.get("name", skill_id),
            "category": cfg.get("category", "knowledge"),
            "description": "",
            "required_context_files": cfg.get("required_context_files", []),
            "command_trigger": f"/{skill_id}",
            "icon": cfg.get("icon", "extension"),
            "color": cfg.get("color", "text-zinc-400"),
            "body": content,
            "full_content": content
        }
    
    yaml_text, body = frontmatter_match.groups()
    name_match = re.search(r"^name:\s*(.+)$", yaml_text, re.MULTILINE)
    desc_match = re.search(r"^description:\s*(?:>[-+]?|\|[-+]?)\s*\n(.*?)(?=\n[a-zA-Z0-9_-]+:|\Z)", yaml_text, re.DOTALL | re.MULTILINE)
    if not desc_match:
        desc_match = re.search(r"^description:\s*(.+)$", yaml_text, re.MULTILINE)
        
    cfg = SKILL_CONFIG.get(skill_id, {})
    raw_name = name_match.group(1).strip() if name_match else skill_id
    display_name = cfg.get("name", raw_name)
    category = cfg.get("category", "knowledge")
    desc = desc_match.group(1).strip().replace("\n", " ") if desc_match else ""
    # Clean multiple spaces and strip leading/trailing quotes if any
    desc = re.sub(r"\s+", " ", desc).strip()
    if desc.startswith(('"', "'")) and desc.endswith(('"', "'")):
        desc = desc[1:-1]
    
    return {
        "id": skill_id,
        "name": display_name,
        "category": category,
        "description": desc,
        "required_context_files": cfg.get("required_context_files", []),
        "command_trigger": f"/{skill_id}",
        "icon": cfg.get("icon", "extension"),
        "color": cfg.get("color", "text-zinc-400"),
        "body": body.strip(),
        "full_content": content
    }

def parse_frameworks():
    frameworks = []
    if not FRAMEWORKS_DIR.exists():
        return frameworks
    for fw_path in sorted(FRAMEWORKS_DIR.glob("*/*.md")):
        if fw_path.name == "README.md":
            continue
        content = fw_path.read_text(encoding="utf-8")
        fid = fw_path.stem
        category = fw_path.parent.name  # strategy | discovery | prioritization
        
        # Parse title from H1
        title_match = re.search(r"^#\s*(?:[^\w\s]+\s*)?(?:[A-Za-z]+\s+Framework:\s*)?(.+)$", content, re.MULTILINE)
        name = title_match.group(1).strip() if title_match else fid.replace("-", " ").title()
        
        # Parse description from Primary Purpose or Theoretical Foundation
        desc_match = re.search(r"###\s*Primary Purpose\s*\n+(.+?)(?=\n\n|\n###|\Z)", content, re.DOTALL)
        if not desc_match:
            desc_match = re.search(r"###\s*Theoretical Foundation\s*\n+(.+?)(?=\n\n|\n###|\Z)", content, re.DOTALL)
        desc = desc_match.group(1).strip().replace("\n", " ") if desc_match else f"{name} framework."
        desc = re.sub(r"\s+", " ", desc)
        
        frameworks.append({
            "id": fid,
            "name": name,
            "category": category,
            "description": desc,
            "path": str(fw_path.relative_to(ROOT_DIR))
        })
    return frameworks

def parse_context_files():
    context_files = []
    if not CONTEXT_DIR.exists():
        return context_files
    for ctx_path in sorted(CONTEXT_DIR.glob("*")):
        if ctx_path.name.startswith("."):
            continue
        fname = ctx_path.name
        meta = CONTEXT_METADATA.get(fname, {})
        title = meta.get("title")
        desc = meta.get("description")
        
        content = ctx_path.read_text(encoding="utf-8")
        if not title:
            t_match = re.search(r"^#\s*(?:[^\w\s]+\s*)?(?:Product Knowledge Core\s*—\s*)?([^\n\(]+)", content, re.MULTILINE)
            title = t_match.group(1).strip() if t_match else fname
        if not desc:
            d_match = re.search(r"^#[^\n]+\n\n([^\n#]+)", content)
            desc = d_match.group(1).strip().replace("\n", " ") if d_match else f"Context file {fname}"
        desc = re.sub(r"\s+", " ", desc)
            
        context_files.append({
            "filename": fname,
            "title": title,
            "description": desc
        })
    return context_files

def export_to_agy(skills):
    target_dir = ROOT_DIR / ".agents" / "skills"
    target_dir.mkdir(parents=True, exist_ok=True)
    for s in skills:
        skill_folder = target_dir / s["id"]
        skill_folder.mkdir(parents=True, exist_ok=True)
        (skill_folder / "SKILL.md").write_text(s["full_content"], encoding="utf-8")
    print(f"✅ Exported {len(skills)} skills to AGY native folder: {target_dir}")

def export_to_cursor(skills):
    target_dir = ROOT_DIR / ".cursor" / "rules"
    target_dir.mkdir(parents=True, exist_ok=True)
    for s in skills:
        mdc_content = f"""---
description: {s['description']}
globs: "*"
---
{s['body']}
"""
        (target_dir / f"{s['id']}.mdc").write_text(mdc_content, encoding="utf-8")
    print(f"✅ Exported {len(skills)} rules to Cursor rules folder: {target_dir}")

def export_to_claude(skills):
    target_dir = ROOT_DIR / ".claude" / "commands"
    target_dir.mkdir(parents=True, exist_ok=True)
    for s in skills:
        cmd_content = f"# Command: /{s['id']}\n\n{s['description']}\n\n{s['body']}"
        (target_dir / f"{s['id']}.md").write_text(cmd_content, encoding="utf-8")
    print(f"✅ Exported {len(skills)} commands to Claude folder: {target_dir}")

def export_bundle(skills, frameworks):
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    bundle_path = DIST_DIR / "pm_sidekick_system_prompt.md"
    bundle_text = "# 🚀 AI PM Sidekick — System Prompt & Skill Bundle\n\n"
    bundle_text += "This bundle contains all AI PM Sidekick skills and modular frameworks for use as a Custom GPT or Claude Project system prompt.\n\n"
    
    bundle_text += "## 🧭 Operational Directives\n"
    bundle_text += "1. **Context Hydration First**: Ingest `.context/` before drafting deliverables.\n"
    bundle_text += "2. **Strict Asset Separation**: Never confuse internal `ui/specs/` with user product deliverables in `docs/` or `mockups/`.\n"
    bundle_text += "3. **Socratic Clarifying Gate**: Pause and ask 2–4 targeted questions when requirements are ambiguous.\n"
    bundle_text += "4. **Knowledge Compounding**: Propose updates to `.context/*.md` and append to `.context/decisions.md`.\n\n"
    bundle_text += "---\n\n"
    
    bundle_text += "# 🛠️ Core Skills Catalog\n\n"
    for s in skills:
        bundle_text += f"## Skill: {s['id']} ({s['name']})\n"
        bundle_text += f"- **Category**: `{s['category']}`\n"
        bundle_text += f"- **Trigger**: `{s['command_trigger']}`\n"
        bundle_text += f"- **Description**: {s['description']}\n"
        bundle_text += f"- **Required Context**: {', '.join(s['required_context_files'])}\n\n"
        bundle_text += f"{s['body']}\n\n---\n\n"
        
    bundle_text += "# 🗺️ Modular Strategic, Discovery & Prioritization Frameworks\n\n"
    for fw in frameworks:
        bundle_text += f"## Framework: {fw['name']} (`{fw['id']}`)\n"
        bundle_text += f"- **Category**: `{fw['category']}`\n"
        bundle_text += f"- **Path**: `{fw['path']}`\n"
        bundle_text += f"- **Primary Purpose**: {fw['description']}\n\n"
        
    bundle_path.write_text(bundle_text, encoding="utf-8")
    print(f"✅ Exported single prompt bundle: {bundle_path}")

def export_root_routers():
    """Generates .cursorrules, .agents/project-harness/SKILL.md, and CLAUDE.md."""
    
    # 1. Cursor Global Rules (.cursorrules)
    cursorrules_path = ROOT_DIR / ".cursorrules"
    cursorrules_content = """# AI PM Sidekick — Global Workspace Instructions & Harness Router

You are **AI PM Sidekick**, an expert AI partner for Product Managers, Technical PMs, and Engineering Leaders.
You operate natively within this workspace using the `.context/` Product Knowledge Core, modular strategic frameworks, and strict architectural isolation.

---

## 🧭 1. Mandatory 4-Stage Execution Protocol

For any deliverable generation, refinement, or strategic analysis, execute in 4 strict stages:

### Stage 1: Context Hydration First
Before generating or modifying any product artifact:
1. Read `.context/harness-config.yaml` to determine operating mode (`standalone` vs `embedded`) and deliverable tier (`lean`, `standard`, `enterprise`).
2. Read `.context/product.md` and `.context/conventions.md`.
3. Ingest domain-specific context:
   - For Discovery & Brainstorms: `.context/discovery.md`
   - For Strategy, Bottlenecks & Constraints: `.context/strategy-and-constraints.md`
   - For Architecture, Data Models & Tech Stacks: `.context/architecture.md`
   - For Historical Product Decisions: `.context/decisions.md`
4. In `embedded` mode, inspect repository manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.) and directory layouts.

### Stage 2: Socratic Clarifying Gate
Before generating full specifications:
- Evaluate whether required inputs are missing, ambiguous, or contradictory.
- If critical gaps exist, **STOP and ask 2 to 4 sharp, concrete clarifying questions** before generating the full document.
- If the user explicitly asks to proceed with assumptions, proceed immediately and explicitly document all working assumptions in a dedicated callout block.

### Stage 3: Grounded Generation
- Produce deliverables matching the active tier (`lean` for MVPs, `standard` for Agile squads, `enterprise` for compliance and scale).
- Apply relevant frameworks from `frameworks/` (e.g., Wardley Mapping, Theory of Constraints, OST, JTBD, RICE, WSJF, Kano).
- Adhere to Given/When/Then Gherkin acceptance criteria and INVEST guidelines for user stories.

### Stage 4: Knowledge Compounding (Write-Back)
- After completing work, identify new product truths, user insights, validated/invalidated hypotheses, or architectural constraints.
- Propose concise updates to `.context/*.md` files and append significant decisions to `.context/decisions.md`.

---

## 🚫 2. Absolute Separation of Concerns (Zero Context Contamination)

- **Internal Sidekick UI Specs (`ui/specs/`) and Views (`ui/views/`)**:
  - `ui/specs/` contains specifications for the Sidekick's own GUI (e.g., `PM_COMMAND_CENTER_PRD.md`, `sidepanel_*.md`).
  - `ui/views/` and `ui/stitch/` contain the Sidekick web application frontend screens.
  - **NEVER** confuse these files with the user's product specifications.
  - **NEVER** overwrite, mix, or reference Sidekick UI specs as the user's product context.
- **User Product Artifacts (`docs/` and `mockups/`)**:
  - All PRDs, user stories, technical specs, and product documentation created for the user's product MUST be saved in `docs/`.
  - All interactive HTML prototypes and wireframes created for the user's product MUST be saved in `mockups/`.

---

## ⚡ 3. Skills and Slash Commands Directory

- `/create-prd`: Generates PRDs across Lean, Standard Agile, and Enterprise tiers.
- `/create-user-stories`: Breaks down features into INVEST stories with Gherkin BDD.
- `/refine-user-stories`: Grooms stories, applies SPIDR splitting, and scores readiness.
- `/create-mockup`: Builds self-contained Tailwind HTML wireframes and prototypes.
- `/create-design-brief`: Produces UI/UX briefs with user flows and WCAG guidelines.
- `/create-documentation`: Generates API schemas, Mermaid diagrams, and user manuals.
- `/brainstorm`: Structured feature ideation with SCAMPER, HMW, and 6 Hats.
- `/validate-idea`: Idea validation via Strategyzer 4-Risk, Mom Test, and Pre-mortem.
- `/apply-framework`: Runs frameworks from `frameworks/` over ideas or PRDs.
- `/ingest-context`: Ingests unstructured notes/transcripts and updates `.context/`.
- `/connect-mcp`: Configures MCP integrations for Jira, Confluence, GitHub, Figma, Miro, Notion.
- `/sync-jira`: Syncs epics and user stories directly to Jira.
- `/sync-confluence`: Publishes PRDs and specs to Confluence spaces.
- `/sync-github-issues`: Bi-directionally syncs GitHub Issues and milestones.
- `/sync-figma`: Reads Figma designs and attaches specs to Figma canvas nodes.
- `/sync-miro`: Exports brainstorms and roadmaps to Miro visual boards.
- `/sync-notion`: Bi-directionally syncs Notion databases and wikis.
- `/gui-run`: Launches the PM Command Center local GUI on port 3000.

---

## 🛠️ 4. Tool & Script Guidelines

- **Python Scripts**: All helper scripts in `scripts/` use Python standard library only. Do not introduce external pip dependencies.
- **Manifest**: Consult `dist/harness-manifest.json` for live machine-readable metadata on all skills, frameworks, and context files.
"""
    cursorrules_path.write_text(cursorrules_content.strip() + "\n", encoding="utf-8")
    print(f"✅ Generated root Cursor instructions: {cursorrules_path}")

    # 2. AGY Project Harness Skill (.agents/project-harness/SKILL.md)
    agy_harness_dir = ROOT_DIR / ".agents" / "project-harness"
    agy_harness_dir.mkdir(parents=True, exist_ok=True)
    agy_harness_path = agy_harness_dir / "SKILL.md"
    agy_harness_content = """---
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
"""
    agy_harness_path.write_text(agy_harness_content.strip() + "\n", encoding="utf-8")
    
    # Also link or duplicate into .agents/skills/project-harness/SKILL.md for AGY skill discovery
    agy_skill_harness = ROOT_DIR / ".agents" / "skills" / "project-harness"
    agy_skill_harness.mkdir(parents=True, exist_ok=True)
    (agy_skill_harness / "SKILL.md").write_text(agy_harness_content.strip() + "\n", encoding="utf-8")
    print(f"✅ Generated AGY project harness router: {agy_harness_path}")

    # 3. Claude Code Guide (CLAUDE.md)
    claude_md_path = ROOT_DIR / "CLAUDE.md"
    claude_md_content = """# AI PM Sidekick — Claude Code Workspace Guide

Welcome to **AI PM Sidekick**, a local-first product management command center and AI harness.

## 🧭 Core Workflow & The 4-Stage Protocol

When assisting product managers, technical PMs, or engineering leads, always follow this protocol:

1. **Stage 1: Context Hydration**
   - Check `.context/harness-config.yaml` to know the workspace mode (`standalone` vs `embedded`) and deliverable tier (`lean`, `standard`, `enterprise`).
   - Hydrate core knowledge from `.context/product.md`, `.context/conventions.md`, `.context/discovery.md`, `.context/strategy-and-constraints.md`, and `.context/architecture.md`.
   - In `embedded` mode, check repository package manifests and structure.

2. **Stage 2: Socratic Clarifying Gate**
   - Identify ambiguities or missing requirements in the user's prompt.
   - If critical information is absent, pause and ask 2–4 concise questions before drafting.
   - If the user instructs to proceed with assumptions, explicitly document those assumptions in the output.

3. **Stage 3: Grounded Generation**
   - Use the appropriate template from `templates/` and tier conventions from `.context/conventions.md`.
   - Reference frameworks in `frameworks/` (Wardley mapping, Theory of Constraints, OST, JTBD, RICE, WSJF, Kano).
   - Ensure user stories meet INVEST criteria and Given/When/Then Gherkin acceptance criteria.

4. **Stage 4: Knowledge Compounding (Write-Back)**
   - Offer to record new product discoveries, technical facts, and validated assumptions in `.context/*.md`.
   - Append major product decisions to `.context/decisions.md`.

## 🚫 Critical Guardrail: Zero Context Contamination

- **Internal UI vs User Product**:
  - `ui/specs/` and `ui/views/` are internal assets for the Sidekick's own web UI. **DO NOT** read them as product requirements for the user's product.
  - All user-facing PRDs, stories, and technical specs belong in `docs/`.
  - All user-facing UI wireframes and HTML mockups belong in `mockups/`.

## ⚡ Slash Commands & Skills

| Command | Purpose |
|---------|---------|
| `/create-prd` | Generate PRD (Lean, Standard, or Enterprise) |
| `/create-user-stories` | Break down features into INVEST stories + Gherkin AC |
| `/refine-user-stories` | Groom stories, SPIDR split, readiness score |
| `/create-mockup` | Interactive Tailwind HTML wireframe |
| `/create-design-brief` | UI/UX design brief with WCAG guidelines |
| `/create-documentation` | OpenAPI specs, Mermaid diagrams, user guides |
| `/brainstorm` | SCAMPER, HMW, 6 Hats feature ideation |
| `/validate-idea` | Strategyzer 4-Risk & Mom Test validation |
| `/apply-framework` | Execute framework from `frameworks/` |
| `/ingest-context` | Ingest notes/interviews into `.context/` |
| `/connect-mcp` | Configure Jira, Confluence, GitHub, Figma, Miro, Notion |
| `/sync-jira` | Export stories and epics to Jira |
| `/sync-confluence` | Publish docs to Confluence spaces |
| `/sync-github-issues` | Bi-directionally sync GitHub Issues and milestones |
| `/sync-figma` | Inspect designs and push specs to Figma |
| `/sync-miro` | Export brainstorms and roadmaps to Miro |
| `/sync-notion` | Bi-directionally sync Notion databases and wikis |
| `/gui-run` | Launch PM Command Center GUI on port 3000 |

## 📦 Architecture & Conventions

- **Python Scripts**: Standard library only (Python 3.10+). No external dependencies.
- **Manifest**: Live metadata is in `dist/harness-manifest.json`.
- **Frameworks**: Located in `frameworks/strategy/`, `frameworks/discovery/`, and `frameworks/prioritization/`.
"""
    claude_md_path.write_text(claude_md_content.strip() + "\n", encoding="utf-8")
    print(f"✅ Generated Claude Code guide: {claude_md_path}")

def export_manifest(skills, frameworks, context_files):
    """Generates dist/harness-manifest.json."""
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = DIST_DIR / "harness-manifest.json"
    
    # Clean skills list for manifest schema
    manifest_skills = []
    for s in skills:
        manifest_skills.append({
            "id": s["id"],
            "name": s["name"],
            "category": s["category"],
            "description": s["description"],
            "required_context_files": s["required_context_files"],
            "command_trigger": s["command_trigger"],
            "icon": s["icon"],
            "color": s["color"]
        })
        
    manifest_data = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "version": "1.0.0",
        "generated_at": datetime.now().isoformat(),
        "skills": manifest_skills,
        "frameworks": frameworks,
        "context_files": context_files
    }
    
    manifest_path.write_text(json.dumps(manifest_data, indent=2) + "\n", encoding="utf-8")
    print(f"✅ Generated harness manifest: {manifest_path} (18 skills, {len(frameworks)} frameworks, {len(context_files)} context files)")

def main():
    if not SKILLS_DIR.exists():
        print(f"Error: Skills directory not found at {SKILLS_DIR}")
        return
    
    skills = []
    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skills.append(parse_skill_file(skill_file))
        
    frameworks = parse_frameworks()
    context_files = parse_context_files()
    
    print(f"Found {len(skills)} canonical skills, {len(frameworks)} frameworks, and {len(context_files)} context files.")
    export_to_agy(skills)
    export_to_cursor(skills)
    export_to_claude(skills)
    export_bundle(skills, frameworks)
    export_root_routers()
    export_manifest(skills, frameworks, context_files)
    print("\n🎉 All skill exports and harness generation completed successfully!")

if __name__ == "__main__":
    main()
