def rerank(query, docs):

    query_words = set(query.lower())

    scored = []

    for i, row in docs.iterrows():
        text = (row["name"] + row["description"]).lower()
        score = sum([1 for w in query_words if w in text])
        scored.append((i, score))

    ranked = sorted(scored, key=lambda x: x[1], reverse=True)

    return [i[0] for i in ranked if i[1] > 0]
