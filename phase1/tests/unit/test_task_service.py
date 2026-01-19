import pytest
from src.todo_app.services.task_service import TaskService


def test_add_task_valid_description(task_service):
    """Test adding a task with a valid description"""
    task = task_service.add_task("Test task description")

    assert task.id == 1
    assert task.description == "Test task description"
    assert task.completed is False
    assert len(task_service.get_all_tasks()) == 1


def test_add_task_empty_description(task_service):
    """Test that adding a task with empty description raises ValueError"""
    with pytest.raises(ValueError):
        task_service.add_task("")

    with pytest.raises(ValueError):
        task_service.add_task("   ")


def test_add_multiple_tasks(task_service):
    """Test adding multiple tasks with sequential IDs"""
    task1 = task_service.add_task("First task")
    task2 = task_service.add_task("Second task")
    task3 = task_service.add_task("Third task")

    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3

    all_tasks = task_service.get_all_tasks()
    assert len(all_tasks) == 3


def test_get_all_tasks_empty_list(task_service):
    """Test getting all tasks when the list is empty"""
    tasks = task_service.get_all_tasks()

    assert len(tasks) == 0


def test_get_all_tasks_with_tasks(task_service):
    """Test getting all tasks when the list has tasks"""
    task_service.add_task("Task 1")
    task_service.add_task("Task 2")

    tasks = task_service.get_all_tasks()

    assert len(tasks) == 2
    assert tasks[0].description == "Task 1"
    assert tasks[1].description == "Task 2"


def test_get_task_by_id_existing_task(task_service):
    """Test getting a task by its ID when it exists"""
    task = task_service.add_task("Test task")

    found_task = task_service.get_task_by_id(task.id)

    assert found_task is not None
    assert found_task.id == task.id
    assert found_task.description == task.description


def test_get_task_by_id_nonexistent_task(task_service):
    """Test getting a task by its ID when it doesn't exist"""
    task_service.add_task("Test task")

    nonexistent_task = task_service.get_task_by_id(999)

    assert nonexistent_task is None


def test_update_task_valid(task_service):
    """Test updating an existing task's description"""
    task = task_service.add_task("Original description")

    success = task_service.update_task(task.id, "Updated description")

    assert success is True
    updated_task = task_service.get_task_by_id(task.id)
    assert updated_task.description == "Updated description"


def test_update_task_nonexistent(task_service):
    """Test updating a non-existent task"""
    success = task_service.update_task(999, "New description")

    assert success is False


def test_update_task_empty_description(task_service):
    """Test that updating with empty description raises ValueError"""
    task = task_service.add_task("Original description")

    with pytest.raises(ValueError):
        task_service.update_task(task.id, "")


def test_mark_task_complete_valid(task_service):
    """Test marking an existing task as complete"""
    task = task_service.add_task("Test task")
    assert task.completed is False

    success = task_service.mark_task_complete(task.id)

    assert success is True
    completed_task = task_service.get_task_by_id(task.id)
    assert completed_task.completed is True


def test_mark_task_complete_nonexistent(task_service):
    """Test marking a non-existent task as complete"""
    success = task_service.mark_task_complete(999)

    assert success is False


def test_delete_task_valid(task_service):
    """Test deleting an existing task"""
    task = task_service.add_task("Test task")
    all_tasks_before = task_service.get_all_tasks()
    assert len(all_tasks_before) == 1

    success = task_service.delete_task(task.id)

    assert success is True
    all_tasks_after = task_service.get_all_tasks()
    assert len(all_tasks_after) == 0


def test_delete_task_nonexistent(task_service):
    """Test deleting a non-existent task"""
    success = task_service.delete_task(999)

    assert success is False


def test_get_next_task_id(task_service):
    """Test getting the next available task ID"""
    # Initially should be 1
    assert task_service.get_next_task_id() == 1

    # Add a task, next ID should be 2
    task_service.add_task("Test task")
    assert task_service.get_next_task_id() == 2

    # Add another task, next ID should be 3
    task_service.add_task("Another task")
    assert task_service.get_next_task_id() == 3