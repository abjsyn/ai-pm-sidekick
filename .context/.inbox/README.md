# Context Memory Inbox (`.context/.inbox/`)

Proposed changes to protected context files (`product.md`, `strategy-and-constraints.md`, `decisions.md`) are staged here as Markdown patch files (`YYYYMMDD-HHMMSS-<skill-name>.md`).

## How to Review

1. **Via UI:** Open `pm-command-center.html` and click **Approve & Merge** or **Discard** in the Context Inbox panel.

2. **Via CLI / Agent:** Run `/compact-context --apply-inbox` or manually move approved sections into the target `.context/*.md` file and delete the staged `.inbox/` file.
