"""
main.py
-------
Entry point: builds the RAG pipeline once, then runs an interactive
chat loop with conversational memory (the bonus challenge).

Usage:
    python main.py

Environment variables (set the one matching your PROVIDER below, in a
.env file or your shell — see .env.example):
    GROQ_API_KEY / GEMINI_API_KEY / OPENROUTER_API_KEY
"""

import os
from dotenv import load_dotenv

from retriever import Retriever
from generator import generate_answer
from memory import ChatMemory, condense_question

load_dotenv()  # reads a .env file if present

# ---- config -----------------------------------------------------
PROVIDER = "groq"                      # "groq" | "gemini" | "openrouter"
EMBEDDING_BACKEND = "sentence-transformers"  # "sentence-transformers" | "tfidf"
TOP_K = 5
# -------------------------------------------------------------------


def main():
    retriever = Retriever(
        data_folder="synthetic_data",
        embedding_backend=EMBEDDING_BACKEND,
    )
    memory = ChatMemory()

    print("AuraHealth Nexus RAG assistant. Type 'exit' to quit, "
          "'clear' to reset conversation memory.\n")

    while True:
        question = input("You: ").strip()
        if not question:
            continue
        if question.lower() in ("exit", "quit"):
            break
        if question.lower() == "clear":
            memory.clear()
            print("(conversation memory cleared)\n")
            continue

        # 1. Resolve follow-ups like "and what's the treatment for it?"
        #    into a standalone question before retrieval.
        standalone_question = condense_question(
            question, memory.get_history(), provider=PROVIDER
        )

        # 2. Retrieve relevant chunks
        results = retriever.retrieve(standalone_question, top_k=TOP_K)
        context = retriever.format_context(results)

        # 3. Generate a grounded answer
        answer = generate_answer(
            question, context, memory.get_history(), provider=PROVIDER
        )

        print(f"\nAssistant: {answer}\n")
        print("  (sources: " +
              ", ".join(sorted({r["source"] for r in results})) + ")\n")

        # 4. Save this turn to memory for future follow-ups
        memory.add(question, answer)


if __name__ == "__main__":
    main()
