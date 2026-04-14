import pandas as pd
from rank_bm25 import BM25Okapi

df = pd.read_csv("data/products.csv")

# =========================
# 商品“增强描述”（关键）
# =========================
corpus = []
for _, row in df.iterrows():
    text = f"""
    {row['name']}
    {row['category']}
    {row['description']}
    {row.get('scenario','')}
    {row.get('user_type','')}
    """
    corpus.append(text.lower().split())

bm25 = BM25Okapi(corpus)

# =========================
# Query增强（关键）
# =========================
def expand_query(q):
    rules = {
        "耳机": "降噪 通勤 学生党 音质",
        "跑鞋": "缓震 轻便 运动 日常",
        "键盘": "办公 手感 打字 舒适"
    }

    for k, v in rules.items():
        if k in q:
            q = q + " " + v

    return q.lower().split()


def search(query, k=3):
    tokenized_query = expand_query(query)

    scores = bm25.get_scores(tokenized_query)

    top_k = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]

    return df.iloc[top_k]
