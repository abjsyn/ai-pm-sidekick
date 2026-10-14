# Command: /sync-miro

Exports SCAMPER, HMW, 6 Thinking Hats brainstorm sessions, and outcome roadmaps directly to Miro visual whiteboards via Miro MCP integration.

# 🧠 Miro Whiteboard Sync Skill

## Overview
The `sync-miro` skill bridges AI PM Sidekick brainstorming (`brainstorm`) and roadmap planning directly into Miro visual whiteboards using Model Context Protocol (MCP). It turns text concepts into organized color-coded sticky notes, cards, and shapes on Miro boards.

---

## 🛠️ Step-by-Step Execution Workflow

1. **Verify Miro MCP Connection**:
   - Check `MIRO_ACCESS_TOKEN`.
   - If missing, prompt user to run `/connect-mcp` or `python3 scripts/setup-mcp.py`.

2. **Select Board & Target Structure**:
   - Prompt user for **Miro Board ID** or choose to create a **New Miro Board**.
   - Select layout style:
     - **Brainstorm Matrix**: SCAMPER categories, How Might We (HMW) clusters, 6 Thinking Hats.
     - **2x2 Matrix**: Value vs. Effort quadrants.
     - **Roadmap Grid**: Now / Next / Later lanes.

3. **Execute Miro MCP Calls**:
   - `miro_create_board` (if creating a new board).
   - `miro_create_sticky_note` with color mapping:
     - 🟡 Yellow: Ideas / Opportunities
     - 🟢 Green: High Value / Low Effort
     - 🔴 Red: Risks / Constraints / Black Hat
     - 🔵 Blue: Process / Next Steps
   - Position elements in grid/matrix layout.

4. **Deliver Board URL**:
   - Provide direct link to open and view the Miro whiteboard.

---

## 🔄 Flow Handling & Next Skill Suggestions
- **Next Step 1 (Validate Winner Idea)**: "Would you like to evaluate the top brainstorm idea using `validate-idea`?"
- **Next Step 2 (Draft PRD)**: "Would you like to turn these Miro concepts into a PRD using `create-prd`?"