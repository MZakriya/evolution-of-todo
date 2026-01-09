from sqlmodel import SQLModel
from typing import Optional
from models import Task, TaskStatus, TaskPriority


class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None
    priority: TaskPriority = TaskPriority.MEDIUM
    status: TaskStatus = TaskStatus.TODO


class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[TaskPriority] = None
    status: Optional[TaskStatus] = None


class TaskRead(Task):
    pass  # Inherits all fields from Task model for API responses