from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index():
    df = pd.read_csv("data/products.csv")

    texts = (df["name"] + " " + df["category"] + " " + df["description"]).tolist()
    embeddings = model.encode(texts)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    faiss.write_index(index, "vectorstore/faiss.index")
    df.to_pickle("vectorstore/meta.pkl")

if __name__ == "__main__":
    build_index()
