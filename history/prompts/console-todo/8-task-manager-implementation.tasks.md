---
id: 8
title: Task Manager Implementation
stage: tasks
date: 2025-12-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: console-todo
branch: master
user: user
command: sp.implement
labels: [implementation,manager,logic,phase2,phase3]
links:
  spec: phase-1/specs/001_console_mvp.md
  plan: phase-1/plan.md
  tasks: phase-1/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - phase-1/src/manager.py
 - phase-1/tasks.md
tests:
 - none
---

## Prompt

@skills/spec-driven-dev @skills/python-uv-ops

**Action: Execute Phase 2 (T007) and Phase 3 Logic (T008, T009, T010, T011)**

We need to implement the core Logic Manager and the "Add Task" functionality.

**Instructions:**
1.  **Create File:** Create `phase-1/src/manager.py`.
2.  **Imports:** Import `Task`, `Status`, `Priority` from `.models`.
3.  **Implement `TodoManager` Class (T007):**
    -   Initialize an empty list/dict to store tasks in `__init__`.
4.  **Implement `add_task` Method (T008 - T011):**
    -   **Signature:** `add_task(self, title: str, description: str, priority: Priority)` -> `Task`
    -   **Validation (T011):** Check if `title` is empty (raise ValueError).
    -   **Auto ID (T009):** Generate a unique ID (simple counter or max_id + 1).
    -   **Default Status (T010):** Set status to `Status.TODO` (or Incomplete) by default.
    -   **Storage:** Create the `Task` object and append it to the internal list.
    -   **Return:** Return the created `Task` object.

**Post-Execution:**
-   Update `phase-1/tasks.md`: Mark **[x] T007** through **[x] T011** as complete.
-   Show the code for `src/manager.py`.

## Response snapshot

Successfully completed the requested tasks for implementing the TodoManager and Add Task functionality:

**Tasks Executed:**
- ✅ **T007** - Create TodoManager class with in-memory storage (list/dict)
- ✅ **T008** - Implement create_task method in TodoManager with validation
- ✅ **T009** - Add auto-generated unique ID assignment for new tasks
- ✅ **T010** - Set initial status to "incomplete" for new tasks
- ✅ **T011** - Validate that task title is not empty before creation

**File Created:**
- `phase-1/src/manager.py` containing:
  - `TodoManager` class with in-memory storage using a list
  - `add_task` method that implements all required functionality:
    - Validates that title is not empty
    - Generates unique IDs automatically using a counter
    - Sets default status to `Status.TODO`
    - Creates and stores the Task object
    - Returns the created Task object

**Verification:**
- Updated `phase-1/tasks.md` to mark T007-T011 as complete ([X])

The core logic for task management is now implemented with proper validation and unique ID generation.

## Outcome

- ✅ Impact: Completed task manager implementation for console todo app
- 🧪 Tests: none
- 📁 Files: Created manager.py with TodoManager and add_task functionality
- 🔁 Next prompts: Ready for CLI menu implementation (Task T012-T014)
- 🧠 Reflection: Manager properly implemented with validation and unique ID generation

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation of CLI menu for adding tasks (Task T012-T014)