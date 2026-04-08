import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# Sample dataset (you can replace with real dataset later)
data = {
    "text": [
        "I am very happy",
        "I feel sad",
        "I am angry",
        "I am excited",
        "I am depressed",
        "I feel great",
        "I am frustrated"
    ],
    "emotion": [
        "happy",
        "sad",
        "angry",
        "happy",
        "sad",
        "happy",
        "angry"
    ]
}

df = pd.DataFrame(data)

# Convert text → numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])

# Train model
model = MultinomialNB()
model.fit(X, df["emotion"])

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Save model
pickle.dump(model, open("models/text_emotion_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

print("Model trained and saved!")