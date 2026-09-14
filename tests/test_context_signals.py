from detectors.contact import detect_suspicious_contact
from detectors.impersonation import detect_impersonation


def test_detects_impersonation_and_urgency():
    assert detect_impersonation("I am your manager, send me the report right now.")


def test_detects_unsolicited_valuable_offer():
    assert detect_suspicious_contact(
        "Sorry, wrong number, but I can show you a guaranteed returns investment opportunity."
    )