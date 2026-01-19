from typing import Optional
from src.todo_app.services.task_service import TaskService


class TodoCLI:
    """
    Command-line interface for the todo application
    """

    def __init__(self, task_service: TaskService):
        """
        Initialize the CLI with a task service

        Args:
            task_service: The service to handle task operations
        """
        self.task_service = task_service

    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "="*50)
        print("           TODO APPLICATION")
        print("="*50)
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Mark task as complete")
        print("4. Update task description")
        print("5. Delete task")
        print("6. Exit")
        print("="*50)

    def get_user_choice(self) -> str:
        """
        Get user's menu choice

        Returns:
            str: The user's choice
        """
        try:
            choice = input("Enter your choice (1-6): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nExiting application...")
            return "6"

    def add_task(self):
        """Handle adding a new task"""
        try:
            description = input("Enter task description: ").strip()
            if not description:
                print("Error: Task description cannot be empty.")
                return

            task = self.task_service.add_task(description)
            print(f"✓ Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error adding task: {e}")

    def view_tasks(self):
        """Handle viewing all tasks"""
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("\nNo tasks found.")
            return

        print(f"\n{'ID':<4} {'Status':<8} {'Description'}")
        print("-" * 50)
        for task in tasks:
            status = "✓ Done" if task.completed else "○ Todo"
            print(f"{task.id:<4} {status:<8} {task.description}")

    def mark_task_complete(self):
        """Handle marking a task as complete"""
        try:
            task_id_str = input("Enter task ID to mark as complete: ").strip()
            if not task_id_str:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_str)
            success = self.task_service.mark_task_complete(task_id)

            if success:
                print(f"✓ Task {task_id} marked as complete.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
        except Exception as e:
            print(f"Unexpected error marking task complete: {e}")

    def update_task(self):
        """Handle updating a task description"""
        try:
            task_id_str = input("Enter task ID to update: ").strip()
            if not task_id_str:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_str)
            task = self.task_service.get_task_by_id(task_id)

            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            new_description = input(f"Enter new description (current: '{task.description}'): ").strip()
            if not new_description:
                print("Error: Task description cannot be empty.")
                return

            success = self.task_service.update_task(task_id, new_description)

            if success:
                print(f"✓ Task {task_id} updated successfully.")
            else:
                print(f"Error: Failed to update task {task_id}.")
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Error: Please enter a valid task ID (number).")
            else:
                print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error updating task: {e}")

    def delete_task(self):
        """Handle deleting a task"""
        try:
            task_id_str = input("Enter task ID to delete: ").strip()
            if not task_id_str:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_str)
            success = self.task_service.delete_task(task_id)

            if success:
                print(f"✓ Task {task_id} deleted successfully.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
        except Exception as e:
            print(f"Unexpected error deleting task: {e}")

    def run(self):
        """Run the main application loop"""
        print("Welcome to the Todo Application!")
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_task_complete()
            elif choice == "4":
                self.update_task()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

            # Pause to let user see the result before showing menu again
            input("\nPress Enter to continue...")