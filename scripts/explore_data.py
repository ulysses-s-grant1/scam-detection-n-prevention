import pandas as pd

# download and clean the raw dataset
df = pd.read_csv("data/spam.csv", encoding="latin-1")
df = df[["v1", "v2"]]
df.columns = ["label", "message"]
df.to_csv("data/spam_clean.csv", index=False)

print(df.head())
print(df.shape)
print(df["label"].value_counts())