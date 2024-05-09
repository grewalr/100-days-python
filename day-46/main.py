import requests
import spotipy
from settings import *
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from bs4 import BeautifulSoup

# spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))

authentication_manager = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID, 
        client_secret=SPOTIPY_CLIENT_SECRET, 
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private",
        cache_path="./.cache"
)

spotify = spotipy.Spotify(auth_manager=authentication_manager)
URL = "https://www.billboard.com/charts/hot-100"

# year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = "2000-01-01"

# artist = spotify.search(q="artist:Tom Grennan", type="artist")

# print(artist)

response = requests.get(url=f"{URL}/{year}")
response.raise_for_status()
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# print(song_names)



