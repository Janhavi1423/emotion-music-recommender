def get_songs_by_emotion(emotion):
    query_map = {
        "happy": "happy songs",
        "sad": "sad songs",
        "angry": "workout songs",
        "neutral": "chill songs"
    }

    query = query_map.get(emotion, "top songs")

    results = sp.search(q=query, type="track", limit=10)

    songs = []
    for item in results["tracks"]["items"]:
        songs.append({
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "url": item["external_urls"]["spotify"],
            "preview": item["preview_url"],
            "image": item["album"]["images"][0]["url"]
        })

    return songs