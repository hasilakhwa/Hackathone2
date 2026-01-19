from datetime import datetime
from typing import List, Optional


class Task:
    """
    Represents a single todo item in the application
    """

    def __init__(self, task_id: int, description: str, completed: bool = False):
        """
        Initialize a Task instance

        Args:
            task_id: Unique identifier for the task
            description: Text description of the task
            completed: Status indicating if the task is completed (default: False)
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        if len(description) >= 1000:
            raise ValueError("Task description must be less than 1000 characters")

        if not isinstance(completed, bool):
            raise ValueError("Completed status must be a boolean")

        self._id = task_id
        self._description = description.strip()
        self._completed = completed
        self._created_at = datetime.now()

    @property
    def id(self) -> int:
        """
        Get the task ID

        Returns:
            int: The unique identifier of the task
        """
        return self._id

    @property
    def description(self) -> str:
        """
        Get the task description

        Returns:
            str: The description of the task
        """
        return self._description

    @description.setter
    def description(self, value: str):
        """
        Set the task description with validation

        Args:
            value: The new description for the task

        Raises:
            ValueError: If the description is empty or too long
        """
        if not value or not value.strip():
            raise ValueError("Task description cannot be empty")

        if len(value) >= 1000:
            raise ValueError("Task description must be less than 1000 characters")

        self._description = value.strip()

    @property
    def completed(self) -> bool:
        """
        Get the completion status

        Returns:
            bool: True if the task is completed, False otherwise
        """
        return self._completed

    @completed.setter
    def completed(self, value: bool):
        """
        Set the completion status

        Args:
            value: The new completion status

        Raises:
            ValueError: If the value is not a boolean
        """
        if not isinstance(value, bool):
            raise ValueError("Completed status must be a boolean")
        self._completed = value

    @property
    def created_at(self) -> datetime:
        """
        Get the creation timestamp

        Returns:
            datetime: The timestamp when the task was created
        """
        return self._created_at

    def to_dict(self) -> dict:
        """
        Convert task to dictionary representation

        Returns:
            dict: Dictionary containing task properties
        """
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }

    def __str__(self) -> str:
        """
        String representation of the task

        Returns:
            str: Formatted string representation of the task
        """
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.description}"

    def __repr__(self) -> str:
        """
        Developer-friendly representation of the task

        Returns:
            str: Detailed string representation of the task
        """
        return f"Task(id={self.id}, description='{self.description}', completed={self.completed})"


class TaskList:
    """
    Collection of Task entities stored in memory
    """

    def __init__(self):
        """Initialize an empty task list with next ID counter"""
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, description: str) -> Task:
        """
        Add a new task to the list

        Args:
            description: Description of the new task

        Returns:
            Task: The newly created task
        """
        task = Task(self._next_id, description, completed=False)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the list

        Returns:
            List[Task]: All tasks in the list
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID

        Args:
            task_id: The ID of the task to find

        Returns:
            Task: The task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, description: str) -> bool:
        """
        Update the description of an existing task

        Args:
            task_id: The ID of the task to update
            description: The new description for the task

        Returns:
            bool: True if the task was updated, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.description = description
        return True

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            bool: True if the task was marked complete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = True
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the list

        Args:
            task_id: The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task

        Returns:
            int: The next available task ID
        """
        return self._next_id