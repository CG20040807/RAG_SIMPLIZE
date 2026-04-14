import faiss
import numpy as np
import pandas as pd
import os
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

INDEX_PATH = "vectorstore/faiss.index"
DATA_PATH = "vectorstore/meta.pkl"

def build_if_not_exists():
    if os.path.exists(INDEX_PATH):
        return

    os.makedirs("vectorstore", exist_ok=True)

    df = pd.read_csv("data/products.csv")

    texts = (df["name"] + " " + df["category"] + " " + df["description"]).tolist()
    emb = model.encode(texts)

    index = faiss.IndexFlatL2(emb.shape[1])
    index.add(np.array(emb))

    faiss.write_index(index, INDEX_PATH)
    df.to_pickle(DATA_PATH)

# 自动保证可用
build_if_not_exists()

index = faiss.read_index(INDEX_PATH)
df = pd.read_pickle(DATA_PATH)

def search(query, k=5):
    vec = model.encode([query])
    D, I = index.search(np.array(vec), k)
    return df.iloc[I[0]]
