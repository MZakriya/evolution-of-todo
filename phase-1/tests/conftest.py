import pytest
import sys
from pathlib import Path
# Add the src directory to the path so imports work correctly
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from manager import TodoManager
from models import Priority


@pytest.fixture
def empty_todo_manager():
    """Fixture that provides an empty TodoManager instance."""
    return TodoManager()


@pytest.fixture
def todo_manager_with_tasks():
    """Fixture that provides a TodoManager with some pre-existing tasks."""
    manager = TodoManager()
    manager.add_task("Test Task 1", "Description 1", Priority.MEDIUM)
    manager.add_task("Test Task 2", "Description 2", Priority.HIGH)
    return manager