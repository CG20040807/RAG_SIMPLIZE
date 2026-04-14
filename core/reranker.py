from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs):
    pairs = [
        (query, row["name"] + " " + row["description"])
        for _, row in docs.iterrows()
    ]

    scores = reranker.predict(pairs)

    ranked = sorted(
        zip(docs.index, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [i[0] for i in ranked]
