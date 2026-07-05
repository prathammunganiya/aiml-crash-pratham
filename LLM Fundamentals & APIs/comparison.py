import time
import csv
import os
import importlib
from dotenv import load_dotenv
load_dotenv()
groq_key = os.environ["GROQ_API_KEY"]
genai = None

if importlib.util.find_spec("google.generativeai") is not None:
    genai = importlib.import_module("google.generativeai")

Groq = None
if importlib.util.find_spec("groq") is not None:
    groq_module = importlib.import_module("groq")
    Groq = groq_module.Groq
else:
    raise ImportError("groq package is not installed. Install it with pip install groq")


genai.configure(api_key="GEMINI_KEY")
groq_client = Groq(api_key="GROQ_KEY")

PROMPT = "Explain what is machine learning in simple terms."
results = []

# Gemini
start = time.time()
model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content(PROMPT)
gemini_text = response.text
gemini_time = round(time.time() - start, 2)
results.append({"Provider": "Gemini", "Response Time (s)": gemini_time, "Response Length": len(gemini_text), "Output": gemini_text[:200]})

# Groq
start = time.time()
chat = groq_client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[{"role": "user", "content": PROMPT}]
)
groq_text = chat.choices[0].message.content
groq_time = round(time.time() - start, 2)
results.append({"Provider": "Groq/Llama3-70b", "Response Time (s)": groq_time, "Response Length": len(groq_text), "Output": groq_text[:200]})

# Save CSV
os.makedirs("outputs", exist_ok=True)
with open("outputs/comparison_results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"\n{'Provider':<20} {'Time(s)':<12} {'Length':<10} {'Output Preview'}")
print("-" * 80)
for r in results:
    print(f"{r['Provider']:<20} {r['Response Time (s)']:<12} {r['Response Length']:<10} {r['Output'][:50]}...")
print("\nSaved to outputs/comparison_results.csv")