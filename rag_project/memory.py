"""
memory.py
---------
Bonus challenge: lightweight conversational memory.

Two things make follow-up questions work ("What are the symptoms of
Phase 2?" -> "And what is the treatment for it?"):

1. ChatMemory stores each (question, answer) turn so it can be passed
   to the LLM as prior context (see generator.py's chat_history param).

2. condense_question() rewrites a follow-up into a fully standalone
   question BEFORE retrieval — this matters because the retriever only
   ever sees the current query string, so "it" or "that" needs to be
   resolved into something the embedder can actually search for.
   Without this step, retrieval for "what is the treatment for it?"
   would search for the literal word "it" and return junk.
"""

from typing import List, Dict


class ChatMemory:
    def __init__(self, max_turns: int = 6):
        self.max_turns = max_turns
        self.turns: List[Dict] = []

    def add(self, question: str, answer: str):
        self.turns.append({"question": question, "answer": answer})
        self.turns = self.turns[-self.max_turns:]

    def get_history(self) -> List[Dict]:
        return self.turns

    def clear(self):
        self.turns = []


def condense_question(question: str, chat_history: List[Dict],
                       provider: str = "groq") -> str:
    """
    Use a cheap/fast LLM call to rewrite a follow-up question into a
    standalone one, using the last couple of turns as context.
    If there's no history yet, just return the question unchanged
    (saves an API call on the very first turn).
    """
    if not chat_history:
        return question

    recent = chat_history[-2:]
    history_text = "\n".join(
        f"Q: {t['question']}\nA: {t['answer']}" for t in recent
    )

    prompt = (
        "Given this recent conversation:\n"
        f"{history_text}\n\n"
        f"Rewrite this follow-up question as a fully standalone question "
        f"that doesn't depend on the conversation above. "
        f"Only output the rewritten question, nothing else.\n\n"
        f"Follow-up question: {question}"
    )

    if provider == "groq":
        import os
        from groq import Groq
        client = Groq(api_key=os.environ["GROQ_API_KEY"])
        resp = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # small/fast model is enough for this
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return resp.choices[0].message.content.strip()

    # If you're using a different provider, swap in the equivalent call here.
    return question
