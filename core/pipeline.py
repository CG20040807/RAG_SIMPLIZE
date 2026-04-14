from core.intent import is_ecommerce
from core.llm import rewrite_query, general_answer
from core.retriever import retrieve
from core.reranker import rerank

def run(query):

    # 1️⃣ 意图判断
    if not is_ecommerce(query):
        return general_answer(query)

    # 2️⃣ query改写
    new_query = rewrite_query(query)

    # 3️⃣ 检索
    docs = retrieve(new_query, 50)

    # 4️⃣ rerank
    ranked_ids = rerank(query, docs)

    # 5️⃣ 兜底
    if not ranked_ids:
        return "没找到相关商品"

    results = []

    for i in ranked_ids[:5]:
        row = docs.loc[i]

        results.append({
            "name": row["name"],
            "price": row["price"],
            "category": row["category"]
        })

    return results
