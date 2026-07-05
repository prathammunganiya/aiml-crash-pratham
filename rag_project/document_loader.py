"""
document_loader.py
-------------------
Step 1 of the RAG pipeline: load and lightly clean the raw .txt documents.

Each document becomes a dict:
    {
        "source": "AuraHealth_Employee_Handbook_2026.txt",
        "text": "<full cleaned text>"
    }
"""

import os
import re
from pathlib import Path
from typing import List, Dict


def clean_text(raw_text: str) -> str:
    """Normalize line endings and collapse excessive blank lines/whitespace."""
    text = raw_text.replace("\r\n", "\n").replace("\r", "\n")
    # collapse 3+ blank lines into 2 (keeps paragraph breaks, removes noise)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # collapse repeated spaces/tabs
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def load_documents(folder_path: str) -> List[Dict]:
    """
    Load every .txt file in `folder_path` into memory.

    Returns a list of {"source": filename, "text": cleaned_text} dicts.
    """
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    documents = []
    for file_path in sorted(folder.glob("*.txt")):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            raw = f.read()
        documents.append({
            "source": file_path.name,
            "text": clean_text(raw),
        })

    if not documents:
        raise ValueError(f"No .txt files found in {folder_path}")

    return documents


if __name__ == "__main__":
    docs = load_documents("synthetic_data")
    print(f"Loaded {len(docs)} documents:")
    for d in docs:
        print(f"  - {d['source']}  ({len(d['text'])} chars, "
              f"~{len(d['text'].split())} words)")
