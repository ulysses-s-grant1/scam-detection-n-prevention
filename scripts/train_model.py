import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/spam_clean.csv")

X = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

extra_examples = pd.DataFrame({
     "message": [
        "I won a prize at school competition",
        "She won first prize in the science fair",
        "Congrats on winning the prize at the game night",
        "Hi, is this the dog groomer on 5th street? I need to bring Bella in tomorrow morning. ...Wait, I think my assistant gave me the wrong number! I'm so sorry to bother you. I'm David, I own a clothing boutique downtown. You seem really polite, it's nice to meet you!",
        "Babe, I wish I could video call you tonight, but the signal here on the base is terrible and my commanding officer is incredibly strict about cameras. It's so lonely out here, reading your texts is the only thing keeping my spirits up. Can we just stick to messaging for now?",
        "I know we only matched on Tuesday, but I really feel like you're my soulmate. I've never connected with anyone like this. But I'm completely freaking out right now, my bank just froze my account while I'm traveling and the hotel is threatening to kick me out. Could you please wire me $150 just until tomorrow so I have a place to sleep?",
        "It's been so great getting to know you this week. You mentioned wanting to travel more, my uncle's cryptocurrency trading platform has been making me incredible returns lately and it's super easy to use. I could show you how to set up an account if you want? Just send me a screenshot of your current banking app so I can see what limits we're working with.",
        "Just left the arcade, we finally pooled enough tickets for that top shelf prize! Bringing the giant stuffed bear over to your place now lol",
        "Hey! They just pulled the raffle tickets at the neighborhood block party and you actually won the bakery basket. Text me when you're home so I can drop it off on your porch."
    ],
    "label": ["ham", "ham", "ham", "spam", "spam", "spam", "spam", "ham", "ham"]
})

# add reinforcement examples ONLY to training data, never to test data
X_train = pd.concat([X_train, extra_examples["message"]], ignore_index=True)
y_train = pd.concat([y_train, extra_examples["label"]], ignore_index=True)

X_train = pd.concat([X_train, extra_examples["message"]], ignore_index=True)
y_train = pd.concat([y_train, extra_examples["label"]], ignore_index=True)

vectorizer = CountVectorizer(ngram_range=(1, 2))
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)


vectorizer = CountVectorizer(ngram_range=(1, 2))
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)


model = MultinomialNB()
model.fit(X_train_vectors, y_train)

predictions = model.predict(X_test_vectors)
accuracy = accuracy_score(y_test, predictions)
from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(f"Accuracy: {accuracy:.2%}")


regression_tests = [
    ("I won a prize at school competition", "ham"),
    ("Congratulations! You've won a free prize, claim now!", "spam"),
    ("So sorry, I thought this was my assistant's number! Have a blessed day. 🌸 ...Wait, since I already bothered you, you seem nice—do you happen to live in the area? I'm trying to find a good sushi place for a client meeting.", "spam"),
    ("Hey it's me! I finally got my new phone sorted out so save this number. Btw, that trading group I mentioned last week is closing their intake tomorrow, did you still want me to send the invite link?", "spam")
]

print("\n--- Regression Checks ---")
for message, expected in regression_tests:
    vector = vectorizer.transform([message])
    predicted = model.predict(vector)[0]
    result = "✓ PASS" if predicted == expected else "✗ FAIL"
    print(f"{result} | expected: {expected}, got: {predicted} | {message}")

results_df = pd.DataFrame({
    "message": X_test,
    "actual": y_test,
    "predicted": predictions
})

missed_spam = results_df[(results_df["actual"] == "spam") & (results_df["predicted"] == "ham")]
print(missed_spam)