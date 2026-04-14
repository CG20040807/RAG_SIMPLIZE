from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(df):
    texts = (df["name"] + " " + df["description"]).tolist()
    embeddings = model.encode(texts, normalize_embeddings=True)
    return np.array(embeddings)
