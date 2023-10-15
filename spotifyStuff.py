import spotipy
import flask
from flask import *
import os
from spotipy import *
import Chatwithgpt
import json
import getSummary as gs

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="bf59f0ce78b14139b3492db629cb4bb6",
                                               client_secret="f39b5d6b702341bb963c9bd9ee84478e",
                                               redirect_uri='http://localhost:3000',
                                               scope=scope))


# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

        def getTitle():
            return title

        def getArtist():
            return artist


def createPlaylist(bookName):
    playlist = sp.user_playlist_create(user=sp.me()['id'], name=bookName, public=False,
                                       description=f"Auto generated playlist for {bookName}")
    playlist_ID = playlist['id']

    summary = gs.get_summary(bookName)
    print(summary)

    listOfSongs = []

    gpt_result = Chatwithgpt.chat_with_gpt(summary)
    print(gpt_result)
    data_gpt = json.loads(gpt_result)
    print(data_gpt)
    '''
    for title_artist in gpt_result:
        print(title_artist)
        listOfSongs.append(Song(title_artist["title"], title_artist["artist"]))
'''
    print(type(data_gpt))
    for title_artist in data_gpt["playlist"]:
        print(title_artist)
        listOfSongs.append(Song(title_artist["title"], title_artist["artist"]))
    print(listOfSongs)

    for song in listOfSongs:
        try:
            tArtString = "track:" + song.title  # + "%20artist:" + song.artist
            item = sp.search(q=tArtString, limit=1, type='track')
            print(item)
            print("abcdefgh")
            tracks = [item["tracks"]["items"][0]["uri"]]
            #tracks = ['spotify:track:2nMeu6UenVvwUktBCpLMK9']
            print(tracks)
            print("why isn't this working")
            sp.playlist_add_items(playlist_id=playlist_ID,
                                  items=tracks,
                                  position=0)
        except:
            print('Something went wrong')


createPlaylist("The Great Gatsby")
