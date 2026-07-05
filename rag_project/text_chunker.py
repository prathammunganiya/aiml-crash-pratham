"""
text_chunker.py
---------------
Step 2 of the RAG pipeline: split long documents into overlapping,
retrieval-sized chunks.

Strategy (recursive splitting, no external deps required):
  1. Try splitting on paragraph breaks ("\n\n").
  2. If a "paragraph" is still too long, split on sentences.
  3. If a sentence is still too long, hard-split on characters.
  4. Merge small pieces back together up to `chunk_size`, keeping a
     `chunk_overlap` window of trailing characters between consecutive
     chunks so context isn't lost at chunk boundaries.

Each output chunk is a dict:
    {
        "text": "<chunk text>",
        "source": "AuraHealth_Employee_Handbook_2026.txt",
        "chunk_id": "AuraHealth_Employee_Handbook_2026.txt::3"
    }
"""

import re
from typing import List, Dict

CHUNK_SIZE = 800       # target characters per chunk (~150-200 words)
CHUNK_OVERLAP = 150    # characters repeated between consecutive chunks


def split_into_sentences(paragraph: str) -> List[str]:
    # simple sentence splitter good enough for policy/clinical prose
    sentences = re.split(r"(?<=[.!?])\s+", paragraph.strip())
    return [s for s in sentences if s]


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE,
               chunk_overlap: int = CHUNK_OVERLAP) -> List[str]:
    """Recursively split `text` into chunks of roughly `chunk_size` chars."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    # Break any paragraph that's too long into sentences
    units = []
    for para in paragraphs:
        if len(para) <= chunk_size:
            units.append(para)
        else:
            units.extend(split_into_sentences(para))

    # Merge units into chunk_size-sized windows, with overlap
    chunks = []
    current = ""
    for unit in units:
        if len(unit) > chunk_size:
            # hard split an oversized single sentence/unit
            for i in range(0, len(unit), chunk_size):
                piece = unit[i:i + chunk_size]
                if current:
                    chunks.append(current)
                    current = current[-chunk_overlap:] if chunk_overlap else ""
                current += piece
            continue

        if len(current) + len(unit) + 1 <= chunk_size:
            current = f"{current} {unit}".strip()
        else:
            chunks.append(current)
            # start new chunk with overlap from the end of the previous one
            overlap_text = current[-chunk_overlap:] if chunk_overlap else ""
            current = f"{overlap_text} {unit}".strip()

    if current:
        chunks.append(current)

    return chunks


def chunk_documents(documents: List[Dict], chunk_size: int = CHUNK_SIZE,
                     chunk_overlap: int = CHUNK_OVERLAP) -> List[Dict]:
    """Chunk every document and tag each chunk with its source + chunk id."""
    all_chunks = []
    for doc in documents:
        pieces = chunk_text(doc["text"], chunk_size, chunk_overlap)
        for idx, piece in enumerate(pieces):
            all_chunks.append({
                "text": piece,
                "source": doc["source"],
                "chunk_id": f"{doc['source']}::{idx}",
            })
    return all_chunks


if __name__ == "__main__":
    from document_loader import load_documents

    docs = load_documents("synthetic_data")
    chunks = chunk_documents(docs)
    print(f"Produced {len(chunks)} chunks from {len(docs)} documents.\n")
    lengths = [len(c["text"]) for c in chunks]
    print(f"Avg chunk length: {sum(lengths)/len(lengths):.0f} chars, "
          f"min: {min(lengths)}, max: {max(lengths)}")
    print("\nSample chunk:")
    print("-" * 60)
    print(chunks[5]["chunk_id"])
    print(chunks[5]["text"][:400])
