import requests
import spotipy
import spotipy.util as util
from bs4 import BeautifulSoup
import pprint

website = "https://www.radiox.co.uk/radio/last-played-songs/"
page = requests.get(website)
soup = BeautifulSoup(page.content, "html.parser")
tracks = []
artists = []

for a in soup.find_all("div", id=lambda x: x and x.startswith('song_promo_')):
    try:
        track = a.find('span', attrs={'class': 'track'})
        artist = a.find('span', attrs={'class': 'artist'})
        track = track.contents[0].strip()
        artist = artist.contents[0].strip()
        if artist == '':
            artist = a.find('a', attrs={'class': 'first'})
            artist = artist.contents[0].strip()
        tracks.append(track)
        artists.append(artist)
    except:
        isTrue = True

artist = None

for a in soup.find_all("div", id=lambda x: x and x.startswith('song_promo_')):
    try:
        artist = a.find('a', attrs={'class': 'first'})
        artist = artist.contents[0].strip()
        track = a.find('a', attrs={'class': 'track'})
        track = track.contents[0].strip()
        if artist != '':
            if track != '':
                tracks.append(track)
                artists.append(artist)
    except:
        isTrue = True

artist = None
track = None
# we now have artists and tracks, which are the songs to add

# for track in tracks:
    # print(track)

#for artist in artists:
    # print(artist)

f = open("details.txt", "r")
cid = (f.readline())
secret = (f.readline())
username = f.readline()
f.close()
scope = 'playlist-modify-private'
url = 'https://localhost:8888/callback'

token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret,
                                   redirect_uri='https://www.google.com/')

sp = spotipy.Spotify(token)

track_ids = []

for i in range(len(tracks)):
    track = None
    track = sp.search(q='artist:' + artists[i] + ' track:' + tracks[i], type='track', limit=1)
    track_ids.append(track['tracks']['items'])

spotify_tracks = []

for track in track_ids:
    try:
        spotify_tracks.append(track[0]['uri'])
    except:
        isTrue = True



# ids = [track_ids[0][0]['uri'], track_ids[1][0]['uri']]

# for track in tracks:
#     print()

playlist = sp.user_playlist_create(username, "Radio X", public=False)

playlist = playlist['id']

sp.user_playlist_add_tracks(username, playlist_id=playlist, tracks=spotify_tracks)

# credentials = oauth2.SpotifyClientCredentials(
#       client_id=CLIENT_ID,
#        client_secret=CLIENT_SECRET)
# oauth2.SpotifyClientCredentials(s)
#
# token = credentials.get_access_token()
# spotify = spotipy.Spotify(auth=token)
# track = "coldplay yellow"
# res = spotify.search(track, type="track", limit=1)
# print(res)
