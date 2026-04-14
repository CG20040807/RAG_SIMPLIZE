import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/products.csv")

# ❗ 加强：n-gram + stopwords
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    stop_words=["性价比", "推荐", "好用", "不错", "优质"]
)

doc_vectors = vectorizer.fit_transform(
    df["name"] + " " + df["category"] + " " + df["description"]
)

# =========================
# 🔥 Query增强（关键升级）
# =========================
def expand_query(q):
    mapping = {
        "耳机": "耳机 降噪 通勤 学生党 音质",
        "跑鞋": "跑鞋 轻便 运动 缓震",
        "键盘": "键盘 办公 舒适 打字 手感"
    }

    for k, v in mapping.items():
        if k in q:
            return q + " " + v

    return q


def search(query, k=3):
    query = expand_query(query)

    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, doc_vectors).flatten()

    # ❗关键：防止“分数太接近”
    scores = scores + (scores - scores.mean()) * 0.1

    top_k = scores.argsort()[-k:][::-1]

    return df.iloc[top_k]
