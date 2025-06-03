import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from controller import WorkflowController

from dotenv import load_dotenv
load_dotenv()


@pytest.fixture
def controller():
    return WorkflowController()

def test_process_returns_files(controller):
    input_text = "開發一個協助自由接案者的時間管理 App"
    files = controller.process(input_text)
    
    # 確認回傳是 list，且有四個檔案
    assert isinstance(files, list)
    assert len(files) == 4

    # 檢查檔案是否存在，且是 md 檔
    for f in files:
        assert os.path.exists(f)
        assert f.endswith(".md")

def test_generated_content_not_empty(controller):
    input_text = "設計一款智能助理App"
    files = controller.process(input_text)

    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            # 檢查檔案內容不為空
            assert content.strip() != ""

def teardown_module(module):
    # 測試結束後清理 outputs 目錄的檔案
    output_dir = "outputs"
    if os.path.exists(output_dir):
        for filename in os.listdir(output_dir):
            filepath = os.path.join(output_dir, filename)
            os.remove(filepath)
