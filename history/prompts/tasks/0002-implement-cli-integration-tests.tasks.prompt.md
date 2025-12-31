---
id: 2
title: "Implement CLI Integration Tests"
stage: tasks
date: "2025-12-31"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "console-todo-app"
branch: "main"
user: "unknown"
command: "/sp.implement"
labels: ["testing", "integration-tests", "cli", "pytest"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "phase-1/tests/test_cli.py"
  - "phase-1/tasks.md"
tests:
  - "test_cli.py::test_add_task_flow"
  - "test_cli.py::test_view_task_flow"
  - "test_cli.py::test_exit_flow"
---

# Implement CLI Integration Tests

## Prompt Text
```
@skills/spec-driven-dev @skills/testing-qa @skills/python-uv-ops

**Action: Execute Task T052: Write Integration Tests for CLI Flow**

We have Unit Tests for Logic (`test_manager.py`), but we need to ensure the **CLI Interface (`main.py`)** correctly interacts with the user and the manager.

**Instructions:**
1.  **Create File:** `phase-1/tests/test_cli.py`.
2.  **Strategy:**
    -   Use `unittest.mock.patch` to simulate user input (`builtins.input` or `rich.console.Console.input`).
    -   Use `capsys` (pytest fixture) to capture and verify what is printed to the terminal.
3.  **Test Scenarios:**
    -   **Test Add Task Flow:** Simulate user selecting "1", entering "Buy Milk", "Desc", "HIGH", and verify "Task Added" message appears.
    -   **Test View Task Flow:** Simulate user selecting "2" and verify the table headers appear in output.
    -   **Test Exit Flow:** Simulate user selecting "5" (Exit) and verify the loop breaks.

**Post-Execution:**
-   Update `phase-1/tasks.md`: Mark **[x] T052** as complete.
-   Run `uv run pytest phase-1/tests/test_cli.py` and show the results.
```

## Response Text
Successfully implemented integration tests for the CLI flow, including tests for add task, view task, and exit functionality. All tests pass and task T052 has been marked as complete.

## Outcome Impact
Implemented comprehensive integration tests for the CLI interface that verify the main application loop correctly handles user input and displays appropriate output. These tests validate the integration between the CLI interface and the underlying business logic.

## Tests Summary
- Created test_add_task_flow to verify task creation flow
- Created test_view_task_flow to verify task viewing functionality
- Created test_exit_flow to verify application exit behavior
- All tests pass successfully with pytest

## Files Summary
- Created test_cli.py with integration tests for CLI functionality
- Updated tasks.md to mark T052 as complete

## Next Prompts
- Implement performance tests (T055)
- Execute remaining phases in tasks.md

## Reflection Note
The CLI integration tests provide confidence that the user interface correctly interacts with the business logic layer.

## Failure Modes Observed
- Initial challenges with mocking the rich.prompt.Prompt.ask function required careful handling of user input sequences

## Next Experiment to Improve Prompt Quality
Consider using more specific mock strategies for rich console interactions to improve test reliability.