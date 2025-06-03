import streamlit as st
from controller import WorkflowController

from dotenv import load_dotenv
load_dotenv()


def main():
    st.title("AI Workflow Assistant")

    idea = st.text_area("請輸入你的產品想法", height=150)

    if st.button("開始產生"):
        if not idea.strip():
            st.warning("請先輸入產品想法")
            return

        controller = WorkflowController()
        files = controller.process(idea)

        st.success("產生完成！以下是輸出檔案：")
        for file in files:
            st.write(f"- {file}")

if __name__ == "__main__":
    main()
