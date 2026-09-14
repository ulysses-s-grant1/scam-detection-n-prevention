from detectors.urls import detect_suspicious_urls


def test_detects_shortened_url():
    result = detect_suspicious_urls("Click https://bit.ly/account-check")
    assert any("shortened URL" in match for match in result)


def test_ignores_ordinary_url():
    assert not detect_suspicious_urls("Read https://example.com/about")