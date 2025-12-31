# API Contracts for Console Todo App

## Task Creation Contract
- **Function**: create_task(title: str, description: str, priority: str) -> Task
- **Validates**: title is not empty, priority is valid enum
- **Returns**: Task object with assigned ID and "incomplete" status
- **Preconditions**: title must be provided and not empty
- **Postconditions**: New task exists in storage with unique ID

## Task Retrieval Contract
- **Function**: get_all_tasks() -> List[Task]
- **Returns**: All tasks in creation order
- **Preconditions**: None
- **Postconditions**: Returns complete list of all tasks

## Task Update Contract
- **Function**: update_task(task_id: int, title: str, description: str, priority: str) -> bool
- **Validates**: task exists, title is not empty
- **Returns**: True if successful, False if task not found
- **Preconditions**: Task with given ID must exist
- **Postconditions**: Task attributes updated if successful

## Task Deletion Contract
- **Function**: delete_task(task_id: int) -> bool
- **Validates**: task exists
- **Returns**: True if successful, False if task not found
- **Preconditions**: Task with given ID must exist
- **Postconditions**: Task removed from storage if successful

## Task Status Update Contract
- **Function**: update_task_status(task_id: int, status: str) -> bool
- **Validates**: task exists, status is valid enum
- **Returns**: True if successful, False if task not found
- **Preconditions**: Task with given ID must exist
- **Postconditions**: Task status updated if successful

## Input Validation Contract
- **Function**: validate_input(input_type: str, value: any) -> bool
- **Validates**: Input matches expected type and constraints
- **Returns**: True if valid, False otherwise
- **Preconditions**: input_type must be specified
- **Postconditions**: Validates input against defined constraints