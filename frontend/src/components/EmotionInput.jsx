import React, { useState } from "react";
import API from "../api/client";

function EmotionInput({ setSongs, setEmotion }) {
  const [text, setText] = useState("");

  const handleSubmit = async () => {
    const res = await API.post("/text-emotion", { text });
    setSongs(res.data.songs);
    setEmotion(res.data.emotion);
  };

  return (
    <div>
      <input
        className="input-box"
        placeholder="Type your feeling..."
        onChange={(e) => setText(e.target.value)}
      />

      <button className="btn" onClick={handleSubmit}>
        Get Songs 🎵
      </button>
    </div>
  );
}

export default EmotionInput;