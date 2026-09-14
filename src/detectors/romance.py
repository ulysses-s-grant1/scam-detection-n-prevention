import re


def detect_romance_manipulation(message):
    lower_message = message.lower()
    relationship_signal = re.search(
        r"\b(soulmate|love of my life|never felt this way|deeply in love|only one for me)\b",
        lower_message,
    )
    financial_signal = re.search(
        r"\b(send|wire|borrow|loan|transfer)\b.{0,80}\b(money|cash|\$\d+|account|crypto|rent|hospital|ticket)\b",
        lower_message,
    )
    return ["romantic pressure + financial request"] if relationship_signal and financial_signal else []