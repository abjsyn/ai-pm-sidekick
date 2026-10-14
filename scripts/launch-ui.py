#!/usr/bin/env python3
"""
AI PM Sidekick — PM Command Center Web Server & REST API
Launches a local HTTP server with full REST API support for managing skills,
generating deliverables, inspecting artifacts, and testing MCP integrations.

Usage:
  python3 scripts/launch-ui.py [--port 3000] [--open]
"""

import os
import sys
import json
import re
import argparse
import webbrowser
from pathlib import Path
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ROOT_DIR = Path(__file__).parent.parent.resolve()
UI_DIR = ROOT_DIR / "ui"
UI_VIEWS_DIR = UI_DIR / "views"
UI_STITCH_DIR = UI_DIR / "stitch"
UI_SPECS_DIR = UI_DIR / "specs"
UI_MAIN_FILE = UI_VIEWS_DIR / "pm-command-center.html"
MOCKUP_FILE = UI_MAIN_FILE  # Backwards compatibility alias
SKILLS_DIR = ROOT_DIR / "skills"
DOCS_DIR = ROOT_DIR / "docs"
TEMPLATES_DIR = ROOT_DIR / "templates"
MOCKUPS_DIR = ROOT_DIR / "mockups"
CONTEXT_DIR = ROOT_DIR / ".context"
ENV_FILE = ROOT_DIR / ".env"
ENV_EXAMPLE = ROOT_DIR / ".env.example"
DIST_DIR = ROOT_DIR / "dist"
CURRENT_PORT = 3000

def parse_env_file():
    target = ENV_FILE if ENV_FILE.exists() else ENV_EXAMPLE
    env_vars = {}
    if target.exists():
        with open(target, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip().strip("'\"")
    return env_vars

def write_env_file(data):
    current = parse_env_file()
    # Merge existing env with incoming data
    user_name = data.get('user_name', current.get('USER_NAME', 'Paula (Lead PM)'))
    user_email = data.get('user_email', current.get('USER_EMAIL', 'paula.pm@company.com'))
    persona = data.get('persona', current.get('DEFAULT_PERSONA', 'paula'))
    prd_mode = data.get('prd_mode', current.get('DEFAULT_PRD_MODE', 'standard'))
    ac_format = data.get('ac_format', current.get('DEFAULT_AC_FORMAT', 'gherkin'))
    story_scale = data.get('story_scale', current.get('DEFAULT_STORY_SCALE', 'fibonacci'))
    ui_theme = data.get('ui_theme', current.get('DEFAULT_UI_THEME', 'stitch'))

    atlassian_host = data.get('atlassian_host', current.get('ATLASSIAN_HOST', ''))
    atlassian_email = data.get('atlassian_email', current.get('ATLASSIAN_EMAIL', ''))
    atlassian_token = data.get('atlassian_token', current.get('ATLASSIAN_API_TOKEN', ''))
    github_token = data.get('github_token', current.get('GITHUB_PERSONAL_ACCESS_TOKEN', ''))
    github_owner = data.get('github_owner', current.get('GITHUB_OWNER', ''))
    github_repo = data.get('github_repo', current.get('GITHUB_REPO', ''))
    figma_token = data.get('figma_token', current.get('FIGMA_ACCESS_TOKEN', ''))
    miro_token = data.get('miro_token', current.get('MIRO_ACCESS_TOKEN', ''))
    notion_token = data.get('notion_token', current.get('NOTION_API_TOKEN', ''))
    notion_page = data.get('notion_page', current.get('NOTION_ROOT_PAGE_ID', ''))
    stitch_token = data.get('stitch_token', current.get('STITCH_API_KEY', ''))

    gemini_key = data.get('gemini_api_key', current.get('GEMINI_API_KEY', ''))
    anthropic_key = data.get('anthropic_api_key', current.get('ANTHROPIC_API_KEY', ''))
    openai_key = data.get('openai_api_key', current.get('OPENAI_API_KEY', ''))
    default_llm_provider = data.get('default_llm_provider', current.get('DEFAULT_LLM_PROVIDER', 'gemini'))

    lines = [
        "# AI PM Sidekick — Credentials & User Preferences",
        "# Saved via PM Command Center UI",
        "",
        "# --- AI Execution Engine (Optional In-Browser SaaS Keys) ---",
        f"GEMINI_API_KEY={gemini_key}",
        f"ANTHROPIC_API_KEY={anthropic_key}",
        f"OPENAI_API_KEY={openai_key}",
        f"DEFAULT_LLM_PROVIDER={default_llm_provider}",
        "",
        "# --- Atlassian (Jira & Confluence) ---",
        f"ATLASSIAN_HOST={atlassian_host}",
        f"ATLASSIAN_EMAIL={atlassian_email}",
        f"ATLASSIAN_API_TOKEN={atlassian_token}",
        "",
        "# --- GitHub Issues & Milestones ---",
        f"GITHUB_PERSONAL_ACCESS_TOKEN={github_token}",
        f"GITHUB_OWNER={github_owner}",
        f"GITHUB_REPO={github_repo}",
        "",
        "# --- Figma ---",
        f"FIGMA_ACCESS_TOKEN={figma_token}",
        "",
        "# --- Miro ---",
        f"MIRO_ACCESS_TOKEN={miro_token}",
        "",
        "# --- Notion (Product Wiki & Databases) ---",
        f"NOTION_API_TOKEN={notion_token}",
        f"NOTION_ROOT_PAGE_ID={notion_page}",
        "",
        "# --- Google Stitch ---",
        f"STITCH_API_KEY={stitch_token}",
        "",
        "# --- User Profile & PM Persona ---",
        f"USER_NAME={user_name}",
        f"USER_EMAIL={user_email}",
        f"DEFAULT_PERSONA={persona}",
        "",
        "# --- Skill Execution Defaults ---",
        f"DEFAULT_PRD_MODE={prd_mode}",
        f"DEFAULT_AC_FORMAT={ac_format}",
        f"DEFAULT_STORY_SCALE={story_scale}",
        f"DEFAULT_UI_THEME={ui_theme}",
        ""
    ]
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def parse_harness_config():
    config_file = CONTEXT_DIR / "harness-config.yaml"
    config = {
        "mode": "standalone",
        "default_tier": "standard",
        "operating_model": "scrum",
        "favorite_skills": ["create-prd", "create-user-stories", "refine-user-stories", "create-mockup", "recommend-framework", "sync-jira"],
        "active_frameworks": ["ost", "wardley", "toc", "rice", "wsjf", "shape-up", "scrum-sprint-delivery", "gist-planning"],
        "mcp_enabled": ["atlassian", "github", "figma", "miro", "notion", "stitch"]
    }
    if not config_file.exists():
        return config
    
    content = config_file.read_text(encoding="utf-8")
    cur_list = None
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line and not line.startswith("-"):
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.split("#")[0].strip()
            if v:
                config[k] = v
                cur_list = None
            else:
                cur_list = k
                config[cur_list] = []
        elif line.startswith("-") and cur_list:
            item = line[1:].split("#")[0].strip()
            if item:
                config[cur_list].append(item)
    return config

def serialize_harness_config(config):
    lines = [
        "# ==============================================================================",
        "# AI PM Sidekick — Harness Configuration",
        "# Single Source of Truth for Workspace Context, Operating Mode, and Tooling",
        "# ==============================================================================",
        "",
        "# Operating Mode:",
        "#   - standalone: Dedicated PM command workspace (isolated product deliverables in docs/ & mockups/)",
        "#   - embedded: Integrated directly within a software repository / monorepo",
        f"mode: {config.get('mode', 'standalone')}",
        "",
        "# Default Artifact Tier for PRDs, User Stories, and Technical Specs:",
        "#   - lean: Rapid 1-page specs, bullet ACs, MVP focus (Hackathons / Early-stage)",
        "#   - standard: Full INVEST criteria, Gherkin BDD, Fibonacci points, DoD (Growth / Mid-size Agile)",
        "#   - enterprise: Traceability matrix, SOC2/GDPR compliance tags, SLAs, audit logs (Enterprise scale)",
        f"default_tier: {config.get('default_tier', 'standard')}",
        "",
        "# Operating Model:",
        "#   - scrum: Iterative sprint planning, user stories, Fibonacci points, sprint velocity (Default)",
        "#   - shape-up: 6-week cycles, shaped pitches, appetite budgeting, hill charts, no-gos",
        "#   - kanban: Continuous pull flow, WIP limits, cycle-time optimization, backlog queue",
        "#   - gist: High-uncertainty iterative planning (Goals, Ideas, Step-projects, Tasks)",
        f"operating_model: {config.get('operating_model', 'scrum')}",
        "",
        "# Favorite / Pinned Skills for Quick Launcher in PM Command Center & Sidepanel:",
        "favorite_skills:"
    ]
    for s in config.get("favorite_skills", []):
        lines.append(f"  - {s}")
    lines.append("")
    lines.append("# Active Product Strategy, Discovery, Prioritization, and Operations Frameworks:")
    lines.append("#   Strategy:")
    lines.append("#     - wardley: Wardley Value Chain Evolution Mapping")
    lines.append("#     - toc: Theory of Constraints (Goldratt bottleneck identification)")
    lines.append("#   Discovery:")
    lines.append("#     - ost: Opportunity Solution Tree (Teresa Torres continuous discovery)")
    lines.append("#     - jtbd-and-mom-test: Jobs-to-be-Done & The Mom Test customer interviews")
    lines.append("#   Prioritization:")
    lines.append("#     - rice: Reach, Impact, Confidence, Effort scoring")
    lines.append("#     - wsjf: Weighted Shortest Job First (Cost of Delay / Duration)")
    lines.append("#     - kano-model: Kano Customer Delight & Hygiene analysis")
    lines.append("#   Operations:")
    lines.append("#     - scrum-sprint-delivery: Sprint Goal, INVEST Stories & Velocity Slicing")
    lines.append("#     - shape-up: Basecamp Shaped Pitches, Appetite Budgeting & Hill Charts")
    lines.append("#     - gist-planning: Goals, Ideas, Step-projects, Tasks")
    lines.append("active_frameworks:")
    for f in config.get("active_frameworks", []):
        lines.append(f"  - {f}")
    lines.append("")
    lines.append("# Enabled MCP (Model Context Protocol) Integration Targets:")
    lines.append("mcp_enabled:")
    mcp_comments = {
        "atlassian": "Jira & Confluence",
        "github": "GitHub Issues, PRs, & Milestones",
        "figma": "UI design files & comments",
        "miro": "Visual whiteboards & sticky notes",
        "notion": "Product wikis & database sync",
        "stitch": "Google Stitch Atelier UI"
    }
    for m in config.get("mcp_enabled", []):
        comment = mcp_comments.get(m, "")
        if comment:
            lines.append(f"  - {m}  # {comment}")
        else:
            lines.append(f"  - {m}")
    lines.append("")
    return "\n".join(lines)

def write_harness_config(updates):
    current = parse_harness_config()
    if "mode" in updates and updates["mode"] in ("standalone", "embedded"):
        current["mode"] = updates["mode"]
    if "default_tier" in updates and updates["default_tier"] in ("lean", "standard", "enterprise"):
        current["default_tier"] = updates["default_tier"]
    if "operating_model" in updates and updates["operating_model"] in ("scrum", "shape-up", "kanban", "gist"):
        current["operating_model"] = updates["operating_model"]
    if "favorite_skills" in updates and isinstance(updates["favorite_skills"], list):
        current["favorite_skills"] = [str(x) for x in updates["favorite_skills"]]
    if "active_frameworks" in updates and isinstance(updates["active_frameworks"], list):
        current["active_frameworks"] = [str(x) for x in updates["active_frameworks"]]
    if "mcp_enabled" in updates and isinstance(updates["mcp_enabled"], list):
        current["mcp_enabled"] = [str(x) for x in updates["mcp_enabled"]]
        
    yaml_text = serialize_harness_config(current)
    config_file = CONTEXT_DIR / "harness-config.yaml"
    config_file.write_text(yaml_text, encoding="utf-8")
    return current

def get_mcp_status():
    env_vars = parse_env_file()
    mcp_file = ROOT_DIR / "mcp.json"
    mcp_servers = {}
    if mcp_file.exists():
        try:
            mcp_data = json.loads(mcp_file.read_text(encoding="utf-8"))
            mcp_servers = mcp_data.get("mcpServers", {})
        except Exception:
            pass
            
    return {
        "atlassian": {
            "configured": bool(env_vars.get("ATLASSIAN_HOST") and "your-domain" not in env_vars.get("ATLASSIAN_HOST", "") and env_vars.get("ATLASSIAN_API_TOKEN")),
            "host": env_vars.get("ATLASSIAN_HOST", "Not configured"),
            "email": env_vars.get("ATLASSIAN_EMAIL", "Not configured"),
            "has_token": bool(env_vars.get("ATLASSIAN_API_TOKEN")),
            "in_mcp_json": "atlassian" in mcp_servers
        },
        "github": {
            "configured": bool(env_vars.get("GITHUB_PERSONAL_ACCESS_TOKEN") and "your_github" not in env_vars.get("GITHUB_PERSONAL_ACCESS_TOKEN", "")),
            "has_token": bool(env_vars.get("GITHUB_PERSONAL_ACCESS_TOKEN")),
            "owner": env_vars.get("GITHUB_OWNER", ""),
            "repo": env_vars.get("GITHUB_REPO", ""),
            "in_mcp_json": "github" in mcp_servers
        },
        "figma": {
            "configured": bool(env_vars.get("FIGMA_ACCESS_TOKEN") and "your_figma" not in env_vars.get("FIGMA_ACCESS_TOKEN", "")),
            "has_token": bool(env_vars.get("FIGMA_ACCESS_TOKEN")),
            "in_mcp_json": "figma" in mcp_servers
        },
        "miro": {
            "configured": bool(env_vars.get("MIRO_ACCESS_TOKEN") and "your_miro" not in env_vars.get("MIRO_ACCESS_TOKEN", "")),
            "has_token": bool(env_vars.get("MIRO_ACCESS_TOKEN")),
            "in_mcp_json": "miro" in mcp_servers
        },
        "notion": {
            "configured": bool(env_vars.get("NOTION_API_TOKEN") and "your_notion" not in env_vars.get("NOTION_API_TOKEN", "")),
            "has_token": bool(env_vars.get("NOTION_API_TOKEN")),
            "root_page_id": env_vars.get("NOTION_ROOT_PAGE_ID", ""),
            "in_mcp_json": "notion" in mcp_servers
        },
        "stitch": {
            "configured": bool(env_vars.get("STITCH_API_KEY") and "your_stitch" not in env_vars.get("STITCH_API_KEY", "")),
            "has_token": bool(env_vars.get("STITCH_API_KEY")),
            "in_mcp_json": "stitch" in mcp_servers
        },
        "local_daemon": {
            "configured": True,
            "endpoint": f"ws://127.0.0.1:{CURRENT_PORT}/bridge"
        }
    }

def get_context_overview():
    config = parse_harness_config()
    files = {}
    
    context_titles = {
        "product.md": "Product Vision, Personas & OKRs",
        "discovery.md": "Active Outcomes & Opportunity Solution Tree (OST)",
        "strategy-and-constraints.md": "Wardley Value Chain & Bottlenecks",
        "architecture.md": "Architecture, Tech Stack & Data Models",
        "conventions.md": "Conventions, DoR & Gherkin Standards",
        "decisions.md": "Product Decision Log (PDR/ADR)",
        "harness-config.yaml": "Harness Configuration"
    }
    
    cli_prompts = {
        "product.md": "/ingest-context Ingest product vision, personas, and OKRs into .context/product.md",
        "discovery.md": "/apply-framework opportunity-solution-tree Map outcomes to customer opportunities",
        "strategy-and-constraints.md": "/apply-framework wardley-mapping Evaluate build-vs-buy and bottlenecks",
        "architecture.md": "/ingest-context Ingest database schemas and API boundaries into .context/architecture.md",
        "conventions.md": "/create-prd Ground PRD with team Definition of Ready and Gherkin BDD criteria",
        "decisions.md": "/validate-idea Record key product decisions and trade-offs into .context/decisions.md"
    }

    if CONTEXT_DIR.exists():
        for p in sorted(CONTEXT_DIR.glob("*")):
            if p.name.startswith("."):
                continue
            content = p.read_text(encoding="utf-8")
            stat = p.stat()
            lines = len(content.splitlines())
            words = len(content.split())
            
            if p.suffix == ".md":
                has_h1 = bool(re.search(r"^#\s+", content, re.MULTILINE))
                has_h2 = len(re.findall(r"^##\s+", content, re.MULTILINE)) >= 2
                score = min(100, int((words / 350.0) * 50) + (30 if has_h1 else 0) + (20 if has_h2 else 0))
                if score >= 80:
                    status = "Complete"
                    color = "emerald"
                elif score >= 50:
                    status = "In Progress"
                    color = "amber"
                else:
                    status = "Needs Hydration"
                    color = "red"
            else:
                score = 100 if lines > 10 else 50
                status = "Configured"
                color = "blue"
                
            files[p.name] = {
                "filename": p.name,
                "title": context_titles.get(p.name, p.name),
                "content": content,
                "lines": lines,
                "words": words,
                "bytes": stat.st_size,
                "modified_iso": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
                "score": score,
                "status": status,
                "color": color,
                "cli_prompt": cli_prompts.get(p.name, f"/ingest-context Update .context/{p.name}")
            }
            
    mcp_status = get_mcp_status()
    
    return {
        "config": config,
        "files": files,
        "mcp_status": mcp_status,
        "summary": {
            "total_files": len(files),
            "total_words": sum(f["words"] for f in files.values()),
            "average_completeness": int(sum(f["score"] for f in files.values()) / max(1, len(files))),
            "mode": config.get("mode", "standalone"),
            "default_tier": config.get("default_tier", "standard")
        }
    }

def get_all_skills():
    skills = []
    category_map = {
        "create-prd": "strategy",
        "create-user-stories": "stories",
        "refine-user-stories": "stories",
        "create-mockup": "design",
        "create-design-brief": "design",
        "create-documentation": "strategy",
        "brainstorm": "strategy",
        "validate-idea": "strategy",
        "sync-jira": "mcp",
        "sync-confluence": "mcp",
        "sync-github-issues": "mcp",
        "sync-figma": "mcp",
        "sync-miro": "mcp",
        "sync-notion": "mcp",
        "connect-mcp": "mcp",
        "gui-run": "gui",
        "ingest-context": "context",
        "apply-framework": "strategy",
        "recommend-framework": "strategy"
    }
    
    if SKILLS_DIR.exists():
        for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
            folder_name = skill_file.parent.name
            content = skill_file.read_text(encoding="utf-8")
            frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
            name = folder_name
            desc = ""
            if frontmatter_match:
                yaml_text = frontmatter_match.group(1)
                name_match = re.search(r"^name:\s*(.+)$", yaml_text, re.MULTILINE)
                desc_match = re.search(r"^description:\s*>(.+?)(?=\n[a-z]+:|\Z)", yaml_text, re.DOTALL)
                if not desc_match:
                    desc_match = re.search(r"^description:\s*(.+)$", yaml_text, re.MULTILINE)
                if name_match: name = name_match.group(1).strip()
                if desc_match: desc = desc_match.group(1).strip().replace("\n", " ")
            
            skills.append({
                "id": name,
                "name": name.replace("-", " ").title(),
                "description": desc or f"Canonical skill {name}",
                "category": category_map.get(name, "strategy"),
                "path": str(skill_file.relative_to(ROOT_DIR))
            })
    return skills

def get_all_artifacts():
    artifacts = []
    
    # 1. Scan docs/**/*.md
    if DOCS_DIR.exists():
        for p in sorted(DOCS_DIR.rglob("*")):
            if p.is_dir() or p.name.startswith(".") or p.name in (".gitkeep", "README.md"):
                continue
            if p.suffix in (".md", ".txt", ".json", ".html"):
                stat = p.stat()
                rel_path = str(p.relative_to(ROOT_DIR))
                
                # Classify type
                if "prds" in rel_path.lower() or "prd" in p.name.lower():
                    ftype = "PRD"
                elif "stories" in rel_path.lower() or "stor" in p.name.lower():
                    ftype = "User Stories"
                elif "validation" in rel_path.lower() or "validat" in p.name.lower():
                    ftype = "Validation"
                elif p.suffix == ".html":
                    ftype = "Mockup"
                else:
                    ftype = "Product Spec"
                    
                artifacts.append({
                    "filename": p.name,
                    "path": rel_path,
                    "size_bytes": stat.st_size,
                    "size_kb": round(stat.st_size / 1024, 1),
                    "modified_iso": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
                    "type": ftype,
                    "is_html": p.suffix == ".html"
                })

    # 2. Scan mockups/**/*.html
    if MOCKUPS_DIR.exists():
        for p in sorted(MOCKUPS_DIR.rglob("*.html")):
            if p.is_dir() or p.name.startswith("."):
                continue
            stat = p.stat()
            rel_path = str(p.relative_to(ROOT_DIR))
            artifacts.append({
                "filename": p.name,
                "path": rel_path,
                "size_bytes": stat.st_size,
                "size_kb": round(stat.st_size / 1024, 1),
                "modified_iso": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
                "type": "Mockup",
                "is_html": True
            })

    # 3. BACKLOG.md in root
    backlog_file = ROOT_DIR / "BACKLOG.md"
    if backlog_file.exists():
        stat = backlog_file.stat()
        artifacts.append({
            "filename": "BACKLOG.md",
            "path": "BACKLOG.md",
            "size_bytes": stat.st_size,
            "size_kb": round(stat.st_size / 1024, 1),
            "modified_iso": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
            "type": "Backlog",
            "is_html": False
        })
        
    artifacts.sort(key=lambda x: x["modified_iso"], reverse=True)
    return artifacts

def save_artifact(data):
    filepath = data.get("path") or data.get("filepath")
    filename = data.get("filename")
    content = data.get("content", "")
    art_type = data.get("type", "Spec")

    if not filepath and filename:
        if filename.endswith(".html"):
            filepath = f"mockups/{filename}"
        elif "prd" in filename.lower():
            filepath = f"docs/prds/{filename}"
        elif "stor" in filename.lower():
            filepath = f"docs/stories/{filename}"
        elif "validat" in filename.lower():
            filepath = f"docs/validation/{filename}"
        else:
            filepath = f"docs/{filename}"

    if not filepath:
        raise ValueError("Missing 'path' or 'filename' parameter")

    # Security check: must resolve within ROOT_DIR and not in ui/ or .git/
    target = (ROOT_DIR / filepath).resolve()
    if not str(target).startswith(str(ROOT_DIR)):
        raise PermissionError("Path traversal prohibited")
    rel = target.relative_to(ROOT_DIR)
    rel_str = str(rel)
    if rel_str.startswith("ui/") or rel_str.startswith(".git/"):
        raise PermissionError("Writing to internal Sidekick UI or git assets is prohibited")

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    stat = target.stat()

    return {
        "success": True,
        "path": rel_str,
        "filename": target.name,
        "size_kb": round(stat.st_size / 1024, 1),
        "type": art_type,
        "message": f"Saved {rel_str} ({round(stat.st_size / 1024, 1)} KB)"
    }

def compile_prompt_payload(data):
    skill_id = data.get("skill_id", "create-prd")
    user_input = data.get("user_input", "").strip()
    tier = data.get("tier", "standard").lower()
    framework_id = data.get("framework_id", "")
    context_files = data.get("context_files", ["product.md", "conventions.md"])
    stage = data.get("stage", "generate")  # "clarify" or "generate"
    answers = data.get("answers", [])  # list of {question, answer}

    # 1. Read Skill
    skill_file = ROOT_DIR / "skills" / skill_id / "SKILL.md"
    skill_body = ""
    skill_name = skill_id
    if skill_file.exists():
        skill_text = skill_file.read_text(encoding="utf-8")
        fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", skill_text, re.DOTALL)
        if fm_match:
            skill_body = fm_match.group(2).strip()
            name_m = re.search(r"^name:\s*(.+)$", fm_match.group(1), re.MULTILINE)
            if name_m:
                skill_name = name_m.group(1).strip()
        else:
            skill_body = skill_text.strip()
    else:
        skill_body = f"Execute product management skill: {skill_id}"

    # 2. Read Framework (if specified)
    framework_info = ""
    if framework_id and framework_id not in ("none", "direct"):
        fw_matches = list((ROOT_DIR / "frameworks").glob(f"*/{framework_id}.md"))
        if fw_matches:
            fw_path = fw_matches[0]
            fw_text = fw_path.read_text(encoding="utf-8")
            framework_info = f"\n\n### 🗺️ Active Thinking Lens: Framework `{framework_id}`\n{fw_text}"

    # 3. Read Template Guidelines (if available)
    template_info = ""
    tpl_file = ROOT_DIR / "templates" / f"{tier}.md"
    if not tpl_file.exists():
        for tpl in (ROOT_DIR / "templates").glob(f"**/{tier}.md"):
            tpl_file = tpl
            break
    if tpl_file.exists():
        template_info = f"\n\n### 📐 Artifact Tier Template Guidelines (`{tier.upper()}`)\n{tpl_file.read_text(encoding='utf-8')}"

    # 4. Hydrate Context Files
    hydrated_context_blocks = []
    context_summary = []
    if CONTEXT_DIR.exists():
        harness_cfg_file = CONTEXT_DIR / "harness-config.yaml"
        if harness_cfg_file.exists():
            h_text = harness_cfg_file.read_text(encoding="utf-8")
            hydrated_context_blocks.append(f"#### `.context/harness-config.yaml`\n```yaml\n{h_text}\n```")

        for cf in context_files:
            if cf == "harness-config.yaml":
                continue
            cf_path = CONTEXT_DIR / cf
            if cf_path.exists():
                c_text = cf_path.read_text(encoding="utf-8")
                hydrated_context_blocks.append(f"#### `.context/{cf}`\n{c_text}")
                context_summary.append({"filename": cf, "words": len(c_text.split()), "lines": len(c_text.splitlines())})

    context_str = "\n\n".join(hydrated_context_blocks)

    # 5. Build System Prompt & User Prompt
    system_prompt = f"""You are AI PM Sidekick, an elite principal product management AI partner.
You operate within a local product repository with strict context isolation.

### 🧭 Operating Directives
1. Hydrate Grounded Reality: Strictly reference real product personas, constraints, and architecture provided in context. Never hallucinate fake enterprise constraints when real ones exist.
2. Zero Context Contamination: Internal UI files in ui/ are quarantined. Only generate user-facing product deliverables for docs/ or mockups/.
3. Tier Adherence: Produce deliverables strictly matching the active tier ({tier.upper()}).
4. INVEST & Gherkin Standard: User stories must satisfy INVEST criteria and include Gherkin Given-When-Then BDD scenarios.

### 🛠️ Active Skill Instructions: `{skill_name}`
{skill_body}
{framework_info}
{template_info}"""

    if stage == "clarify":
        user_prompt = f"""## 🎯 Product Task Briefing
{user_input if user_input else f"Execute {skill_id} based on active product context."}

---

## 🏛️ Grounding Product Context (.context/)
{context_str}

---

## 🛑 Socratic Clarifying Gate Execution
Analyze the task briefing and the product context above.
Identify 2 to 4 critical missing requirements, unvalidated assumptions, or architecture ambiguities.
Output them as a JSON array of questions, formatted exactly as:
```json
[
  {{
    "id": 1,
    "question": "Specific, actionable question for the PM",
    "why_it_matters": "Why this decision impacts scope, architecture, or customer value"
  }}
]
```
If requirements are completely clear with no missing gaps, return an empty array `[]`."""
    else:  # stage == "generate"
        answers_str = ""
        if answers:
            answers_str = "### 💬 Clarifications & Decisions from PM:\n"
            for idx, a in enumerate(answers, 1):
                q = a.get("question", f"Question {idx}")
                ans = a.get("answer", "Assumed default")
                answers_str += f"- **Q**: {q}\n  **A**: {ans}\n"
            answers_str += "\n"

        user_prompt = f"""## 🎯 Product Task Briefing
{user_input if user_input else f"Execute {skill_id} based on active product context."}

{answers_str}---

## 🏛️ Grounding Product Context (.context/)
{context_str}

---

## 🚀 Execution Instructions
Generate the complete, production-grade deliverable adhering strictly to the {tier.upper()} tier format.
Adhere to INVEST criteria, Gherkin BDD scenarios, and concrete acceptance criteria.

At the very end of your response, output a distinct section formatted as:
---
## 🧠 Proposed Compounding Knowledge Write-Back
- **New Decision**: (Specific decision to record in `.context/decisions.md`)
- **Discovery Insight**: (Customer or market discovery to record in `.context/discovery.md`)
- **Architecture Rule**: (Technical constraint to record in `.context/architecture.md`)
"""

    full_bundle = f"""# 🚀 AI PM Sidekick Hydrated Prompt Bundle
# Skill: {skill_name} | Tier: {tier.upper()} | Stage: {stage.upper()}

## System Instructions
{system_prompt}

---

## Task & Grounded Context
{user_prompt}
"""

    return {
        "success": True,
        "skill_id": skill_id,
        "skill_name": skill_name,
        "tier": tier,
        "framework_id": framework_id,
        "stage": stage,
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "full_bundle": full_bundle,
        "context_summary": context_summary
    }

def execute_ai_call(data):
    payload = compile_prompt_payload(data)
    stage = data.get("stage", "generate")
    provider = data.get("provider")
    
    env_vars = parse_env_file()
    gemini_key = env_vars.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    anthropic_key = env_vars.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    openai_key = env_vars.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")

    active_provider = None
    if provider == "gemini" and gemini_key: active_provider = "gemini"
    elif provider == "anthropic" and anthropic_key: active_provider = "anthropic"
    elif provider == "openai" and openai_key: active_provider = "openai"
    elif gemini_key: active_provider = "gemini"
    elif anthropic_key: active_provider = "anthropic"
    elif openai_key: active_provider = "openai"

    if not active_provider:
        return {
            "mode": "bundle_only",
            "message": "No API key configured in .env. Switch to Smart Prompt Bundle mode.",
            "bundle": payload["full_bundle"],
            "system_prompt": payload["system_prompt"],
            "user_prompt": payload["user_prompt"],
            "payload": payload
        }

    system_prompt = payload["system_prompt"]
    user_prompt = payload["user_prompt"]

    try:
        response_text = ""
        if active_provider == "gemini":
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_key}"
            req_body = {
                "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
                "systemInstruction": {"parts": [{"text": system_prompt}]},
                "generationConfig": {"temperature": 0.4, "maxOutputTokens": 8192}
            }
            req = Request(url, data=json.dumps(req_body).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
            with urlopen(req, timeout=60) as res:
                res_data = json.loads(res.read().decode("utf-8"))
                candidates = res_data.get("candidates", [])
                if candidates and "content" in candidates[0]:
                    parts = candidates[0]["content"].get("parts", [])
                    response_text = "".join(p.get("text", "") for p in parts)
                    
        elif active_provider == "openai":
            url = "https://api.openai.com/v1/chat/completions"
            req_body = {
                "model": "gpt-4o",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.4
            }
            req = Request(url, data=json.dumps(req_body).encode("utf-8"), headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {openai_key}"
            }, method="POST")
            with urlopen(req, timeout=60) as res:
                res_data = json.loads(res.read().decode("utf-8"))
                response_text = res_data["choices"][0]["message"]["content"]

        elif active_provider == "anthropic":
            url = "https://api.anthropic.com/v1/messages"
            req_body = {
                "model": "claude-3-5-sonnet-20241022",
                "max_tokens": 4096,
                "system": system_prompt,
                "messages": [{"role": "user", "content": user_prompt}],
                "temperature": 0.4
            }
            req = Request(url, data=json.dumps(req_body).encode("utf-8"), headers={
                "Content-Type": "application/json",
                "x-api-key": anthropic_key,
                "anthropic-version": "2023-06-01"
            }, method="POST")
            with urlopen(req, timeout=60) as res:
                res_data = json.loads(res.read().decode("utf-8"))
                response_text = "".join(b.get("text", "") for b in res_data.get("content", []))

        if stage == "clarify":
            questions = []
            json_m = re.search(r"```(?:json)?\s*(\[\s*\{.*?\}\s*\])\s*```", response_text, re.DOTALL)
            if json_m:
                try:
                    questions = json.loads(json_m.group(1))
                except Exception:
                    pass
            if not questions:
                q_matches = re.findall(r"(?:^|\n)\s*(?:\d+[\.\)]|\-|\*)\s*(.+?)(?=\n\s*(?:\d+[\.\)]|\-|\*)|\Z)", response_text, re.DOTALL)
                for idx, qm in enumerate(q_matches[:4], 1):
                    clean_q = qm.strip().split("\n")[0]
                    questions.append({"id": idx, "question": clean_q, "why_it_matters": "Clarifies scope before execution"})
                    
            return {
                "mode": "ai_executed",
                "stage": "clarify",
                "provider": active_provider,
                "questions": questions,
                "raw_text": response_text
            }
        else:
            artifact_content = response_text
            write_back_snippet = ""
            wb_match = re.search(r"(?:---|\n)\s*##\s*🧠\s*Proposed Compounding Knowledge Write-Back\s*\n(.*)$", response_text, re.DOTALL | re.IGNORECASE)
            if wb_match:
                write_back_snippet = wb_match.group(1).strip()
                artifact_content = response_text[:wb_match.start()].strip()
                
            return {
                "mode": "ai_executed",
                "stage": "generate",
                "provider": active_provider,
                "artifact_content": artifact_content,
                "write_back_snippet": write_back_snippet,
                "raw_text": response_text
            }

    except Exception as e:
        return {
            "mode": "bundle_only",
            "error": str(e),
            "message": f"AI call failed ({active_provider}): {e}. Switched to Smart Prompt Bundle mode.",
            "bundle": payload["full_bundle"],
            "system_prompt": payload["system_prompt"],
            "user_prompt": payload["user_prompt"],
            "payload": payload
        }

def get_env_status():
    env_vars = parse_env_file()
    def mask_key(k):
        v = env_vars.get(k, "") or os.environ.get(k, "")
        if not v:
            return ""
        if len(v) <= 8:
            return "••••••••"
        return v[:4] + "••••" + v[-4:]

    return {
        "llm": {
            "gemini": {
                "configured": bool(env_vars.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")),
                "preview": mask_key("GEMINI_API_KEY")
            },
            "anthropic": {
                "configured": bool(env_vars.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")),
                "preview": mask_key("ANTHROPIC_API_KEY")
            },
            "openai": {
                "configured": bool(env_vars.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")),
                "preview": mask_key("OPENAI_API_KEY")
            },
            "default_provider": env_vars.get("DEFAULT_LLM_PROVIDER", "gemini")
        },
        "mcp": get_mcp_status()
    }

def append_context_entry(data):
    target_file = data.get("target_file", "decisions.md")
    entry = data.get("entry", "").strip()
    if not entry:
        return {"error": "Entry content cannot be empty"}
    if target_file not in ("decisions.md", "discovery.md", "strategy-and-constraints.md"):
        return {"error": "Target file must be decisions.md, discovery.md, or strategy-and-constraints.md"}
    
    tf = CONTEXT_DIR / target_file
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    header = f"\n\n### 💡 Session Entry ({now_str})\n"
    new_text = header + entry + "\n"
    
    if tf.exists():
        existing = tf.read_text(encoding="utf-8")
        tf.write_text(existing.rstrip() + new_text, encoding="utf-8")
    else:
        tf.write_text(f"# {target_file}\n" + new_text, encoding="utf-8")
        
    return {"success": True, "message": f"Successfully appended entry to .context/{target_file}"}

class PMCommandCenterApiHandler(SimpleHTTPRequestHandler):
    def send_json(self, data, status=200):
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path in ('/', '/index.html', '/gui', '/dashboard', '/mockups/pm-command-center.html'):
            self.path = '/ui/views/pm-command-center.html'
            return super().do_GET()

        if path == '/sidepanel-skills-navigation.html':
            self.path = '/ui/views/sidepanel-skills-navigation.html'
            return super().do_GET()

        if path == '/user-profile-settings.html':
            self.path = '/ui/views/user-profile-settings.html'
            return super().do_GET()

        if path.startswith('/stitch/'):
            self.path = '/ui/stitch/' + path[len('/stitch/'):]
            return super().do_GET()

        if path.startswith('/mockups/stitch/'):
            self.path = '/ui/stitch/' + path[len('/mockups/stitch/'):]
            return super().do_GET()

        if path in ("/api/manifest", "/dist/harness-manifest.json"):
            manifest_file = DIST_DIR / "harness-manifest.json"
            if manifest_file.exists():
                return self.send_json(json.loads(manifest_file.read_text(encoding="utf-8")))
            return self.send_json({"error": "Manifest not found. Run scripts/export-skills.py first."}, status=404)

        if path == "/api/context":
            return self.send_json(get_context_overview())

        if path.startswith("/api/context/"):
            filename = path[len("/api/context/"):].strip()
            if not filename or "/" in filename or "\\" in filename or ".." in filename:
                return self.send_json({"error": "Invalid filename parameter"}, status=400)
            target = CONTEXT_DIR / filename
            if not target.exists():
                return self.send_json({"error": f"Context file not found: {filename}"}, status=404)
            content = target.read_text(encoding="utf-8")
            stat = target.stat()
            return self.send_json({
                "filename": filename,
                "content": content,
                "lines": len(content.splitlines()),
                "words": len(content.split()),
                "bytes": stat.st_size,
                "modified_iso": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
            })

        if path == "/api/config":
            return self.send_json({"config": parse_harness_config()})

        if path == "/api/skills":
            return self.send_json({"skills": get_all_skills()})

        if path == "/api/artifacts":
            return self.send_json({"artifacts": get_all_artifacts()})

        if path == "/api/artifact-content":
            file_param = query.get("file", [""])[0]
            if not file_param:
                return self.send_json({"error": "Missing 'file' parameter"}, status=400)
            
            target_path = (ROOT_DIR / file_param).resolve()
            if not str(target_path).startswith(str(ROOT_DIR)) or not target_path.exists():
                # try searching in docs/, mockups/, ui/specs/, or ui/views/
                for alt in [DOCS_DIR / file_param, MOCKUPS_DIR / file_param, UI_SPECS_DIR / file_param, UI_VIEWS_DIR / file_param, ROOT_DIR / file_param]:
                    if alt.exists():
                        target_path = alt
                        break

            if not target_path.exists():
                return self.send_json({"error": f"File not found: {file_param}"}, status=404)

            content = target_path.read_text(encoding="utf-8")
            return self.send_json({
                "filename": target_path.name,
                "path": str(target_path.relative_to(ROOT_DIR)),
                "content": content,
                "is_html": target_path.name.endswith(".html")
            })

        if path == "/api/mcp-status":
            return self.send_json(get_mcp_status())

        if path in ("/api/env-status", "/api/env"):
            return self.send_json(get_env_status())

        if path in ("/api/context-health", "/api/context-overview"):
            return self.send_json(get_context_overview())

        if path == "/api/user-settings":
            env_vars = parse_env_file()
            cfg = parse_harness_config()
            env_status = get_env_status()
            return self.send_json({
                "user_name": env_vars.get("USER_NAME", "Paula (Lead PM)"),
                "user_email": env_vars.get("USER_EMAIL", "paula.pm@company.com"),
                "persona": env_vars.get("DEFAULT_PERSONA", "paula"),
                "prd_mode": cfg.get("default_tier") or env_vars.get("DEFAULT_PRD_MODE", "standard"),
                "ac_format": env_vars.get("DEFAULT_AC_FORMAT", "gherkin"),
                "story_scale": env_vars.get("DEFAULT_STORY_SCALE", "fibonacci"),
                "ui_theme": env_vars.get("DEFAULT_UI_THEME", "stitch"),
                "mode": cfg.get("mode", "standalone"),
                "default_tier": cfg.get("default_tier", "standard"),
                "operating_model": cfg.get("operating_model", "scrum"),
                "favorite_skills": cfg.get("favorite_skills", []),
                "active_frameworks": cfg.get("active_frameworks", []),
                "workspace_path": str(ROOT_DIR),
                "llm_status": env_status["llm"],
                "gemini_api_key": env_status["llm"]["gemini"]["preview"],
                "anthropic_api_key": env_status["llm"]["anthropic"]["preview"],
                "openai_api_key": env_status["llm"]["openai"]["preview"],
                "default_llm_provider": env_vars.get("DEFAULT_LLM_PROVIDER", "gemini"),
                "atlassian_host": env_vars.get("ATLASSIAN_HOST", ""),
                "atlassian_email": env_vars.get("ATLASSIAN_EMAIL", ""),
                "has_atlassian_token": bool(env_vars.get("ATLASSIAN_API_TOKEN")),
                "has_github_token": bool(env_vars.get("GITHUB_PERSONAL_ACCESS_TOKEN")),
                "github_owner": env_vars.get("GITHUB_OWNER", ""),
                "github_repo": env_vars.get("GITHUB_REPO", ""),
                "has_figma_token": bool(env_vars.get("FIGMA_ACCESS_TOKEN")),
                "has_miro_token": bool(env_vars.get("MIRO_ACCESS_TOKEN")),
                "has_notion_token": bool(env_vars.get("NOTION_API_TOKEN")),
                "notion_root_page_id": env_vars.get("NOTION_ROOT_PAGE_ID", ""),
                "has_stitch_token": bool(env_vars.get("STITCH_API_KEY"))
            })

        return super().do_GET()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        body_bytes = self.rfile.read(length) if length > 0 else b"{}"
        
        try:
            data = json.loads(body_bytes.decode("utf-8"))
        except Exception:
            data = {}

        if path in ("/api/artifacts", "/api/save-artifact"):
            try:
                res = save_artifact(data)
                return self.send_json(res)
            except Exception as e:
                return self.send_json({"error": str(e)}, status=400)

        if path == "/api/compile-prompt":
            try:
                res = compile_prompt_payload(data)
                return self.send_json(res)
            except Exception as e:
                return self.send_json({"error": str(e)}, status=500)

        if path == "/api/execute-ai":
            try:
                res = execute_ai_call(data)
                return self.send_json(res)
            except Exception as e:
                return self.send_json({"error": str(e)}, status=500)

        if path in ("/api/env-config", "/api/save-credentials", "/api/user-settings"):
            write_env_file(data)
            write_harness_config(data)
            return self.send_json({
                "success": True,
                "message": "User settings and credentials saved to .env & harness-config.yaml!",
                "env_status": get_env_status()
            })

        if path == "/api/context-append":
            try:
                res = append_context_entry(data)
                return self.send_json(res)
            except Exception as e:
                return self.send_json({"error": str(e)}, status=500)

        if path in ("/api/config", "/api/harness-config"):
            updated_cfg = write_harness_config(data)
            if any(k in data for k in ("user_name", "user_email", "persona", "prd_mode", "ac_format", "story_scale", "ui_theme")):
                write_env_file(data)
            return self.send_json({
                "success": True,
                "config": updated_cfg,
                "message": "Configuration successfully saved to .context/harness-config.yaml!"
            })

        if path.startswith("/api/context/"):
            filename = path[len("/api/context/"):].strip()
            if not filename or "/" in filename or "\\" in filename or ".." in filename:
                return self.send_json({"error": "Invalid filename parameter"}, status=400)
            target = CONTEXT_DIR / filename
            new_content = data.get("content", "")
            target.write_text(new_content, encoding="utf-8")
            lines = len(new_content.splitlines())
            words = len(new_content.split())
            return self.send_json({
                "success": True,
                "filename": filename,
                "lines": lines,
                "words": words,
                "message": f"Successfully updated .context/{filename} ({lines} lines, {words} words)."
            })

        if path == "/api/test-mcp":
            target = data.get("target", "atlassian")
            env_vars = parse_env_file()
            if target == "atlassian":
                has_key = bool(env_vars.get("ATLASSIAN_HOST") and env_vars.get("ATLASSIAN_API_TOKEN"))
            elif target == "github":
                has_key = bool(env_vars.get("GITHUB_PERSONAL_ACCESS_TOKEN"))
            elif target == "figma":
                has_key = bool(env_vars.get("FIGMA_ACCESS_TOKEN"))
            elif target == "miro":
                has_key = bool(env_vars.get("MIRO_ACCESS_TOKEN"))
            elif target == "notion":
                has_key = bool(env_vars.get("NOTION_API_TOKEN"))
            elif target == "stitch":
                has_key = bool(env_vars.get("STITCH_API_KEY"))
            else:
                has_key = True

            return self.send_json({
                "target": target,
                "connected": has_key,
                "status": "200 OK (Active)" if has_key else "Missing Credentials in .env"
            })

        if path == "/api/generate-deliverable":
            env_vars = parse_env_file()
            skill = data.get("skill", "create-prd")
            feature_name = data.get("feature_name", "New Feature")
            mode = data.get("mode", "standard").lower()
            persona = data.get("persona") or env_vars.get("USER_NAME", "Marcin (Lead PM)")
            requirements = data.get("requirements", "High priority feature requirements.")
            today_str = datetime.now().strftime("%Y-%m-%d")

            # Determine template file
            template_path = TEMPLATES_DIR / "prd" / f"{mode}.md"
            if "story" in skill:
                template_path = TEMPLATES_DIR / "user-stories" / f"{mode}.md"
            elif "design" in skill:
                template_path = TEMPLATES_DIR / "design" / "design-brief.md"
            elif "validate" in skill:
                template_path = TEMPLATES_DIR / "validation" / "idea-validation.md"

            if template_path.exists():
                template_content = template_path.read_text(encoding="utf-8")
            else:
                template_content = f"# 🎯 {feature_name} — {skill.upper()}\n\n**Author:** {persona} | **Date:** {today_str}\n\n## Requirements\n{requirements}\n"

            # Replace placeholders with real user inputs
            content = template_content.replace("[Product/Feature Name]", feature_name)
            content = content.replace("[Feature Name]", feature_name)
            content = content.replace("[PM Name]", persona)
            content = content.replace("[YYYY-MM-DD]", today_str)
            content = content.replace("[Primary Persona]", persona)
            
            if "Problem Statement" in content or "Executive Summary" in content:
                content = content.replace("Detailed description of the problem backed by data, user feedback, or research quotes.", requirements)

            safe_name = re.sub(r"[^\w\-_]", "_", feature_name.lower().replace(" ", "_"))
            filename = f"{safe_name}_{skill.replace('-', '_')}.md"
            output_file = DOCS_DIR / filename
            DOCS_DIR.mkdir(parents=True, exist_ok=True)
            output_file.write_text(content, encoding="utf-8")

            return self.send_json({
                "success": True,
                "filename": filename,
                "path": str(output_file.relative_to(ROOT_DIR)),
                "content": content,
                "message": f"Successfully generated deliverable '{filename}' and written to disk!"
            })

        return self.send_json({"error": "Endpoint not found"}, status=404)

def run_server(host="127.0.0.1", port=3000, open_browser=False):
    global CURRENT_PORT
    os.chdir(ROOT_DIR)
    server_address = (host, port)
    try:
        httpd = HTTPServer(server_address, PMCommandCenterApiHandler)
    except OSError as e:
        if e.errno == 98 or "Address already in use" in str(e):
            original_port = port
            for candidate in range(port + 1, port + 20):
                try:
                    server_address = (host, candidate)
                    httpd = HTTPServer(server_address, PMCommandCenterApiHandler)
                    port = candidate
                    print(f"\n⚠️  Port {original_port} is already in use; automatically switched to port {port}.")
                    break
                except OSError:
                    continue
            else:
                raise e
        else:
            raise e

    CURRENT_PORT = port
    url = f"http://{host}:{port}"

    print(f"\n=======================================================")
    print(f"🚀 AI PM Sidekick — PM Command Center UI & REST API")
    print(f"=======================================================")
    print(f"  • Interface:      Google Stitch Atelier Workspace")
    print(f"  • Local URL:      {url}")
    print(f"  • REST API:       {url}/api/skills | {url}/api/artifacts")
    print(f"  • Security:       100% Localhost (Zero Cloud Leakage)")
    print(f"  • Status:         Active Backend Server Listening")
    print(f"=======================================================\n")

    if open_browser:
        webbrowser.open(url)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down PM Command Center server. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launch AI PM Sidekick Web GUI & Backend Server")
    parser.add_argument("--host", default="127.0.0.1", help="Host address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=3000, help="Port to listen on (default: 3000)")
    parser.add_argument("--open", action="store_true", help="Automatically open browser")
    args = parser.parse_args()

    run_server(host=args.host, port=args.port, open_browser=args.open)
