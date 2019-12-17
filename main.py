import the_html_bit
import the_spotify_section

# temporary measure for authentication, putting tokens in .txt
f = open("details.txt", "r")
cid = f.readline().strip()
secret = f.readline().strip()
username = f.readline().strip()
f.close()

# songs are listed at this url
url = "https://www.radiox.co.uk/radio/last-played-songs/"

# get the html and then get the songs from the html
html = the_html_bit.get_html(url)
songs = the_html_bit.read_songs(html)

# authenticate with spotify, lookup the songs then add them to a matching playlist (if doesn't exist then create one)
session = the_spotify_section.simple_authenticate(cid, secret, username)
tracks = the_spotify_section.find_tracks_in_spotify(songs, session[0])
playlist = the_spotify_section.get_playlist(session[0], username)
the_spotify_section.add_to_playlist(tracks, session[0], username, playlist)
