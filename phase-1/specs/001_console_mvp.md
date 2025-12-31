# Console Todo App Specification

## Overview

A command-line todo application that stores tasks in memory using Python data structures. The application provides basic CRUD operations for managing tasks through an interactive console interface.

## User Scenarios & Testing

### Primary User Flows

1. **Task Management Flow**
   - User starts the application and sees a main menu
   - User selects an option to add, view, update, delete, or mark tasks
   - User completes the selected action with appropriate inputs
   - User returns to the main menu or exits the application

2. **Task Creation Flow**
   - User selects "Add Task" from the menu
   - User enters task title, description, and priority
   - System creates the task with a unique ID and "incomplete" status
   - System confirms task creation and returns to main menu

3. **Task Viewing Flow**
   - User selects "View Tasks" from the menu
   - System displays all tasks with their details in a formatted list
   - User can see task ID, title, description, status, and priority

### Error Handling Scenarios

- User enters invalid task ID when updating/deleting - system shows error and prompts again
- User enters empty title when adding task - system prompts for valid input
- User enters invalid menu option - system shows error and displays menu again

## Functional Requirements

### Core Task Management

1. **Add Task (REQ-001)**
   - System shall allow users to create new tasks with title, description, priority, and status
   - System shall assign a unique ID to each task upon creation
   - System shall set the initial status of new tasks to "incomplete"
   - System shall validate that task title is not empty before creation

2. **View Tasks (REQ-002)**
   - System shall display all tasks in a formatted list with ID, title, description, status, and priority
   - System shall show a message when no tasks exist
   - System shall display tasks in the order they were created

3. **Update Task (REQ-003)**
   - System shall allow users to update task title, description, and priority
   - System shall validate task ID exists before attempting update
   - System shall provide clear feedback when update is successful

4. **Delete Task (REQ-004)**
   - System shall allow users to delete tasks by ID
   - System shall validate task ID exists before attempting deletion
   - System shall ask for confirmation before deleting a task
   - System shall provide clear feedback when deletion is successful

5. **Mark Task Status (REQ-005)**
   - System shall allow users to mark tasks as complete or incomplete
   - System shall validate task ID exists before attempting status change
   - System shall provide clear feedback when status change is successful

### User Interface Requirements

6. **Main Menu Interface (REQ-006)**
   - System shall present a main menu with options for all task operations
   - System shall continuously loop through the menu until user chooses to exit
   - System shall handle invalid menu selections gracefully with appropriate error messages

7. **Input Validation (REQ-007)**
   - System shall validate user inputs for correctness before processing
   - System shall provide helpful error messages for invalid inputs
   - System shall re-prompt users after displaying error messages

### Data Management Requirements

8. **In-Memory Storage (REQ-008)**
   - System shall store all tasks in Python data structures (lists/dictionaries)
   - System shall maintain task data during the application session
   - System shall not persist data between application sessions

## Success Criteria

- Users can create new tasks with title, description, priority, and status in under 30 seconds
- Users can view all tasks in a clear, formatted list with all required information visible
- Users can update any existing task attributes with 95% success rate
- Users can delete tasks with 95% success rate and proper confirmation
- Users can mark tasks as complete/incomplete with 95% success rate
- Application responds to all user inputs within 2 seconds
- Users can complete any task operation without application crashes (99% uptime during usage)
- Error handling prevents application from crashing with invalid inputs (99% success rate)

## Key Entities

### Task Entity

**Attributes:**
- ID: Unique identifier for the task (integer, auto-generated)
- Title: Brief description of the task (string, required)
- Description: Detailed information about the task (string, optional)
- Status: Current state of the task (enum: "complete", "incomplete")
- Priority: Importance level of the task (enum: "low", "medium", "high")

**Validations:**
- ID must be unique within the application session
- Title must not be empty when creating a task
- Status must be one of the defined values
- Priority must be one of the defined values

## Assumptions

- Application will run in a standard terminal/command-line environment
- Users have basic familiarity with command-line interfaces
- Data persistence is not required for this phase (in-memory only)
- The application session ends when the user chooses to exit
- Task IDs are sequential integers starting from 1

## Dependencies

- Python 3.13+ runtime environment
- `rich` library for enhanced console UI (optional enhancement)
- Standard Python libraries for console input/output

## Testing Strategy

- Unit tests for all core task operations using pytest
- Test cases for each CRUD operation with various input scenarios
- Test error handling for invalid inputs and edge cases
- Test data validation for all required fields
- Integration tests for the main menu workflow
- Test data integrity during multiple operations