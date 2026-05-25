def generate_answer(query, results):
    if not results:
        return "No relevant information found."

    top_context = results[0]["text"]
    supporting_context = "\n".join(
        [f"- {item['source']}: {item['text']}" for item in results]
    )

    return f"""Query: {query}

Relevant context:
{supporting_context}

Answer:
Based on the retrieved documents, the most relevant information suggests that {top_context}
"""