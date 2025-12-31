import sys
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO

# Add the src directory to the path so imports work correctly
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from main import main


def test_add_task_flow(capsys):
    """Test Add Task Flow: Simulate user selecting "1", entering "Buy Milk", "Desc", "HIGH", and verify "Task Added" message appears."""
    # Mock user inputs: "1" (add task), "Buy Milk", "Desc", "high", "6" (exit)
    user_inputs = iter(["1", "Buy Milk", "Desc", "high", "6"])

    def mock_prompt_ask(prompt, choices=None, default=None):
        try:
            return next(user_inputs)
        except StopIteration:
            return "6"  # Default to exit if no more inputs

    with patch('rich.prompt.Prompt.ask', side_effect=mock_prompt_ask):
        main()

    # Capture the output
    captured = capsys.readouterr()

    # Verify that the task added message appears in the output
    assert "Task 'Buy Milk' added successfully" in captured.out


def test_view_task_flow(capsys):
    """Test View Task Flow: Simulate user selecting "2" and verify the table headers appear in output."""
    # First add a task, then view tasks, then exit
    user_inputs = iter(["1", "Test Task", "Test Desc", "medium", "2", "6"])

    def mock_prompt_ask(prompt, choices=None, default=None):
        try:
            return next(user_inputs)
        except StopIteration:
            return "6"  # Default to exit if no more inputs

    with patch('rich.prompt.Prompt.ask', side_effect=mock_prompt_ask):
        main()

    # Capture the output
    captured = capsys.readouterr()

    # Verify that the table headers appear in the output
    assert "All Tasks" in captured.out
    assert "ID" in captured.out
    assert "Title" in captured.out
    assert "Description" in captured.out
    assert "Status" in captured.out
    assert "Priority" in captured.out


def test_exit_flow(capsys):
    """Test Exit Flow: Simulate user selecting "5" (Exit) and verify the loop breaks."""
    # Mock user input to select "6" (Exit) immediately
    user_inputs = iter(["6"])

    def mock_prompt_ask(prompt, choices=None, default=None):
        try:
            return next(user_inputs)
        except StopIteration:
            return "6"  # Default to exit if no more inputs

    with patch('rich.prompt.Prompt.ask', side_effect=mock_prompt_ask):
        main()

    # Capture the output
    captured = capsys.readouterr()

    # Verify that the exit message appears in the output
    assert "Goodbye!" in captured.out