import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from core.embedding import load_vectors

vectorizer, vecs, df = load_vectors()

def search(query, k=5):
    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, vecs).flatten()

    top_k = np.argsort(scores)[-k:][::-1]
    return df.iloc[top_k]
