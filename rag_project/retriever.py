"""
retriever.py
------------
Ties embeddings.py + vector_store.py together into one object:
build once from your documents, then call .retrieve(query) repeatedly.
"""

from typing import List, Dict
from document_loader import load_documents
from text_chunker import chunk_documents
from embeddings import get_embedder
from vector_store import VectorStore


class Retriever:
    def __init__(self, data_folder: str = "synthetic_data",
                 embedding_backend: str = "sentence-transformers",
                 chunk_size: int = 800, chunk_overlap: int = 150):
        print(f"[retriever] Loading documents from '{data_folder}'...")
        docs = load_documents(data_folder)

        print(f"[retriever] Chunking {len(docs)} documents...")
        self.chunks = chunk_documents(docs, chunk_size, chunk_overlap)
        print(f"[retriever] Produced {len(self.chunks)} chunks.")

        print(f"[retriever] Loading embedder ('{embedding_backend}')...")
        self.embedder = get_embedder(embedding_backend)
        texts = [c["text"] for c in self.chunks]
        self.embedder.fit(texts)

        print("[retriever] Embedding all chunks (one-time cost)...")
        vectors = self.embedder.embed(texts)

        self.store = VectorStore(dim=vectors.shape[1])
        self.store.add(vectors, self.chunks)
        print("[retriever] Ready.\n")

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        query_vec = self.embedder.embed([query])[0]
        return self.store.search(query_vec, top_k=top_k)

    def format_context(self, results: List[Dict]) -> str:
        """Turn retrieved chunks into a labeled context block for the LLM prompt."""
        blocks = []
        for i, r in enumerate(results, 1):
            blocks.append(f"[Source {i}: {r['source']}]\n{r['text']}")
        return "\n\n---\n\n".join(blocks)


if __name__ == "__main__":
    retriever = Retriever(embedding_backend="tfidf")  # offline self-test
    results = retriever.retrieve(
        "What percentage of test subjects in Project Icarus exhibited "
        "documented behavioral anomalies?", top_k=3
    )
    for r in results:
        print(f"[{r['score']:.3f}] {r['chunk_id']}")
