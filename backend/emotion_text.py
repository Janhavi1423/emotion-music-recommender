def detect_text_emotion(text):
    text = text.lower()

    if any(word in text for word in ["happy", "joy", "great", "awesome"]):
        return "happy"

    elif any(word in text for word in ["sad", "cry", "depressed", "upset"]):
        return "sad"

    elif any(word in text for word in ["angry", "mad", "furious"]):
        return "angry"

    else:
        return "neutral"