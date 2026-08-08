from detectors.urgency import detect_urgency
from detectors.reward import detect_reward

def analyze_message(message):
    results = {}
    results["urgency"] = detect_urgency(message)
    results["reward"] = detect_reward(message)
    return results

if __name__ == "__main__":
    test_message = "Congratulations! You've won a free prize, but act now, offer expires in 24 hours!"
    print(analyze_message(test_message))