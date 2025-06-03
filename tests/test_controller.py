import pytest
from src.controller import WorkflowController

def test_process_input():
    controller = WorkflowController()
    user_text = "設計一款智能助理App"
    files = controller.process_input(user_text)
    assert len(files) == 4
    for f in files:
        assert f.endswith(".md")
