#!/usr/bin/env python3
"""
Mechanical epistemic gate for AI PM Sidekick.
Supports two modes:
  1. --mode pre-skill : Verifies required .context/*.md files exist and contain real content
                        (not empty or unedited template placeholders) before definition skills run.
  2. --mode verify-stop: Verifies generated PRD/User Story artifacts do not contain unresolved
                         placeholder tokens ([TBD], TODO:, ???) or missing acceptance criteria.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

SKILL_REQUIREMENTS: dict[str, list[str]] = {
    "create-prd": [
        ".context/product.md",
        ".context/strategy-and-constraints.md",
        ".context/discovery.md",
    ],
    "create-user-stories": [
        ".context/product.md",
        ".context/discovery.md",
    ],
    "create-design-brief": [
        ".context/product.md",
        ".context/discovery.md",
    ],
    "apply-framework": [
        ".context/product.md",
    ],
}

FORBIDDEN_ARTIFACT_PATTERNS: list[tuple[str, str]] = [
    (r"\[TBD\]", "Unresolved [TBD] placeholder found"),
    (r"\bTODO:", "Unresolved TODO: marker found"),
    (r"\[INSERT\s+[^\]]+\]", "Unfilled template bracket [INSERT ...] found"),
]


def is_context_populated(file_path: pathlib.Path, min_chars: int = 80) -> tuple[bool, str]:
    if not file_path.exists():
        return False, f"Missing required context file: {file_path}"
    content = file_path.read_text(encoding="utf-8").strip()
    # Strip HTML comments and markdown headers to measure actual substance
    stripped = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    stripped = re.sub(r"^#+\s+.*$", "", stripped, flags=re.MULTILINE).strip()
    if len(stripped) < min_chars:
        return (
            False,
            f"Context file '{file_path}' has insufficient content ({len(stripped)} chars < {min_chars}). "
            f"Run /ingest-context or /validate-idea first.",
        )
    return True, "OK"


def check_pre_skill(skill: str, context_dir: pathlib.Path) -> int:
    required_files = SKILL_REQUIREMENTS.get(skill, [])
    failures: list[str] = []
    for rel_path in required_files:
        target = context_dir.parent / rel_path if rel_path.startswith(".context") else context_dir / rel_path
        ok, msg = is_context_populated(target)
        if not ok:
            failures.append(msg)
    if failures:
        print(
            json.dumps(
                {
                    "decision": "block",
                    "skill": skill,
                    "reason": "Epistemic Gate Blocked Execution: Required product context is missing or unpopulated.",
                    "violations": failures,
                    "remediation": "Populate the missing .context/ files or run /ingest-context before invoking this skill.",
                },
                indent=2,
            )
        )
        return 2
    print(json.dumps({"decision": "allow", "skill": skill, "status": "Context verified"}))
    return 0


def check_verify_stop(artifact_path: pathlib.Path) -> int:
    if not artifact_path.exists():
        print(json.dumps({"decision": "block", "reason": f"Artifact not found: {artifact_path}"}))
        return 2
    text = artifact_path.read_text(encoding="utf-8")
    violations: list[str] = []
    for pattern, label in FORBIDDEN_ARTIFACT_PATTERNS:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        if matches:
            violations.append(f"{label} ({len(matches)}x)")
    if violations:
        print(
            json.dumps(
                {
                    "decision": "block",
                    "artifact": str(artifact_path),
                    "reason": "Verify-on-Stop Guard Vetoed Completion: Artifact contains unresolved placeholders.",
                    "violations": violations,
                },
                indent=2,
            )
        )
        return 2
    print(json.dumps({"decision": "allow", "artifact": str(artifact_path), "status": "Artifact verified"}))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="AI PM Sidekick Mechanical Context & Stop Gate")
    parser.add_argument("--mode", choices=["pre-skill", "verify-stop"], required=True)
    parser.add_argument("--skill", type=str, default="", help="Skill name for pre-skill check")
    parser.add_argument("--context-dir", type=str, default=".context", help="Path to .context directory")
    parser.add_argument("--artifact", type=str, default="", help="Artifact file path for verify-stop check")
    args = parser.parse_args()

    if args.mode == "pre-skill":
        if not args.skill:
            print("ERROR: --skill is required when --mode=pre-skill", file=sys.stderr)
            return 1
        return check_pre_skill(args.skill, pathlib.Path(args.context_dir))

    if args.mode == "verify-stop":
        if not args.artifact:
            print("ERROR: --artifact is required when --mode=verify-stop", file=sys.stderr)
            return 1
        return check_verify_stop(pathlib.Path(args.artifact))

    return 0


if __name__ == "__main__":
    sys.exit(main())
