import pytest
import sys
from pathlib import Path
# Add the src directory to the path so imports work correctly
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from datetime import datetime
from models import Task, Status, Priority


def test_task_creation():
    """Test Task creation with valid parameters."""
    task = Task(
        id=1,
        title="Test Task",
        description="Test Description",
        status=Status.TODO,
        priority=Priority.MEDIUM
    )

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.status == Status.TODO
    assert task.priority == Priority.MEDIUM
    assert isinstance(task.created_at, datetime)
    assert isinstance(task.updated_at, datetime)


def test_task_creation_with_string_status():
    """Test Task creation with string status that gets converted to enum."""
    task = Task(
        id=1,
        title="Test Task",
        description="Test Description",
        status="todo",  # String instead of enum
        priority=Priority.MEDIUM
    )

    assert task.status == Status.TODO


def test_task_creation_with_string_priority():
    """Test Task creation with string priority that gets converted to enum."""
    task = Task(
        id=1,
        title="Test Task",
        description="Test Description",
        status=Status.TODO,
        priority="high"  # String instead of enum
    )

    assert task.priority == Priority.HIGH


def test_task_validation_empty_title():
    """Test Validation: Ensure creating a task with empty title raises ValueError."""
    with pytest.raises(ValueError, match="Title cannot be empty"):
        Task(
            id=1,
            title="",  # Empty title
            description="Test Description",
            status=Status.TODO,
            priority=Priority.MEDIUM
        )

    with pytest.raises(ValueError, match="Title cannot be empty"):
        Task(
            id=1,
            title="   ",  # Title with only whitespace
            description="Test Description",
            status=Status.TODO,
            priority=Priority.MEDIUM
        )

    with pytest.raises(ValueError, match="Title cannot be empty"):
        Task(
            id=1,
            title=None,  # None title
            description="Test Description",
            status=Status.TODO,
            priority=Priority.MEDIUM
        )


def test_task_invalid_status():
    """Test that invalid status raises ValueError."""
    with pytest.raises(ValueError, match="Invalid status"):
        Task(
            id=1,
            title="Test Task",
            description="Test Description",
            status="invalid_status",
            priority=Priority.MEDIUM
        )


def test_task_invalid_priority():
    """Test that invalid priority raises ValueError."""
    with pytest.raises(ValueError, match="Invalid priority"):
        Task(
            id=1,
            title="Test Task",
            description="Test Description",
            status=Status.TODO,
            priority="invalid_priority"
        )


def test_enum_validation():
    """Test Enum validation (Status/Priority)."""
    # Test all valid Status values
    for status in Status:
        task = Task(
            id=1,
            title="Test Task",
            description="Test Description",
            status=status,
            priority=Priority.MEDIUM
        )
        assert task.status == status

    # Test all valid Priority values
    for priority in Priority:
        task = Task(
            id=1,
            title="Test Task",
            description="Test Description",
            status=Status.TODO,
            priority=priority
        )
        assert task.priority == priority