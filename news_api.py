import requests

API_KEY = "pub_56fe96d3300c4c01a5b10b4cb42f6b5e"

def get_news(category):
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&category={category}&language=en"
    
    response = requests.get(url)
    data = response.json()

    articles = data.get("results", [])
    
    if not articles:
        return "No news found."

    result = ""
    for i, article in enumerate(articles[:5]):
        result += f"{i+1}. {article['title']}\n"

    return result