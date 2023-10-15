import spotipy
from spotipy import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="bf59f0ce78b14139b3492db629cb4bb6",
                                               client_secret='f39b5d6b702341bb963c9bd9ee84478e',
                                               redirect_uri='http://localhost:3000',
                                               scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])



