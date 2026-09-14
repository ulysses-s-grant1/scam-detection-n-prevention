import re


credential_phrases = [
    "verify your identity",
    "verify identity",
    "verify your account",
    "verify account",
    "log in",
    "login",
    "password",
    "security code",
    "one-time code",
    "one time code",
    "otp",
    "update payment information",
]


def detect_credentials(message):
    lower_message = message.lower()
    return [
        phrase
        for phrase in credential_phrases
        if re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", lower_message)
    ]