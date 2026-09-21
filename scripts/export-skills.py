#!/usr/bin/env python3
"""
AI PM Sidekick — Cross-Tool Skill Exporter
Exports skills defined in `skills/` to target AI tool formats:
  - AGY / Gemini (`.agents/skills/`)
  - Cursor (`.cursor/rules/`)
  - Claude Code / Claude Projects (`.claude/commands/`)
  - All-in-one Markdown bundle (`dist/pm_sidekick_system_prompt.md`)
"""

import os
import shutil
import re
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.resolve()
SKILLS_DIR = ROOT_DIR / "skills"
TEMPLATES_DIR = ROOT_DIR / "templates"
DIST_DIR = ROOT_DIR / "dist"

def parse_skill_file(skill_path):
    content = skill_path.read_text(encoding="utf-8")
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not frontmatter_match:
        return {"name": skill_path.parent.name, "description": "", "body": content}
    
    yaml_text, body = frontmatter_match.groups()
    name_match = re.search(r"^name:\s*(.+)$", yaml_text, re.MULTILINE)
    desc_match = re.search(r"^description:\s*>(.+?)(?=\n[a-z]+:|\Z)", yaml_text, re.DOTALL)
    if not desc_match:
        desc_match = re.search(r"^description:\s*(.+)$", yaml_text, re.MULTILINE)
        
    name = name_match.group(1).strip() if name_match else skill_path.parent.name
    desc = desc_match.group(1).strip().replace("\n", " ") if desc_match else ""
    return {"name": name, "description": desc, "body": body.strip(), "full_content": content}

def export_to_agy(skills):
    target_dir = ROOT_DIR / ".agents" / "skills"
    target_dir.mkdir(parents=True, exist_ok=True)
    for s in skills:
        skill_folder = target_dir / s["name"]
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
        (target_dir / f"{s['name']}.mdc").write_text(mdc_content, encoding="utf-8")
    print(f"✅ Exported {len(skills)} rules to Cursor rules folder: {target_dir}")

def export_to_claude(skills):
    target_dir = ROOT_DIR / ".claude" / "commands"
    target_dir.mkdir(parents=True, exist_ok=True)
    for s in skills:
        cmd_content = f"# Command: /{s['name']}\n\n{s['description']}\n\n{s['body']}"
        (target_dir / f"{s['name']}.md").write_text(cmd_content, encoding="utf-8")
    print(f"✅ Exported {len(skills)} commands to Claude folder: {target_dir}")

def export_bundle(skills):
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    bundle_path = DIST_DIR / "pm_sidekick_system_prompt.md"
    bundle_text = "# 🚀 AI PM Sidekick — System Prompt & Skill Bundle\n\n"
    bundle_text += "This bundle contains all AI PM Sidekick skills for use as a Custom GPT or Claude Project system prompt.\n\n"
    for s in skills:
        bundle_text += f"## Skill: {s['name']}\n**Description**: {s['description']}\n\n{s['body']}\n\n---\n\n"
    bundle_path.write_text(bundle_text, encoding="utf-8")
    print(f"✅ Exported single prompt bundle: {bundle_path}")

def main():
    if not SKILLS_DIR.exists():
        print(f"Error: Skills directory not found at {SKILLS_DIR}")
        return
    
    skills = []
    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skills.append(parse_skill_file(skill_file))
        
    print(f"Found {len(skills)} canonical skills.")
    export_to_agy(skills)
    export_to_cursor(skills)
    export_to_claude(skills)
    export_bundle(skills)
    print("\n🎉 All skill exports completed successfully!")

if __name__ == "__main__":
    main()
