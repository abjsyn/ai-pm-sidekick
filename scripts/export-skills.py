#!/usr/bin/env python3
"""
AI PM Sidekick — Cross-Tool Skill & Framework Exporter + Harness Manifest Generator

Compiles canonical skills (`skills/`) and modular frameworks (`frameworks/`) into:
  - AGY Native Skills (`.agents/skills/`) & Root Harness (`.agents/skills/project-harness/SKILL.md`)
  - Cursor Rules (`.cursor/rules/*.mdc`) & Root Instructions (`.cursorrules`)
  - Claude Code Commands (`.claude/commands/*.md`) & Workspace Guide (`CLAUDE.md`)
  - Universal Prompt Bundle (`dist/pm_sidekick_system_prompt.md`)
  - Machine-Readable Harness Manifest (`dist/harness-manifest.json`)
"""

import os
import shutil
import re
import json
import subprocess
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).parent.parent.resolve()
SKILLS_DIR = ROOT_DIR / "skills"
FRAMEWORKS_DIR = ROOT_DIR / "frameworks"
CONTEXT_DIR = ROOT_DIR / ".context"
TEMPLATES_DIR = ROOT_DIR / "templates"
DIST_DIR = ROOT_DIR / "dist"

def get_git_version():
    """Extracts published version tag from git, falling back to git describe or v0.1.0."""
    try:
        res = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            cwd=str(ROOT_DIR),
            capture_output=True,
            text=True,
            check=True
        )
        tag = res.stdout.strip()
        if tag:
            return tag
    except Exception:
        pass
    try:
        res = subprocess.run(
            ["git", "describe", "--tags", "--always"],
            cwd=str(ROOT_DIR),
            capture_output=True,
            text=True,
            check=True
        )
        tag = res.stdout.strip()
        if tag:
            return tag
    except Exception:
        pass
    return "v0.1.0"

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
    "recommend-framework": {
        "name": "Framework Dispatcher",
        "category": "knowledge",
        "icon": "auto_awesome",
        "color": "text-emerald-400",
        "required_context_files": [".context/harness-config.yaml", ".context/product.md"]
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
        "required_context_files": [".context/product.md", ".context/conventions.md", ".context/harness-config.yaml"]
    },
    "sync-confluence": {
        "name": "Confluence Wiki Sync",
        "category": "sync",
        "icon": "library_books",
        "color": "text-blue-400",
        "required_context_files": [".context/product.md", ".context/conventions.md", ".context/harness-config.yaml"]
    },
    "sync-github-issues": {
        "name": "GitHub Issues Sync",
        "category": "sync",
        "icon": "code",
        "color": "text-zinc-200",
        "required_context_files": [".context/product.md", ".context/conventions.md", ".context/harness-config.yaml"]
    },
    "sync-figma": {
        "name": "Figma Specs Sync",
        "category": "sync",
        "icon": "design_services",
        "color": "text-violet-400",
        "required_context_files": [".context/product.md", ".context/conventions.md", ".context/harness-config.yaml"]
    },
    "sync-miro": {
        "name": "Miro Whiteboards Sync",
        "category": "sync",
        "icon": "dashboard_customize",
        "color": "text-yellow-400",
        "required_context_files": [".context/product.md", ".context/conventions.md", ".context/harness-config.yaml"]
    },
    "sync-notion": {
        "name": "Notion Databases Sync",
        "category": "sync",
        "icon": "sticky_note_2",
        "color": "text-orange-400",
        "required_context_files": [".context/product.md", ".context/conventions.md", ".context/harness-config.yaml"]
    },
    "gui-run": {
        "name": "PM Command Center GUI",
        "category": "gui",
        "icon": "open_in_browser",
        "color": "text-amber-500",
        "required_context_files": [".context/harness-config.yaml"]
    },
    "create-stakeholder-update": {
        "name": "Stakeholder Update & Release Notes",
        "category": "communication",
        "icon": "campaign",
        "color": "text-sky-400",
        "required_context_files": [".context/product.md", ".context/decisions.md"]
    },
    "prepare-user-interview": {
        "name": "User Interview Script & Guide",
        "category": "discovery",
        "icon": "record_voice_over",
        "color": "text-teal-400",
        "required_context_files": [".context/product.md", ".context/discovery.md"]
    },
    "define-metrics-and-experiment": {
        "name": "Metrics & Experiment Plan",
        "category": "specification",
        "icon": "query_stats",
        "color": "text-emerald-400",
        "required_context_files": [".context/product.md", ".context/strategy-and-constraints.md", ".context/architecture.md"]
    },
    "audit-spec": {
        "name": "Spec Auditor & Pre-Mortem Critique",
        "category": "specification",
        "icon": "fact_check",
        "color": "text-rose-400",
        "required_context_files": [".context/product.md", ".context/architecture.md", ".context/strategy-and-constraints.md", ".context/conventions.md"]
    },
    "plan-launch": {
        "name": "GTM Launch Plan",
        "category": "operations",
        "icon": "rocket_launch",
        "color": "text-amber-500",
        "required_context_files": [".context/product.md", ".context/strategy-and-constraints.md"]
    },
    "create-roadmap": {
        "name": "Outcome Roadmap Generator",
        "category": "strategy",
        "icon": "timeline",
        "color": "text-indigo-400",
        "required_context_files": [".context/product.md", ".context/discovery.md", ".context/strategy-and-constraints.md"]
    },
    "prep-meeting": {
        "name": "Meeting Prep & Defense Brief",
        "category": "communication",
        "icon": "forum",
        "color": "text-blue-400",
        "required_context_files": [".context/product.md", ".context/decisions.md", ".context/strategy-and-constraints.md"]
    },
    "analyze-competitor": {
        "name": "Competitor Analysis & Battlecard",
        "category": "strategy",
        "icon": "compare_arrows",
        "color": "text-purple-400",
        "required_context_files": [".context/product.md", ".context/strategy-and-constraints.md"]
    },
    "sync-linear": {
        "name": "Linear Issues & Cycles Sync",
        "category": "sync",
        "icon": "sync_alt",
        "color": "text-violet-400",
        "required_context_files": [".context/product.md", ".context/conventions.md", ".context/harness-config.yaml"]
    },
    "triage-feedback": {
        "name": "Customer Feedback Triage",
        "category": "discovery",
        "icon": "mark_email_unread",
        "color": "text-yellow-400",
        "required_context_files": [".context/product.md", ".context/discovery.md"]
    },
    "evaluate-launch": {
        "name": "Post-Launch Retrospective",
        "category": "operations",
        "icon": "published_with_changes",
        "color": "text-cyan-400",
        "required_context_files": [".context/product.md", ".context/decisions.md"]
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

def parse_yaml_frontmatter(text):
    """Parses simple YAML frontmatter without external dependencies."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    yaml_text, body = match.groups()
    data = {}
    current_key = None
    
    for line in yaml_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        list_match = re.match(r"^\s*-\s*(.+)$", line)
        if list_match and current_key:
            val = list_match.group(1).strip()
            if val.startswith(('"', "'")) and val.endswith(('"', "'")) and len(val) >= 2:
                val = val[1:-1]
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(val)
            continue
            
        kv_match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", line)
        if kv_match:
            current_key = kv_match.group(1).strip()
            val = kv_match.group(2).strip()
            if val:
                if val.startswith("[") and val.endswith("]"):
                    items = [x.strip().strip("'\"") for x in val[1:-1].split(",") if x.strip()]
                    data[current_key] = items
                else:
                    if val.startswith(('"', "'")) and val.endswith(('"', "'")) and len(val) >= 2:
                        val = val[1:-1]
                    data[current_key] = val
            else:
                data[current_key] = []
                
    return data, body

def parse_frameworks():
    frameworks = []
    if not FRAMEWORKS_DIR.exists():
        return frameworks
    for fw_path in sorted(FRAMEWORKS_DIR.glob("*/*.md")):
        if fw_path.name == "README.md":
            continue
        content = fw_path.read_text(encoding="utf-8")
        fid = fw_path.stem
        category = fw_path.parent.name
        
        fm, body = parse_yaml_frontmatter(content)
        
        name = fm.get("name")
        if not name:
            title_match = re.search(r"^#\s*(?:[^\w\s]+\s*)?(?:[A-Za-z]+\s+Framework:\s*)?(.+)$", body, re.MULTILINE)
            name = title_match.group(1).strip() if title_match else fid.replace("-", " ").title()
            
        desc_match = re.search(r"###\s*Primary Purpose\s*\n+(.+?)(?=\n\n|\n###|\Z)", body, re.DOTALL)
        if not desc_match:
            desc_match = re.search(r"###\s*Theoretical Foundation\s*\n+(.+?)(?=\n\n|\n###|\Z)", body, re.DOTALL)
        desc = desc_match.group(1).strip().replace("\n", " ") if desc_match else f"{name} framework."
        desc = re.sub(r"\s+", " ", desc)
        
        frameworks.append({
            "id": fm.get("id", fid),
            "name": name,
            "category": fm.get("category", category),
            "description": desc,
            "problem_signatures": fm.get("problem_signatures", []),
            "best_for_stage": fm.get("best_for_stage", []),
            "data_maturity_required": fm.get("data_maturity_required", "medium"),
            "when_not_to_use": fm.get("when_not_to_use", []),
            "paired_skills": fm.get("paired_skills", []),
            "write_back_target": fm.get("write_back_target", ".context/product.md"),
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

def export_root_routers(skills, frameworks):
    """Generates .cursorrules, .agents/skills/project-harness/SKILL.md, and CLAUDE.md dynamically."""
    
    # Partition frameworks into the 4 standard categories
    frameworks_by_cat = {
        "strategy": [],
        "discovery": [],
        "prioritization": [],
        "operations": []
    }
    for fw in frameworks:
        cat = fw.get("category", "strategy")
        if cat in frameworks_by_cat:
            frameworks_by_cat[cat].append(fw)
        else:
            frameworks_by_cat[cat] = [fw]

    def format_agy_fw_section(fw_list):
        if not fw_list:
            return "_None configured._\n"
        lines = []
        for fw in fw_list:
            desc = fw.get("description", "")
            stages = ", ".join(fw.get("best_for_stage", []))
            maturity = fw.get("data_maturity_required", "medium")
            wb = fw.get("write_back_target", ".context/product.md")
            sigs = "; ".join(fw.get("problem_signatures", [])[:2])
            lines.append(f"- **{fw['name']}** (`{fw['id']}`): {desc}")
            lines.append(f"  - *Target*: `{wb}` | *Data Maturity*: `{maturity}` | *Stages*: `{stages}`")
            if sigs:
                lines.append(f"  - *Solves*: {sigs}")
        return "\n".join(lines)

    def format_cursor_fw_section(fw_list):
        if not fw_list:
            return "  - _None configured._"
        return "\n".join([f"  - `{fw['id']}`: {fw['name']} — {fw['description']}" for fw in fw_list])

    def format_claude_fw_section(fw_list):
        if not fw_list:
            return "- _None configured._"
        return "\n".join([f"- **{fw['name']}** (`{fw['id']}`): {fw['description']}" for fw in fw_list])

    # 1. Cursor Global Rules (.cursorrules)
    cursorrules_path = ROOT_DIR / ".cursorrules"
    cursor_skills_lines = "\n".join([f"- `{s['command_trigger']}`: {s['description']}" for s in skills])
    cursorrules_content = f"""# AI PM Sidekick — Global Workspace Instructions & Harness Router

You are **AI PM Sidekick**, an expert AI partner for Product Managers, Technical PMs, and Engineering Leaders.
You operate natively within this workspace using the `.context/` Product Knowledge Core, modular strategic frameworks, and strict architectural isolation.

---

## 🧭 1. Mandatory 4-Stage Execution Protocol

For any deliverable generation, refinement, or strategic analysis, execute in 4 strict stages:

### Stage 1: Context Hydration First
Before generating or modifying any product artifact:
1. Read `.context/harness-config.yaml` to determine operating mode (`standalone` vs `embedded`), deliverable tier (`lean`, `standard`, `enterprise`), and delivery operating model (`scrum`, `shape-up`, `kanban`, `gist`).
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
- Apply relevant frameworks from `frameworks/` or diagnose bottlenecks with `/recommend-framework`.
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

## ⚡ 3. Skills and Slash Commands Directory ({len(skills)} Skills)

{cursor_skills_lines}

---

## 🗺️ 4. Modular Frameworks ({len(frameworks)} Frameworks across 4 Categories)

Frameworks are located in `frameworks/` and invoked via `/apply-framework <id>` or diagnosed via `/recommend-framework`:

- **Strategy**:
{format_cursor_fw_section(frameworks_by_cat['strategy'])}
- **Discovery**:
{format_cursor_fw_section(frameworks_by_cat['discovery'])}
- **Prioritization**:
{format_cursor_fw_section(frameworks_by_cat['prioritization'])}
- **Operations & Delivery**:
{format_cursor_fw_section(frameworks_by_cat['operations'])}

---

## 🔄 5. Delivery Operating Models (`operating_model`)

Configured via `operating_model` in `.context/harness-config.yaml`:
- `scrum`: 1–2 week sprints, INVEST stories, Fibonacci points, DoD sign-off (Default)
- `shape-up`: 6-week cycles, shaped pitches, appetite budgeting, hill charts, circuit breaker
- `kanban`: Continuous pull flow, WIP limits, cycle-time optimization
- `gist`: Goals, Ideas (ICE scored), Step-projects (<= 2 wks), Tasks for high-uncertainty planning

---

## 🛠️ 6. Tool & Script Guidelines

- **Python Scripts**: All helper scripts in `scripts/` use Python standard library only. Do not introduce external pip dependencies.
- **Manifest**: Consult `dist/harness-manifest.json` for live machine-readable metadata on all skills, frameworks, and context files.
"""
    cursorrules_path.write_text(cursorrules_content.strip() + "\n", encoding="utf-8")
    print(f"✅ Generated root Cursor instructions: {cursorrules_path}")

    # 2. AGY Project Harness Skill (.agents/skills/project-harness/SKILL.md)
    agy_skill_harness = ROOT_DIR / ".agents" / "skills" / "project-harness"
    agy_skill_harness.mkdir(parents=True, exist_ok=True)
    agy_harness_path = agy_skill_harness / "SKILL.md"
    
    skills_table_rows = []
    for s in skills:
        skills_table_rows.append(f"| `{s['command_trigger']}` | **{s['name']}** | `{s['category']}` | {s['description']} |")
    skills_table_md = "\n".join(skills_table_rows)

    agy_harness_content = f"""---
name: project-harness
description: >-
  Core AI PM Sidekick operational router. Hydrates product context from .context/, enforces strict separation between internal UI and user deliverables, applies Socratic inquiry, and compounds knowledge.
---

# 🚀 AI PM Sidekick — Project Harness Router

This is the primary harness router skill for the AI PM Sidekick. It governs how agentic models interact with the workspace, consult product context, and generate production-grade PM deliverables.

## 🧭 1. Operating Principles & 4-Stage Execution Protocol

For any deliverable generation, refinement, or strategic analysis, execute in 4 strict stages:

1. **Stage 1: Context Hydration First**: Always read relevant files from `.context/` before initiating work:
   - Configuration & Operating Model: `.context/harness-config.yaml` (reads `mode`, `default_tier`, and `operating_model`)
   - Conventions & Standards: `.context/conventions.md` (DoR, DoD, Gherkin BDD, and Operating Model cadences)
   - Vision & Personas: `.context/product.md`
   - Discovery & Outcomes: `.context/discovery.md`
   - Strategy & Bottlenecks: `.context/strategy-and-constraints.md`
   - Architecture & Schemas: `.context/architecture.md` (plus repo package manifests in embedded mode)
   - Decision Log: `.context/decisions.md`

2. **Absolute Separation of Concerns (Zero Context Contamination)**:
   - `ui/specs/`, `ui/views/`, and `ui/stitch/` are strictly internal Sidekick web application assets. Never treat them as user product documentation.
   - User PRDs, specs, user stories, and technical documentation MUST be created in `docs/`.
   - User HTML prototypes, wireframes, and mockups MUST be created in `mockups/`.

3. **Stage 2: Socratic Clarifying Gate**:
   - Never hallucinate critical business constraints, user pain points, or architecture.
   - If user requirements lack necessary context for the requested deliverable tier, pause and ask 2–4 targeted clarifying questions.
   - If the user prefers fast iteration, document explicit working assumptions in the output.

4. **Stage 3: Grounded Generation**:
   - Produce deliverables matching the active tier (`lean` for MVPs, `standard` for Agile squads, `enterprise` for compliance and scale).
   - Apply relevant frameworks from `frameworks/` or use `/recommend-framework` to diagnose bottlenecks.
   - Adhere to Given/When/Then Gherkin acceptance criteria and INVEST guidelines for user stories.

5. **Stage 4: Knowledge Compounding (Write-Back)**:
   - When a session yields validated assumptions, architectural decisions, or user insights, propose updating the `.context/*.md` files and logging decisions in `.context/decisions.md`.

---

## ⚡ 2. Active Skills Catalog ({len(skills)} Skills)

| Command / Trigger | Skill Name | Category | Primary Purpose |
| :--- | :--- | :--- | :--- |
{skills_table_md}

---

## 🗺️ 3. Modular Product Frameworks ({len(frameworks)} Frameworks across 4 Categories)

Frameworks are organized into 4 strategic categories and invoked via `/apply-framework <id>` or diagnosed via `/recommend-framework`:

### 📈 Strategy Frameworks
{format_agy_fw_section(frameworks_by_cat['strategy'])}

### 🔍 Discovery Frameworks
{format_agy_fw_section(frameworks_by_cat['discovery'])}

### ⚖️ Prioritization Frameworks
{format_agy_fw_section(frameworks_by_cat['prioritization'])}

### 🚀 Operations & Delivery Frameworks
{format_agy_fw_section(frameworks_by_cat['operations'])}

---

## 🔄 4. Delivery Operating Models (`operating_model`)

Configured via `operating_model` in `.context/harness-config.yaml` and detailed in Section 5 of `.context/conventions.md`:
- **`scrum`** *(Default)*: 1–2 week sprints, INVEST stories, Fibonacci points (<= 5 pts), sprint velocity and DoD sign-off.
- **`shape-up`**: 6-week cycles + 2-week cooldown, shaped pitches, fixed appetite budgeting, hill charts, and circuit breaker.
- **`kanban`**: Continuous pull flow, WIP limits, cycle-time optimization, backlog queue triage.
- **`gist`**: Iterative experiment loops, step-projects (<= 2 weeks), ICE scoring, outcome tracking.

---

## 🛠️ 5. Integration & Tooling Reference

- **Model Context Protocol (MCP)**: Use `/connect-mcp` or tool-specific sync skills (`/sync-jira`, `/sync-confluence`, `/sync-github-issues`, `/sync-linear`, `/sync-figma`, `/sync-miro`, `/sync-notion`).
- **GUI Command Center**: Launch the local visual dashboard on port 3000 via `/gui-run` (`python3 scripts/launch-ui.py --open`).
- **Machine-Readable Manifest**: Consult `dist/harness-manifest.json` for live schema definitions, triggers, and framework metadata.
"""
    agy_harness_path.write_text(agy_harness_content.strip() + "\n", encoding="utf-8")
    print(f"✅ Generated AGY project harness router: {agy_harness_path}")

    # 3. Claude Code Guide (CLAUDE.md)
    claude_md_path = ROOT_DIR / "CLAUDE.md"
    claude_skills_table = "\n".join([f"| `{s['command_trigger']}` | {s['description']} |" for s in skills])
    claude_md_content = f"""# AI PM Sidekick — Claude Code Workspace Guide

Welcome to **AI PM Sidekick**, a local-first product management command center and AI harness.

## 🧭 Core Workflow & The 4-Stage Protocol

When assisting product managers, technical PMs, or engineering leads, always follow this protocol:

1. **Stage 1: Context Hydration**
   - Check `.context/harness-config.yaml` to know the workspace mode (`standalone` vs `embedded`), deliverable tier (`lean`, `standard`, `enterprise`), and delivery operating model (`scrum`, `shape-up`, `kanban`, `gist`).
   - Hydrate core knowledge from `.context/product.md`, `.context/conventions.md`, `.context/discovery.md`, `.context/strategy-and-constraints.md`, and `.context/architecture.md`.
   - In `embedded` mode, check repository package manifests and structure.

2. **Stage 2: Socratic Clarifying Gate**
   - Identify ambiguities or missing requirements in the user's prompt.
   - If critical information is absent, pause and ask 2–4 concise questions before drafting.
   - If the user instructs to proceed with assumptions, explicitly document those assumptions in the output.

3. **Stage 3: Grounded Generation**
   - Use the appropriate template from `templates/` and tier conventions from `.context/conventions.md`.
   - Reference frameworks in `frameworks/` or diagnose via `/recommend-framework`.
   - Ensure user stories meet INVEST criteria and Given/When/Then Gherkin acceptance criteria.

4. **Stage 4: Knowledge Compounding (Write-Back)**
   - Offer to record new product discoveries, technical facts, and validated assumptions in `.context/*.md`.
   - Append major product decisions to `.context/decisions.md`.

## 🚫 Critical Guardrail: Zero Context Contamination

- **Internal UI vs User Product**:
  - `ui/specs/`, `ui/views/`, and `ui/stitch/` are internal assets for the Sidekick's own web UI. **DO NOT** read them as product requirements for the user's product.
  - All user-facing PRDs, stories, and technical specs belong in `docs/`.
  - All user-facing UI wireframes and HTML mockups belong in `mockups/`.

## ⚡ Slash Commands & Skills ({len(skills)} Skills)

| Command | Purpose |
|---------|---------|
{claude_skills_table}

## 🗺️ Modular Product Frameworks ({len(frameworks)} Frameworks across 4 Categories)

Organized across 4 categories in `frameworks/`:
### Strategy
{format_claude_fw_section(frameworks_by_cat['strategy'])}

### Discovery
{format_claude_fw_section(frameworks_by_cat['discovery'])}

### Prioritization
{format_claude_fw_section(frameworks_by_cat['prioritization'])}

### Operations & Delivery
{format_claude_fw_section(frameworks_by_cat['operations'])}

## 🔄 Delivery Operating Models (`operating_model`)

Configured via `operating_model` in `.context/harness-config.yaml`:
- `scrum`: Iterative sprints, INVEST user stories, Fibonacci points, DoD sign-off (Default)
- `shape-up`: 6-week cycles, shaped pitches, appetite budgeting, hill charts, circuit breaker
- `kanban`: Continuous pull flow, WIP limits, cycle-time optimization
- `gist`: Goals, Ideas (ICE scored), Step-projects (<= 2 wks), Tasks for high-uncertainty planning

## 📦 Architecture & Conventions

- **Python Scripts**: Standard library only (Python 3.10+). No external dependencies.
- **Manifest**: Live metadata is in `dist/harness-manifest.json`.
- **Frameworks**: Located in `frameworks/strategy/`, `frameworks/discovery/`, `frameworks/prioritization/`, and `frameworks/operations/`.
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
        "version": get_git_version(),
        "generated_at": datetime.now().isoformat(),
        "skills": manifest_skills,
        "frameworks": frameworks,
        "context_files": context_files
    }
    
    manifest_path.write_text(json.dumps(manifest_data, indent=2) + "\n", encoding="utf-8")
    print(f"✅ Generated harness manifest: {manifest_path} ({len(skills)} skills, {len(frameworks)} frameworks, {len(context_files)} context files)")

def validate_all():
    """Validates YAML frontmatter and required sections for all skills and frameworks."""
    print("=" * 70)
    print("🔍 AI PM Sidekick — Diagnostic Schema & Frontmatter Linter")
    print("=" * 70)
    
    errors = []
    
    # 1. Validate Skills in skills/*/SKILL.md
    print("\n📦 Checking Canonical Skills (skills/*/SKILL.md)...")
    if not SKILLS_DIR.exists():
        errors.append(f"Missing skills directory: {SKILLS_DIR}")
    else:
        skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
        if not skill_files:
            errors.append(f"No skill files found in {SKILLS_DIR}")
        for sf in skill_files:
            folder_name = sf.parent.name
            content = sf.read_text(encoding="utf-8")
            fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
            if not fm_match:
                errors.append(f"❌ Skill '{folder_name}' ({sf}): Missing YAML frontmatter enclosed in '---'.")
                continue
            
            yaml_text, body = fm_match.groups()
            name_match = re.search(r"^name:\s*(.+)$", yaml_text, re.MULTILINE)
            desc_match = re.search(r"^description:\s*(?:>[-+]?|\|[-+]?)\s*\n(.*?)(?=\n[a-zA-Z0-9_-]+:|\Z)", yaml_text, re.DOTALL | re.MULTILINE)
            if not desc_match:
                desc_match = re.search(r"^description:\s*(.+)$", yaml_text, re.MULTILINE)
            
            if not name_match or not name_match.group(1).strip():
                errors.append(f"❌ Skill '{folder_name}': Missing or empty 'name' in YAML frontmatter.")
            elif name_match.group(1).strip() != folder_name:
                errors.append(f"⚠️ Skill '{folder_name}': Frontmatter name '{name_match.group(1).strip()}' differs from folder name '{folder_name}'.")
                
            if not desc_match or not desc_match.group(1).strip():
                errors.append(f"❌ Skill '{folder_name}': Missing or empty 'description' in YAML frontmatter.")
                
            if not re.search(r"^#\s+.+", body, re.MULTILINE):
                errors.append(f"❌ Skill '{folder_name}': Missing H1 title in body.")
                
            print(f"  ✓ skill: {folder_name}")

    # 2. Validate Frameworks in frameworks/*/*.md
    print("\n🗺️  Checking Modular Frameworks (frameworks/*/*.md)...")
    valid_categories = {"strategy", "discovery", "prioritization", "operations"}
    valid_maturities = {"low", "medium", "high"}
    required_sections = [
        ("## 1.", "Mental Model & Trigger Conditions"),
        ("## 2.", "Required .context/ Inputs & Socratic Questions"),
        ("## 3.", "Step-by-Step Execution & Scoring Rubric"),
        ("## 4.", "Output Format"),
        ("## 5.", ".context/ Write-Back Target"),
    ]
    
    if not FRAMEWORKS_DIR.exists():
        errors.append(f"Missing frameworks directory: {FRAMEWORKS_DIR}")
    else:
        fw_files = [f for f in sorted(FRAMEWORKS_DIR.glob("*/*.md")) if f.name != "README.md"]
        if not fw_files:
            errors.append(f"No framework files found in {FRAMEWORKS_DIR}")
        for fw in fw_files:
            rel_path = fw.relative_to(ROOT_DIR)
            content = fw.read_text(encoding="utf-8")
            fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
            if not fm_match:
                errors.append(f"❌ Framework {rel_path}: Missing YAML frontmatter enclosed in '---'.")
                continue
                
            fm, body = parse_yaml_frontmatter(content)
            
            if not fm.get("id"):
                errors.append(f"❌ Framework {rel_path}: Missing required frontmatter key 'id'.")
            elif fm.get("id") != fw.stem:
                errors.append(f"❌ Framework {rel_path}: Frontmatter id '{fm.get('id')}' does not match filename stem '{fw.stem}'.")
                
            if not fm.get("name"):
                errors.append(f"❌ Framework {rel_path}: Missing required frontmatter key 'name'.")
                
            cat = fm.get("category")
            if not cat or cat not in valid_categories:
                errors.append(f"❌ Framework {rel_path}: 'category' must be one of {sorted(valid_categories)}, got '{cat}'.")
                
            sigs = fm.get("problem_signatures")
            if not sigs or not isinstance(sigs, list) or len(sigs) < 2:
                errors.append(f"❌ Framework {rel_path}: 'problem_signatures' must be a list with at least 2 items.")
                
            stages = fm.get("best_for_stage")
            if not stages or not isinstance(stages, list) or len(stages) < 1:
                errors.append(f"❌ Framework {rel_path}: 'best_for_stage' must be a non-empty list.")
                
            maturity = fm.get("data_maturity_required")
            if not maturity or maturity not in valid_maturities:
                errors.append(f"❌ Framework {rel_path}: 'data_maturity_required' must be one of {sorted(valid_maturities)}, got '{maturity}'.")
                
            when_not = fm.get("when_not_to_use")
            if not when_not or not isinstance(when_not, list) or len(when_not) < 1:
                errors.append(f"❌ Framework {rel_path}: 'when_not_to_use' must be a non-empty list of anti-patterns.")
                
            skills_p = fm.get("paired_skills")
            if not skills_p or not isinstance(skills_p, list) or len(skills_p) < 1:
                errors.append(f"❌ Framework {rel_path}: 'paired_skills' must be a non-empty list.")
                
            wb = fm.get("write_back_target")
            if not wb or not isinstance(wb, str) or not wb.startswith(".context/"):
                errors.append(f"❌ Framework {rel_path}: 'write_back_target' must point to a file in '.context/' (got '{wb}').")
                
            for prefix, desc in required_sections:
                if prefix not in body:
                    errors.append(f"❌ Framework {rel_path}: Missing standard section '{prefix} {desc}'.")
                    
            print(f"  ✓ framework: {fw.parent.name}/{fw.name} ({fm.get('name', fw.stem)})")

    print("\n" + "-" * 70)
    if errors:
        print(f"❌ Found {len(errors)} validation error(s):")
        for err in errors:
            print(f"  {err}")
        print("-" * 70)
        return False
    else:
        print("✅ PASS: All skills and frameworks strictly conform to diagnostic schemas!")
        print("-" * 70)
        return True

def main():
    import sys
    is_validate_only = "--validate" in sys.argv
    
    # Run validation automatically before export
    success = validate_all()
    if not success:
        print("\n❌ Schema validation failed. Exiting.")
        sys.exit(1)
        
    if is_validate_only:
        print("\n✨ Schema validation completed successfully. All artifacts are compliant.")
        sys.exit(0)

    if not SKILLS_DIR.exists():
        print(f"Error: Skills directory not found at {SKILLS_DIR}")
        sys.exit(1)
    
    skills = []
    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skills.append(parse_skill_file(skill_file))
        
    frameworks = parse_frameworks()
    context_files = parse_context_files()
    
    print(f"\nFound {len(skills)} canonical skills, {len(frameworks)} frameworks, and {len(context_files)} context files.")
    export_to_agy(skills)
    export_to_cursor(skills)
    export_to_claude(skills)
    export_bundle(skills, frameworks)
    export_root_routers(skills, frameworks)
    export_manifest(skills, frameworks, context_files)
    print("\n🎉 All skill exports and harness generation completed successfully!")

if __name__ == "__main__":
    main()
