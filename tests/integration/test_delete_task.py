import pytest
from src.todo_app.services.task_service import TaskService


def test_delete_task_integration():
    """Integration test for deleting a task"""
    task_service = TaskService()

    # Add a task
    task = task_service.add_task("Task to delete")

    # Verify the task exists
    all_tasks_before = task_service.get_all_tasks()
    assert len(all_tasks_before) == 1
    assert task_service.get_task_by_id(task.id) is not None

    # Delete the task
    success = task_service.delete_task(task.id)

    # Verify the operation was successful
    assert success is True

    # Verify the task is gone
    all_tasks_after = task_service.get_all_tasks()
    assert len(all_tasks_after) == 0
    assert task_service.get_task_by_id(task.id) is None


def test_delete_multiple_tasks():
    """Integration test for deleting multiple tasks"""
    task_service = TaskService()

    # Add multiple tasks
    task1 = task_service.add_task("Task 1")
    task2 = task_service.add_task("Task 2")
    task3 = task_service.add_task("Task 3")

    # Verify all tasks exist
    all_tasks_before = task_service.get_all_tasks()
    assert len(all_tasks_before) == 3

    # Delete them one by one
    success1 = task_service.delete_task(task1.id)
    success2 = task_service.delete_task(task2.id)
    success3 = task_service.delete_task(task3.id)

    # Verify all operations were successful
    assert success1 is True
    assert success2 is True
    assert success3 is True

    # Verify all tasks are gone
    all_tasks_after = task_service.get_all_tasks()
    assert len(all_tasks_after) == 0


def test_delete_nonexistent_task():
    """Integration test for attempting to delete a non-existent task"""
    task_service = TaskService()

    # Try to delete a task that doesn't exist
    success = task_service.delete_task(999)

    # Verify the operation failed
    assert success is False


def test_delete_task_then_verify_others_remain():
    """Integration test to ensure deleting one task doesn't affect others"""
    task_service = TaskService()

    # Add multiple tasks
    task1 = task_service.add_task("Task to keep 1")
    task2 = task_service.add_task("Task to delete")
    task3 = task_service.add_task("Task to keep 2")

    # Verify all tasks exist
    all_tasks_before = task_service.get_all_tasks()
    assert len(all_tasks_before) == 3

    # Delete the middle task
    success = task_service.delete_task(task2.id)
    assert success is True

    # Verify only the deleted task is gone
    all_tasks_after = task_service.get_all_tasks()
    assert len(all_tasks_after) == 2

    # Verify the other tasks still exist
    remaining_task1 = task_service.get_task_by_id(task1.id)
    remaining_task3 = task_service.get_task_by_id(task3.id)
    assert remaining_task1 is not None
    assert remaining_task3 is not None
    assert remaining_task1.description == "Task to keep 1"
    assert remaining_task3.description == "Task to keep 2"

    # Verify the deleted task is gone
    deleted_task = task_service.get_task_by_id(task2.id)
    assert deleted_task is None


def test_delete_all_tasks():
    """Integration test for deleting all tasks"""
    task_service = TaskService()

    # Add multiple tasks
    task1 = task_service.add_task("Task 1")
    task2 = task_service.add_task("Task 2")
    task3 = task_service.add_task("Task 3")

    # Verify all tasks exist
    all_tasks_before = task_service.get_all_tasks()
    assert len(all_tasks_before) == 3

    # Delete all tasks
    success1 = task_service.delete_task(task1.id)
    success2 = task_service.delete_task(task2.id)
    success3 = task_service.delete_task(task3.id)

    # Verify all operations were successful
    assert success1 is True
    assert success2 is True
    assert success3 is True

    # Verify no tasks remain
    all_tasks_after = task_service.get_all_tasks()
    assert len(all_tasks_after) == 0


def test_delete_task_then_add_new():
    """Integration test to ensure new tasks get correct IDs after deletion"""
    task_service = TaskService()

    # Add and delete a task
    task1 = task_service.add_task("First task")
    success = task_service.delete_task(task1.id)
    assert success is True

    # Add a new task
    task2 = task_service.add_task("Second task")

    # Verify the new task gets the next available ID
    assert task2.id == 2  # Should be 2 since 1 was deleted but IDs are sequential

    # Verify the service's next ID is correct
    next_id = task_service.get_next_task_id()
    assert next_id == 3


def test_delete_task_error_handling():
    """Integration test for error handling in delete task flow"""
    task_service = TaskService()

    # Try to delete with invalid ID
    success_negative = task_service.delete_task(-1)
    assert success_negative is False

    success_zero = task_service.delete_task(0)
    assert success_zero is False

    # Verify no tasks were affected by the invalid operations
    all_tasks = task_service.get_all_tasks()
    assert len(all_tasks) == 0