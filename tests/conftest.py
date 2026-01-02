import pytest
from src.todo_app.services.task_service import TaskService


@pytest.fixture
def task_service():
    """Create a fresh TaskService instance for each test"""
    return TaskService()