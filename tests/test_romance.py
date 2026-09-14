from detectors.romance import detect_romance_manipulation


def test_detects_romantic_financial_pressure():
    result = detect_romance_manipulation(
        "You are my soulmate, but I need you to wire money for my hospital bill."
    )
    assert result


def test_does_not_flag_normal_affection():
    assert not detect_romance_manipulation("You are my soulmate and I cannot wait to see you.")