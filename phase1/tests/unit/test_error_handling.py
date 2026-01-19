import pytest
from src.todo_app.services.task_service import TaskService


def test_error_handling_for_nonexistent_operations(task_service):
    """Test error handling for operations on non-existent tasks"""
    # Try to get a non-existent task
    nonexistent_task = task_service.get_task_by_id(999)
    assert nonexistent_task is None

    # Try to update a non-existent task
    update_result = task_service.update_task(999, "New description")
    assert update_result is False

    # Try to mark complete a non-existent task
    complete_result = task_service.mark_task_complete(999)
    assert complete_result is False

    # Try to delete a non-existent task
    delete_result = task_service.delete_task(999)
    assert delete_result is False


def test_input_validation_for_task_descriptions(task_service):
    """Test input validation for task descriptions (empty, too long)"""
    # Test empty description
    with pytest.raises(ValueError):
        task_service.add_task("")

    # Test whitespace-only description
    with pytest.raises(ValueError):
        task_service.add_task("   ")

    # Test description that's too long (1000+ characters)
    long_description = "x" * 1001
    with pytest.raises(ValueError):
        task_service.add_task(long_description)

    # Test valid descriptions
    valid_task = task_service.add_task("Valid description")
    assert valid_task is not None

    valid_task2 = task_service.add_task("x" * 999)  # Just under the limit
    assert valid_task2 is not None


def test_input_validation_for_update_task(task_service):
    """Test input validation when updating task descriptions"""
    # Add a valid task first
    task = task_service.add_task("Original description")

    # Try to update with empty description
    with pytest.raises(ValueError):
        task_service.update_task(task.id, "")

    # Try to update with whitespace-only description
    with pytest.raises(ValueError):
        task_service.update_task(task.id, "   ")

    # Try to update with too-long description
    long_description = "x" * 1001
    with pytest.raises(ValueError):
        task_service.update_task(task.id, long_description)

    # Verify original task is unchanged
    unchanged_task = task_service.get_task_by_id(task.id)
    assert unchanged_task.description == "Original description"


def test_special_characters_in_task_descriptions(task_service):
    """Test handling special characters in task descriptions"""
    special_descriptions = [
        "Task with symbols: !@#$%^&*()",
        "Task with numbers: 123456789",
        "Task with unicode: café résumé naïve",
        "Task with quotes: 'single' and \"double\"",
        "Task with special spaces: \t \n \r",
        "Task with brackets: [] {} ()",
        "Task with math symbols: + - = < >",
        "Task with path-like: C:\\Users\\Name or /home/user"
    ]

    for i, desc in enumerate(special_descriptions):
        task = task_service.add_task(desc)
        assert task.description == desc.strip()
        assert task.id == i + 1  # Sequential IDs


def test_error_messages_for_invalid_task_ids(task_service):
    """Test error handling for invalid task IDs"""
    # Test negative ID
    result = task_service.get_task_by_id(-1)
    assert result is None

    result = task_service.update_task(-1, "New description")
    assert result is False

    result = task_service.mark_task_complete(-1)
    assert result is False

    result = task_service.delete_task(-1)
    assert result is False

    # Test zero ID
    result = task_service.get_task_by_id(0)
    assert result is None

    result = task_service.update_task(0, "New description")
    assert result is False

    result = task_service.mark_task_complete(0)
    assert result is False

    result = task_service.delete_task(0)
    assert result is False


def test_task_model_validation_errors():
    """Test validation errors at the model level"""
    from src.todo_app.models.task import Task

    # Test invalid ID
    with pytest.raises(ValueError):
        Task(0, "Valid description")

    with pytest.raises(ValueError):
        Task(-1, "Valid description")

    with pytest.raises(ValueError):
        Task("invalid", "Valid description")

    # Test invalid description
    with pytest.raises(ValueError):
        Task(1, "")

    with pytest.raises(ValueError):
        Task(1, "   ")

    # Test too long description
    with pytest.raises(ValueError):
        Task(1, "x" * 1001)

    # Test invalid completion status
    with pytest.raises(ValueError):
        Task(1, "Valid description", completed="invalid")

    # Test valid creation
    valid_task = Task(1, "Valid description")
    assert valid_task.id == 1
    assert valid_task.description == "Valid description"
    assert valid_task.completed is False


def test_task_model_update_validation():
    """Test validation during task updates"""
    from src.todo_app.models.task import Task

    task = Task(1, "Original description")

    # Valid update
    task.description = "Updated description"
    assert task.description == "Updated description"

    # Invalid updates should raise errors
    with pytest.raises(ValueError):
        task.description = ""

    with pytest.raises(ValueError):
        task.description = "   "

    # Task should remain unchanged after invalid updates
    assert task.description == "Updated description"

    # Test completion status validation
    with pytest.raises(ValueError):
        task.completed = "invalid"

    # Task status should remain unchanged
    assert task.completed is False


def test_task_list_operations_with_invalid_ids():
    """Test TaskList operations with invalid IDs"""
    from src.todo_app.models.task import TaskList

    task_list = TaskList()

    # Add a valid task
    task = task_list.add_task("Test task")

    # Test operations with invalid IDs
    assert task_list.get_task_by_id(-1) is None
    assert task_list.get_task_by_id(0) is None
    assert task_list.get_task_by_id(999) is None

    assert task_list.update_task(-1, "New description") is False
    assert task_list.update_task(0, "New description") is False
    assert task_list.update_task(999, "New description") is False

    assert task_list.mark_task_complete(-1) is False
    assert task_list.mark_task_complete(0) is False
    assert task_list.mark_task_complete(999) is False

    assert task_list.delete_task(-1) is False
    assert task_list.delete_task(0) is False
    assert task_list.delete_task(999) is False