"""
vector_store.py
---------------
Step 4 of the RAG pipeline: store chunk embeddings and search them.

Uses FAISS (Facebook AI Similarity Search) when it's installed, since
it's fast and is exactly what the task brief suggests. Falls back to a
plain numpy matrix + cosine similarity if FAISS isn't available in your
environment (functionally identical for a dataset this small — the
difference only matters at large scale).
"""

import numpy as np
from typing import List, Dict


class VectorStore:
    def __init__(self, dim: int):
        self.dim = dim
        self.chunks: List[Dict] = []   # parallel metadata for each vector
        self._use_faiss = False
        self._matrix = None
        try:
            import faiss
            self._faiss = faiss
            self.index = faiss.IndexFlatIP(dim)  # inner product = cosine (vectors are normalized)
            self._use_faiss = True
        except ImportError:
            print("[vector_store] faiss not installed — using numpy "
                  "cosine-similarity fallback (fine for small datasets).")
            self.index = None

    def add(self, vectors: np.ndarray, chunk_metadata: List[Dict]):
        assert len(vectors) == len(chunk_metadata)
        if self._use_faiss:
            self.index.add(vectors)
        else:
            self._matrix = vectors if self._matrix is None else np.vstack([self._matrix, vectors])
        self.chunks.extend(chunk_metadata)

    def search(self, query_vector: np.ndarray, top_k: int = 5) -> List[Dict]:
        """Return top_k chunks (with similarity scores) for a single query vector."""
        query_vector = query_vector.reshape(1, -1)

        if self._use_faiss:
            scores, indices = self.index.search(query_vector, top_k)
            scores, indices = scores[0], indices[0]
        else:
            sims = (self._matrix @ query_vector.T).flatten()
            indices = np.argsort(-sims)[:top_k]
            scores = sims[indices]

        results = []
        for idx, score in zip(indices, scores):
            if idx == -1:
                continue
            chunk = dict(self.chunks[idx])
            chunk["score"] = float(score)
            results.append(chunk)
        return results


if __name__ == "__main__":
    from document_loader import load_documents
    from text_chunker import chunk_documents
    from embeddings import get_embedder

    docs = load_documents("synthetic_data")
    chunks = chunk_documents(docs)
    texts = [c["text"] for c in chunks]

    embedder = get_embedder("tfidf")   # offline self-test
    embedder.fit(texts)
    vectors = embedder.embed(texts)

    store = VectorStore(dim=vectors.shape[1])
    store.add(vectors, chunks)

    query = "What is the master override code for the Cognitive Reset Sequence?"
    query_vec = embedder.embed([query])[0]
    results = store.search(query_vec, top_k=3)

    print(f"Query: {query}\n")
    for r in results:
        print(f"[{r['score']:.3f}] {r['chunk_id']}")
        print(r["text"][:200], "...\n")
