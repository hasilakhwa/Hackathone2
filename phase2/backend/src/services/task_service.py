from sqlmodel import Session, select, func
from typing import List, Optional
from ..models.task import Task, TaskCreate, TaskUpdate
from ..models.user import User
from fastapi import HTTPException, status


class TaskService:
    @staticmethod
    def get_tasks_by_user_id(session: Session, user_id: int) -> List[Task]:
        """Get all tasks for a specific user"""
        statement = select(Task).where(Task.user_id == user_id)
        tasks = session.exec(statement).all()
        return tasks

    @staticmethod
    def get_task_by_id_and_user_id(session: Session, task_id: int, user_id: int) -> Optional[Task]:
        """Get a specific task for a specific user"""
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = session.exec(statement).first()
        return task

    @staticmethod
    def create_task(session: Session, task: TaskCreate) -> Task:
        """Create a new task"""
        db_task = Task.model_validate(task)
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task

    @staticmethod
    def update_task(session: Session, task_id: int, user_id: int, task_update: TaskUpdate) -> Optional[Task]:
        """Update a task for a specific user"""
        db_task = TaskService.get_task_by_id_and_user_id(session, task_id, user_id)
        if not db_task:
            return None

        task_data = task_update.model_dump(exclude_unset=True)
        for key, value in task_data.items():
            setattr(db_task, key, value)

        db_task.updated_at = func.now()
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task

    @staticmethod
    def delete_task(session: Session, task_id: int, user_id: int) -> bool:
        """Delete a task for a specific user"""
        db_task = TaskService.get_task_by_id_and_user_id(session, task_id, user_id)
        if not db_task:
            return False

        session.delete(db_task)
        session.commit()
        return True

    @staticmethod
    def toggle_task_completion(session: Session, task_id: int, user_id: int) -> Optional[Task]:
        """Toggle the completion status of a task for a specific user"""
        db_task = TaskService.get_task_by_id_and_user_id(session, task_id, user_id)
        if not db_task:
            return None

        db_task.completed = not db_task.completed
        db_task.updated_at = func.now()
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task