---
id: 1
title: Add Description Column to Task Table
stage: refactor
date: 2025-12-29
surface: agent
model: Claude Sonnet 4.5
feature: console-todo
branch: main
user: user
command: sp.implement
labels: [ui, table, enhancement]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - D:\All Projects\evolution-of-todo\phase-1\src\main.py
tests:
 - D:\All Projects\evolution-of-todo\phase-1\test_description.py
---

## Prompt

@skills/spec-driven-dev @skills/python-uv-ops

**Action: Fix UI - Add Description Column to Task Table**

The user tested the "View Tasks" feature.
**Issue:** The table displays ID, Title, Status, and Priority, but is **missing the Description**.

**Instructions:**
1.  **Edit `src/main.py`**:
    -   Locate the logic for "View Tasks".
    -   Update the `Table` definition to include a column for "Description" (between Title and Status, or after Title).
    -   Ensure the `table.add_row` call includes `task.description`.

**Post-Execution:**
-   Run the app using `uv run src/main.py` to verify the table now has 5 columns.

## Response snapshot

Successfully added the Description column to the task table in main.py. The table now displays 5 columns: ID, Title, Description, Status, and Priority. This was verified by creating a test script that confirmed the table structure now includes the Description column and properly displays task descriptions.

## Outcome

- ✅ Impact: Fixed UI issue by adding missing Description column to task table
- 🧪 Tests: Created temporary test script to verify the 5-column table display
- 📁 Files: Modified main.py to add Description column to table definition and row data
- 🔁 Next prompts: Ready for next implementation tasks
- 🧠 Reflection: The fix was straightforward - just needed to add the column definition and include the description field in the table row data

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - Table now correctly shows 5 columns
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Complete remaining tasks in the task list