urgency_phrases = ['Immediately', 'ASAP', 'As Soon As Possible', '24 hours', 'Final notice', 'Act now', 'Expires', 'Verify identity',
'Suspended', 'Compromised', 'Locked', 'Suspicious activity', 'Arrest', 'Warrant', 'IRS', 
'Federal', 'Police', 'Security team', 'Fraud department']

def detect_urgency(message):
    matches = []
    lower_message = message.lower()          
    for urgency_phrase in urgency_phrases:
        lower_phrase = urgency_phrase.lower()      
        if lower_phrase in lower_message:                    
            matches.append(urgency_phrase)          
    return matches

if __name__ == "__main__":
    test_message = "Lunch tomorrrow."
    result = detect_urgency(test_message)
    print(result)