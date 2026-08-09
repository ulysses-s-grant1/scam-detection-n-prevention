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
    
if __name__ == "__main__":
    from analyzer import analyze_message
    
    test_message = "Congratulations! You've won a free prize, but act now, offer expires in 24 hours!"
    results = analyze_message(test_message)
    print(explain_results(results))