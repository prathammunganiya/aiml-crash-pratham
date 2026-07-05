import pandas as pd

data = {
    "name": ["A","B","C","D","E","F","G","H","I","J"],
    "city": ["Jaipur","Delhi","Delhi","Mumbai","Jaipur",
             "Delhi","Mumbai","Jaipur","Mumbai","Delhi"],
    "math_score": [90,80,85,70,95,78,88,67,92,75],
    "science_score": [88,82,80,75,90,85,89,70,91,78],
    "english_score": [86,79,83,72,94,80,90,68,93,77]
}

df = pd.DataFrame(data)

print(df[["math_score","science_score","english_score"]].mean())

df["total"] = (
    df["math_score"] +
    df["science_score"] +
    df["english_score"]
)

print(df.loc[df["total"].idxmax()])

print(df.groupby("city").size())

print(df[df["math_score"] > 75])

print(df.nlargest(3, "total"))