"""
generator.py
------------
Step 6 of the RAG pipeline: send the retrieved context + user question
to an LLM and get back a grounded answer.

Supports three providers (pick whichever API key you already have
working from your earlier LLM Fundamentals practical):
  - "groq"       -> requires GROQ_API_KEY
  - "gemini"     -> requires GEMINI_API_KEY
  - "openrouter" -> requires OPENROUTER_API_KEY

All three expose an OpenAI-compatible /chat/completions endpoint (or in
Gemini's case, the official SDK), so the interface is one function:
    generate_answer(question, context, chat_history) -> str
"""

import os
from typing import List, Dict

SYSTEM_PROMPT = """You are an internal assistant for AuraHealth Nexus. \
Answer the user's question using ONLY the information in the provided \
context below. Do not use any outside knowledge and do not guess.

If the answer is not contained in the context, reply exactly: \
"I don't have enough information in the provided documents to answer that."

Be precise and include exact numbers, codes, or names when the context \
provides them."""


def _build_messages(question: str, context: str,
                     chat_history: List[Dict]) -> List[Dict]:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    # include prior turns so follow-up questions ("and what's the treatment
    # for it?") resolve correctly
    for turn in chat_history:
        messages.append({"role": "user", "content": turn["question"]})
        messages.append({"role": "assistant", "content": turn["answer"]})

    user_msg = f"Context:\n{context}\n\nQuestion: {question}"
    messages.append({"role": "user", "content": user_msg})
    return messages


def generate_answer(question: str, context: str,
                     chat_history: List[Dict] = None,
                     provider: str = "groq") -> str:
    chat_history = chat_history or []
    messages = _build_messages(question, context, chat_history)

    if provider == "groq":
        from groq import Groq
        client = Groq(api_key=os.environ["GROQ_API_KEY"])
        resp = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.1,
        )
        return resp.choices[0].message.content

    elif provider == "openrouter":
        from openai import OpenAI
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ["OPENROUTER_API_KEY"],
        )
        resp = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct",
            messages=messages,
            temperature=0.1,
        )
        return resp.choices[0].message.content

    elif provider == "gemini":
        import google.generativeai as genai
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        model = genai.GenerativeModel(
            "gemini-1.5-flash", system_instruction=SYSTEM_PROMPT
        )
        # Gemini wants history as its own turn format; keep it simple by
        # folding history + context into one prompt for this project's scope.
        history_text = "\n".join(
            f"Q: {t['question']}\nA: {t['answer']}" for t in chat_history
        )
        prompt = f"{history_text}\n\nContext:\n{context}\n\nQuestion: {question}"
        resp = model.generate_content(prompt)
        return resp.text

    else:
        raise ValueError(f"Unknown provider: {provider}")


def generate_answer_streaming(question: str, context: str,
                               chat_history: List[Dict] = None,
                               provider: str = "groq"):
    """Same as generate_answer but yields tokens as they arrive (Groq shown;
    OpenRouter follows the identical OpenAI-style pattern)."""
    chat_history = chat_history or []
    messages = _build_messages(question, context, chat_history)

    if provider == "groq":
        from groq import Groq
        client = Groq(api_key=os.environ["GROQ_API_KEY"])
        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.1,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta
    else:
        # fall back to non-streaming for providers not wired up above
        yield generate_answer(question, context, chat_history, provider)
