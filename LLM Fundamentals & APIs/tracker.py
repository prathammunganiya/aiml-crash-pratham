import os
import csv
import time
from datetime import datetime
from groq import Groq  # type: ignore[import]
from dotenv import load_dotenv
load_dotenv()
groq_key = os.environ["GROQ_API_KEY"]

client = Groq(api_key=GROQ_KEY)

os.makedirs("outputs", exist_ok=True)
LOG_FILE = "outputs/token_usage_log.csv"

COST_PER_1K_INPUT  = 0.00005
COST_PER_1K_OUTPUT = 0.00008

def call_and_log(prompt):
    start = time.time()
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    elapsed = round(time.time() - start, 2)

    usage = response.usage
    input_tokens  = usage.prompt_tokens
    output_tokens = usage.completion_tokens
    total_tokens  = usage.total_tokens
    cost = (input_tokens / 1000 * COST_PER_1K_INPUT) + (output_tokens / 1000 * COST_PER_1K_OUTPUT)

    log = {
        "Timestamp"    : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Prompt"       : prompt[:100],
        "Response"     : response.choices[0].message.content[:100],
        "Input Tokens" : input_tokens,
        "Output Tokens": output_tokens,
        "Total Tokens" : total_tokens,
        "Est. Cost ($)": round(cost, 6),
        "Time (s)"     : elapsed
    }

    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=log.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(log)

    print(f" Logged | Tokens: {total_tokens} | Cost: ${round(cost, 6)}")

def generate_report():
    with open(LOG_FILE, "r") as f:
        rows = list(csv.DictReader(f))
    print("\n========= USAGE REPORT =========")
    print(f"Total Requests : {len(rows)}")
    print(f"Total Tokens   : {sum(int(r['Total Tokens']) for r in rows)}")
    print(f"Total Cost     : ${round(sum(float(r['Est. Cost ($)']) for r in rows), 6)}")
    print("================================\n")

prompts = [
    "What is deep learning?",
    "Explain neural networks in 2 lines.",
    "What is the difference between AI and ML?"
]
for p in prompts:
    call_and_log(p)
generate_report()