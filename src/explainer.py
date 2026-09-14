def explain_results(results):
    explanation_parts = []

    for signal_name, matches in results["signals"].items():
        if matches:
            matches_text = ", ".join(matches)

            if signal_name == "urgency":
                line = f"""⚠️ Urgency Warning: We noticed phrases like "{matches_text}." Scammers love to use artificial time limits to make you panic so you'll hand over personal info without thinking. Take a deep breath, slow down, and verify who sent this before you click anything!"""
            elif signal_name == "reward":
                line = f"""⚠️ Reward Alert: We noticed phrases like "{matches_text}." Scammers often promise unrealistic rewards to lure you in. Remember, if it sounds too good to be true, it probably is!"""
            elif signal_name == "payment":
                line = f"""⚠️ Payment Warning: We noticed payment-related language like "{matches_text}." Do not send money, gift cards, or cryptocurrency until you verify the request through a trusted, independent channel."""
            elif signal_name == "credentials":
                line = f"""⚠️ Account Security Warning: We noticed a request for account information like "{matches_text}." Do not click links or share passwords and security codes; open the official app or website yourself instead."""
            elif signal_name == "urls":
                line = f"""⚠️ Link Warning: We noticed a potentially suspicious link ({matches_text}). Do not open it; visit the organization's official website using a trusted bookmark or manually typed address."""
            elif signal_name == "impersonation":
                line = f"""⚠️ Impersonation Warning: This message combines a claimed identity with pressure to act quickly. Verify the sender using a known contact method before taking any action."""
            elif signal_name == "contact":
                line = f"""⚠️ Unsolicited Contact Warning: This message combines an unexpected contact with a valuable offer. Do not share money or personal information with someone you have not independently verified."""
            elif signal_name == "romance":
                line = f"""⚠️ Relationship Scam Warning: This message combines intense romantic language with a financial request. Do not send money or account information to someone you have not met and independently verified."""

            explanation_parts.append(line)

    ml_result = results["ml"]
    if ml_result["prediction"] == "spam":
        explanation_parts.append(
            f"🤖 Machine Learning Model: Our trained model also flags this message as likely spam, "
            f"with {ml_result['confidence']:.2%} confidence, based on patterns learned from real scam and legitimate messages."
        )

    if not explanation_parts:
        return "No obvious scam signals found, but stay cautious — scammers constantly adapt."
    else:
        return "\n\n".join(explanation_parts)

def calculate_risk_level(results):
    signal_weights = {
        "urgency": 1,
        "reward": 1,
        "payment": 2,
        "credentials": 2,
        "urls": 2,
        "impersonation": 2,
        "contact": 2,
        "romance": 2,
    }
    detected_signals = [
        signal_name
        for signal_name, matches in results["signals"].items()
        if matches
    ]
    signal_count = len(detected_signals)
    risk_score = sum(signal_weights.get(signal_name, 1) for signal_name in detected_signals)

    ml_result = results.get("ml", {})
    if ml_result.get("prediction") == "spam" and ml_result.get("confidence", 0) >= 0.8:
        risk_score += 1

    if risk_score == 0:
        level = "None"
    elif risk_score == 1:
        level = "Low"
    elif risk_score <= 3:
        level = "Medium"
    else:
        level = "High"
    
    return {"level": level, "signal_count": signal_count, "risk_score": risk_score}

if __name__ == "__main__":
    from analyzer import analyze_message

    messages_to_test = [
        "Congratulations! You've won a free prize, but act now, offer expires in 24 hours!",
        "I won a prize at school competition"
    ]

    for msg in messages_to_test:
        results = analyze_message(msg)
        risk = calculate_risk_level(results)
        print(risk)
        print(explain_results(results))
        print("---")