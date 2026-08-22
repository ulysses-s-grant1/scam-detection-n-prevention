import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/spam_clean.csv")

X = df["message"]
Y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)


model = MultinomialNB()
model.fit(X_train_vectors, y_train)

predictions = model.predict(X_test_vectors)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2%}")


new_messages = [
    "I won a prize at school competition",
    "Congratulations! You've won a free prize, claim now!"
]

new_vectors = vectorizer.transform(new_messages)
new_predictions = model.predict(new_vectors)

for message, prediction in zip(new_messages, new_predictions):
    print(f"{prediction}: {message}")