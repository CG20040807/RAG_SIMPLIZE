import faiss
import pandas as pd
import os
from core.embedding import encode
from core.index_builder import build

# ❗如果index不存在 → 自动创建
if not os.path.exists("vectorstore/faiss.index"):
    build()

index = faiss.read_index("vectorstore/faiss.index")
df = pd.read_pickle("vectorstore/data.pkl")

def retrieve(query, k=50):
    q_vec = encode([query])
    scores, idx = index.search(q_vec, k)
    return df.iloc[idx[0]]
