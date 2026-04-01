def get_general_answer(query):
    query_lower = query.lower()

    # Full forms
    if "full form of cpu" in query_lower:
        return "CPU stands for Central Processing Unit."

    elif "full form of ram" in query_lower:
        return "RAM stands for Random Access Memory."

    elif "full form of ai" in query_lower:
        return "AI stands for Artificial Intelligence."

    # Definitions
    elif "ai" in query_lower or "artificial intelligence" in query_lower:
        return "Artificial Intelligence (AI) is the simulation of human intelligence in machines."

    elif "python" in query_lower:
        return "Python is a high-level programming language used in web development, data science, and AI."

    # General fallback
    elif "what is" in query_lower:
        topic = query_lower.replace("what is", "").strip()
        return f"{topic.capitalize()} is an important concept in technology or general knowledge."

    else:
        return f"{query.capitalize()} is a commonly discussed topic related to technology or general knowledge."
