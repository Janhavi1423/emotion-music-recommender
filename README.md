# 🎧 Emotion-Based Music Recommendation System

##  Project Overview

This project is an AI-powered web application that detects user emotions (via text or face) and recommends music accordingly.

It combines:

* 🧠 Machine Learning (Emotion Detection)
* 🎥 Computer Vision (Face Detection)
* 🌐 Full Stack Development (React + Flask)
* 🎵 Music Recommendation System

---

## 🚀 Features

✔️ Detect emotion from text
✔️ Detect emotion from face (webcam)
✔️ Recommend songs based on emotion
✔️ Play song preview 🎵
✔️ Open full song in Spotify 🎧
✔️ Beautiful modern UI

---

## 🧠 Technologies Used

### Frontend:

* React.js
* CSS (Glassmorphism UI)

### Backend:

* Flask (Python)
* REST API

### AI / ML:

* TensorFlow / Keras
* OpenCV
* FER-2013 Dataset

---

## 🎯 How It Works

1. User enters text OR uses webcam
2. Emotion is detected
3. Backend processes emotion
4. Songs are recommended
5. User can:

   * Play preview
   * Open in Spotify

---

## 📂 Project Structure

emotion-music-recommender/
│
├── backend/
│   ├── app.py
│   ├── emotion_text.py
│   ├── emotion_face.py
│   ├── recommender.py
│   ├── models/
│   │   └── face_emotion_model.h5
│
├── frontend/
│   ├── src/
│   ├── components/
│
└── README.md

---

## ⚙️ Setup Instructions

### 🔹 Backend

cd backend
pip install -r requirements.txt
python app.py

---

### 🔹 Frontend

cd frontend
npm install
npm start

---

## 📊 Dataset Used

* FER-2013 (Facial Emotion Dataset)

---

## 🎥 Demo

(Add screenshots or screen recording here)

---

## 🧠 Future Improvements

* Real Spotify API integration
* Playlist creation
* User login system
* Mood history tracking

---

## 🙌 Conclusion

This project demonstrates how AI and web development can be combined to create an intelligent and interactive user experience.

---

## ⭐ Author

Janhavi Jagtap
