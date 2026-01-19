import pytest
from src.todo_app.services.task_service import TaskService


def test_mark_task_complete_integration():
    """Integration test for marking a task as complete"""
    task_service = TaskService()

    # Add a task
    task = task_service.add_task("Task to mark complete")

    # Verify initial state
    assert task.completed is False

    # Mark the task as complete
    success = task_service.mark_task_complete(task.id)

    # Verify the operation was successful
    assert success is True

    # Get the task again and verify it's marked as complete
    updated_task = task_service.get_task_by_id(task.id)
    assert updated_task is not None
    assert updated_task.completed is True


def test_mark_multiple_tasks_complete():
    """Integration test for marking multiple tasks as complete"""
    task_service = TaskService()

    # Add multiple tasks
    task1 = task_service.add_task("First task")
    task2 = task_service.add_task("Second task")
    task3 = task_service.add_task("Third task")

    # Verify all are initially incomplete
    for task in [task1, task2, task3]:
        assert task_service.get_task_by_id(task.id).completed is False

    # Mark them all as complete
    success1 = task_service.mark_task_complete(task1.id)
    success2 = task_service.mark_task_complete(task2.id)
    success3 = task_service.mark_task_complete(task3.id)

    # Verify all operations were successful
    assert success1 is True
    assert success2 is True
    assert success3 is True

    # Verify all tasks are now complete
    for task in [task1, task2, task3]:
        updated_task = task_service.get_task_by_id(task.id)
        assert updated_task.completed is True


def test_mark_nonexistent_task_complete():
    """Integration test for attempting to mark a non-existent task as complete"""
    task_service = TaskService()

    # Try to mark a task that doesn't exist
    success = task_service.mark_task_complete(999)

    # Verify the operation failed
    assert success is False


def test_mark_already_completed_task():
    """Integration test for marking an already completed task"""
    task_service = TaskService()

    # Add and complete a task
    task = task_service.add_task("Already completed task")
    first_mark = task_service.mark_task_complete(task.id)
    assert first_mark is True

    # Verify it's completed
    assert task_service.get_task_by_id(task.id).completed is True

    # Try to mark it complete again
    second_mark = task_service.mark_task_complete(task.id)

    # Verify the operation still succeeds (idempotent)
    assert second_mark is True

    # Verify it's still completed
    final_task = task_service.get_task_by_id(task.id)
    assert final_task.completed is True


def test_mark_task_complete_then_view():
    """Integration test for marking a task complete and then viewing it"""
    task_service = TaskService()

    # Add a task
    task = task_service.add_task("Task to mark and view")

    # Mark it as complete
    task_service.mark_task_complete(task.id)

    # Get all tasks and verify the status
    all_tasks = task_service.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].id == task.id
    assert all_tasks[0].completed is True
    assert all_tasks[0].description == task.description


def test_mark_task_complete_error_handling():
    """Integration test for error handling in mark complete flow"""
    task_service = TaskService()

    # Try to mark complete with invalid ID (should fail gracefully)
    success = task_service.mark_task_complete(-1)
    assert success is False

    success = task_service.mark_task_complete(0)
    assert success is False

    # Verify no tasks were affected
    all_tasks = task_service.get_all_tasks()
    assert len(all_tasks) == 0