import streamlit as st
from core.pipeline import run

st.set_page_config(page_title="电商RAG系统", layout="centered")

st.title("🛒 AI电商推荐系统")

# ======================
# 输入引导（关键）
# ======================
st.markdown("### 💡 你可以这样问我")

st.info("""
- 200元以内跑鞋推荐  
- 送女生生日礼物  
- 性价比耳机推荐  
- 办公键盘推荐  
""")

query = st.text_input(
    "请输入你的需求",
    placeholder="例如：200元跑鞋 / 送女生礼物 / 降噪耳机"
)

# ======================
# UI渲染（绝不再写json）
# ======================
def render(item):
    st.markdown(f"""
### 🛍️ {item.name}

💰 价格：{item.price} 元  
🏷️ 类别：{item.category}  

📌 推荐理由：{item.reason}

---
""")

if query:
    results = run(query)

    st.markdown("## 🧠 推荐结果")

    for r in results:
        render(r)
