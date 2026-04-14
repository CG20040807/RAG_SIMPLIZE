from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import pickle
import os

VEC_PATH = "vectorstore/vector.pkl"

def build_vectors():
    os.makedirs("vectorstore", exist_ok=True)

    df = pd.read_csv("data/products.csv")

    texts = (df["name"] + " " + df["category"] + " " + df["description"])

    vectorizer = TfidfVectorizer()
    vecs = vectorizer.fit_transform(texts)

    with open(VEC_PATH, "wb") as f:
        pickle.dump((vectorizer, vecs, df), f)


def load_vectors():
    if not os.path.exists(VEC_PATH):
        build_vectors()

    with open(VEC_PATH, "rb") as f:
        return pickle.load(f)
