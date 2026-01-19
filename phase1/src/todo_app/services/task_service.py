from typing import List, Optional
from src.todo_app.models.task import Task, TaskList


class TaskService:
    """
    Business logic layer for task operations
    """

    def __init__(self):
        """Initialize the task service with an in-memory task list"""
        self._task_list = TaskList()

    def add_task(self, description: str) -> Task:
        """
        Add a new task to the system

        Args:
            description: Description of the new task

        Returns:
            Task: The newly created task

        Raises:
            ValueError: If description is empty or invalid
        """
        return self._task_list.add_task(description)

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system

        Returns:
            List[Task]: All tasks in the system
        """
        return self._task_list.get_all_tasks()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task: The task if found, None otherwise
        """
        return self._task_list.get_task_by_id(task_id)

    def update_task(self, task_id: int, description: str) -> bool:
        """
        Update the description of an existing task

        Args:
            task_id: The ID of the task to update
            description: The new description for the task

        Returns:
            bool: True if the task was updated, False if not found

        Raises:
            ValueError: If description is empty or invalid
        """
        return self._task_list.update_task(task_id, description)

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            bool: True if the task was marked complete, False if not found
        """
        return self._task_list.mark_task_complete(task_id)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the system

        Args:
            task_id: The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        return self._task_list.delete_task(task_id)

    def get_next_task_id(self) -> int:
        """
        Get the next available ID for a new task

        Returns:
            int: The next available task ID
        """
        return self._task_list.get_next_id()