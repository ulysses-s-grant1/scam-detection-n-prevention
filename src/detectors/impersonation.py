import re


identity_phrases = [
    "this is your boss",
    "this is your manager",
    "i am your boss",
    "i am your manager",
    "your ceo",
    "your bank",
    "the irs",
    "the police",
]


def detect_impersonation(message):
    lower_message = message.lower()
    has_identity = any(
        re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", lower_message)
        for phrase in identity_phrases
    )
    has_urgent_request = any(
        phrase in lower_message
        for phrase in ("right now", "immediately", "asap", "act now", "send me")
    )
    return ["claimed identity + urgent request"] if has_identity and has_urgent_request else []