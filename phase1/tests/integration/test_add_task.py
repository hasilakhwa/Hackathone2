import pytest
from src.todo_app.services.task_service import TaskService
from src.todo_app.cli.cli import TodoCLI


def test_add_task_integration():
    """Integration test for the add task flow from CLI to service to model"""
    # Set up the components
    task_service = TaskService()
    cli = TodoCLI(task_service)

    # Add a task
    initial_count = len(task_service.get_all_tasks())

    # Simulate adding a task (we'll test the service directly since CLI input is interactive)
    task = task_service.add_task("Integration test task")

    # Verify the task was added
    all_tasks = task_service.get_all_tasks()
    assert len(all_tasks) == initial_count + 1
    assert task.description == "Integration test task"
    assert task.id == 1
    assert task.completed is False


def test_add_multiple_tasks_integration():
    """Integration test for adding multiple tasks"""
    task_service = TaskService()

    # Add multiple tasks
    task1 = task_service.add_task("First integration task")
    task2 = task_service.add_task("Second integration task")
    task3 = task_service.add_task("Third integration task")

    # Verify all tasks were added correctly
    all_tasks = task_service.get_all_tasks()
    assert len(all_tasks) == 3

    descriptions = [task.description for task in all_tasks]
    assert "First integration task" in descriptions
    assert "Second integration task" in descriptions
    assert "Third integration task" in descriptions

    # Verify IDs are sequential
    ids = [task.id for task in all_tasks]
    assert set(ids) == {1, 2, 3}


def test_add_task_then_view_integration():
    """Integration test for adding a task and then viewing it"""
    task_service = TaskService()

    # Add a task
    added_task = task_service.add_task("Task to view")

    # Get all tasks
    all_tasks = task_service.get_all_tasks()

    # Verify the task exists in the list
    assert len(all_tasks) == 1
    retrieved_task = all_tasks[0]
    assert retrieved_task.id == added_task.id
    assert retrieved_task.description == added_task.description
    assert retrieved_task.completed == added_task.completed


def test_add_task_with_special_characters():
    """Integration test for adding tasks with special characters"""
    task_service = TaskService()

    special_descriptions = [
        "Task with spaces and symbols!@#",
        "Task with numbers 12345",
        "Task with unicode: café",
        "Task with    multiple    spaces",
        "Task with 'quotes' and \"double quotes\""
    ]

    for desc in special_descriptions:
        task = task_service.add_task(desc)
        assert task.description == desc.strip()  # Should be stored without leading/trailing spaces


def test_add_task_error_handling():
    """Integration test for error handling when adding invalid tasks"""
    task_service = TaskService()

    # Test adding empty task (should raise ValueError)
    with pytest.raises(ValueError):
        task_service.add_task("")

    with pytest.raises(ValueError):
        task_service.add_task("   ")

    # Verify no tasks were added due to the errors
    all_tasks = task_service.get_all_tasks()
    assert len(all_tasks) == 0