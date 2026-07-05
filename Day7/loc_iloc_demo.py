import pandas as pd

df = pd.read_csv("students.csv")

print("Using LOC")
print(df.loc[0:2, ["Name", "Score"]])

print("\nUsing ILOC")
print(df.iloc[0:3, [0, 3]])

print("\nloc = label based")
print("iloc = position based")