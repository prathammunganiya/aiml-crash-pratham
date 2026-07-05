import os
from groq import Groq  # type: ignore[import]
from dotenv import load_dotenv
load_dotenv()
groq_key = os.environ["GROQ_API_KEY"]
client = Groq(api_key=GROQ_KEY)

messages = [
    {"role": "system", "content": "You are a helpful AI assistant named CodeBot."}
]

print(" CodeBot is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "quit":
        break

    messages.append({"role": "user", "content": user_input})
    print("Bot: ", end="", flush=True)
    full_response = ""

    stream = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        stream=True
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
            full_response += delta

    print()
    messages.append({"role": "assistant", "content": full_response})