import React, { useRef } from "react";
import API from "../api/client";

function FaceDetector({ setSongs, setEmotion }) {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  // Start webcam
  const startCamera = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoRef.current.srcObject = stream;
  };

  // Capture image
  const capture = async () => {
    const canvas = canvasRef.current;
    const video = videoRef.current;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0);

    const image = canvas.toDataURL("image/jpeg");

    const res = await API.post("/face-emotion", { image });

    setEmotion(res.data.emotion);
    setSongs(res.data.songs);
  };

  return (
    <div>
      <h2>Face Emotion Detection 🎥</h2>

      <video ref={videoRef} autoPlay width="300"></video>
      <br />

      <button className="btn" onClick={startCamera}>
        Start Camera
      </button>

      <button className="btn" onClick={capture}>
        Detect Emotion
      </button>

      <canvas ref={canvasRef} style={{ display: "none" }}></canvas>
    </div>
  );
}

export default FaceDetector;