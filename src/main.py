"""
main.py
Streamlit 主程式入口，負責 UI 介面與使用者互動
"""

import streamlit as st
from controller import WorkflowController

def main():
    st.title("AI Workflow Core")
    st.write("將您的想法轉化為具體計劃與文件")

    user_input = st.text_area("請輸入您的想法", height=200)
    if st.button("開始生成"):
        if user_input.strip():
            controller = WorkflowController()
            result_files = controller.process_input(user_input)
            st.success("文件生成完成！請查看 outputs 資料夾。")
            for f in result_files:
                st.markdown(f"- {f}")
        else:
            st.warning("請輸入有效內容")

if __name__ == "__main__":
    main()
