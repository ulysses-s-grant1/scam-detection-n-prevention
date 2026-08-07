reward_phrases = ['Winner', 'Selected', 'Exclusive', 'Guaranteed returns', 'Risk-free', 'won', 'free', 'prize', 'claim', 'earn']

def detect_reward(message):
    matches = []
    lower_message = message.lower()          
    for reward_phrase in reward_phrases:
        lower_phrase = reward_phrase.lower()      
        if lower_phrase in lower_message:                    
            matches.append(reward_phrase)          
    return matches

if __name__ == "__main__":
    scam_test = "Congratulations! You've won a free prize, claim now!"
    normal_test = "Hey, are we still on for lunch tomorrow?"
    
    print(detect_reward(scam_test))
    print(detect_reward(normal_test))