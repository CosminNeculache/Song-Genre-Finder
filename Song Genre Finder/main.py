import os
import requests
from dotenv import load_dotenv

load_dotenv()

LASTFM_KEY = os.getenv("LASTFM_API")
BASE_URL = "http://ws.audioscrobbler.com/2.0/"


def get_top_tracks(limit=51):
    method = "chart.gettoptracks"
    params = {
        "method": method,
        "api_key": LASTFM_KEY,
        "limit": limit,
        "format": "json"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "tracks" in data and "track" in data["tracks"]:
        tracks = data["tracks"]["track"]
        return tracks
    else:
        return []


def get_track_genres(artist_name, track_name):
    method = "track.getInfo"
    params = {
        "method": method,
        "api_key": LASTFM_KEY,
        "artist": artist_name,
        "track": track_name,
        "format": "json"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "track" in data and "toptags" in data["track"] and "tag" in data["track"]["toptags"]:
        genre_tags = data["track"]["toptags"]["tag"]
        genres = [tag["name"] for tag in genre_tags]
        return genres
    else:
        return []


top_tracks = get_top_tracks()

if top_tracks:
    print("Today's Top 50 Tracks:")
    for index, track in enumerate(top_tracks, start=1):
        artist_name = track["artist"]["name"]
        track_name = track["name"]
        genres = get_track_genres(artist_name, track_name)

        if genres:
            genre_str = ", ".join(genres)
            print(f"{index}. {track_name} by {artist_name} (Genres: {genre_str})")
        else:
            print(f"{index}. {track_name} by {artist_name} (Genres not available)")
else:
    print("Top tracks not found.")