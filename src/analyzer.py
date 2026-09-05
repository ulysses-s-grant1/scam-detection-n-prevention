import joblib
from pathlib import Path
from detectors.urgency import detect_urgency
from detectors.reward import detect_reward

BASE_DIR = Path(__file__).resolve().parent.parent
model = joblib.load(BASE_DIR / "models" / "spam_classifier.joblib")
vectorizer = joblib.load(BASE_DIR / "models" / "vectorizer.joblib")


def analyze_message(message):
    signals = {
        "urgency": detect_urgency(message),
        "reward": detect_reward(message),
    }

    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)[0]
    probabilities = model.predict_proba(message_vector)[0]
    confidence = max(probabilities)

    ml_result = {
        "prediction": prediction,
        "confidence": confidence
    }

    return {"signals": signals, "ml": ml_result}


if __name__ == "__main__":
    test_message = "Congratulations! You've won a free prize, but act now, offer expires in 24 hours!"
    result = analyze_message(test_message)
    print(result)