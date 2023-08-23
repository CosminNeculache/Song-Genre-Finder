import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("DEEZER_API")
BASE_URL = "https://api.deezer.com/"


def get_top_songs(limit=51):
    endpoint = "chart/0/tracks"
    params = {
        "limit": limit,
        "output": "json"
    }

    response = requests.get(BASE_URL + endpoint, params=params)
    data = response.json()
    if "data" in data:
        songs = data["data"]
        return songs
    else:
        return []


top_songs = get_top_songs()

if top_songs:
    print("Today's Top 50 Songs:")
    for index, song in enumerate(top_songs, start=1):
        print(f"{index}. {song['title']} by {song['artist']['name']}")
else:
    print("Top songs not found.")