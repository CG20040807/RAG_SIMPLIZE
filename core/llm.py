import requests

API_KEY = "sk-a48bc0257a6d44b3b926548d09d38ce4"

def rewrite_query(query):

    prompt = f"""
你是电商搜索助手。
请把用户需求转换成商品关键词（只输出关键词，用空格分隔）

用户输入：{query}

输出：
"""

    try:
        res = requests.post(
            "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "qwen-turbo",
                "input": {
                    "prompt": prompt
                }
            },
            timeout=10
        )

        data = res.json()

        # ✅ 安全解析（关键）
        if "output" in data and "text" in data["output"]:
            return data["output"]["text"].strip()

        return query  # fallback

    except Exception as e:
        return query  # ❗绝对不能让系统崩


def general_answer(query):
    return "这个问题更偏通用问题，不属于商品推荐"
