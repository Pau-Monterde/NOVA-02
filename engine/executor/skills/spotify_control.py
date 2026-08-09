from engine.models.context_model import RequestContext
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "2a0f53c3646f48e280e5d333c679135c"
CLIENT_SECRET = "f9142db935904257b9aef660cf16f0ec"
REDIRECT_URI = "http://127.0.0.1:8888/callback"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-modify-playback-state user-read-playback-state"
    )
)

def spotify_control(context:RequestContext):
    devices = sp.devices()

    try: 
        sp.start_playback()

    except Exception as e:
        return "No se ha podido ejecutar spotify en el dispositivo"

def play(context:RequestContext):
    sp.start_playback()

def pause(context:RequestContext):
    sp.pause_playback()

def next_track(context:RequestContext):
    sp.next_track()

def prev_track(context:RequestContext):
    sp.previous_track()
