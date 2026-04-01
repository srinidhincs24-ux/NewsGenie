def detect_query_type(query):
    news_keywords = ["news", "latest", "update", "headlines"]

    if any(word in query.lower() for word in news_keywords):
        return "news"
    else:
        return "general"