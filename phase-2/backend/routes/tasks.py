from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from typing import List
from db import get_session
from auth import get_current_user
from models import Task, User
from schemas import TaskCreate, TaskUpdate, TaskRead

router = APIRouter()


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: TaskCreate,
    current_user_id: str = Depends(get_current_user),
    session=Depends(get_session)
):
    """
    Create a new task for the current user.
    """
    # Create a new task with the current user's ID
    db_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        status=task.status,
        user_id=int(current_user_id)  # Convert user_id to int as needed
    )

    session.add(db_task)
    await session.commit()
    await session.refresh(db_task)

    return db_task


@router.get("/", response_model=List[TaskRead])
async def get_tasks(
    current_user_id: str = Depends(get_current_user),
    session=Depends(get_session)
):
    """
    Get all tasks for the current user.
    """
    # Query tasks that belong to the current user
    statement = select(Task).where(Task.user_id == int(current_user_id))
    results = await session.exec(statement)
    tasks = results.all()

    return tasks


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session=Depends(get_session)
):
    """
    Get a specific task by ID if it belongs to the current user.
    """
    statement = select(Task).where(Task.id == task_id, Task.user_id == int(current_user_id))
    result = await session.exec(statement)
    task = result.first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to current user"
        )

    return task


@router.put("/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    current_user_id: str = Depends(get_current_user),
    session=Depends(get_session)
):
    """
    Update a specific task by ID if it belongs to the current user.
    """
    statement = select(Task).where(Task.id == task_id, Task.user_id == int(current_user_id))
    result = await session.exec(statement)
    db_task = result.first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to current user"
        )

    # Update the task fields that are provided
    for field, value in task_update.dict(exclude_unset=True).items():
        setattr(db_task, field, value)

    await session.commit()
    await session.refresh(db_task)

    return db_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session=Depends(get_session)
):
    """
    Delete a specific task by ID if it belongs to the current user.
    """
    statement = select(Task).where(Task.id == task_id, Task.user_id == int(current_user_id))
    result = await session.exec(statement)
    db_task = result.first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to current user"
        )

    await session.delete(db_task)
    await session.commit()

    # Return nothing for 204 status code