import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vectorstore/faiss.index")
df = pd.read_pickle("vectorstore/meta.pkl")

def search(query, k=5):
    vec = model.encode([query])
    D, I = index.search(np.array(vec), k)
    return df.iloc[I[0]]
