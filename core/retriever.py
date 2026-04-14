import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/products.csv")

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(
    df["name"] + " " + df["category"] + " " + df["description"]
)

def search(query, k=5):
    q = vectorizer.transform([query])
    scores = cosine_similarity(q, vectors).flatten()

    top_k = scores.argsort()[-k:][::-1]
    return df.iloc[top_k]
