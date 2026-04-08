def recommend_music(emotion):
    music_db = {
        "happy": [
            {
                "name": "Happy",
                "artist": "Pharrell Williams",
                "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
                "url": "https://open.spotify.com",
                "image": "https://upload.wikimedia.org/wikipedia/en/3/3e/Pharrell_Williams_-_Happy.jpg"
            },
            {
                "name": "On Top of the World",
                "artist": "Imagine Dragons",
                "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                "url": "https://open.spotify.com",
                "image": "https://upload.wikimedia.org/wikipedia/en/7/7a/Imagine_Dragons_On_Top_of_the_World.jpg"
            }
        ],

        "sad": [
            {
                "name": "Someone Like You",
                "artist": "Adele",
                "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                "url": "https://open.spotify.com",
                "image": "https://upload.wikimedia.org/wikipedia/en/1/1b/Adele_-_Someone_Like_You.png"
            }
        ],

        "angry": [
            {
                "name": "Believer",
                "artist": "Imagine Dragons",
                "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
                "url": "https://open.spotify.com",
                "image": "https://upload.wikimedia.org/wikipedia/en/5/5c/Imagine_Dragons_Believer.jpg"
            }
        ],

        "neutral": [
            {
                "name": "Perfect",
                "artist": "Ed Sheeran",
                "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
                "url": "https://open.spotify.com",
                "image": "https://upload.wikimedia.org/wikipedia/en/8/8f/Ed_Sheeran_Perfect_Single_cover.jpg"
            }
        ]
    }

    return music_db.get(emotion, [])