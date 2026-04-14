import streamlit as st
from core.pipeline import run
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.title("电商RAG系统")

st.caption("例：跑鞋 / 熬夜吃什么 / Python怎么写")

query = st.text_input("请输入需求")

if query:
    result = run(query)

    if isinstance(result, str):
        st.warning(result)
    else:
        for r in result:
            st.markdown(f"""
### {r['name']}
💰 {r['price']} 元  
📦 {r['category']}
---
""")
