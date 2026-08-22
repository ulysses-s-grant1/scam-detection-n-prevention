import pandas as pd

df = pd.read_csv("data/spam.csv", encoding="latin-1")


df = df[["v1", "v2"]]
df.columns = ["label", "message"]

print(df.head())
print(df.shape)
print(df["label"].value_counts())

df.to_csv("data/spam_clean.csv", index=False)