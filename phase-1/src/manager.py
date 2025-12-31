try:
    # When running as part of the package
    from .models import Task, Status, Priority
except ImportError:
    # When running in test context
    from models import Task, Status, Priority
from typing import List


class TodoManager:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str, priority: Priority) -> Task:
        # Validation: Check if title is empty
        if not title or title.strip() == "":
            raise ValueError("Title cannot be empty")

        # Auto ID: Generate a unique ID
        task_id = self._next_id
        self._next_id += 1

        # Default Status: Set status to Status.TODO by default
        status = Status.TODO

        # Create the Task object and append it to the internal list
        task = Task(
            id=task_id,
            title=title,
            description=description,
            status=status,
            priority=priority
        )
        self._tasks.append(task)

        # Return the created Task object
        return task

    def get_all_tasks(self):
        # Return the list of tasks (ordering by creation time is automatic since it's a list)
        return self._tasks

    def update_task(self, task_id: int, title: str = None, description: str = None, priority: Priority = None):
        # Find task by ID (T021, T026)
        task = None
        for t in self._tasks:
            if t.id == task_id:
                task = t
                break

        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        # Update fields if provided (T020)
        if title is not None:
            # Validate title is not empty during update (T022)
            if not title or title.strip() == "":
                raise ValueError("Title cannot be empty")
            task.title = title

        if description is not None:
            task.description = description

        if priority is not None:
            task.priority = priority

        # Provide clear feedback when update is successful (T023)
        return task

    def delete_task(self, task_id: int) -> bool:
        # Find task by ID (T028)
        task_index = None
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                task_index = i
                break

        if task_index is None:
            raise ValueError(f"Task with ID {task_id} not found")

        # Remove from list (T027)
        self._tasks.pop(task_index)

        # Returns True on success (T027, T030)
        return True

    def update_task_status(self, task_id: int, status: Status):
        # Find task by ID (T034)
        task = None
        for t in self._tasks:
            if t.id == task_id:
                task = t
                break

        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        # Validate status is a valid enum value (T035)
        if not isinstance(status, Status):
            raise ValueError(f"Invalid status: {status}. Must be one of {list(Status)}")

        # Update the status
        task.status = status

        # Provide clear feedback when status change is successful (T036)
        return task