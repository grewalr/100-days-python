import requests
import spotipy
from settings import *
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from pprint import pprint


authentication_manager = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private",
        cache_path="./.cache"
)

spotify = spotipy.Spotify(auth_manager=authentication_manager)
URL = "https://www.billboard.com/charts/hot-100"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "2000-01-01"

response = requests.get(url=f"{URL}/{date}")
response.raise_for_status()
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = spotify.user_playlist_create(
        user=SPOTIFY_USERNAME,
        name=f"{date} Billboard 100",
        public=False,
        description=f"Top 100 songs on the date {date}"
)

playlist_id = playlist["uri"]

# spotify.user_playlist_add_tracks(user=SPOTIFY_USERNAME,
#                                  playlist_id=playlist_id, 
#                                  tracks=song_uris)

spotify.playlist_add_items(playlist_id=playlist_id, items=song_uris)