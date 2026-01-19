import pytest
from datetime import datetime
from src.todo_app.models.task import Task, TaskList


def test_task_creation_valid():
    """Test creating a valid task with proper parameters"""
    task = Task(1, "Test description")

    assert task.id == 1
    assert task.description == "Test description"
    assert task.completed is False
    assert isinstance(task.created_at, datetime)


def test_task_creation_with_completion_status():
    """Test creating a task with explicit completion status"""
    task = Task(1, "Test description", completed=True)

    assert task.id == 1
    assert task.description == "Test description"
    assert task.completed is True


def test_task_description_validation():
    """Test that task description cannot be empty"""
    with pytest.raises(ValueError):
        Task(1, "")

    with pytest.raises(ValueError):
        Task(1, "   ")

    with pytest.raises(ValueError):
        Task(1, None)


def test_task_description_length_validation():
    """Test that task description cannot be too long"""
    long_description = "x" * 1000

    with pytest.raises(ValueError):
        Task(1, long_description)


def test_task_id_validation():
    """Test that task ID must be a positive integer"""
    with pytest.raises(ValueError):
        Task(0, "Test description")

    with pytest.raises(ValueError):
        Task(-1, "Test description")

    with pytest.raises(ValueError):
        Task("invalid", "Test description")


def test_task_completion_status_validation():
    """Test that completion status must be a boolean"""
    with pytest.raises(ValueError):
        Task(1, "Test description", completed="invalid")


def test_task_description_update():
    """Test updating task description with validation"""
    task = Task(1, "Original description")

    task.description = "Updated description"
    assert task.description == "Updated description"

    with pytest.raises(ValueError):
        task.description = ""

    with pytest.raises(ValueError):
        task.description = "   "


def test_task_completion_update():
    """Test updating task completion status"""
    task = Task(1, "Test description")

    assert task.completed is False
    task.completed = True
    assert task.completed is True

    with pytest.raises(ValueError):
        task.completed = "invalid"


def test_task_to_dict():
    """Test converting task to dictionary representation"""
    task = Task(1, "Test description", completed=True)
    task_dict = task.to_dict()

    assert task_dict['id'] == 1
    assert task_dict['description'] == "Test description"
    assert task_dict['completed'] is True
    assert 'created_at' in task_dict


def test_task_string_representation():
    """Test string representation of task"""
    task = Task(1, "Test description", completed=True)
    completed_str = str(task)
    assert "[✓]" in completed_str
    assert "1." in completed_str
    assert "Test description" in completed_str

    task_incomplete = Task(2, "Incomplete task", completed=False)
    incomplete_str = str(task_incomplete)
    assert "[○]" in incomplete_str


def test_task_list_initialization():
    """Test initializing an empty task list"""
    task_list = TaskList()

    assert len(task_list.get_all_tasks()) == 0
    assert task_list.get_next_id() == 1


def test_task_list_add_task():
    """Test adding a task to the list"""
    task_list = TaskList()

    task = task_list.add_task("New task")

    assert task.id == 1
    assert task.description == "New task"
    assert len(task_list.get_all_tasks()) == 1
    assert task_list.get_next_id() == 2


def test_task_list_get_all_tasks():
    """Test getting all tasks from the list"""
    task_list = TaskList()

    task1 = task_list.add_task("Task 1")
    task2 = task_list.add_task("Task 2")

    all_tasks = task_list.get_all_tasks()

    assert len(all_tasks) == 2
    assert all_tasks[0] == task1
    assert all_tasks[1] == task2


def test_task_list_get_task_by_id():
    """Test finding a task by its ID"""
    task_list = TaskList()

    task1 = task_list.add_task("Task 1")
    task2 = task_list.add_task("Task 2")

    found_task = task_list.get_task_by_id(1)
    assert found_task == task1

    found_task = task_list.get_task_by_id(2)
    assert found_task == task2

    not_found = task_list.get_task_by_id(999)
    assert not_found is None


def test_task_list_update_task():
    """Test updating a task's description"""
    task_list = TaskList()

    task = task_list.add_task("Original description")

    # Update the task
    result = task_list.update_task(1, "Updated description")
    assert result is True

    # Verify the update
    updated_task = task_list.get_task_by_id(1)
    assert updated_task.description == "Updated description"

    # Try to update non-existent task
    result = task_list.update_task(999, "New description")
    assert result is False


def test_task_list_mark_task_complete():
    """Test marking a task as complete"""
    task_list = TaskList()

    task = task_list.add_task("Task to complete")
    assert task.completed is False

    # Mark as complete
    result = task_list.mark_task_complete(1)
    assert result is True

    # Verify completion
    completed_task = task_list.get_task_by_id(1)
    assert completed_task.completed is True

    # Try to mark non-existent task
    result = task_list.mark_task_complete(999)
    assert result is False


def test_task_list_delete_task():
    """Test deleting a task from the list"""
    task_list = TaskList()

    task1 = task_list.add_task("Task 1")
    task2 = task_list.add_task("Task 2")

    assert len(task_list.get_all_tasks()) == 2

    # Delete a task
    result = task_list.delete_task(1)
    assert result is True
    assert len(task_list.get_all_tasks()) == 1

    # Verify the correct task was deleted
    remaining_task = task_list.get_task_by_id(2)
    assert remaining_task is not None

    # Try to delete non-existent task
    result = task_list.delete_task(999)
    assert result is False