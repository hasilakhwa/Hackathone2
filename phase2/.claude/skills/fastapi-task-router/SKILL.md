---
name: fastapi-task-router
description: Implement the full set of RESTful task endpoints in FastAPI with user_id prefix and auth dependencies. Use for creating/updating the API router.
---

# FastAPI Task Router Endpoints

## Instructions

1. **Router setup**
   - Use APIRouter with prefix="/api/{user_id}/tasks"

2. **Endpoints**
   - GET / → list tasks (filter by user_id)
   - POST / → create task (set user_id)
   - GET /{id} → get single task (ownership check)
   - PUT /{id} → update task
   - DELETE /{id} → delete task
   - PATCH /{id}/complete → toggle completed

3. **Dependencies**
   - Use Depends(get_current_user) and Depends(get_session)

## Best Practices
- Use Pydantic models for request/response (TaskCreate, TaskRead, TaskUpdate)
- Return JSON with consistent structure
- Use HTTP status codes properly (201 create, 204 delete)
- Add tags=["tasks"] for Swagger

## Example Structure

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from .models import Task, TaskCreate, TaskRead, TaskUpdate
from .auth import get_current_user
from .database import get_session

router = APIRouter(prefix="/api/{user_id}/tasks", tags=["tasks"])

@router.get("/", response_model=list[TaskRead])
def list_tasks(user_id: int, current_user: int = Depends(get_current_user), session: Session = Depends(get_session)):
    if current_user != user_id:
        raise HTTPException(403, "Forbidden")
    tasks = session.exec(select(Task).where(Task.user_id == user_id)).all()
    return tasks

@router.post("/", response_model=TaskRead, status_code=201)
def create_task(task_create: TaskCreate, user_id: int, current_user: int = Depends(get_current_user), session: Session = Depends(get_session)):
    if current_user != user_id:
        raise HTTPException(403, "Forbidden")
    task = Task(**task_create.dict(), user_id=user_id)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

# Similarly for GET/{id}, PUT/{id}, DELETE/{id}, PATCH/{id}/complete