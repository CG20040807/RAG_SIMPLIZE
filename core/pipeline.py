from core.retriever import search
from dataclasses import dataclass

# ======================
# ViewModel（关键升级）
# ======================
@dataclass
class ProductView:
    name: str
    price: int
    category: str
    reason: str


# ======================
# Controller（统一逻辑）
# ======================
def run(query):
    docs = search(query)

    results = []

    for _, row in docs.iterrows():
        results.append(
            ProductView(
                name=row["name"],
                price=int(row["price"]),
                category=row["category"],
                reason=f"该商品匹配需求「{query}」，在同类商品中性价比较高"
            )
        )

    return results[:3]
