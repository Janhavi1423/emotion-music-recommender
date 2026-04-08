from flask import Flask, request, jsonify
from flask_cors import CORS
from emotion_text import detect_text_emotion
from recommender import recommend_music
import base64
import cv2
import numpy as np
from emotion_face import detect_face_emotion

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/text-emotion", methods=["POST"])
def text_emotion():
    data = request.get_json()
    text = data.get("text", "")

    emotion = detect_text_emotion(text)
    songs = recommend_music(emotion)

    return jsonify({
        "emotion": emotion,
        "songs": songs
    })
@app.route("/face-emotion", methods=["POST"])
def face_emotion():
    try:
        print("API HIT")

        data = request.get_json()
        image_data = data["image"]

        image_data = image_data.split(",")[1]
        img_bytes = base64.b64decode(image_data)

        np_arr = np.frombuffer(img_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        print("Before prediction")

        emotion = detect_face_emotion(frame)

        from recommender import recommend_music
        songs = recommend_music(emotion)

        return jsonify({
            "emotion": emotion,
            "songs": songs
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)