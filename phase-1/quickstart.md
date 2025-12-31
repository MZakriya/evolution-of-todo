# Quickstart Guide for Console Todo App

## Getting Started

### Prerequisites
- Python 3.13+ installed
- `uv` package manager installed

### Setup
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies: `uv sync`
4. Run the application: `uv run src/main.py`

### Running Tests
- Execute tests: `uv run pytest`
- Run specific test file: `uv run pytest tests/test_todo.py`

## Project Structure
```
phase-1/
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── todo_manager.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_todo.py
├── pyproject.toml
├── phase-1/specs/001_console_mvp.md
├── phase-1/plan.md
├── phase-1/research.md
├── phase-1/data-model.md
└── phase-1/contracts/
    └── api-contracts.md
```

## Key Components

### Task Model
- Located in `src/models/task.py`
- Represents a single todo task with id, title, description, status, and priority

### Todo Manager
- Located in `src/services/todo_manager.py`
- Handles all CRUD operations for tasks
- Manages in-memory storage

### Main Application
- Located in `src/main.py`
- Implements CLI interface and menu system
- Orchestrates user interactions

## Development Workflow
1. Implement models based on data-model.md
2. Implement services based on contracts/api-contracts.md
3. Create CLI interface based on functional requirements
4. Write tests based on testing strategy in spec
5. Validate against success criteria in spec