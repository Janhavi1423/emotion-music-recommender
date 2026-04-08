import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("models/face_emotion_model.h5")

# Emotion labels (7 classes)
labels = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

# Load face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_face_emotion(frame):
    try:
        # Convert image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0:
            return "neutral"

        for (x, y, w, h) in faces:
            # Extract face region
            face = gray[y:y+h, x:x+w]

            # Resize to model input size
            face = cv2.resize(face, (48,48))

            # 🔥 FIX: Convert grayscale → RGB (3 channels)
            face = cv2.cvtColor(face, cv2.COLOR_GRAY2RGB)

            # Normalize
            face = face / 255.0

            # Reshape for model
            face = np.reshape(face, (1,48,48,3))

            # Predict emotion
            pred = model.predict(face)

            emotion = labels[np.argmax(pred)]

            return emotion

        return "neutral"

    except Exception as e:
        print("Face Detection Error:", str(e))
        return "neutral"