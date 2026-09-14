from detectors.credentials import detect_credentials


def test_detects_identity_verification_request():
    result = detect_credentials("Verify your identity immediately using this link.")
    assert "verify your identity" in result


def test_detects_security_code_request():
    result = detect_credentials("Please send me the security code you received.")
    assert "security code" in result