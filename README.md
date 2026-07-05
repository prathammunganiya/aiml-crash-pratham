# AIML_Crash_Course_Pratham

THIS REPOSITORY CONTAINS PYTHON PRACTICE TASKS COMPLETED DURING AI/ML COURSE THAT I DID UNDER 45 DAY INDUSTRIAL TRAINING.

# Q1 - Extended Intro

This project displays a personalized introduction on the screen.

## Concepts Used

- Python variables
- Dictionaries
- f-strings
- String methods

## File

- intro.py

## Output

- Name
- City
- Favorite subject
- Target role

# Q2 - Skills Counter

This task displays a numbered list of skills along with their total count.

## Concepts Used

- Lists
- for loops
- enumerate()
- len()

## File

- skills_counter.py

# Q3 - Even or Odd Checker

This task checks whether a number is even, odd, or zero.

## Concepts Used

- if / elif / else
- Modulo operator
- User input
- try / except

## File

- even_odd.py

# Q4 - Tip Calculator

This task calculates the tip amount and total bill.

## Concepts Used

- Functions
- Parameters
- Return values
- Dictionaries
- Float math

## File

- tip_calculator.py

# Q5 - Word Frequency

This task counts how many times each word appears in a sentence.

## Concepts Used

- Strings
- split()
- Dictionaries
- Loops

## File

- word_frequency.py

# Q6 - Simple Calculator

This task performs basic arithmetic operations.

## Concepts Used

- Functions
- User input
- Dictionaries
- Conditional statements

## File

- calculator.py

# Q7 - Grade Classifier

This task classifies student grades based on scores.

## Concepts Used

- Lists of dictionaries
- Functions
- Conditional statements
- Sorting with lambda

## File

- grade_classifier.py

# Q8 - Number Guessing Game

This task creates a number guessing game.

## Concepts Used

- while loops
- random module
- Conditional statements

## File

- guessing_game.py

# Q9 - Mini Contact Book

This task creates a simple contact lookup system.

## Concepts Used

- Lists
- Dictionaries
- Functions
- Searching

## File

- contact_book.py
```


```
# AIML Crash Course

## Day 4 Tasks

### student_report.py
Student report card system using OOP.

Run:
python student_report.py

### comprehension_drills.py
Practice list comprehensions.

Run:
python comprehension_drills.py

### file_records.py
Reads student CSV and generates results.

Run:
python file_records.py

### typed_calculator.py
Calculator with type hints.

Run:
python typed_calculator.py

### library_system.py
Inheritance example.

Run:
python library_system.py

### config_manager.py
JSON configuration manager.

Run:
python config_manager.py

### pandas_explore.py
Pandas data analysis.

Run:
python pandas_explore.py

### fraction_class.py
Fraction operations using dunder methods.

Run:
python fraction_class.py

### inventory.py
Inventory management system.

Run:
python inventory.py
```

```
## Day 7 – Python Intermediate + Pandas & NumPy

### student_profile.py

Builds a student profile card using dictionaries, f-strings, and type hints.

### json_report.py

Reads a JSON file and generates a short report.

### learner_class.py

Demonstrates classes, objects, and methods.

### dataframe_filter.py

Selects columns and filters rows in a DataFrame.

### loc_iloc_demo.py

Shows the difference between `.loc` and `.iloc`.

### missing_values.py

Demonstrates handling missing values with `dropna()` and `fillna()`.

### insights.py

Uses `describe()` and `value_counts()` for quick insights.

### numpy_basics.py

Creates, inspects, and slices NumPy arrays.

### numpy_advanced.py

Demonstrates masking, broadcasting, and cosine similarity.
```

```
# Pandas + Visualization + SQL Assignment
**CodeTrade.io — AI/ML Internship Practice Assignment**

---

## Structure

pandas-sql-assignment/
├── Data/          # Sales dataset
├── notebooks/     # Jupyter Notebook (all 9 tasks)
├── sql/           # 15 SQL queries
└── visuals/       # 6 charts + dashboard

---

## Tasks

| # | Task | Tools |
|---|------|-------|
| 1 | Data Audit | pandas |
| 2 | Data Cleaning | pandas |
| 3 | GroupBy Analysis | pandas |
| 4 | Merge & Key Metrics | pandas |
| 5 | Pivot Tables | pandas |
| 6 | Six Visualizations | matplotlib, seaborn |
| 7 | Chart Story (3 insights) | markdown |
| 8 | SQLite + 15 SQL Queries | sqlite3 |
| 9 | Pandas vs SQL Comparison | pandas, sqlite3 |

---

## Dataset

Synthetic sales data generated using numpy — 200 customers, 50 products, 1000 orders across 2023.

---

## Tech Stack

Python | pandas | numpy | matplotlib | seaborn | sqlite3 | Jupyter Notebook

---

# E-Commerce Sales Performance Analysis

## Project Overview
Exploratory Data Analysis on the Brazilian Olist E-Commerce dataset
as part of the CodeTrade.io DecodeLabs Phase 1 Mini Project.

## Business Questions Answered
1. Which product categories generate highest revenue?
2. Which cities/regions contribute most sales?
3. Which customer segments provide highest value?
4. What purchasing patterns exist in customer behavior?
5. Top products by sales volume and revenue
6. How do payment methods influence trends?
7. Which sellers contribute the most value?
8. How do review scores vary by category?
9. Sales volume across time periods
10. Repeat vs one-time customers
11. Data quality issues in merged dataset
12. Merge reliability across source files

## Dataset
Brazilian E-Commerce Public Dataset by Olist  
 https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

# California Housing Price Prediction
### Linear Regression | CodeTrade.io AI/ML Internship

---

## About
Predicting California house prices using **Linear Regression** on a dataset of 20,640 records across 4 tasks — baseline model, feature comparison, split testing, and metric verification.

**Dataset:** `housing.csv` — 20,640 rows × 10 columns  
**Target:** `median_house_value`  
**Library:** scikit-learn

---

## Files
| File | Description |
|------|-------------|
| `housing.csv` | California housing dataset |
| `baseline.py` | Baseline linear regression model |
| `compare_models.py` | 1-feature vs 5-feature model comparison |
| `splits.py` | 80/20, 70/30, 60/40 split analysis |
| `metrics.py` | Manual metric verification + outlier experiment |

---

## Task Results Summary

| Task | What Was Done | Key Result |
|------|--------------|------------|
| Task 1 | Baseline model using `median_income` | R² ≈ 0.47 |
| Task 2 | Added 4 more features | R² improved to ≈ 0.52 |
| Task 3 | Tested 3 different splits | 80/20 was most stable |
| Task 4 | Manual vs sklearn metrics | Results matched exactly  |

---

> Keep `housing.csv` in the **same folder** as all `.py` files before running.

---

## Best Model Metrics (Task 4)

| Metric | Value |
|--------|-------|
| RMSE | ~69,000 |
| MAE | ~51,000 |
| R² | ~0.52 |
| Median Abs Error | ~43,000 |


##  Phase 2 Mini Project

# Order Delay Intelligence

A machine learning project built during the **CodeTrade.io AI/ML Internship**
(DecodeLabs Batch 2026) to predict and explain e-commerce order delays.

---

## What This Project Does
- Predicts whether an order will be delayed using classification models
- Explains predictions using SHAP values
- Provides business recommendations based on findings

---

## Dataset
[Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) by Olist (Kaggle)

---

## Project Structure
```
phase2_mini_project/
├── data/               → CSV files from Kaggle
├── plots/              → Generated charts
├── notebooks/
│   ├── 01_eda.ipynb    → Data cleaning & visualization
│   ├── 02_sql.ipynb    → SQL queries on SQLite
│   └── 03_modeling.ipynb → ML models + SHAP
└── report.md           → Final findings & recommendations
```

---

## Models Used
| Model | F1-Score |
|-------|----------|
| Logistic Regression (baseline) | ~0.67 |
| XGBoost (tuned) | ~0.80 |

---

## How to Run
```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn xgboost shap

# Open notebooks in order
jupyter lab
```

---

# LLM Fundamentals & APIs — Practical Assignment
**Intern:** Pratham Munganiya | **Program:** CodeTrade.io

---

## Project Structure
\```
llm_practical/
├── .env
├── requirements.txt
├── task1_comparison.py
├── task2_prompts.ipynb
├── task3_chat.py
├── task4_tracker.py
└── outputs/
    ├── comparison_results.csv
    ├── prompt_results.csv
    └── token_usage_log.csv
\```

---

## Tasks

| Task | File | Description | Run |
|------|------|-------------|-----|
| 1 | `task1_comparison.py` | Compare Gemini vs Groq responses, save to CSV | `python task1_comparison.py` |
| 2 | `task2_prompts.ipynb` | Test 5 prompt styles, find best result | `jupyter notebook task2_prompts.ipynb` |
| 3 | `task3_chat.py` | Streaming chatbot with full chat history | `python task3_chat.py` |
| 4 | `task4_tracker.py` | Log token usage & cost, generate report | `python task4_tracker.py` |


---


# AuraHealth Nexus — RAG Capstone

A RAG (Retrieval-Augmented Generation) system built over 10 fictional AuraHealth
Nexus documents. The LLM answers *only* from retrieved document chunks —
never from its own pre-trained knowledge.

## How it flows

```
synthetic_data/*.txt
   → document_loader.py   loads & cleans raw text
   → text_chunker.py      splits into 800-char chunks, 150-char overlap
   → embeddings.py        text → vectors (MiniLM, local, free)
   → vector_store.py      stores vectors, does similarity search (FAISS)
   → retriever.py         top-k search → labeled context block
   → memory.py            (bonus) remembers chat, rewrites follow-ups
   → generator.py         sends context + question to LLM → answer
```

## Setup

```bash
cd rag_project
pip install -r requirements.txt
cp .env.example .env        # then paste your API key inside
```

In `main.py` / `evaluate.py`, set:
```python
PROVIDER = "groq"   # or "gemini" / "openrouter" — match your .env key
```

First run downloads the embedding model (~80MB, one-time, needs internet).

## Run it

| Command | What it does |
|---|---|
| `python main.py` | Interactive chatbot, with memory |
| `python evaluate.py` | Runs all 30 assignment questions, prints answers + sources |

**Memory example:**
```
You: What are the symptoms of Phase 2 NeuroCrystal Syndrome?
Assistant: ...
You: And what is the treatment for it?
Assistant: ...   (correctly figures out "it" = Phase 2 NeuroCrystal Syndrome)
```

## Why it's built this way

- **Chunking** — splits by paragraph → sentence, with overlap, so facts don't
  get cut off at a chunk boundary.
- **Embeddings** — MiniLM is free, local, no API key needed.
- **Vector DB** — FAISS does exact similarity search, accurate enough at
  ~200 chunks.
- **Prompting** — system prompt bans outside knowledge and gives a fixed
  "I don't know" fallback, to stop hallucination.
- **Memory** — passes recent Q&A to the LLM, and rewrites vague follow-ups
  ("what about it?") into standalone questions before searching.

## Files

| File | Purpose |
|---|---|
| `document_loader.py` | Load & clean the 10 `.txt` files |
| `text_chunker.py` | Split into overlapping chunks |
| `embeddings.py` | Text → vectors (MiniLM / TF-IDF fallback) |
| `vector_store.py` | FAISS similarity search |
| `retriever.py` | Combines embedding + search into one call |
| `generator.py` | LLM call with grounded prompt |
| `memory.py` | Conversational memory + follow-up rewriting |
| `main.py` | Interactive CLI chatbot |
| `evaluate.py` | Runs all 30 evaluation questions |

##  Author

Pratham Munganiya — B.Tech CSE 
Industrial Training Intern at CodeTrade.io