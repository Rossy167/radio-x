import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


def simple_authenticate(cid, secret, username):
    scope = 'playlist-modify-public'
    url = 'https://www.google.com/'

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret,
                                       redirect_uri=url)
    if token:
        sp = spotipy.Spotify(auth=token)
    else:
        print("Can't get token for", username)

    details = [sp, username]
    return details


def find_tracks_in_spotify(songs, sp):
    not_on_spotify = 0
    track_ids = []
    for i in range(len(songs[0])):
        track = sp.search(q='artist:' + songs[1][i] + ' track:' + songs[0][i], type='track', limit=1)
        track_ids.append(track['tracks']['items'])
    spotify_tracks = []

    for track in track_ids:
        try:
            spotify_tracks.append(track[0]['uri'])
        except:
            not_on_spotify += 1
    print("not on spotify: " + str(not_on_spotify))
    return spotify_tracks


def add_to_playlist(spotify_tracks, sp, username, playlist):
    sp.user_playlist_replace_tracks(username, playlist_id=playlist, tracks=spotify_tracks)
    print("tracks: " + str(len(spotify_tracks)))


def create_playlist(sp, username):
    new_playlist = sp.user_playlist_create(username, "Radio X (code generated)", public=True)
    new_playlist = new_playlist['id']
    print("created playlist with id: " + new_playlist)
    return new_playlist


def get_playlist(sp, username):
    playlists = sp.user_playlists(username)
    playlists = (playlists['items'])
    for playlist in playlists:
        if playlist['name'] == "Radio X (code generated)":
            print("found matching playlist with id: " + playlist['id'])
            return playlist['id']
    playlist = create_playlist(sp, username)
    return playlist

# details = simple_authenticate("my", "secret", "stuff")
# playlist = get_playlist(details[0], details[1])
