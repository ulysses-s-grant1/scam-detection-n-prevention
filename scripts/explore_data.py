import pandas as pd

df = pd.read_csv("data/spam_clean.csv")

for word in ["won", "prize", "free"]:
    ham_count = df[df["label"] == "ham"]["message"].str.lower().str.contains(word).sum()
    spam_count = df[df["label"] == "spam"]["message"].str.lower().str.contains(word).sum()
    print(f"'{word}' → appears in {ham_count} ham messages, {spam_count} spam messages")