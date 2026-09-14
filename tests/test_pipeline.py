from analyzer import analyze_message
from explainer import calculate_risk_level, explain_results

def test_high_signal_message_is_medium_or_higher():
    result = analyze_message("Congratulations! You've won a free prize, but act now, offer expires in 24 hours!")
    risk = calculate_risk_level(result)
    assert risk['signal_count'] >= 2

def test_innocent_message_has_low_risk():
    result = analyze_message("I won a prize at school competition")
    risk = calculate_risk_level(result)
    assert risk['level'] == "Low"

def test_explain_results_returns_something_for_flagged_message():
    result = analyze_message("Your account has been suspended. Verify identity immediately.")
    explanation = explain_results(result)
    assert explanation is not None


def test_payment_request_is_medium_or_higher():
    result = analyze_message("Your manager needs gift cards. Buy them and send the codes now.")
    risk = calculate_risk_level(result)
    assert risk["level"] in {"Medium", "High"}
    assert "payment" in result["signals"]


def test_credential_request_is_medium_or_higher():
    result = analyze_message("Verify your identity and send the security code immediately.")
    risk = calculate_risk_level(result)
    assert risk["level"] in {"Medium", "High"}
    assert "credentials" in result["signals"]


def test_high_confidence_model_result_contributes_to_risk():
    result = {
        "signals": {"urgency": [], "reward": [], "payment": [], "credentials": []},
        "ml": {"prediction": "spam", "confidence": 0.95},
    }
    risk = calculate_risk_level(result)
    assert risk["level"] == "Low"
    assert risk["risk_score"] == 1


def test_suspicious_url_is_medium_or_higher():
    result = analyze_message("Verify your account at https://bit.ly/account-check immediately.")
    risk = calculate_risk_level(result)
    assert risk["level"] in {"Medium", "High"}
    assert result["signals"]["urls"]