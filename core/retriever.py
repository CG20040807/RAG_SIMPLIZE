import faiss
import pandas as pd
from core.embedding import encode

index = faiss.read_index("vectorstore/faiss.index")
df = pd.read_pickle("vectorstore/data.pkl")

def retrieve(query, k=50):
    q_vec = encode([query])
    scores, idx = index.search(q_vec, k)
    return df.iloc[idx[0]]
