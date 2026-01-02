import pytest
from src.todo_app.services.task_service import TaskService


def test_update_task_description_integration():
    """Integration test for updating a task's description"""
    task_service = TaskService()

    # Add a task
    original_task = task_service.add_task("Original description")

    # Update the task description
    success = task_service.update_task(original_task.id, "Updated description")

    # Verify the operation was successful
    assert success is True

    # Get the task again and verify the description was updated
    updated_task = task_service.get_task_by_id(original_task.id)
    assert updated_task is not None
    assert updated_task.description == "Updated description"
    assert updated_task.id == original_task.id  # ID should remain the same
    assert updated_task.completed == original_task.completed  # Status should remain the same


def test_update_multiple_tasks():
    """Integration test for updating multiple tasks"""
    task_service = TaskService()

    # Add multiple tasks
    task1 = task_service.add_task("Task 1 original")
    task2 = task_service.add_task("Task 2 original")

    # Update both tasks
    success1 = task_service.update_task(task1.id, "Task 1 updated")
    success2 = task_service.update_task(task2.id, "Task 2 updated")

    # Verify both operations were successful
    assert success1 is True
    assert success2 is True

    # Verify both tasks were updated correctly
    updated_task1 = task_service.get_task_by_id(task1.id)
    updated_task2 = task_service.get_task_by_id(task2.id)

    assert updated_task1.description == "Task 1 updated"
    assert updated_task2.description == "Task 2 updated"


def test_update_nonexistent_task():
    """Integration test for attempting to update a non-existent task"""
    task_service = TaskService()

    # Try to update a task that doesn't exist
    success = task_service.update_task(999, "New description")

    # Verify the operation failed
    assert success is False


def test_update_task_preserves_attributes():
    """Integration test to ensure updating preserves other attributes"""
    task_service = TaskService()

    # Add a task and mark it as complete
    original_task = task_service.add_task("Original description")
    task_service.mark_task_complete(original_task.id)

    # Verify it's marked as complete
    task_before_update = task_service.get_task_by_id(original_task.id)
    assert task_before_update.completed is True

    # Update the description
    success = task_service.update_task(original_task.id, "Updated description")

    # Verify the operation was successful
    assert success is True

    # Get the task again and verify only description changed
    updated_task = task_service.get_task_by_id(original_task.id)
    assert updated_task.description == "Updated description"
    assert updated_task.id == original_task.id  # ID preserved
    assert updated_task.completed is True  # Completion status preserved


def test_update_task_then_view():
    """Integration test for updating a task and then viewing it"""
    task_service = TaskService()

    # Add a task
    task = task_service.add_task("Original description")

    # Update the task
    task_service.update_task(task.id, "Updated description")

    # Get all tasks and verify the update
    all_tasks = task_service.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].description == "Updated description"
    assert all_tasks[0].id == task.id


def test_update_task_error_handling():
    """Integration test for error handling in update task flow"""
    task_service = TaskService()

    # Add a task
    task = task_service.add_task("Original description")

    # Try to update with empty description (should raise ValueError)
    with pytest.raises(ValueError):
        task_service.update_task(task.id, "")

    with pytest.raises(ValueError):
        task_service.update_task(task.id, "   ")

    # Verify the original task was not changed due to the errors
    unchanged_task = task_service.get_task_by_id(task.id)
    assert unchanged_task.description == "Original description"


def test_update_task_special_characters():
    """Integration test for updating task with special characters"""
    task_service = TaskService()

    # Add a task
    task = task_service.add_task("Original description")

    # Update with special characters
    special_description = "Updated with special chars: !@#$%^&*()_+"
    success = task_service.update_task(task.id, special_description)

    # Verify the operation was successful
    assert success is True

    # Verify the description was updated correctly
    updated_task = task_service.get_task_by_id(task.id)
    assert updated_task.description == special_description


def test_update_task_trims_whitespace():
    """Integration test to ensure description is properly handled"""
    task_service = TaskService()

    # Add a task
    task = task_service.add_task("Original description")

    # Update with leading/trailing whitespace (should be handled by model validation)
    success = task_service.update_task(task.id, "  Updated with spaces  ")

    # Verify the operation was successful
    assert success is True

    # Get the task and verify the description is properly stored
    updated_task = task_service.get_task_by_id(task.id)
    # Based on our model implementation, it should trim whitespace
    assert updated_task.description == "Updated with spaces"