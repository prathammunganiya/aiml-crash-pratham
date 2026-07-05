import pandas as pd

df = pd.read_csv("students.csv")

filtered = df[
    (df["Score"] > 80) &
    (df["City"] == "Banswara")
]

print(filtered[["Name", "Score", "City"]])