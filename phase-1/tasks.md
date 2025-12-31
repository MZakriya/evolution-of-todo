# Console Todo App - Tasks

## Feature: Console Todo App (Phase I of "Evolution of Todo" project)

## Phase 1: Setup
**Goal:** Initialize project structure and dependencies for in-memory console app

- [X] T001 Create project directory structure with src/, tests/, and pyproject.toml for console app
- [X] T002 Set up pyproject.toml with Python 3.13+ requirement and dependencies (rich, pytest)
- [X] T003 Initialize git repository with proper .gitignore for Python console app

## Phase 2: Foundational
**Goal:** Create foundational components that all user stories depend on

- [X] T004 Create Task entity with id, title, description, status, and priority attributes
- [X] T005 Implement Task validation logic (title not empty, valid status/priority enums)
- [X] T006 Create Status and Priority enum classes for console app
- [X] T007 Create TodoManager class with in-memory storage (list/dict) for console app

## Phase 3: User Story 1 - Add Task [US1]
**Goal:** Allow users to create new tasks with title, description, priority, and status
**Independent Test Criteria:** User can add a task with all required information and see it assigned a unique ID

- [X] T008 [US1] Implement create_task method in TodoManager with validation
- [X] T009 [US1] Add auto-generated unique ID assignment for new tasks
- [X] T010 [US1] Set initial status to "incomplete" for new tasks
- [X] T011 [US1] Validate that task title is not empty before creation
- [X] T012 [US1] Create CLI menu option for adding tasks
- [X] T013 [US1] Implement user prompts for task creation (title, description, priority)
- [X] T014 [US1] Display confirmation message after task creation

## Phase 4: User Story 2 - View Tasks [US2]
**Goal:** Allow users to view all tasks in a formatted list with all required information
**Independent Test Criteria:** User can see all tasks with ID, title, description, status, and priority in creation order

- [X] T015 [US2] Implement get_all_tasks method in TodoManager
- [X] T016 [US2] Ensure tasks are returned in creation order
- [X] T017 [US2] Create CLI menu option for viewing tasks
- [X] T018 [US2] Display "no tasks" message when task list is empty
- [X] T019 [US2] Format task display with rich library (ID, title, description, status, priority)

## Phase 5: User Story 3 - Update Task [US3]
**Goal:** Allow users to update task title, description, and priority
**Independent Test Criteria:** User can update existing task attributes with proper validation and feedback

- [X] T020 [US3] Implement update_task method in TodoManager with validation
- [X] T021 [US3] Validate task ID exists before attempting update
- [X] T022 [US3] Validate title is not empty during update
- [X] T023 [US3] Provide clear feedback when update is successful
- [X] T024 [US3] Create CLI menu option for updating tasks
- [X] T025 [US3] Implement user prompts for task update (ID, new title, description, priority)
- [X] T026 [US3] Validate user-entered task ID exists before update

## Phase 6: User Story 4 - Delete Task [US4]
**Goal:** Allow users to delete tasks by ID with confirmation
**Independent Test Criteria:** User can delete existing tasks with confirmation and receive success feedback

- [X] T027 [US4] Implement delete_task method in TodoManager with validation
- [X] T028 [US4] Validate task ID exists before attempting deletion
- [X] T029 [US4] Ask for confirmation before deleting a task
- [X] T030 [US4] Provide clear feedback when deletion is successful
- [X] T031 [US4] Create CLI menu option for deleting tasks
- [X] T032 [US4] Implement user prompts for task deletion (ID) with confirmation

## Phase 7: User Story 5 - Mark Task Status [US5]
**Goal:** Allow users to mark tasks as complete or incomplete
**Independent Test Criteria:** User can change task status with validation and receive success feedback

- [X] T033 [US5] Implement update_task_status method in TodoManager
- [X] T034 [US5] Validate task ID exists before attempting status change
- [X] T035 [US5] Validate status is a valid enum value
- [X] T036 [US5] Provide clear feedback when status change is successful
- [X] T037 [US5] Create CLI menu option for marking task status
- [X] T038 [US5] Implement user prompts for status change (ID, new status)

## Phase 8: User Story 6 - Main Menu Interface [US6]
**Goal:** Present a main menu with all task operations that loops until user exits
**Independent Test Criteria:** User can navigate main menu and return to it after operations

- [X] T039 [US6] Create main application loop that continuously displays menu
- [X] T040 [US6] Implement main menu with options for all task operations
- [X] T041 [US6] Add exit option to main menu
- [X] T042 [US6] Return to main menu after each operation completes
- [X] T043 [US6] Handle invalid menu selections with appropriate error messages

## Phase 9: User Story 7 - Input Validation [US7]
**Goal:** Validate user inputs and handle errors gracefully
**Independent Test Criteria:** Invalid inputs are caught with helpful error messages and user is re-prompted

- [X] T044 [US7] Implement input validation for all user inputs
- [X] T045 [US7] Display helpful error messages for invalid inputs
- [X] T046 [US7] Re-prompt users after displaying error messages
- [X] T047 [US7] Handle invalid task IDs with appropriate error handling
- [X] T048 [US7] Validate priority values are from the allowed enum
- [X] T049 [US7] Handle empty title inputs during task creation

## Phase 10: Testing
**Goal:** Implement comprehensive tests for all functionality

- [X] T050 Write unit tests for Task model validation
- [X] T051 Write unit tests for TodoManager CRUD operations
- [X] T052 Write integration tests for CLI flow
- [X] T053 Write tests for error handling scenarios
- [X] T054 Write tests for data validation requirements
- [X] T055 Test success criteria (response times, error handling, uptime)

## Phase 11: Polish & Cross-Cutting Concerns
**Goal:** Finalize the application with proper error handling and user experience

- [X] T056 Ensure 2-second response time for all inputs
- [X] T057 Verify 99% uptime during usage (no crashes)
- [X] T058 Test error handling prevents crashes (99% success rate)
- [X] T059 Implement graceful shutdown when user exits
- [X] T060 Add proper exception handling throughout the application
- [X] T061 Finalize UI with rich library for enhanced console experience

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