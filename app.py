import streamlit as st
from core.pipeline import run

st.set_page_config(page_title="工业级RAG电商系统")

st.title("🛒 FAISS + Rerank 电商推荐系统")

query = st.text_input("请输入你的需求（如：200元跑鞋 / 降噪耳机）")

if query:
    results = run(query)

    st.subheader("推荐结果")

    for r in results:
        st.markdown(f"""
### 🛍 {r['name']}
💰 价格：{r['price']}
🏷 类别：{r['category']}

📌 推荐理由：{r['reason']}
---
""")
