from chatbot import detect_query_type
from news_api import get_news

def get_general_answer(query):
    query = query.lower()

    if "ai" in query or "artificial intelligence" in query:
        return "Artificial Intelligence (AI) is the simulation of human intelligence in machines that can learn, reason, and make decisions."

    elif "python" in query:
        return "Python is a high-level programming language known for its simplicity and wide use in web development, data science, and AI."

    elif "c language" in query or "c better than python" in query:
        return "C is faster and more efficient than Python, but Python is easier to learn and more versatile."

    elif "what is" in query:
        return f"{query.replace('what is', '').strip().capitalize()} is an important concept in technology and computing."

    else:
        return f"{query.capitalize()} is a topic related to modern technology, computing, or general knowledge."

def process_query(query, category):
    if detect_query_type(query) == "news":
        return get_news(category)
    else:
        return get_general_answer(query)
