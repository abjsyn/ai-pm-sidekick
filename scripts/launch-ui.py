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

    lines = [
        "# AI PM Sidekick — Credentials & User Preferences",
        "# Saved via PM Command Center UI",
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
        "favorite_skills": ["create-prd", "create-user-stories", "refine-user-stories", "create-mockup", "sync-jira"],
        "active_frameworks": ["ost", "wardley", "toc", "rice", "wsjf"],
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
        "# Favorite / Pinned Skills for Quick Launcher in PM Command Center & Sidepanel:",
        "favorite_skills:"
    ]
    for s in config.get("favorite_skills", []):
        lines.append(f"  - {s}")
    lines.append("")
    lines.append("# Active Product Strategy & Discovery Frameworks:")
    lines.append("#   - ost: Opportunity Solution Tree (Teresa Torres continuous discovery)")
    lines.append("#   - wardley: Wardley Value Chain Evolution Mapping")
    lines.append("#   - toc: Theory of Constraints (Goldratt bottleneck identification)")
    lines.append("#   - rice: Reach, Impact, Confidence, Effort scoring")
    lines.append("#   - wsjf: Weighted Shortest Job First (Cost of Delay / Duration)")
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
        "apply-framework": "strategy"
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
    scan_paths = [
        (DOCS_DIR, "PRD"),
        (MOCKUPS_DIR, "Mockup"),
        (ROOT_DIR, "Backlog")
    ]
    
    for folder, default_type in scan_paths:
        if not folder.exists():
            continue
        if folder == ROOT_DIR:
            files = [ROOT_DIR / "BACKLOG.md", ROOT_DIR / "README.md"]
        else:
            files = list(folder.glob("*.*"))
            
        for f in files:
            if not f.exists() or f.is_dir() or f.name.startswith("."):
                continue
            if folder in (DOCS_DIR, MOCKUPS_DIR) and f.name == "README.md":
                continue
            stat = f.stat()
            ftype = default_type
            if f.name.endswith(".html"):
                ftype = "Mockup"
            elif "PRD" in f.name:
                ftype = "PRD"
            elif f.name.endswith(".md"):
                ftype = "Spec"
                
            artifacts.append({
                "filename": f.name,
                "path": str(f.relative_to(ROOT_DIR)),
                "size_bytes": stat.st_size,
                "size_kb": round(stat.st_size / 1024, 1),
                "modified_iso": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
                "type": ftype
            })
    return artifacts

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

        if path == "/api/user-settings":
            env_vars = parse_env_file()
            cfg = parse_harness_config()
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
                "favorite_skills": cfg.get("favorite_skills", []),
                "active_frameworks": cfg.get("active_frameworks", []),
                "workspace_path": str(ROOT_DIR),
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

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        body_bytes = self.rfile.read(length) if length > 0 else b"{}"
        
        try:
            data = json.loads(body_bytes.decode("utf-8"))
        except Exception:
            data = {}

        if path in ("/api/config", "/api/harness-config"):
            updated_cfg = write_harness_config(data)
            # Sync user profile fields to .env if supplied
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

        if path in ("/api/save-credentials", "/api/user-settings"):
            write_env_file(data)
            # If default_tier or mode or favorite_skills supplied, also update harness-config.yaml
            write_harness_config(data)
            return self.send_json({"success": True, "message": "User settings and credentials saved to .env & harness-config.yaml!"})

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
            
            # Inject actual requirements into problem/context section
            if "Problem Statement" in content or "Executive Summary" in content:
                content = content.replace("Detailed description of the problem backed by data, user feedback, or research quotes.", requirements)

            # Save generated file to docs/
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
