import re


def detect_suspicious_contact(message):
    lower_message = message.lower()
    wrong_number = re.search(r"\b(wrong number|wrong person|sorry to bother)\b", lower_message)
    unsolicited_offer = any(
        phrase in lower_message
        for phrase in ("guaranteed returns", "investment opportunity", "make money", "crypto platform")
    )
    return ["unsolicited contact + valuable offer"] if wrong_number and unsolicited_offer else []