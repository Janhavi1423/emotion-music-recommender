import React, { useState, useEffect } from "react";

function MusicPlayer({ songs }) {
  const [current, setCurrent] = useState(null);

  useEffect(() => {
    if (songs.length > 0) {
      setCurrent(songs[0].preview);
    }
  }, [songs]);

  return (
    <div>
      <h2>Recommended Songs 🎵</h2>

      <div className="song-grid">
        {songs.map((song, index) => (
          <div
            key={index}
            className="song-card"
            onClick={() => setCurrent(song.preview)}
          >
            <img 
              src={song.image} 
              className="song-img" 
              alt="cover"
              onError={(e) => e.target.src = "https://via.placeholder.com/300"}
            />
            <h4>{song.name}</h4>
            <p>{song.artist}</p>

            <a href={song.url} target="_blank" rel="noreferrer">
              🎧 Play on Spotify
            </a>
          </div>
        ))}
      </div>

      {current && (
        <div>
          <h3>Now Playing 🎶</h3>
          <audio controls autoPlay src={current}></audio>
        </div>
      )}
    </div>
  );
}

export default MusicPlayer;