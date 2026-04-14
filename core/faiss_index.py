import faiss
import numpy as np
from core.embedding import get_embeddings
import pandas as pd

df = pd.read_csv("data/products.csv")

embeddings = get_embeddings(df)

dim = embeddings.shape[1]

index = faiss.IndexFlatIP(dim)
index.add(embeddings)

def search_index(query_vector, k=20):
    scores, idx = index.search(query_vector, k)
    return idx[0], scores[0], df
