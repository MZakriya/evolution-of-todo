---
id: 11
title: View Tasks Implementation
stage: tasks
date: 2025-12-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: console-todo
branch: master
user: user
command: sp.implement
labels: [implementation,tasks,view,phase4]
links:
  spec: phase-1/specs/001_console_mvp.md
  plan: phase-1/plan.md
  tasks: phase-1/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - phase-1/src/manager.py
 - phase-1/src/main.py
 - phase-1/tasks.md
tests:
 - none
---

## Prompt

@skills/spec-driven-dev @skills/python-uv-ops

**Action: Execute User Story 2: View Tasks (Tasks T015 - T019)**

We need to visualize the tasks stored in memory.

**Instructions:**
1.  **Update `src/manager.py` (T015-T016):**
    -   Implement `get_all_tasks(self)` method.
    -   It should return the list of tasks. (Ordering by creation time is automatic since it's a list).

2.  **Update `src/main.py` (T017-T019):**
    -   Add a new option in the Main Menu: `"2. View Tasks"`.
    -   **Implement Display Logic:**
        -   Call `manager.get_all_tasks()`.
        -   **If list is empty:** Print a message "No tasks found" (T018).
        -   **If list has tasks:**
            -   Create a `rich.table.Table`.
            -   Columns: ID, Title, Status, Priority.
            -   Loop through tasks and add rows to the table.
            -   Colorize the output (e.g., Green for Done, Red for High Priority) if possible.
            -   Print the table to the console.

**Post-Execution:**
-   Update `phase-1/tasks.md`: Mark **[x] T015** through **[x] T019** as complete.
-   Don't break the existing "Add Task" functionality.

## Response snapshot

Successfully implemented User Story 2: View Tasks (Tasks T015-T019):

**Tasks Executed:**
- ✅ **T015** - Implement get_all_tasks method in TodoManager
- ✅ **T016** - Ensure tasks are returned in creation order
- ✅ **T017** - Create CLI menu option for viewing tasks
- ✅ **T018** - Display "no tasks" message when task list is empty
- ✅ **T019** - Format task display with rich library (ID, title, description, status, priority)

**Files Updated:**
- `phase-1/src/manager.py` - Added `get_all_tasks()` method
- `phase-1/src/main.py` - Added View Tasks menu option and display logic with rich formatting and colorization
- `phase-1/tasks.md` - Updated to mark tasks T015-T019 as complete

**Features Implemented:**
- New "View Tasks" option in the main menu
- Proper display of all tasks in a rich table format
- Colorized output based on task status and priority
- "No tasks found" message when the list is empty
- Maintained existing "Add Task" functionality

The View Tasks functionality is now fully implemented and integrated with the existing application.

## Outcome

- ✅ Impact: Completed View Tasks functionality for console todo app
- 🧪 Tests: none
- 📁 Files: Updated manager.py and main.py with view functionality
- 🔁 Next prompts: Ready for Update Task functionality (Phase 5)
- 🧠 Reflection: View tasks properly implemented with rich formatting and colorization

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Test the view functionality with some tasks