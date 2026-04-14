from core.retriever import search
from core.llm import call_llm

def build_context(docs):
    return "\n".join([
        f"{r['name']} | {r['price']}元 | {r['description']}"
        for _, r in docs.iterrows()
    ])

def answer(query):
    docs = search(query)

    context = build_context(docs)

    prompt = f"""
你是一个20年专业电商推荐系统。

用户需求：{query}

候选商品：
{context}

要求：
1. 推荐3个商品
2. 从多方面考虑后给出详细的理由
3. 仔细对比后按性价比排序
4. 用中文结构化输出，不要多余符号空白及emoji
"""

    return call_llm(prompt)
