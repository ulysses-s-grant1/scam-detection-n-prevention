import re


payment_phrases = [
    "gift card",
    "gift cards",
    "wire transfer",
    "western union",
    "cash app",
    "venmo",
    "zelle",
    "bitcoin",
    "cryptocurrency",
    "crypto",
    "send money",
]


def detect_payment(message):
    lower_message = message.lower()
    return [
        phrase
        for phrase in payment_phrases
        if re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", lower_message)
    ]