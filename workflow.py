from chatbot import detect_query_type
from news_api import get_news
from duckduckgo_search import DDGS

def get_general_answer(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=2))
            if results:
                return results[0]["body"]
            else:
                return "No answer found."
    except Exception as e:
        return "⚠️ Error fetching answer."

def process_query(query, category):
    if detect_query_type(query) == "news":
        return get_news(category)
    else:
        return get_general_answer(query)
