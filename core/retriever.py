from sentence_transformers import SentenceTransformer
from core.faiss_index import search_index
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, k=20):

    q_vec = model.encode([query], normalize_embeddings=True)

    idx, scores, df = search_index(np.array(q_vec), k)

    return df.iloc[idx]
