from chatbot import detect_query_type
from news_api import get_news
from duckduckgo_search import DDGS

def get_general_answer(query):
    try:
        results = DDGS().text(query, max_results=2)
        return "\n".join([r["body"] for r in results])
    except:
        return "Sorry, couldn't fetch answer."

def process_query(query, category):
    if detect_query_type(query) == "news":
        try:
            return get_news(category)
        except:
            return "⚠️ News API failed."
    else:
        return get_general_answer(query)