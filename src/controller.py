"""
controller.py
負責調度各 AI Agent，整合輸入輸出流程
"""

from agents.prd_agent import PRDAgent
from agents.research_agent import ResearchAgent
from agents.task_agent import TaskAgent
from agents.kpi_agent import KPIAgent
from utils.helpers import save_markdown

class WorkflowController:
    def __init__(self):
        self.prd_agent = PRDAgent()
        self.research_agent = ResearchAgent()
        self.task_agent = TaskAgent()
        self.kpi_agent = KPIAgent()

    def process_input(self, user_text: str):
        """
        主流程：
        1. 呼叫 ResearchAgent 做市場調研
        2. 呼叫 PRDAgent 產出需求文檔
        3. 呼叫 TaskAgent 產生任務分解
        4. 呼叫 KPIAgent 生成 KPI 指標與排程
        5. 輸出所有 Markdown 文件路徑清單
        """

        research_md = self.research_agent.generate_research_report(user_text)
        prd_md = self.prd_agent.generate_prd(user_text, research_md)
        tasks_md = self.task_agent.generate_tasks(prd_md)
        kpi_md = self.kpi_agent.generate_kpi(tasks_md)

        # 儲存所有文件
        files = []
        for name, content in zip(
            ["research", "prd", "tasks", "kpi"],
            [research_md, prd_md, tasks_md, kpi_md]
        ):
            path = save_markdown(name, content)
            files.append(path)

        return files
