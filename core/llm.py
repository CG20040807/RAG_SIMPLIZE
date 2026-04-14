import requests

API_KEY = "sk-a48bc0257a6d44b3b926548d09d38ce4"

def call_llm(prompt):
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "qwen-turbo",
        "input": {
            "prompt": prompt
        }
    }

    res = requests.post(url, json=data, headers=headers)
    return res.json()["output"]["text"]
