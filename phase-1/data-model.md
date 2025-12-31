# Data Model for Console Todo App

## Entity: Task

### Fields:
- **id**: integer (auto-generated, unique within session)
- **title**: string (required, non-empty)
- **description**: string (optional)
- **status**: enum (complete, incomplete)
- **priority**: enum (low, medium, high)

### Validations:
- id must be unique within application session
- title must not be empty when creating task
- status must be one of defined values
- priority must be one of defined values

### State Transitions:
- **status**: incomplete → complete (via mark_complete)
- **status**: complete → incomplete (via mark_incomplete)

## Entity: TodoManager

### Responsibilities:
- Manage in-memory storage of Task objects
- Handle all CRUD operations
- Maintain task ordering (creation order)
- Validate business rules

### Storage:
- Internal storage using Python list to maintain order
- Optional dictionary mapping for ID-based lookups