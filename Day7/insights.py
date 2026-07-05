import pandas as pd

df = pd.read_csv("students.csv")

print(df.describe())

print("\nCity Counts")
print(df["City"].value_counts())

print("\nObservation:")
print("Highest score is above 90.")
print("Banswara appears most frequently.")