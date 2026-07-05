"""
embeddings.py
-------------
Step 3 of the RAG pipeline: turn text chunks into vector embeddings.

Two backends are supported:

1. "sentence-transformers" (default, recommended) — uses the free,
   local `all-MiniLM-L6-v2` model. No API key needed, runs on CPU.
   First run downloads the model (~80MB) from HuggingFace, so you
   need internet access once.

2. "tfidf" — a pure scikit-learn fallback with no downloads at all.
   It's not true semantic search (it matches on word overlap, not
   meaning), but it's handy for quick offline testing of the
   chunking/retrieval plumbing before your model download finishes,
   or if HuggingFace is unreachable on your network.

Both expose the same interface: `.fit(texts)` and `.embed(texts)`,
so vector_store.py doesn't need to know which one is active.
"""

import numpy as np
from typing import List


class SentenceTransformerEmbedder:
    """Local, free, semantic embeddings via sentence-transformers."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model_name)
        self.dim = self.model.get_sentence_embedding_dimension()

    def fit(self, texts: List[str]):
        # no fitting needed — the model is pre-trained
        return self

    def embed(self, texts: List[str]) -> np.ndarray:
        vectors = self.model.encode(
            texts,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,  # so dot product == cosine similarity
        )
        return vectors.astype("float32")


class TfidfEmbedder:
    """Offline fallback: TF-IDF + cosine similarity. No downloads required."""

    def __init__(self, max_features: int = 4096):
        from sklearn.feature_extraction.text import TfidfVectorizer
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            stop_words="english",
            ngram_range=(1, 2),
        )
        self.dim = None
        self._fitted = False

    def fit(self, texts: List[str]):
        self.vectorizer.fit(texts)
        self.dim = len(self.vectorizer.vocabulary_)
        self._fitted = True
        return self

    def embed(self, texts: List[str]) -> np.ndarray:
        if not self._fitted:
            raise RuntimeError("Call .fit(all_chunk_texts) before .embed().")
        matrix = self.vectorizer.transform(texts).toarray().astype("float32")
        # L2-normalize rows so dot product ~= cosine similarity
        norms = np.linalg.norm(matrix, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return matrix / norms


def get_embedder(backend: str = "sentence-transformers"):
    """
    Factory function. Tries the requested backend, falls back to TF-IDF
    with a warning if sentence-transformers/HuggingFace isn't reachable.
    """
    if backend == "sentence-transformers":
        try:
            return SentenceTransformerEmbedder()
        except Exception as e:
            print(f"[embeddings] Could not load sentence-transformers "
                  f"({e}). Falling back to TF-IDF (word-overlap search, "
                  f"not true semantic search).")
            return TfidfEmbedder()
    elif backend == "tfidf":
        return TfidfEmbedder()
    else:
        raise ValueError(f"Unknown embedding backend: {backend}")


if __name__ == "__main__":
    # Quick offline self-test using the TF-IDF backend (no downloads)
    from document_loader import load_documents
    from text_chunker import chunk_documents

    docs = load_documents("synthetic_data")
    chunks = chunk_documents(docs)
    texts = [c["text"] for c in chunks]

    embedder = get_embedder("tfidf")
    embedder.fit(texts)
    vectors = embedder.embed(texts[:5])
    print(f"Embedded 5 sample chunks -> shape {vectors.shape}")
