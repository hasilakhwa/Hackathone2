from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from ...models.task import TaskRead, TaskCreate, TaskUpdate
from ...services.task_service import TaskService
from ...core.database import get_session
from ..deps import verify_user_id_match_path

router = APIRouter()


@router.get("/tasks", response_model=List[TaskRead])
def get_tasks(
    user_id: int = Depends(verify_user_id_match_path),
    session: Session = Depends(get_session)
):
    """
    Retrieve all tasks for the authenticated user.
    """
    tasks = TaskService.get_tasks_by_user_id(session, user_id)
    return tasks


@router.post("/tasks", response_model=TaskRead)
def create_task(
    task_create: TaskCreate,
    user_id: int = Depends(verify_user_id_match_path),
    session: Session = Depends(get_session)
):
    """
    Create a new task for the authenticated user.
    """
    # Override user_id to ensure it matches the authenticated user
    task_data = task_create.model_dump()
    task_data['user_id'] = user_id

    task_to_create = TaskCreate(**task_data)
    created_task = TaskService.create_task(session, task_to_create)
    return created_task


@router.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(
    task_id: int,
    user_id: int = Depends(verify_user_id_match_path),
    session: Session = Depends(get_session)
):
    """
    Retrieve a specific task by ID for the authenticated user.
    """
    task = TaskService.get_task_by_id_and_user_id(session, task_id, user_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task


@router.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    user_id: int = Depends(verify_user_id_match_path),
    session: Session = Depends(get_session)
):
    """
    Update a specific task by ID for the authenticated user.
    """
    task = TaskService.get_task_by_id_and_user_id(session, task_id, user_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    # Validate the update model
    validated_update = TaskUpdate(**task_update.model_dump(exclude_unset=True))
    updated_task = TaskService.update_task(session, task_id, user_id, validated_update)

    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return updated_task


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    user_id: int = Depends(verify_user_id_match_path),
    session: Session = Depends(get_session)
):
    """
    Delete a specific task by ID for the authenticated user.
    """
    task = TaskService.get_task_by_id_and_user_id(session, task_id, user_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    success = TaskService.delete_task(session, task_id, user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return {"message": "Task deleted successfully"}


@router.patch("/tasks/{task_id}/complete", response_model=TaskRead)
def toggle_task_completion(
    task_id: int,
    user_id: int = Depends(verify_user_id_match_path),
    session: Session = Depends(get_session)
):
    """
    Toggle the completion status of a specific task for the authenticated user.
    """
    task = TaskService.get_task_by_id_and_user_id(session, task_id, user_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    toggled_task = TaskService.toggle_task_completion(session, task_id, user_id)
    if not toggled_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return toggled_task