from analyzer import analyze_message
from explainer import calculate_risk_level, explain_results

def main():
    print("Carespear — paste a message to check it for scam signals. Type 'quit' to exit.\n")

    while True:
        user_input = input("Message: ")

        if user_input == "quit":                                  
            print("Goodbye!")
            break

        results = analyze_message(user_input)                               
        risk = calculate_risk_level(results)                                    
        explanation = explain_results(results)                           

        print(f"\nRisk Level: {risk['level']} ({risk['signal_count']} signal(s) detected)")
        print(explanation)
        print()


if __name__ == "__main__":
    main()