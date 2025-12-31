from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: Status
    priority: Priority
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        # Validate title is not empty
        if not self.title or self.title.strip() == "":
            raise ValueError("Title cannot be empty")

        # Validate status is a valid Status enum
        if not isinstance(self.status, Status):
            try:
                self.status = Status(self.status)
            except ValueError:
                raise ValueError(f"Invalid status: {self.status}. Must be one of {list(Status)}")

        # Validate priority is a valid Priority enum
        if not isinstance(self.priority, Priority):
            try:
                self.priority = Priority(self.priority)
            except ValueError:
                raise ValueError(f"Invalid priority: {self.priority}. Must be one of {list(Priority)}")

        # Set default timestamps if not provided
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()