from core.retriever import search
from core.retriever import retrieve
from core.reranker import rerank

def run(query):

    # 1️⃣ FAISS召回
    docs = retrieve(query, k=30)

    # 2️⃣ rerank精排
    ranked_idx = rerank(query, docs)

    results = []

    for i in ranked_idx[:5]:
        row = docs.loc[i]

        results.append({
            "name": row["name"],
            "price": row["price"],
            "category": row["category"],
            "reason": f"匹配需求：{query}"
        })

    return results
