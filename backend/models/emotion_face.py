import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("models/face_emotion_model.h5")

labels = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_face_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (48,48))
        face = face / 255.0
        face = np.reshape(face, (1,48,48,1))

        pred = model.predict(face)
        emotion = labels[np.argmax(pred)]

        return emotion

    return "neutral"