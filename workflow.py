from chatbot import detect_query_type
from news_api import get_news
import openai

openai.api_key = "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"

def get_general_answer(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}]
    )
    return response['choices'][0]['message']['content']

def process_query(query, category):
    if detect_query_type(query) == "news":
        return get_news(category)
    else:
        return get_general_answer(query)
