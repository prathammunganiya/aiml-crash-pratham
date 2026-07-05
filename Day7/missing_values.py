import pandas as pd
import numpy as np

data = {
    "Name": ["A", "B", "C"],
    "Score": [90, np.nan, 80],
    "Age": [19, 20, np.nan]
}

df = pd.DataFrame(data)

print("Missing Values")
print(df.isnull().sum())

print("\nDrop NA")
print(df.dropna())

print("\nFill NA")
print(df.fillna(0))