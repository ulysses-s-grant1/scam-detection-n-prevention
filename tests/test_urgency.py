from detectors.urgency import detect_urgency

def test_detects_suspended():
    result = detect_urgency("Your account has been suspended.")
    assert "Suspended" in result

def test_no_match_on_normal_message():
    result = detect_urgency("Hey, are we still on for lunch tomorrow?")
    assert not result