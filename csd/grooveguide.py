from flask import Flask, render_template, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

grooveguide = Flask(__name__)


SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))

mood_playlists = {
    "happy": "https://open.spotify.com/playlist/37i9dQZF1EVJSvZp5AOML2",
    "sad": "https://open.spotify.com/playlist/37i9dQZF1DWSqBruwoIXkA",
    "angry": "https://open.spotify.com/playlist/37i9dQZF1EIgNZCaOGb0Mi",
    "relaxed": "https://open.spotify.com/playlist/75nyJIOPfJEAzQIG8XMDFM",
    "soft": "https://open.spotify.com/playlist/37i9dQZF1EIcNUtFW3CJZc?si=61970b0aec444a4f",
    "romance": "https://open.spotify.com/playlist/37i9dQZF1EIh7dFzbJpr7C?si=34bacda71f7f4d03",
    "workout": "https://open.spotify.com/playlist/37i9dQZF1EIdHZWT31d1QN?si=5f8e2cd355d14566",
    "emotional": "https://open.spotify.com/playlist/37i9dQZF1EIerV7MkE62Mz?si=94ee1096d01946fc",
    "rainy":  "https://open.spotify.com/playlist/37i9dQZF1EIfilQIuOCwD7?si=706ba3f9431f4622",
    "nostalgia": "https://open.spotify.com/playlist/37i9dQZF1EIhj2zUFUJqG1?si=8ac8bbdf545740cf",
    "driving": "https://open.spotify.com/playlist/37i9dQZF1EIeEGqN5vooFV?si=afa37ddb907744ba",
    "breakup": "https://open.spotify.com/playlist/37i9dQZF1EIhrKu07W6FWB?si=f8427ea25c684aa4",
    "shower": "https://open.spotify.com/playlist/37i9dQZF1EIfkE4mG1NtgG?si=5b922427c7c14f91",
    "crying": "https://open.spotify.com/playlist/37i9dQZF1EIctw4dMbBUt1?si=f807542221e6457b",
    "bollywood": "https://open.spotify.com/playlist/37i9dQZF1EIcMWU5aFysN5?si=c1776d47100e4f50",
    "dance": "https://open.spotify.com/playlist/37i9dQZF1EIdt7tQbR8QDN?si=c62c14b206a54f9f",
    "party": "https://open.spotify.com/playlist/37i9dQZF1EIdzRg9sDFEY3?si=9570f82351b440dd",
    "lonely": "https://open.spotify.com/playlist/37i9dQZF1EIhrfJdOCmxe4?si=68f83149f499436c",
    "rage": "https://open.spotify.com/playlist/37i9dQZF1EIhuCNl2WSFYd?si=afdca81fc2294da2",
    "fun": "https://open.spotify.com/playlist/37i9dQZF1EIhNeYdg47zFW?si=1a965cd4db5a4cf8",
}

@grooveguide.route("/", methods=["GET", "POST"])
def index():
    song = None

    if request.method == "POST":
        user_input = request.form["user_input"].lower()
        if user_input in mood_playlists:
            mood = user_input

            return redirect(f"/mood/{mood}")

    return render_template("index.html", song=song)

@grooveguide.route("/mood/<mood>", methods=["GET"])
def redirect_to_spotify(mood):
    playlist_url = mood_playlists.get(mood)

    if playlist_url:
        return redirect(playlist_url)
    else:
        return "Playlist not found"

if __name__ == "__main__":
    grooveguide.run(debug=True)
