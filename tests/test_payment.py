from detectors.payment import detect_payment


def test_detects_gift_card_request():
    result = detect_payment("Buy two gift cards and send me the codes.")
    assert "gift cards" in result


def test_does_not_match_partial_words():
    assert not detect_payment("The giftcard catalog is in the office.")