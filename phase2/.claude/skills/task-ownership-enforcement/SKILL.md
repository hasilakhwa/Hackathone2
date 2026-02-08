
```markdown
---
name: task-ownership-enforcement
description: Ensure all task operations (CRUD) are filtered and restricted to the authenticated user's tasks only. Use in every task-related endpoint.
---

# Enforce Task Ownership in FastAPI

## Instructions

1. **List tasks**
   - Filter where task.user_id == current_user_id

2. **Create task**
   - Set task.user_id = current_user_id

3. **Get / Update / Delete / Complete**
   - First fetch task by id AND user_id
   - If not found → 404
   - Proceed only if owned

## Best Practices
- Always use both id and user_id in WHERE clause
- Never trust client-provided user_id in path
- Use 403 if user tries to access others' tasks
- Return 404 for non-owned tasks (security through obscurity)

## Example Structure

```python
from fastapi import Depends, HTTPException
from sqlmodel import select
from .models import Task
from .auth import get_current_user

async def get_task_or_404(task_id: int, user_id: int = Depends(get_current_user), session=Depends(get_session)):
    stmt = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    task = session.exec(stmt).first()
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@app.get("/api/{user_id}/tasks/{task_id}")
async def get_task(task: Task = Depends(get_task_or_404)):
    return task

@app.put("/api/{user_id}/tasks/{task_id}")
async def update_task(update_data: TaskUpdate, task: Task = Depends(get_task_or_404), session=Depends(get_session)):
    task.title = update_data.title or task.title
    # ... other fields
    session.add(task)
    session.commit()
    session.refresh(task)
    return task