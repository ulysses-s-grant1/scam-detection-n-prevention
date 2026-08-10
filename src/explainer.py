def explain_results(results):
    explanation_parts = []
    
    for signal_name, matches in results.items():
        if matches:
            matches_text = ", ".join(matches)
            
            if signal_name == "urgency":
                line = f"""⚠️ Urgency Warning: We noticed phrases like "{matches_text}." Scammers love to use artificial time limits to make you panic so you'll hand over personal info without thinking. Take a deep breath, slow down, and verify who sent this before you click anything!"""
            elif signal_name == "reward":
                line = f"""⚠️ Reward Alert: We noticed phrases like "{matches_text}." Scammers often promise unrealistic rewards to lure you in. Remember, if it sounds too good to be true, it probably is!"""

            explanation_parts.append(line)
    
    if not explanation_parts:
        return "No obvious scam signals found, but stay cautious — scammers constantly adapt."
    else:
        return "\n\n".join(explanation_parts)

def calculate_risk_level(results):
    signal_count = 0
    
    for signal_name, matches in results.items():
        if matches:
            signal_count += 1
    
    if signal_count == 0:
        level = "None"
    elif signal_count == 1:
        level = "Low"
    elif signal_count == 2:
        level = "Medium"
    else:
        level = "High"
    
    return {"level": level, "signal_count": signal_count}

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