from chatbot import detect_query_type
from news_api import get_news

def get_general_answer(query):
    query_lower = query.lower()

    if "full form of cpu" in query_lower:
        return "CPU stands for Central Processing Unit."

    elif "full form of ram" in query_lower:
        return "RAM stands for Random Access Memory."

    elif "ai" in query_lower:
        return "Artificial Intelligence (AI) is the simulation of human intelligence in machines."

    elif "python" in query_lower:
        return "Python is a high-level programming language used in web development, data science, and AI."

    elif "what is" in query_lower:
        topic = query_lower.replace("what is", "").strip()
        return f"{topic.capitalize()} is an important concept in technology."

    else:
        return f"{query.capitalize()} is a commonly discussed topic."
        
def process_query(query, category):
    if detect_query_type(query) == "news":
        return get_news(category)
    else:
        return get_general_answer(query)
