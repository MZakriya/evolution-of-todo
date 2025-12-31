import sys
import os
import time
from pathlib import Path

# Add the phase-1 directory to the path so imports work correctly
phase1_path = str(Path(__file__).parent.parent)
sys.path.insert(0, phase1_path)

from src.manager import TodoManager
from src.models import Priority, Status
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.spinner import Spinner


def main():
    console = Console()
    manager = TodoManager()

    # Wrap the main loop in a global try...except Exception block (T060)
    try:
        while True:  # T039: Create a `while True:` loop
            # Display a nice Menu Panel (Add Task, View Tasks, Exit) (T061)
            menu_content = (
                "[bold cyan]1.[/bold cyan] Add Task\n"
                "[bold cyan]2.[/bold cyan] View Tasks\n"  # Added View Tasks option (T017)
                "[bold cyan]3.[/bold cyan] Update Task\n"  # Added Update Task option (T024)
                "[bold cyan]4.[/bold cyan] Delete Task\n"  # Added Delete Task option (T031)
                "[bold cyan]5.[/bold cyan] Mark Task Status\n"  # Added Mark Task Status option (T037)
                "[bold cyan]6.[/bold cyan] Exit"
            )
            menu_panel = Panel(menu_content, title="Todo App Menu", border_style="blue")
            console.print(menu_panel)

            try:
                choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6"], default="6")
            except KeyboardInterrupt:
                console.print("\n[blue]Goodbye![/blue]")
                break  # Handle KeyboardInterrupt gracefully (T059)
            except EOFError:
                console.print("\n[blue]Goodbye![/blue]")
                break

            if choice == "1":  # Handle Option "Add Task" (T012)
                try:
                    # Prompt user for `Title` (Str), `Description` (Str), and `Priority` (Choice: LOW, MEDIUM, HIGH) (T013)
                    title = Prompt.ask("Enter task title")

                    # Validate title is not empty during creation (T049)
                    if not title.strip():
                        console.print("[red]Error: Title cannot be empty. Task not created.[/red]")
                        continue

                    description = Prompt.ask("Enter task description (optional)", default="")

                    priority_choice = Prompt.ask(
                        "Enter priority",
                        choices=["low", "medium", "high"],
                        default="medium"
                    )

                    priority = Priority(priority_choice)

                    # Use spinner when adding task (T061)
                    with console.status("[bold green]Adding task...", spinner="clock"):
                        time.sleep(0.5)  # Simulate small delay for better UX
                        task = manager.add_task(title, description, priority)

                    # Print a success message in Green (T014)
                    console.print(f"[green]Task '{task.title}' added successfully with ID {task.id}![/green]")

                except ValueError as e:
                    console.print(f"[red]Error: {e}[/red]")
                except Exception as e:
                    console.print(f"[red]Unexpected error: {e}[/red]")

            elif choice == "2":  # Handle Option "View Tasks" (T017)
                try:
                    tasks = manager.get_all_tasks()  # Call manager.get_all_tasks()

                    if not tasks:  # If list is empty: Print a message "No tasks found" (T018)
                        console.print("[yellow]No tasks found[/yellow]")
                    else:  # If list has tasks:
                        # Create a rich.table.Table
                        task_table = Table(title="All Tasks")
                        task_table.add_column("ID", style="dim")
                        task_table.add_column("Title")
                        task_table.add_column("Description")
                        task_table.add_column("Status")
                        task_table.add_column("Priority")

                        # Loop through tasks and add rows to the table
                        for task in tasks:
                            # Colorize the output (e.g., Green for Done, Red for High Priority)
                            status_color = "green" if task.status == Status.DONE else "red" if task.status == Status.IN_PROGRESS else "white"
                            priority_color = "red" if task.priority == Priority.HIGH else "yellow" if task.priority == Priority.MEDIUM else "blue"

                            task_table.add_row(
                                str(task.id),
                                task.title,
                                task.description,
                                f"[{status_color}]{task.status.value}[/]",
                                f"[{priority_color}]{task.priority.value}[/]"
                            )

                        console.print(task_table)
                except Exception as e:
                    console.print(f"[red]Error displaying tasks: {e}[/red]")

            elif choice == "3":  # Handle Option "Update Task" (T024-T026)
                try:
                    # Prompt for Task ID (T025)
                    task_id_input = Prompt.ask("Enter task ID to update")

                    # Validate that the input is a number (T047)
                    try:
                        task_id = int(task_id_input)
                    except ValueError:
                        console.print("[red]Error: Task ID must be a number.[/red]")
                        continue

                    # Get the current task to show existing values
                    current_tasks = manager.get_all_tasks()
                    current_task = None
                    for task in current_tasks:
                        if task.id == task_id:
                            current_task = task
                            break

                    if current_task is None:
                        console.print(f"[red]Task with ID {task_id} not found[/red]")
                        continue

                    # Prompt for new values, allowing user to press Enter to keep current values (T025)
                    new_title = Prompt.ask(f"Enter new title (current: {current_task.title})", default=current_task.title)

                    # Validate title is not empty during update (T045, T046, T049)
                    if not new_title.strip():
                        console.print("[red]Error: Title cannot be empty.[/red]")
                        continue

                    new_description = Prompt.ask(f"Enter new description (current: {current_task.description})", default=current_task.description)
                    new_priority_choice = Prompt.ask(
                        f"Enter new priority (current: {current_task.priority.value})",
                        choices=["low", "medium", "high"],
                        default=current_task.priority.value
                    )

                    # Validate priority values are from the allowed enum (T048)
                    try:
                        new_priority = Priority(new_priority_choice)
                    except ValueError:
                        console.print(f"[red]Error: Invalid priority value: {new_priority_choice}[/red]")
                        continue

                    # Call manager.update_task() (T025)
                    updated_task = manager.update_task(
                        task_id=task_id,
                        title=new_title,
                        description=new_description,
                        priority=new_priority
                    )

                    # Show success message (T023)
                    console.print(f"[green]Task updated successfully![/green]")

                except ValueError as e:
                    console.print(f"[red]Error: {e}[/red]")
                except Exception as e:
                    console.print(f"[red]Unexpected error: {e}[/red]")

            elif choice == "4":  # Handle Option "Delete Task" (T031-T032)
                try:
                    # Prompt for Task ID (T032)
                    task_id_input = Prompt.ask("Enter task ID to delete")

                    # Validate that the input is a number (T047)
                    try:
                        task_id = int(task_id_input)
                    except ValueError:
                        console.print("[red]Error: Task ID must be a number.[/red]")
                        continue

                    # Confirm deletion (y/n) (T029)
                    confirm = Prompt.ask(f"Are you sure you want to delete task {task_id}? (y/n)", choices=["y", "n"], default="n")

                    if confirm == "y":
                        # Use spinner when deleting task (T061)
                        with console.status("[bold red]Deleting task...", spinner="clock"):
                            time.sleep(0.5)  # Simulate small delay for better UX
                            manager.delete_task(task_id)

                        # Show success message (T030)
                        console.print(f"[green]Task {task_id} deleted successfully![/green]")
                    else:
                        console.print("[yellow]Deletion cancelled.[/yellow]")

                except ValueError as e:
                    console.print(f"[red]Error: {e}[/red]")
                except Exception as e:
                    console.print(f"[red]Unexpected error: {e}[/red]")

            elif choice == "5":  # Handle Option "Mark Task Status" (T037-T038)
                try:
                    # Prompt for Task ID (T038)
                    task_id_input = Prompt.ask("Enter task ID to update status")

                    # Validate that the input is a number (T047)
                    try:
                        task_id = int(task_id_input)
                    except ValueError:
                        console.print("[red]Error: Task ID must be a number.[/red]")
                        continue

                    # Get the current task to show existing values
                    current_tasks = manager.get_all_tasks()
                    current_task = None
                    for task in current_tasks:
                        if task.id == task_id:
                            current_task = task
                            break

                    if current_task is None:
                        console.print(f"[red]Task with ID {task_id} not found[/red]")
                        continue

                    # Prompt for new status (T038)
                    new_status_choice = Prompt.ask(
                        f"Enter new status (current: {current_task.status.value})",
                        choices=["todo", "in_progress", "done"],
                        default=current_task.status.value
                    )

                    # Convert string to Status enum
                    if new_status_choice == "todo":
                        new_status = Status.TODO
                    elif new_status_choice == "in_progress":
                        new_status = Status.IN_PROGRESS
                    elif new_status_choice == "done":
                        new_status = Status.DONE
                    else:
                        console.print(f"[red]Invalid status: {new_status_choice}[/red]")
                        continue

                    # Call manager.update_task_status() (T038)
                    updated_task = manager.update_task_status(task_id=task_id, status=new_status)

                    # Show success message (T036)
                    console.print(f"[green]Task status updated successfully![/green]")

                except ValueError as e:
                    console.print(f"[red]Error: {e}[/red]")
                except Exception as e:
                    console.print(f"[red]Unexpected error: {e}[/red]")

            elif choice == "6":  # Handle Option "Exit" (T041)
                console.print("[blue]Goodbye![/blue]")
                break

    except KeyboardInterrupt:
        console.print("\n[blue]Goodbye![/blue]")  # Handle KeyboardInterrupt at the top level (T059)
    except Exception as e:
        console.print(f"\n[red]Unexpected error in main application: {e}[/red]")  # Global exception handling (T060)
    finally:
        console.print("\n[blue]Goodbye![/blue]")  # Ensure graceful shutdown (T059)


if __name__ == "__main__":
    main()