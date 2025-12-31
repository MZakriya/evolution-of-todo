import pytest
import sys
from pathlib import Path
# Add the src directory to the path so imports work correctly
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from manager import TodoManager
from models import Task, Status, Priority


def test_add_task():
    """Test add_task (Check ID assignment, default status)."""
    manager = TodoManager()

    # Test adding a task
    task = manager.add_task("Test Task", "Test Description", Priority.MEDIUM)

    # Check ID assignment
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.priority == Priority.MEDIUM

    # Check default status
    assert task.status == Status.TODO


def test_add_task_with_empty_title():
    """Test that adding a task with empty title raises ValueError."""
    manager = TodoManager()

    with pytest.raises(ValueError, match="Title cannot be empty"):
        manager.add_task("", "Test Description", Priority.MEDIUM)

    with pytest.raises(ValueError, match="Title cannot be empty"):
        manager.add_task("   ", "Test Description", Priority.MEDIUM)


def test_get_all_tasks():
    """Test get_all_tasks."""
    manager = TodoManager()

    # Initially should be empty
    tasks = manager.get_all_tasks()
    assert len(tasks) == 0

    # Add some tasks
    task1 = manager.add_task("Task 1", "Description 1", Priority.LOW)
    task2 = manager.add_task("Task 2", "Description 2", Priority.HIGH)

    # Check that all tasks are returned
    tasks = manager.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0] == task1
    assert tasks[1] == task2


def test_update_task_success():
    """Test update_task (Success scenario)."""
    manager = TodoManager()
    original_task = manager.add_task("Original Title", "Original Description", Priority.MEDIUM)

    # Update the task
    updated_task = manager.update_task(
        task_id=original_task.id,
        title="Updated Title",
        description="Updated Description",
        priority=Priority.HIGH
    )

    # Check that the task was updated
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"
    assert updated_task.priority == Priority.HIGH

    # Check that the same object was returned
    assert updated_task.id == original_task.id


def test_update_task_invalid_id():
    """Test update_task (Invalid ID scenario)."""
    manager = TodoManager()

    with pytest.raises(ValueError, match="Task with ID 999 not found"):
        manager.update_task(999, title="New Title")


def test_update_task_empty_title():
    """Test update_task with empty title raises ValueError."""
    manager = TodoManager()
    task = manager.add_task("Original Title", "Original Description", Priority.MEDIUM)

    with pytest.raises(ValueError, match="Title cannot be empty"):
        manager.update_task(task.id, title="")


def test_delete_task_success():
    """Test delete_task (Success)."""
    manager = TodoManager()
    task = manager.add_task("Test Task", "Test Description", Priority.MEDIUM)

    # Delete the task
    result = manager.delete_task(task.id)

    # Check that deletion was successful
    assert result is True

    # Check that the task is no longer in the list
    tasks = manager.get_all_tasks()
    assert len(tasks) == 0


def test_delete_task_invalid_id():
    """Test delete_task (Invalid ID)."""
    manager = TodoManager()

    with pytest.raises(ValueError, match="Task with ID 999 not found"):
        manager.delete_task(999)


def test_update_task_status():
    """Test update_task_status (Mark complete)."""
    manager = TodoManager()
    task = manager.add_task("Test Task", "Test Description", Priority.MEDIUM)

    # Initially should be TODO
    assert task.status == Status.TODO

    # Update status to DONE
    updated_task = manager.update_task_status(task.id, Status.DONE)

    # Check that the status was updated
    assert updated_task.status == Status.DONE
    assert updated_task.id == task.id


def test_update_task_status_invalid_id():
    """Test update_task_status with invalid ID."""
    manager = TodoManager()

    with pytest.raises(ValueError, match="Task with ID 999 not found"):
        manager.update_task_status(999, Status.DONE)


def test_update_task_status_invalid_status():
    """Test update_task_status with invalid status."""
    manager = TodoManager()
    task = manager.add_task("Test Task", "Test Description", Priority.MEDIUM)

    with pytest.raises(ValueError, match="Invalid status"):
        manager.update_task_status(task.id, "invalid_status")


def test_manager_with_fixtures(empty_todo_manager, todo_manager_with_tasks):
    """Test manager functionality using fixtures."""
    # Test empty manager fixture
    assert len(empty_todo_manager.get_all_tasks()) == 0

    # Test manager with tasks fixture
    tasks = todo_manager_with_tasks.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Test Task 1"
    assert tasks[1].title == "Test Task 2"