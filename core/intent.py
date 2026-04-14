def is_ecommerce(query):

    keywords = ["买", "推荐", "耳机", "跑鞋", "保健品", "键盘"]

    return any(k in query for k in keywords)
