import streamlit as st
from core.rag import answer
from core.retriever import build_if_not_exists

st.title("🛒 电商RAG系统")

# 🔥 关键：启动时保证index存在
build_if_not_exists()

query = st.text_input("输入你的需求")

if query:
    result = answer(query)
    st.write(result)
