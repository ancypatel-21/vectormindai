from ingest import load_documents
from search import search_documents
from answer import generate_answer

def main():
    documents = load_documents()

    print("VectorMindAI - Semantic Retrieval Platform")
    query = input("Enter your query: ").strip()

    results = search_documents(query, documents, top_k=3)

    print("\nTop Matches:\n")
    for result in results:
        print(f"Source   : {result['source']}")
        print(f"Distance : {result['distance']:.4f}")
        print(f"Text     : {result['text']}")
        print("-" * 50)

    answer = generate_answer(query, results)

    print("\nFinal Answer:\n")
    print(answer)

if __name__ == "__main__":
    main()