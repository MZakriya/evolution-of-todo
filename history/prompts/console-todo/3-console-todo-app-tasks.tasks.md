---
id: 3
title: Console Todo App Tasks
stage: tasks
date: 2025-12-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: console-todo
branch: master
user: user
command: sp.tasks
labels: [tasks,console,todo,phase1]
links:
  spec: phase-1/specs/001_console_mvp.md
  plan: phase-1/plan.md
  ticket: null
  adr: null
  pr: null
files:
 - phase-1/tasks.md
tests:
 - pytest requirements for todo features
---

## Prompt

@skills/project-management

Great. We have the Spec and the Plan.
Now, break down the `phase-1/plan.md` into granular, actionable **Tasks**.

**Requirement:**
1. Create a file `phase-1/tasks.md`.
2. List tasks in a logical order (e.g., Setup -> Models -> Logic -> UI -> Tests).
3. Each task should be small enough to be implemented in a single turn.
4. Add a "Status" checkbox for each task (e.g., - [ ] Task Name).

**Example Format for tasks.md:**
- [ ] **Task 1:** Initialize project and create `src/main.py` entry point.
- [ ] **Task 2:** Create `Task` data model in `src/models.py`.
- [ ] **Task 3:** Implement `TaskManager` class with Add/Delete methods.
...

## Response snapshot

# Console Todo App - Tasks

## Feature: Console Todo App (Phase I of "Evolution of Todo" project)

## Phase 1: Setup
**Goal:** Initialize project structure and dependencies

- [ ] T001 Create project directory structure with src/, tests/, and pyproject.toml
- [ ] T002 Set up pyproject.toml with Python 3.13+ requirement and dependencies (rich, pytest)
- [ ] T003 Initialize git repository with proper .gitignore for Python project

## Phase 2: Foundational
**Goal:** Create foundational components that all user stories depend on

- [ ] T004 Create Task entity with id, title, description, status, and priority attributes
- [ ] T005 Implement Task validation logic (title not empty, valid status/priority enums)
- [ ] T006 Create Status and Priority enum classes
- [ ] T007 Create TodoManager class with in-memory storage (list/dict)

## Phase 3: User Story 1 - Add Task [US1]
**Goal:** Allow users to create new tasks with title, description, priority, and status
**Independent Test Criteria:** User can add a task with all required information and see it assigned a unique ID

- [ ] T008 [US1] Implement create_task method in TodoManager with validation
- [ ] T009 [US1] Add auto-generated unique ID assignment for new tasks
- [ ] T010 [US1] Set initial status to "incomplete" for new tasks
- [ ] T011 [US1] Validate that task title is not empty before creation
- [ ] T012 [US1] Create CLI menu option for adding tasks
- [ ] T013 [US1] Implement user prompts for task creation (title, description, priority)
- [ ] T014 [US1] Display confirmation message after task creation

## Phase 4: User Story 2 - View Tasks [US2]
**Goal:** Allow users to view all tasks in a formatted list with all required information
**Independent Test Criteria:** User can see all tasks with ID, title, description, status, and priority in creation order

- [ ] T015 [US2] Implement get_all_tasks method in TodoManager
- [ ] T016 [US2] Ensure tasks are returned in creation order
- [ ] T017 [US2] Create CLI menu option for viewing tasks
- [ ] T018 [US2] Display "no tasks" message when task list is empty
- [ ] T019 [US2] Format task display with rich library (ID, title, description, status, priority)

## Phase 5: User Story 3 - Update Task [US3]
**Goal:** Allow users to update task title, description, and priority
**Independent Test Criteria:** User can update existing task attributes with proper validation and feedback

- [ ] T020 [US3] Implement update_task method in TodoManager with validation
- [ ] T021 [US3] Validate task ID exists before attempting update
- [ ] T022 [US3] Validate title is not empty during update
- [ ] T023 [US3] Provide clear feedback when update is successful
- [ ] T024 [US3] Create CLI menu option for updating tasks
- [ ] T025 [US3] Implement user prompts for task update (ID, new title, description, priority)
- [ ] T026 [US3] Validate user-entered task ID exists before update

## Phase 6: User Story 4 - Delete Task [US4]
**Goal:** Allow users to delete tasks by ID with confirmation
**Independent Test Criteria:** User can delete existing tasks with confirmation and receive success feedback

- [ ] T027 [US4] Implement delete_task method in TodoManager with validation
- [ ] T028 [US4] Validate task ID exists before attempting deletion
- [ ] T029 [US4] Ask for confirmation before deleting a task
- [ ] T030 [US4] Provide clear feedback when deletion is successful
- [ ] T031 [US4] Create CLI menu option for deleting tasks
- [ ] T032 [US4] Implement user prompts for task deletion (ID) with confirmation

## Phase 7: User Story 5 - Mark Task Status [US5]
**Goal:** Allow users to mark tasks as complete or incomplete
**Independent Test Criteria:** User can change task status with validation and receive success feedback

- [ ] T033 [US5] Implement update_task_status method in TodoManager
- [ ] T034 [US5] Validate task ID exists before attempting status change
- [ ] T035 [US5] Validate status is a valid enum value
- [ ] T036 [US5] Provide clear feedback when status change is successful
- [ ] T037 [US5] Create CLI menu option for marking task status
- [ ] T038 [US5] Implement user prompts for status change (ID, new status)

## Phase 8: User Story 6 - Main Menu Interface [US6]
**Goal:** Present a main menu with all task operations that loops until user exits
**Independent Test Criteria:** User can navigate main menu and return to it after operations

- [ ] T039 [US6] Create main application loop that continuously displays menu
- [ ] T040 [US6] Implement main menu with options for all task operations
- [ ] T041 [US6] Add exit option to main menu
- [ ] T042 [US6] Return to main menu after each operation completes
- [ ] T043 [US6] Handle invalid menu selections with appropriate error messages

## Phase 9: User Story 7 - Input Validation [US7]
**Goal:** Validate user inputs and handle errors gracefully
**Independent Test Criteria:** Invalid inputs are caught with helpful error messages and user is re-prompted

- [ ] T044 [US7] Implement input validation for all user inputs
- [ ] T045 [US7] Display helpful error messages for invalid inputs
- [ ] T046 [US7] Re-prompt users after displaying error messages
- [ ] T047 [US7] Handle invalid task IDs with appropriate error handling
- [ ] T048 [US7] Validate priority values are from the allowed enum
- [ ] T049 [US7] Handle empty title inputs during task creation

## Phase 10: Testing
**Goal:** Implement comprehensive tests for all functionality

- [ ] T050 Write unit tests for Task model validation
- [ ] T051 Write unit tests for TodoManager CRUD operations
- [ ] T052 Write integration tests for CLI flow
- [ ] T053 Write tests for error handling scenarios
- [ ] T054 Write tests for data validation requirements
- [ ] T055 Test success criteria (response times, error handling, uptime)

## Phase 11: Polish & Cross-Cutting Concerns
**Goal:** Finalize the application with proper error handling and user experience

- [ ] T056 Ensure 2-second response time for all inputs
- [ ] T057 Verify 99% uptime during usage (no crashes)
- [ ] T058 Test error handling prevents crashes (99% success rate)
- [ ] T059 Implement graceful shutdown when user exits
- [ ] T060 Add proper exception handling throughout the application
- [ ] T061 Finalize UI with rich library for enhanced console experience

## Dependencies
- T001-T007 must be completed before any user story tasks
- Each user story can be developed independently after foundational tasks

## Parallel Execution Opportunities
- [P] T008-T014 [US1] and T015-T019 [US2] can be developed in parallel (different functionality)
- [P] T020-T026 [US3] and T027-T032 [US4] can be developed in parallel (both update operations)
- [P] T033-T038 [US5] and T039-T043 [US6] can be developed in parallel (status change and menu)

## Implementation Strategy
- MVP Scope: Complete US1 (Add Task) and US2 (View Tasks) for basic functionality
- Incremental Delivery: Each user story adds complete, testable functionality
- Test-Driven Development: Each task includes validation of requirements

## Outcome

- ✅ Impact: Created granular, actionable task breakdown for console todo app
- 🧪 Tests: Defined comprehensive testing approach across multiple phases
- 📁 Files: Created tasks.md with 61 individual tasks organized by user story
- 🔁 Next prompts: Ready for implementation of individual tasks
- 🧠 Reflection: Tasks are organized logically and follow the checklist format

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation of foundational tasks