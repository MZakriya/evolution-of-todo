---
id: 2
title: Implement Update Delete Operations
stage: refactor
date: 2025-12-29
surface: agent
model: Claude Sonnet 4.5
feature: console-todo
branch: main
user: user
command: sp.implement
labels: [crud, update, delete, ui]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - D:\All Projects\evolution-of-todo\phase-1\src\manager.py
 - D:\All Projects\evolution-of-todo\phase-1\src\main.py
 - D:\All Projects\evolution-of-todo\phase-1\tasks.md
tests:
 - D:\All Projects\evolution-of-todo\phase-1\test_update_delete.py
---

## Prompt

@skills/spec-driven-dev @skills/python-uv-ops

**Action: Execute User Story 3 (Update) & User Story 4 (Delete)**

We need to complete the CRUD operations by allowing users to modify and remove tasks.

**Instructions:**

1.  **Update `src/manager.py` (Logic):**
    -   **Implement `update_task` (T020-T023):**
        -   Arguments: `task_id` (int), `title` (optional), `description` (optional), `priority` (optional).
        -   Logic: Find task by ID. If not found, raise `ValueError`. Update fields if provided.
    -   **Implement `delete_task` (T027-T030):**
        -   Arguments: `task_id` (int).
        -   Logic: Find task by ID. If not found, raise `ValueError`. Remove from list. Returns `True` on success.

2.  **Update `src/main.py` (UI):**
    -   Add Menu Options: `"3. Update Task"`, `"4. Delete Task"`.
    -   **Handle "Update Task" (T024-T026):**
        -   Prompt for Task ID.
        -   Prompt for new Title, Description, Priority (Allow user to press Enter to keep current values).
        -   Call `manager.update_task()`.
        -   Show success message.
    -   **Handle "Delete Task" (T031-T032):**
        -   Prompt for Task ID.
        -   Confirm deletion (y/n).
        -   Call `manager.delete_task()`.
        -   Show success message.

**Post-Execution:**
-   Update `phase-1/tasks.md`: Mark **[x] T020-T032** as complete.
-   Run the app to verify.

## Response snapshot

Successfully implemented Update and Delete functionality for the console todo app:

1. **Updated `src/manager.py`**:
   - Implemented `update_task` method with validation for task ID existence and title emptiness
   - Implemented `delete_task` method with validation for task ID existence
   - Both methods raise ValueError when task ID is not found

2. **Updated `src/main.py`**:
   - Added "Update Task" and "Delete Task" options to the main menu (options 3 and 4)
   - Implemented Update Task functionality with prompts that show current values and allow keeping them with Enter
   - Implemented Delete Task functionality with confirmation prompt (y/n)
   - Updated menu choices to include options 1-5

3. **Updated `phase-1/tasks.md`**:
   - Marked tasks T020-T032 as completed for both User Story 3 (Update) and User Story 4 (Delete)

The implementation was tested and verified to work correctly with a test script that confirmed both update and delete operations function as expected.

## Outcome

- ✅ Impact: Added complete CRUD functionality with Update and Delete operations
- 🧪 Tests: Created and ran test script to verify update and delete functionality
- 📁 Files: Modified manager.py, main.py, and tasks.md files
- 🔁 Next prompts: Ready for next implementation tasks (User Story 5 - Mark Task Status)
- 🧠 Reflection: The implementation follows the same pattern as existing code with proper validation and user feedback

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - Update and delete operations work correctly
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Implement User Story 5 (Mark Task Status)