import os
import faiss
import pandas as pd
from core.embedding import encode

def build():

    df = pd.read_csv("data/products.csv")

    texts = (df["name"] + " " + df["description"]).tolist()
    vectors = encode(texts)

    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)

    os.makedirs("vectorstore", exist_ok=True)

    faiss.write_index(index, "vectorstore/faiss.index")
    df.to_pickle("vectorstore/data.pkl")


if __name__ == "__main__":
    build()
