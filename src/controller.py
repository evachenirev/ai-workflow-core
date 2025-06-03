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

    def process(self, input_text):
        prd = self.prd_agent.generate_prd(input_text)
        research = self.research_agent.generate_research(input_text)
        tasks = self.task_agent.generate_tasks(input_text)
        kpi = self.kpi_agent.generate_kpi(input_text)

        # 輸出為 Markdown 檔案，並回傳檔案路徑清單
        files = []
        files.append(save_markdown("prd.md", prd))
        files.append(save_markdown("research.md", research))
        files.append(save_markdown("tasks.md", tasks))
        files.append(save_markdown("kpi.md", kpi))

        return files
