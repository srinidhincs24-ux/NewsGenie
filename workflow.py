from chatbot import detect_query_type
from news_api import get_news

def process_query(query, category):
    query_type = detect_query_type(query)

    if query_type == "news":
        try:
            return get_news(category)
        except:
            return "⚠️ News API failed. Try again later."
    else:
        return f"🤖 Answer: {query}"