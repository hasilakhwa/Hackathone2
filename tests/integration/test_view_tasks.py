import pytest
from src.todo_app.services.task_service import TaskService


def test_view_tasks_empty_list():
    """Integration test for viewing tasks when the list is empty"""
    task_service = TaskService()

    # Get all tasks when list is empty
    all_tasks = task_service.get_all_tasks()

    # Verify the list is empty
    assert len(all_tasks) == 0


def test_view_tasks_single_task():
    """Integration test for viewing a single task"""
    task_service = TaskService()

    # Add a single task
    added_task = task_service.add_task("Single task for viewing")

    # Get all tasks
    all_tasks = task_service.get_all_tasks()

    # Verify the list has one task
    assert len(all_tasks) == 1
    assert all_tasks[0].id == added_task.id
    assert all_tasks[0].description == added_task.description
    assert all_tasks[0].completed == added_task.completed


def test_view_tasks_multiple_tasks():
    """Integration test for viewing multiple tasks"""
    task_service = TaskService()

    # Add multiple tasks
    task1 = task_service.add_task("First task")
    task2 = task_service.add_task("Second task")
    task3 = task_service.add_task("Third task")

    # Get all tasks
    all_tasks = task_service.get_all_tasks()

    # Verify all tasks are returned
    assert len(all_tasks) == 3

    # Verify each task is present
    task_ids = [task.id for task in all_tasks]
    assert task1.id in task_ids
    assert task2.id in task_ids
    assert task3.id in task_ids

    task_descriptions = [task.description for task in all_tasks]
    assert task1.description in task_descriptions
    assert task2.description in task_descriptions
    assert task3.description in task_descriptions


def test_view_tasks_with_completed_tasks():
    """Integration test for viewing tasks including completed ones"""
    task_service = TaskService()

    # Add tasks and mark some as complete
    task1 = task_service.add_task("Incomplete task")
    task2 = task_service.add_task("Completed task")
    task_service.mark_task_complete(task2.id)

    # Get all tasks
    all_tasks = task_service.get_all_tasks()

    # Verify both tasks are returned
    assert len(all_tasks) == 2

    # Find the tasks by ID
    incomplete_task = task_service.get_task_by_id(task1.id)
    completed_task = task_service.get_task_by_id(task2.id)

    assert incomplete_task is not None
    assert completed_task is not None
    assert incomplete_task.completed is False
    assert completed_task.completed is True


def test_view_tasks_after_modifications():
    """Integration test for viewing tasks after various operations"""
    task_service = TaskService()

    # Add initial tasks
    task1 = task_service.add_task("Original task 1")
    task2 = task_service.add_task("Original task 2")

    # Update a task
    task_service.update_task(task1.id, "Updated task 1")

    # Mark a task as complete
    task_service.mark_task_complete(task2.id)

    # Get all tasks
    all_tasks = task_service.get_all_tasks()

    # Verify the list has both tasks with modifications
    assert len(all_tasks) == 2

    # Find the updated and completed tasks
    updated_task = task_service.get_task_by_id(task1.id)
    completed_task = task_service.get_task_by_id(task2.id)

    assert updated_task.description == "Updated task 1"
    assert completed_task.completed is True


def test_view_tasks_after_deletion():
    """Integration test for viewing tasks after some have been deleted"""
    task_service = TaskService()

    # Add multiple tasks
    task1 = task_service.add_task("Task to keep 1")
    task2 = task_service.add_task("Task to delete")
    task3 = task_service.add_task("Task to keep 2")

    # Delete one task
    success = task_service.delete_task(task2.id)
    assert success is True

    # Get all tasks
    all_tasks = task_service.get_all_tasks()

    # Verify only the remaining tasks are returned
    assert len(all_tasks) == 2

    task_ids = [task.id for task in all_tasks]
    assert task1.id in task_ids
    assert task3.id in task_ids
    assert task2.id not in task_ids  # Deleted task should not be in the list