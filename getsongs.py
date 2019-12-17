import requests
import spotipy
import spotipy.util as util
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials

# get the url from the website
website = "https://www.radiox.co.uk/radio/last-played-songs/"
page = requests.get(website)
soup = BeautifulSoup(page.content, "html.parser")
tracks = []
artists = []

# get list of artists and tracks
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

# get the login details from .txt later will be proper auth
f = open("details.txt", "r")
cid = (f.readline())
secret = (f.readline())
username = f.readline()
f.close()
scope = 'playlist-modify-public'
url = 'https://www.google.com/'
cid = (cid.strip())
secret = (secret.strip())
username = (username.strip())

# authentication stuff
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret,
                                   redirect_uri=url)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

# search the artist and song names and get the IDs from it
track_ids = []
for i in range(len(tracks)):
    track = sp.search(q='artist:' + artists[i] + ' track:' + tracks[i], type='track', limit=1)
    track_ids.append(track['tracks']['items'])
spotify_tracks = []

for track in track_ids:
    try:
        spotify_tracks.append(track[0]['uri'])
    except:
        isTrue = True

# create a playlist titled radio x and add the list of songs to it
playlist = sp.user_playlist_create(username, "Radio X (code generated)", public=True)
playlist = playlist['id']
sp.user_playlist_add_tracks(username, playlist_id=playlist, tracks=spotify_tracks)
