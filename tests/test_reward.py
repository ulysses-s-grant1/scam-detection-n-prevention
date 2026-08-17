from detectors.reward import detect_reward

def test_detects_reward():
    result = detect_reward("Congratulations! You've won a Free prize, claim now!")
    assert "free" in result

def test_no_match_on_normal_message():
    result = detect_reward("Hey, are we still on for lunch tomorrow?")
    assert not result

def test_detects_reward_regardless_of_casing():
    result = detect_reward("Congratulations! You've WON a FREE prize, claim now!")
    assert "free" in result