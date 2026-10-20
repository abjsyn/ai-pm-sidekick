#!/usr/bin/env python3
"""
AI PM Sidekick — MCP Connection & Setup Utility
Configures MCP (Model Context Protocol) servers for external PM tools:
  - Atlassian (Jira & Confluence)
  - Figma
  - Miro

Target AI environments:
  - AGY / Antigravity (.agents/mcp.json or ~/.gemini/antigravity-cli/mcp.json)
  - Claude Code (.claude/mcp.json or ~/.claude.json)
  - Cursor (.cursor/mcp.json)
"""

import os
import sys
import json
import argparse
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.resolve()

DEFAULT_CONFIG = {
    "mcpServers": {
        "atlassian": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-atlassian"],
            "env": {
                "ATLASSIAN_HOST": "${ATLASSIAN_HOST}",
                "ATLASSIAN_EMAIL": "${ATLASSIAN_EMAIL}",
                "ATLASSIAN_API_TOKEN": "${ATLASSIAN_API_TOKEN}"
            }
        },
        "github": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": {
                "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}",
                "GITHUB_OWNER": "${GITHUB_OWNER}",
                "GITHUB_REPO": "${GITHUB_REPO}"
            }
        },
        "figma": {
            "command": "npx",
            "args": ["-y", "@figma/mcp"],
            "env": {
                "FIGMA_ACCESS_TOKEN": "${FIGMA_ACCESS_TOKEN}"
            }
        },
        "miro": {
            "command": "npx",
            "args": ["-y", "mcp-server-miro"],
            "env": {
                "MIRO_ACCESS_TOKEN": "${MIRO_ACCESS_TOKEN}"
            }
        },
        "notion": {
            "command": "npx",
            "args": ["-y", "@notionhq/notion-mcp-server"],
            "env": {
                "NOTION_API_TOKEN": "${NOTION_API_TOKEN}",
                "NOTION_ROOT_PAGE_ID": "${NOTION_ROOT_PAGE_ID}"
            }
        },
        "stitch": {
            "command": "npx",
            "args": ["-y", "@_davideast/stitch-mcp", "proxy"],
            "env": {
                "STITCH_API_KEY": "${STITCH_API_KEY}"
            }
        },
        "linear": {
            "command": "npx",
            "args": ["-y", "mcp-server-linear"],
            "env": {
                "LINEAR_API_KEY": "${LINEAR_API_KEY}"
            }
        }
    }
}

ENV_TEMPLATE = """# AI PM Sidekick — MCP Integration Credentials
# Fill in your API credentials below. Do NOT commit real secrets to Git.

# --- Atlassian (Jira & Confluence) ---
ATLASSIAN_HOST=https://your-domain.atlassian.net
ATLASSIAN_EMAIL=user@company.com
ATLASSIAN_API_TOKEN=your_atlassian_api_token_here

# --- GitHub Issues & Milestones ---
GITHUB_PERSONAL_ACCESS_TOKEN=your_github_personal_access_token_here
GITHUB_OWNER=your_github_username_or_org
GITHUB_REPO=your_github_repo_name

# --- Figma ---
FIGMA_ACCESS_TOKEN=your_figma_personal_access_token_here

# --- Miro ---
MIRO_ACCESS_TOKEN=your_miro_access_token_here

# --- Notion (Product Wiki & Databases) ---
NOTION_API_TOKEN=your_notion_api_token_here
NOTION_ROOT_PAGE_ID=your_notion_root_page_id_here

# --- Google Stitch ---
STITCH_API_KEY=your_stitch_api_key_here

# --- Linear (Cycles, Projects & Issues) ---
LINEAR_API_KEY=your_linear_api_key_here

# --- User Profile & PM Persona ---
USER_NAME=Paula (Lead PM)
USER_EMAIL=paula.pm@company.com
DEFAULT_PERSONA=paula

# --- Skill Execution Defaults ---
DEFAULT_PRD_MODE=standard
DEFAULT_AC_FORMAT=gherkin
DEFAULT_STORY_SCALE=fibonacci
DEFAULT_UI_THEME=stitch
"""

def load_env_file(env_path):
    env_vars = {}
    if not env_path.exists():
        return env_vars
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                env_vars[k.strip()] = v.strip().strip("'\"")
    return env_vars

def substitute_env(val, env_map):
    if isinstance(val, str) and val.startswith("${") and val.endswith("}"):
        var_name = val[2:-1]
        return env_map.get(var_name, os.environ.get(var_name, val))
    return val

def resolve_config(config, env_map):
    resolved = json.loads(json.dumps(config))
    for server_name, server_cfg in resolved.get("mcpServers", {}).items():
        if "env" in server_cfg:
            for k, v in server_cfg["env"].items():
                server_cfg["env"][k] = substitute_env(v, env_map)
    return resolved

def get_target_paths(target):
    paths = []
    if target in ("agy", "all"):
        paths.append(ROOT_DIR / ".agents" / "mcp.json")
    if target in ("claude", "all"):
        paths.append(ROOT_DIR / ".claude" / "mcp.json")
    if target in ("cursor", "all"):
        paths.append(ROOT_DIR / ".cursor" / "mcp.json")
    if target in ("root", "all"):
        paths.append(ROOT_DIR / "mcp.json")
    return paths

def create_env_example():
    env_example_path = ROOT_DIR / ".env.example"
    if not env_example_path.exists():
        env_example_path.write_text(ENV_TEMPLATE, encoding="utf-8")
        print(f"📄 Created template environment file: {env_example_path}")

def check_status():
    print("🔍 Checking MCP Environment Readiness...\n")
    
    # Check Node / NPX
    import shutil
    npx_path = shutil.which("npx")
    node_path = shutil.which("node")
    print(f"  • Node.js executable: {'✅ ' + node_path if node_path else '❌ Not found (Required for MCP servers)'}")
    print(f"  • NPX executable:     {'✅ ' + npx_path if npx_path else '❌ Not found (Required for MCP servers)'}")
    
    # Check Env vars
    env_path = ROOT_DIR / ".env"
    env_vars = load_env_file(env_path) if env_path.exists() else {}
    
    req_vars = {
        "Atlassian": ["ATLASSIAN_HOST", "ATLASSIAN_EMAIL", "ATLASSIAN_API_TOKEN"],
        "GitHub": ["GITHUB_PERSONAL_ACCESS_TOKEN", "GITHUB_OWNER", "GITHUB_REPO"],
        "Figma": ["FIGMA_ACCESS_TOKEN"],
        "Miro": ["MIRO_ACCESS_TOKEN"],
        "Notion": ["NOTION_API_TOKEN"],
        "Google Stitch": ["STITCH_API_KEY"]
    }
    
    print("\n🔐 Credential Check:")
    for tool, vars_list in req_vars.items():
        missing = [v for v in vars_list if not env_vars.get(v) and not os.environ.get(v) or env_vars.get(v, "").startswith("your_")]
        if not missing:
            print(f"  • {tool:<14}: ✅ All credentials configured")
        else:
            print(f"  • {tool:<14}: ⚠️  Missing or default: {', '.join(missing)}")
            
    print("\n📁 Checking Target Configuration Files:")
    for p in [ROOT_DIR / ".agents" / "mcp.json", ROOT_DIR / ".claude" / "mcp.json", ROOT_DIR / ".cursor" / "mcp.json", ROOT_DIR / "mcp.json"]:
        if p.exists():
            print(f"  • {p.relative_to(ROOT_DIR)}: ✅ Present")
        else:
            print(f"  • {p.relative_to(ROOT_DIR)}: ❌ Not created yet")

def main():
    parser = argparse.ArgumentParser(description="Configure MCP integrations for AI PM Sidekick.")
    parser.add_argument("--target", choices=["agy", "claude", "cursor", "root", "all"], default="all",
                        help="Target AI environment configuration file (default: all)")
    parser.add_argument("--tool", choices=["atlassian", "github", "figma", "miro", "notion", "stitch", "linear", "all"], default="all",
                        help="Specific tool integration to enable (default: all)")
    parser.add_argument("--check", action="store_true", help="Check setup readiness and credentials")
    parser.add_argument("--interactive", action="store_true", help="Prompt interactively for credentials")
    args = parser.parse_args()

    create_env_example()

    if args.check:
        check_status()
        return

    env_path = ROOT_DIR / ".env"
    env_vars = load_env_file(env_path) if env_path.exists() else {}

    if args.interactive:
        print("\n⚙️  Interactive MCP Connection Setup\n")
        
        # Atlassian
        if args.tool in ("atlassian", "all"):
            print("--- Atlassian (Jira & Confluence) Setup ---")
            host = input(f"Atlassian Host [{env_vars.get('ATLASSIAN_HOST', 'https://your-domain.atlassian.net')}]: ").strip()
            if host: env_vars['ATLASSIAN_HOST'] = host
            email = input(f"Atlassian Email [{env_vars.get('ATLASSIAN_EMAIL', 'user@company.com')}]: ").strip()
            if email: env_vars['ATLASSIAN_EMAIL'] = email
            token = input(f"Atlassian API Token [{env_vars.get('ATLASSIAN_API_TOKEN', '')}]: ").strip()
            if token: env_vars['ATLASSIAN_API_TOKEN'] = token

        # GitHub
        if args.tool in ("github", "all"):
            print("\n--- GitHub (Issues & Milestones) Setup ---")
            gh_token = input(f"GitHub Personal Access Token [{env_vars.get('GITHUB_PERSONAL_ACCESS_TOKEN', '')}]: ").strip()
            if gh_token: env_vars['GITHUB_PERSONAL_ACCESS_TOKEN'] = gh_token
            gh_owner = input(f"GitHub Owner/Org [{env_vars.get('GITHUB_OWNER', '')}]: ").strip()
            if gh_owner: env_vars['GITHUB_OWNER'] = gh_owner
            gh_repo = input(f"GitHub Repo Name [{env_vars.get('GITHUB_REPO', '')}]: ").strip()
            if gh_repo: env_vars['GITHUB_REPO'] = gh_repo

        # Figma
        if args.tool in ("figma", "all"):
            print("\n--- Figma Setup ---")
            figma_token = input(f"Figma Personal Access Token [{env_vars.get('FIGMA_ACCESS_TOKEN', '')}]: ").strip()
            if figma_token: env_vars['FIGMA_ACCESS_TOKEN'] = figma_token

        # Miro
        if args.tool in ("miro", "all"):
            print("\n--- Miro Setup ---")
            miro_token = input(f"Miro Access Token [{env_vars.get('MIRO_ACCESS_TOKEN', '')}]: ").strip()
            if miro_token: env_vars['MIRO_ACCESS_TOKEN'] = miro_token

        # Notion
        if args.tool in ("notion", "all"):
            print("\n--- Notion (Product Wiki & Databases) Setup ---")
            notion_token = input(f"Notion Integration Token [{env_vars.get('NOTION_API_TOKEN', '')}]: ").strip()
            if notion_token: env_vars['NOTION_API_TOKEN'] = notion_token
            notion_page = input(f"Notion Root Page/Database ID [{env_vars.get('NOTION_ROOT_PAGE_ID', '')}]: ").strip()
            if notion_page: env_vars['NOTION_ROOT_PAGE_ID'] = notion_page

        # Google Stitch
        if args.tool in ("stitch", "all"):
            print("\n--- Google Stitch Setup ---")
            stitch_key = input(f"Google Stitch API Key [{env_vars.get('STITCH_API_KEY', '')}]: ").strip()
            if stitch_key: env_vars['STITCH_API_KEY'] = stitch_key

        # Linear
        if args.tool in ("linear", "all"):
            print("\n--- Linear (Cycles, Projects & Issues) Setup ---")
            linear_key = input(f"Linear API Key [{env_vars.get('LINEAR_API_KEY', '')}]: ").strip()
            if linear_key: env_vars['LINEAR_API_KEY'] = linear_key

        # Save to .env
        env_content = "\n".join([f"{k}={v}" for k, v in env_vars.items()])
        env_path.write_text(env_content + "\n", encoding="utf-8")
        print(f"\n✅ Credentials saved to {env_path}\n")

    # Filter tools if requested
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if args.tool != "all":
        config["mcpServers"] = {k: v for k, v in config["mcpServers"].items() if k == args.tool}

    resolved_config = resolve_config(config, env_vars)

    target_paths = get_target_paths(args.target)
    for p in target_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(resolved_config, indent=2) + "\n", encoding="utf-8")
        print(f"🚀 Exported MCP config to: {p}")

    print("\n🎉 MCP Configuration Complete!")
    print("Run `python3 scripts/setup-mcp.py --check` anytime to inspect connection status.")

if __name__ == "__main__":
    main()
