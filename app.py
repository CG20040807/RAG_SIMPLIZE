import streamlit as st
from core.rag import answer

st.set_page_config(page_title="电商RAG系统")

st.title("🛒 电商AI推荐系统（RAG）")

query = st.text_input("请输入你的需求（例如：200元跑鞋）")

if query:
    with st.spinner("AI正在思考中..."):
        result = answer(query)

    st.markdown("### 推荐结果")
    st.write(result)
