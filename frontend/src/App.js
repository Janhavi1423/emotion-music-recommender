import React, { useState } from "react";
import EmotionInput from "./components/EmotionInput";
import MusicPlayer from "./components/MusicPlayer";
import FaceDetector from "./components/FaceDetector";
import "./index.css";

function App() {
  const [songs, setSongs] = useState([]);
  const [emotion, setEmotion] = useState("");

  const emojiMap = {
    happy: "😊",
    sad: "😢",
    angry: "😡",
    neutral: "😐",
    surprise: "😲",
    fear: "😨",
    disgust: "🤢"
  };

  return (
    <div className="container">
      <h1 className="title">🎧 Emotion Music AI</h1>

      {/* TEXT INPUT */}
      <EmotionInput setSongs={setSongs} setEmotion={setEmotion} />

      <hr />

      {/* FACE INPUT (CAMERA) */}
      <FaceDetector setSongs={setSongs} setEmotion={setEmotion} />

      {emotion && (
        <h2>
          {emojiMap[emotion]} Feeling: {emotion}
        </h2>
      )}

      <MusicPlayer songs={songs} />
    </div>
  );
}

export default App;