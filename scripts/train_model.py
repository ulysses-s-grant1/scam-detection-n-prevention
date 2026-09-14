from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "spam_clean.csv"
MODEL_DIR = BASE_DIR / "models"


def build_reinforcement_examples():
    return pd.DataFrame({
        "message": [
            "I won a prize at school competition",
            "She won first prize in the science fair",
            "Congrats on winning the prize at the game night",
            "Hi, is this the dog groomer on 5th street? I need to bring Bella in tomorrow morning. Wait, I think my assistant gave me the wrong number! I'm so sorry to bother you. I'm David, I own a clothing boutique downtown.",
            "Babe, I wish I could video call you tonight, but the signal here on the base is terrible. Can we just stick to messaging for now?",
            "We only matched on Tuesday, but my bank froze my account while traveling. Could you wire me $150 until tomorrow?",
            "My uncle's cryptocurrency trading platform has been making incredible returns. Send a screenshot of your banking app so I can see your limits.",
            "Just left the arcade, we pooled enough tickets for that top shelf prize!",
            "The neighborhood block party raffle winner gets a bakery basket. Text me when you're home.",
        ],
        "label": ["ham", "ham", "ham", "spam", "spam", "spam", "spam", "ham", "ham"],
    })


def train():
    df = pd.read_csv(DATA_PATH)
    X_train, X_test, y_train, y_test = train_test_split(
        df["message"], df["label"], test_size=0.2, random_state=42,
        stratify=df["label"],
    )
    extra_examples = build_reinforcement_examples()
    X_train = pd.concat([X_train, extra_examples["message"]], ignore_index=True)
    y_train = pd.concat([y_train, extra_examples["label"]], ignore_index=True)

    vectorizer = CountVectorizer(ngram_range=(1, 2))
    X_train_vectors = vectorizer.fit_transform(X_train)
    X_test_vectors = vectorizer.transform(X_test)
    model = MultinomialNB()
    model.fit(X_train_vectors, y_train)
    predictions = model.predict(X_test_vectors)

    print(classification_report(y_test, predictions, zero_division=0))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions, labels=["ham", "spam"]))

    regression_tests = [
        ("I won a prize at school competition", "ham"),
        ("Congratulations! You've won a free prize, claim now!", "spam"),
        ("We only matched on Tuesday, but my bank froze my account while traveling. Could you wire me $150 until tomorrow?", "spam"),
    ]
    print("\n--- Regression Checks ---")
    for message, expected in regression_tests:
        predicted = model.predict(vectorizer.transform([message]))[0]
        result = "PASS" if predicted == expected else "FAIL"
        print(f"{result} | expected: {expected}, got: {predicted} | {message}")

    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_DIR / "spam_classifier.joblib")
    joblib.dump(vectorizer, MODEL_DIR / "vectorizer.joblib")


if __name__ == "__main__":
    train()