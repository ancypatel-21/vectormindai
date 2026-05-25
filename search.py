from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(documents):
    texts = [doc["text"] for doc in documents]
    embeddings = model.encode(texts, convert_to_numpy=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings.astype(np.float32))

    return index, embeddings

def search_documents(query, documents, top_k=3):
    index, _ = build_index(documents)

    query_embedding = model.encode([query], convert_to_numpy=True).astype(np.float32)
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx, dist in zip(indices[0], distances[0]):
        results.append({
            "source": documents[idx]["source"],
            "text": documents[idx]["text"],
            "distance": float(dist)
        })

    return results