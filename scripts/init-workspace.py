#!/usr/bin/env python3
"""
AI PM Sidekick — Workspace Initializer
Initializes either:
  1. Standalone Mode: Dedicated PM workspace with .context/ core and launches GUI via scripts/launch-ui.py.
  2. Embedded Mode: Scans repo manifest files (package.json, pyproject.toml, Cargo.toml, go.mod, etc.)
     to pre-populate .context/architecture.md and anchor the PM harness to the existing codebase.

Usage:
  python3 scripts/init-workspace.py [--mode standalone|embedded] [--tier lean|standard|enterprise] [--no-gui]
"""

import os
import sys
import json
import re
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).parent.parent.resolve()
LAUNCHER_SCRIPT = ROOT_DIR / "scripts" / "launch-ui.py"

# ==============================================================================
# MANIFEST SCANNERS (Embedded Mode)
# ==============================================================================

def scan_package_json(target_dir: Path) -> dict:
    pkg_file = target_dir / "package.json"
    if not pkg_file.exists():
        return {}
    try:
        data = json.loads(pkg_file.read_text(encoding="utf-8"))
        deps = list(data.get("dependencies", {}).keys())
        dev_deps = list(data.get("devDependencies", {}).keys())
        scripts = data.get("scripts", {})
        
        # Categorize frameworks
        frameworks = []
        ui_libs = []
        testing = []
        backend = []
        db_orm = []
        
        all_deps = set(deps + dev_deps)
        
        # Frontend / Fullstack
        if "next" in all_deps: frameworks.append("Next.js")
        elif "react" in all_deps: frameworks.append("React")
        if "vue" in all_deps or "nuxt" in all_deps: frameworks.append("Vue / Nuxt")
        if "svelte" in all_deps or "@sveltejs/kit" in all_deps: frameworks.append("Svelte / SvelteKit")
        if "astro" in all_deps: frameworks.append("Astro")
        if "tailwindcss" in all_deps: ui_libs.append("Tailwind CSS")
        if "@mui/material" in all_deps or "@chakra-ui/react" in all_deps: ui_libs.append("Component UI Library")
        
        # Backend
        if "express" in all_deps: backend.append("Express.js")
        if "@nestjs/core" in all_deps: backend.append("NestJS")
        if "fastify" in all_deps: backend.append("Fastify")
        if "koa" in all_deps: backend.append("Koa")
        if "hono" in all_deps: backend.append("Hono")
        
        # DB / ORM
        if "prisma" in all_deps or "@prisma/client" in all_deps: db_orm.append("Prisma ORM")
        if "drizzle-orm" in all_deps: db_orm.append("Drizzle ORM")
        if "typeorm" in all_deps: db_orm.append("TypeORM")
        if "mongoose" in all_deps: db_orm.append("Mongoose (MongoDB)")
        if "pg" in all_deps: db_orm.append("PostgreSQL client (pg)")
        
        # Testing
        if "jest" in all_deps: testing.append("Jest")
        if "vitest" in all_deps: testing.append("Vitest")
        if "cypress" in all_deps: testing.append("Cypress")
        if "@playwright/test" in all_deps: testing.append("Playwright")
        
        return {
            "name": data.get("name", target_dir.name),
            "version": data.get("version", "0.1.0"),
            "description": data.get("description", "Node/TypeScript application"),
            "runtime": "Node.js / TypeScript" if (target_dir / "tsconfig.json").exists() or "typescript" in all_deps else "Node.js (JavaScript)",
            "frameworks": frameworks,
            "ui_libs": ui_libs,
            "backend": backend,
            "db_orm": db_orm,
            "testing": testing,
            "scripts": scripts,
            "raw_dependencies_count": len(deps),
            "raw_dev_dependencies_count": len(dev_deps)
        }
    except Exception as e:
        return {"error": f"Failed to parse package.json: {e}"}

def scan_python_manifests(target_dir: Path) -> dict:
    pyproject = target_dir / "pyproject.toml"
    reqs = target_dir / "requirements.txt"
    pipfile = target_dir / "Pipfile"
    
    if not (pyproject.exists() or reqs.exists() or pipfile.exists()):
        return {}
        
    content = ""
    if pyproject.exists():
        content += "\n" + pyproject.read_text(encoding="utf-8", errors="ignore")
    if reqs.exists():
        content += "\n" + reqs.read_text(encoding="utf-8", errors="ignore")
    if pipfile.exists():
        content += "\n" + pipfile.read_text(encoding="utf-8", errors="ignore")
        
    lower_content = content.lower()
    
    frameworks = []
    if "fastapi" in lower_content: frameworks.append("FastAPI")
    if "django" in lower_content: frameworks.append("Django")
    if "flask" in lower_content: frameworks.append("Flask")
    if "tornado" in lower_content: frameworks.append("Tornado")
    
    db_orm = []
    if "sqlalchemy" in lower_content: db_orm.append("SQLAlchemy")
    if "tortoise-orm" in lower_content: db_orm.append("Tortoise ORM")
    if "alembic" in lower_content: db_orm.append("Alembic (Migrations)")
    if "psycopg" in lower_content or "asyncpg" in lower_content: db_orm.append("PostgreSQL Driver")
    if "redis" in lower_content: db_orm.append("Redis Driver")
    if "pydantic" in lower_content: db_orm.append("Pydantic (Data Validation)")
    
    ai_ml = []
    if "torch" in lower_content: ai_ml.append("PyTorch")
    if "transformers" in lower_content: ai_ml.append("HuggingFace Transformers")
    if "langchain" in lower_content: ai_ml.append("LangChain")
    if "openai" in lower_content: ai_ml.append("OpenAI SDK")
    if "google-genai" in lower_content or "google-generativeai" in lower_content: ai_ml.append("Google GenAI SDK")
    
    testing = []
    if "pytest" in lower_content: testing.append("Pytest")
    if "unittest" in lower_content: testing.append("Unittest")
    
    # Try extracting name from pyproject.toml
    name_match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', content)
    proj_name = name_match.group(1) if name_match else target_dir.name
    
    desc_match = re.search(r'description\s*=\s*["\']([^"\']+)["\']', content)
    proj_desc = desc_match.group(1) if desc_match else "Python project"

    return {
        "name": proj_name,
        "description": proj_desc,
        "runtime": "Python 3",
        "frameworks": frameworks,
        "db_orm": db_orm,
        "ai_ml": ai_ml,
        "testing": testing
    }

def scan_cargo(target_dir: Path) -> dict:
    cargo = target_dir / "Cargo.toml"
    if not cargo.exists():
        return {}
    content = cargo.read_text(encoding="utf-8", errors="ignore")
    name_match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', content)
    frameworks = []
    if "actix" in content.lower(): frameworks.append("Actix Web")
    if "axum" in content.lower(): frameworks.append("Axum")
    if "tokio" in content.lower(): frameworks.append("Tokio Async Runtime")
    if "serde" in content.lower(): frameworks.append("Serde Serialization")
    if "diesel" in content.lower(): frameworks.append("Diesel ORM")
    if "sqlx" in content.lower(): frameworks.append("SQLx")
    
    return {
        "name": name_match.group(1) if name_match else target_dir.name,
        "runtime": "Rust",
        "frameworks": frameworks
    }

def scan_go_mod(target_dir: Path) -> dict:
    gomod = target_dir / "go.mod"
    if not gomod.exists():
        return {}
    content = gomod.read_text(encoding="utf-8", errors="ignore")
    mod_match = re.search(r'module\s+([^\s\n]+)', content)
    frameworks = []
    if "gin-gonic/gin" in content: frameworks.append("Gin Web Framework")
    if "labstack/echo" in content: frameworks.append("Echo")
    if "gofiber/fiber" in content: frameworks.append("Fiber")
    if "gorm.io/gorm" in content: frameworks.append("GORM")
    
    return {
        "name": mod_match.group(1).split("/")[-1] if mod_match else target_dir.name,
        "runtime": "Go",
        "frameworks": frameworks
    }

def scan_docker(target_dir: Path) -> dict:
    compose_files = [target_dir / "docker-compose.yml", target_dir / "docker-compose.yaml", target_dir / "compose.yaml"]
    services = []
    for cf in compose_files:
        if cf.exists():
            text = cf.read_text(encoding="utf-8", errors="ignore")
            # simple regex to find top-level service names
            svc_matches = re.findall(r"^[ \t]{2}([a-zA-Z0-9_-]+):", text, re.MULTILINE)
            services.extend(svc_matches)
    
    has_dockerfile = (target_dir / "Dockerfile").exists()
    return {
        "has_dockerfile": has_dockerfile,
        "services": list(set(services))
    }

def scan_workspace(target_dir: Path) -> dict:
    scan = {
        "root": str(target_dir),
        "folder_name": target_dir.name,
        "project_name": target_dir.name,
        "runtimes": [],
        "frameworks": [],
        "databases": [],
        "testing": [],
        "docker_services": [],
        "scripts": {},
        "description": "Codebase scanned by AI PM Sidekick"
    }
    
    # 1. Node.js / TS
    pkg = scan_package_json(target_dir)
    if pkg:
        if pkg.get("name"):
            scan["project_name"] = pkg["name"]
        scan["runtimes"].append(pkg.get("runtime", "Node.js"))
        scan["frameworks"].extend(pkg.get("frameworks", []))
        scan["frameworks"].extend(pkg.get("backend", []))
        scan["frameworks"].extend(pkg.get("ui_libs", []))
        scan["databases"].extend(pkg.get("db_orm", []))
        scan["testing"].extend(pkg.get("testing", []))
        scan["scripts"].update(pkg.get("scripts", {}))
        if pkg.get("description"):
            scan["description"] = pkg["description"]
            
    # 2. Python
    py = scan_python_manifests(target_dir)
    if py:
        if py.get("name") and scan["project_name"] == target_dir.name:
            scan["project_name"] = py["name"]
        scan["runtimes"].append(py.get("runtime", "Python"))
        scan["frameworks"].extend(py.get("frameworks", []))
        scan["frameworks"].extend(py.get("ai_ml", []))
        scan["databases"].extend(py.get("db_orm", []))
        scan["testing"].extend(py.get("testing", []))
        if py.get("description") and scan["description"] == "Codebase scanned by AI PM Sidekick":
            scan["description"] = py["description"]

    # 3. Rust
    cargo = scan_cargo(target_dir)
    if cargo:
        if cargo.get("name") and scan["project_name"] == target_dir.name:
            scan["project_name"] = cargo["name"]
        scan["runtimes"].append(cargo["runtime"])
        scan["frameworks"].extend(cargo.get("frameworks", []))

    # 4. Go
    go = scan_go_mod(target_dir)
    if go:
        if go.get("name") and scan["project_name"] == target_dir.name:
            scan["project_name"] = go["name"]
        scan["runtimes"].append(go["runtime"])
        scan["frameworks"].extend(go.get("frameworks", []))

    # 5. Docker
    docker = scan_docker(target_dir)
    if docker.get("has_dockerfile"):
        scan["docker_services"].append("Dockerfile (Containerized App)")
    scan["docker_services"].extend(docker.get("services", []))

    # De-duplicate
    scan["runtimes"] = list(dict.fromkeys(scan["runtimes"]))
    scan["frameworks"] = list(dict.fromkeys(scan["frameworks"]))
    scan["databases"] = list(dict.fromkeys(scan["databases"]))
    scan["testing"] = list(dict.fromkeys(scan["testing"]))
    scan["docker_services"] = list(dict.fromkeys(scan["docker_services"]))

    # Detect top-level structure
    subdirs = [d.name for d in target_dir.iterdir() if d.is_dir() and not d.name.startswith(".")]
    scan["top_level_directories"] = sorted(subdirs)

    return scan

# ==============================================================================
# ARCHITECTURE GENERATOR (Embedded vs Standalone)
# ==============================================================================

def generate_embedded_architecture_md(scan_data: dict, target_dir: Path) -> str:
    runtimes_str = ", ".join(scan_data["runtimes"]) if scan_data["runtimes"] else "General Polyglot / Scripting"
    frameworks_str = ", ".join(scan_data["frameworks"]) if scan_data["frameworks"] else "Native Standard Library"
    db_str = ", ".join(scan_data["databases"]) if scan_data["databases"] else "File-based / API integration"
    test_str = ", ".join(scan_data["testing"]) if scan_data["testing"] else "Standard test runner"
    docker_str = ", ".join(scan_data["docker_services"]) if scan_data["docker_services"] else "Host Native"
    dirs_str = ", ".join([f"`{d}/`" for d in scan_data["top_level_directories"][:12]])

    scripts_md = ""
    if scan_data.get("scripts"):
        scripts_md = "### Available Repository Scripts\n| Command | Script Definition |\n| :--- | :--- |\n"
        for k, v in list(scan_data["scripts"].items())[:8]:
            scripts_md += f"| `npm run {k}` | `{v}` |\n"
        scripts_md += "\n"

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    proj_name = scan_data.get("project_name") or scan_data["folder_name"]

    return f"""# 🏛️ Product Knowledge Core — Architecture & Technical Context (`architecture.md`)

> **Auto-scanned & Pre-populated in Embedded Mode**  
> *Last Scanned: {now_str} | Host Directory: `{scan_data['root']}`*

This document anchors AI PM Sidekick skills (PRDs, User Stories, Design Briefs, Mockups) directly to the technical reality of this repository. When generating stories, the AI will reference these real frameworks, databases, and directories to prevent hallucinated architecture.

---

## ⚙️ 1. Codebase Overview & Operating Mode

- **Operating Mode**: `embedded` (Codebase Integrated)
- **Project Name**: `{proj_name}`
- **Description**: {scan_data['description']}
- **Primary Runtimes**: {runtimes_str}
- **Frameworks & Core Libraries**: {frameworks_str}
- **Data Persistence & ORM**: {db_str}
- **Testing Suites**: {test_str}
- **Container / Services**: {docker_str}

---

## 📂 2. Repository Layout & Module Boundaries

The primary structural directories identified in this repository:
{dirs_str}

### Component & Architecture Guidelines for PM Deliverables:
- When writing **User Stories**, ensure technical tasks map to existing directories (e.g., frontend components vs backend controllers).
- When specifying **Data Models**, align entity properties with detected ORMs ({db_str}).
- When defining **Non-Functional Requirements**, respect runtime characteristics ({runtimes_str}).

---

## 💻 3. Technology Stack Reference Table

| Architectural Layer | Detected Technology | Purpose / Notes |
| :--- | :--- | :--- |
| **Runtime & Language** | {runtimes_str} | Primary execution environment |
| **Web & App Frameworks** | {frameworks_str} | Client UI & API service routing |
| **Database & Caching** | {db_str} | State management & storage |
| **Testing & Quality** | {test_str} | Automated verification suites |
| **Infrastructure / DevOps** | {docker_str} | Local orchestration & deployment |

---

{scripts_md}## 🌐 4. API Boundaries & External Integrations

*PM Note: Document high-level API boundaries, external microservices, and 3rd-party webhook endpoints below:*

- **Primary API Style**: REST / JSON / GraphQL
- **Authentication**: JWT / Session / OAuth2 Bearer Tokens
- **External Dependencies & Webhooks**:
  - Payment Gateways (Stripe, etc.)
  - Communication (Email, SMS, Webhooks)
  - Tool Ecosystem (Jira, Confluence, Figma via MCP)

---

## 🛡️ 5. Security, Access Control & Compliance

- **Environment Secrets**: Managed via `.env` (never committed to git).
- **Compliance Constraints**: Adhere to conventions outlined in `.context/conventions.md`.
"""

def generate_harness_config(mode: str, tier: str, operating_model: str = "scrum") -> str:
    return f"""# ==============================================================================
# AI PM Sidekick — Harness Configuration
# Single Source of Truth for Workspace Context, Operating Mode, and Tooling
# ==============================================================================

# Operating Mode:
#   - standalone: Dedicated PM command workspace (isolated product deliverables in docs/ & mockups/)
#   - embedded: Integrated directly within a software repository / monorepo
mode: {mode}

# Default Artifact Tier for PRDs, User Stories, and Technical Specs:
#   - lean: Rapid 1-page specs, bullet ACs, MVP focus (Hackathons / Early-stage)
#   - standard: Full INVEST criteria, Gherkin BDD, Fibonacci points, DoD (Growth / Mid-size Agile)
#   - enterprise: Traceability matrix, SOC2/GDPR compliance tags, SLAs, audit logs (Enterprise scale)
default_tier: {tier}

# Operating Model:
#   - scrum: Iterative sprint planning, user stories, Fibonacci points, sprint velocity (Default)
#   - shape-up: 6-week cycles, shaped pitches, appetite budgeting, hill charts, no-gos
#   - kanban: Continuous pull flow, WIP limits, cycle-time optimization, backlog queue
#   - gist: High-uncertainty iterative planning (Goals, Ideas, Step-projects, Tasks)
operating_model: {operating_model}

# Favorite / Pinned Skills for Quick Launcher in PM Command Center & Sidepanel:
favorite_skills:
  - create-prd
  - create-user-stories
  - refine-user-stories
  - create-mockup
  - recommend-framework
  - sync-jira

# Active Product Strategy, Discovery, Prioritization, and Operations Frameworks:
#   Strategy:
#     - wardley: Wardley Value Chain Evolution Mapping
#     - toc: Theory of Constraints (Goldratt bottleneck identification)
#   Discovery:
#     - ost: Opportunity Solution Tree (Teresa Torres continuous discovery)
#     - jtbd-and-mom-test: Jobs-to-be-Done & The Mom Test customer interviews
#   Prioritization:
#     - rice: Reach, Impact, Confidence, Effort scoring
#     - wsjf: Weighted Shortest Job First (Cost of Delay / Duration)
#     - kano-model: Kano Customer Delight & Hygiene analysis
#   Operations:
#     - scrum-sprint-delivery: Sprint Goal, INVEST Stories & Velocity Slicing
#     - shape-up: Basecamp Shaped Pitches, Appetite Budgeting & Hill Charts
#     - gist-planning: Goals, Ideas, Step-projects, Tasks
active_frameworks:
  - ost
  - wardley
  - toc
  - rice
  - wsjf
  - shape-up
  - scrum-sprint-delivery
  - gist-planning

# Enabled MCP (Model Context Protocol) Integration Targets:
mcp_enabled:
  - atlassian  # Jira & Confluence
  - github     # GitHub Issues, PRs, & Milestones
  - figma      # UI design files & comments
  - miro       # Visual whiteboards & sticky notes
  - notion     # Product wikis & database sync
  - stitch     # Google Stitch Atelier UI
"""

# ==============================================================================
# INITIALIZATION RUNNER
# ==============================================================================

def initialize_workspace(target_dir: Path, mode: str = "standalone", tier: str = "standard", operating_model: str = "scrum", force: bool = False, dry_run: bool = False) -> dict:
    context_dir = target_dir / ".context"
    docs_dir = target_dir / "docs"
    mockups_dir = target_dir / "mockups"
    
    actions_taken = []
    
    print(f"\n=======================================================")
    print(f"🚀 AI PM Sidekick — Workspace Initializer")
    print(f"=======================================================")
    print(f"  • Target Path:        {target_dir.resolve()}")
    print(f"  • Selected Mode:      {mode.upper()}")
    print(f"  • Artifact Tier:      {tier.upper()}")
    print(f"  • Operating Model:    {operating_model.upper()}")
    print(f"  • Overwrite:          {'FORCED' if force else 'Safe (Preserve Existing)'}")
    print(f"=======================================================\n")

    if not dry_run:
        context_dir.mkdir(parents=True, exist_ok=True)
        docs_dir.mkdir(parents=True, exist_ok=True)
        mockups_dir.mkdir(parents=True, exist_ok=True)

    # 1. Ensure clean docs/ and mockups/ with .gitkeep & README.md
    for fldr, label in [(docs_dir, "Product Deliverables & Specifications (`docs/`)"), (mockups_dir, "Product UI Mockups & Prototypes (`mockups/`)")]:
        keep_file = fldr / ".gitkeep"
        readme_file = fldr / "README.md"
        if not keep_file.exists() and not dry_run:
            keep_file.write_text("# Keep directory in git tracking\n", encoding="utf-8")
            actions_taken.append(f"Created {keep_file.relative_to(target_dir)}")
        if not readme_file.exists() and not dry_run:
            readme_text = f"# 📄 {label}\n\nReserved exclusively for PM product deliverables generated by AI PM Sidekick.\nInternal Sidekick UI assets are safely quarantined in `ui/` to prevent LLM context contamination.\n"
            readme_file.write_text(readme_text, encoding="utf-8")
            actions_taken.append(f"Created {readme_file.relative_to(target_dir)}")

    # 2. Write harness-config.yaml
    config_file = context_dir / "harness-config.yaml"
    if not config_file.exists() or force:
        if not dry_run:
            config_file.write_text(generate_harness_config(mode, tier, operating_model), encoding="utf-8")
        actions_taken.append(f"Configured .context/harness-config.yaml (operating_model: {operating_model})")
    else:
        # Update mode, tier, and operating_model inside existing config without wiping comments
        current_text = config_file.read_text(encoding="utf-8")
        updated_text = re.sub(r"^mode:\s*.*$", f"mode: {mode}", current_text, flags=re.MULTILINE)
        updated_text = re.sub(r"^default_tier:\s*.*$", f"default_tier: {tier}", updated_text, flags=re.MULTILINE)
        
        # Preserve or update operating_model
        if re.search(r"^operating_model:\s*.*$", updated_text, flags=re.MULTILINE):
            updated_text = re.sub(r"^operating_model:\s*.*$", f"operating_model: {operating_model}", updated_text, flags=re.MULTILINE)
        else:
            op_block = f"\n# Operating Model:\n#   - scrum: Iterative sprint planning (Default)\n#   - shape-up: 6-week cycles, shaped pitches, appetite budgeting\n#   - kanban: Continuous pull flow, WIP limits\n#   - gist: High-uncertainty iterative planning\noperating_model: {operating_model}\n"
            updated_text = re.sub(r"(^default_tier:\s*.*$)", rf"\1\n{op_block}", updated_text, flags=re.MULTILINE)
            
        # Ensure recommend-framework is in favorite_skills
        if "recommend-framework" not in updated_text:
            updated_text = re.sub(
                r"(favorite_skills:\s*\n(?:\s*-\s*[^\n]+\n)*)",
                r"\g<1>  - recommend-framework\n",
                updated_text
            )
            
        if not dry_run:
            config_file.write_text(updated_text, encoding="utf-8")
        actions_taken.append(f"Updated .context/harness-config.yaml (mode: {mode}, tier: {tier}, operating_model: {operating_model})")

    # 3. Handle architecture.md
    arch_file = context_dir / "architecture.md"
    if mode == "embedded":
        print("🔍 Scanning repository manifests for embedded codebase context...")
        scan_data = scan_workspace(target_dir)
        print(f"   • Runtimes detected:    {', '.join(scan_data['runtimes']) or 'None'}")
        print(f"   • Frameworks detected:  {', '.join(scan_data['frameworks']) or 'None'}")
        print(f"   • Databases / ORMs:     {', '.join(scan_data['databases']) or 'None'}")
        print(f"   • Testing frameworks:   {', '.join(scan_data['testing']) or 'None'}")
        if scan_data.get("docker_services"):
            print(f"   • Containers / Services:{', '.join(scan_data['docker_services'])}")
        
        if not arch_file.exists() or force:
            arch_content = generate_embedded_architecture_md(scan_data, target_dir)
            if not dry_run:
                arch_file.write_text(arch_content, encoding="utf-8")
            actions_taken.append("Pre-populated .context/architecture.md from repo manifests")
        else:
            actions_taken.append("Preserved existing .context/architecture.md (use --force to overwrite)")
    else:
        # Standalone mode: check if architecture.md exists, if not copy or generate
        source_arch = ROOT_DIR / ".context" / "architecture.md"
        if not arch_file.exists() and source_arch.exists() and target_dir != ROOT_DIR:
            if not dry_run:
                arch_file.write_text(source_arch.read_text(encoding="utf-8"), encoding="utf-8")
            actions_taken.append("Copied canonical .context/architecture.md for standalone workspace")

    # 4. Ensure other 5 core files exist from source if in a different target_dir
    source_context = ROOT_DIR / ".context"
    core_files = ["product.md", "discovery.md", "strategy-and-constraints.md", "conventions.md", "decisions.md"]
    for cf in core_files:
        dest_file = context_dir / cf
        if not dest_file.exists() and source_context.exists():
            src_file = source_context / cf
            if src_file.exists() and not dry_run:
                dest_file.write_text(src_file.read_text(encoding="utf-8"), encoding="utf-8")
                actions_taken.append(f"Scaffolded .context/{cf}")
        elif dest_file.exists() and cf == "conventions.md":
            conv_text = dest_file.read_text(encoding="utf-8")
            if "operating_model" not in conv_text:
                sec5_text = r"""
## 🔄 5. Operating Model Conventions (`operating_model`)

AI PM Sidekick supports 4 delivery operating models configured via `operating_model` in `.context/harness-config.yaml`. Each model shapes how backlogs, cycles, estimation, and handoffs are executed:

| Operating Model | Core Cadence | Unit of Work | Estimation & Sizing | Primary Delivery Gate |
| :--- | :--- | :--- | :--- | :--- |
| **`scrum`** *(Default)* | 1–2 week sprints | INVEST User Stories + Gherkin ACs | Fibonacci story points ($\le 5$ pts) | Definition of Ready ($\ge 85\%$) & Sprint Goal |
| **`shape-up`** | 6-week cycles + 2-week cooldown | Shaped Pitches & Scopes | Fixed Appetite (Small = 1–2 wks, Big = 6 wks) | Betting Table approval & Circuit Breaker |
| **`kanban`** | Continuous pull flow | Backlog items with WIP limits | Cycle time & throughput metrics | WIP column limits & SLA throughput |
| **`gist`** | Iterative experiment loops | Step-projects ($\le 2$ weeks) & Tasks | ICE scoring (Impact, Confidence, Ease) | Metric validation gate to unlock next step |

### Operating Model Selection Heuristics:
1. **Choose `scrum`** when cross-functional engineering sprints require predictable velocity, sprint commitments, and rigorous DoD sign-off.
2. **Choose `shape-up`** when teams suffer from backlog bloat and sprint rollover fatigue, and need bounded appetites with high autonomous design/build agency.
3. **Choose `kanban`** for operational maintenance, ongoing developer platform enhancements, or bug triage queues where work arrives unpredictably.
4. **Choose `gist`** for high-uncertainty 0-to-1 innovation tracks where committing to a multi-month solution is premature before smoke testing ideas with fast step-projects.
"""
                if not dry_run:
                    dest_file.write_text(conv_text.rstrip() + "\n" + sec5_text, encoding="utf-8")
                actions_taken.append("Preserved and synced Section 5 Operating Model in .context/conventions.md")

    print("\n✅ Initialization Summary:")
    for a in actions_taken:
        print(f"   ✔ {a}")

    return {
        "status": "success",
        "mode": mode,
        "tier": tier,
        "operating_model": operating_model,
        "actions": actions_taken
    }

def prompt_operating_model(default: str = "scrum") -> str:
    """Interactively prompts the user to select an operating delivery model."""
    print("\nSelect delivery operating model:")
    print("  1. scrum     — Iterative sprints, INVEST stories, Fibonacci points (Default)")
    print("  2. shape-up  — 6-week cycles, shaped pitches, appetite budgeting, hill charts")
    print("  3. kanban    — Continuous pull flow, WIP limits, cycle-time optimization")
    print("  4. gist      — High-uncertainty iterative planning (Goals, Ideas, Step-projects, Tasks)")
    try:
        val = input(f"Enter operating model [1-4 or name] (default: {default}): ").strip().lower()
        model_map = {
            "1": "scrum", "scrum": "scrum",
            "2": "shape-up", "shape-up": "shape-up", "shapeup": "shape-up",
            "3": "kanban", "kanban": "kanban",
            "4": "gist", "gist": "gist"
        }
        return model_map.get(val, default) if val else default
    except (EOFError, KeyboardInterrupt):
        return default

def main():
    parser = argparse.ArgumentParser(
        description="Initialize AI PM Sidekick in Standalone or Embedded Mode",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Initialize standalone workspace and launch GUI:
  python3 scripts/init-workspace.py --mode standalone --open

  # Initialize standalone workspace without starting GUI:
  python3 scripts/init-workspace.py --mode standalone --no-gui

  # Initialize embedded mode in current repository:
  python3 scripts/init-workspace.py --mode embedded

  # Initialize embedded mode with enterprise compliance tier:
  python3 scripts/init-workspace.py --mode embedded --tier enterprise

  # Initialize with Shape Up operating model:
  python3 scripts/init-workspace.py --operating-model shape-up

  # Interactively configure workspace options:
  python3 scripts/init-workspace.py --interactive
        """
    )
    parser.add_argument("--mode", choices=["standalone", "embedded"], default="standalone",
                        help="Operating mode: 'standalone' (PM command center) or 'embedded' (codebase-integrated). Default: standalone")
    parser.add_argument("--tier", choices=["lean", "standard", "enterprise"], default="standard",
                        help="Default deliverable tier (lean, standard, enterprise). Default: standard")
    parser.add_argument("--operating-model", choices=["scrum", "shape-up", "kanban", "gist"], default=None,
                        help="Operating delivery model: 'scrum' (default), 'shape-up', 'kanban', or 'gist'")
    parser.add_argument("-i", "--interactive", action="store_true",
                        help="Prompt interactively for workspace options (mode, tier, operating model)")
    parser.add_argument("--target-dir", default=str(ROOT_DIR),
                        help="Target repository directory to initialize. Default: current workspace")
    parser.add_argument("--no-gui", action="store_true",
                        help="Do not launch the web GUI after initializing (standalone mode only)")
    parser.add_argument("--open", action="store_true",
                        help="Automatically open browser tab when launching web GUI")
    parser.add_argument("--port", type=int, default=3000,
                        help="Port for the PM Command Center GUI server. Default: 3000")
    parser.add_argument("--force", action="store_true",
                        help="Force overwrite existing .context/ templates")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show initialization actions without writing to disk")

    args = parser.parse_args()
    target_path = Path(args.target_dir).resolve()

    mode = args.mode
    tier = args.tier
    operating_model = args.operating_model

    if args.interactive:
        print("\n🚀 AI PM Sidekick — Interactive Workspace Setup")
        print("--------------------------------------------------")
        try:
            mode_input = input(f"Select operating mode [standalone | embedded] (default: {mode}): ").strip().lower()
            if mode_input in ["standalone", "embedded"]:
                mode = mode_input
                
            tier_input = input(f"Select artifact tier [lean | standard | enterprise] (default: {tier}): ").strip().lower()
            if tier_input in ["lean", "standard", "enterprise"]:
                tier = tier_input
        except (EOFError, KeyboardInterrupt):
            pass
            
        operating_model = prompt_operating_model(default=operating_model or "scrum")
    elif operating_model is None:
        operating_model = "scrum"

    result = initialize_workspace(
        target_dir=target_path,
        mode=mode,
        tier=tier,
        operating_model=operating_model,
        force=args.force,
        dry_run=args.dry_run
    )

    if args.dry_run:
        print("\n🔍 Dry run complete. No files written.")
        return

    # In standalone mode, launch the GUI unless --no-gui is specified
    if mode == "standalone" and not args.no_gui:
        if LAUNCHER_SCRIPT.exists():
            print(f"\n🚀 Launching PM Command Center GUI on port {args.port}...")
            cmd = [sys.executable, str(LAUNCHER_SCRIPT), "--port", str(args.port)]
            if args.open:
                cmd.append("--open")
            try:
                subprocess.run(cmd)
            except KeyboardInterrupt:
                print("\nPM Command Center stopped.")
        else:
            print(f"\n⚠️  Launcher script not found at {LAUNCHER_SCRIPT}. Start manually with python3 scripts/launch-ui.py")
    else:
        print(f"\n✨ Workspace initialized in {mode.upper()} mode ({tier.upper()} tier, {operating_model.upper()} model).")
        if mode == "embedded":
            print("💡 The Product Knowledge Core (.context/) is now anchored to this codebase.")
            print("   You can start generating PRDs and User Stories with full architectural context!")
        else:
            print("💡 Start the PM Command Center anytime by running: python3 scripts/launch-ui.py --open")

if __name__ == "__main__":
    main()
