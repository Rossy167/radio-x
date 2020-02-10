import csv
import the_html_bit
import the_spotify_section

# QD solution for details, probably store as environment variables later
with open('details.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for line in readCSV:
        authentication = {
            "cid": line[0].strip(),
            "secret": line[1].strip(),
            "username": line[2].strip()
        }

# songs are listed at this url
url = "https://www.radiox.co.uk/radio/last-played-songs/"

# get the html and then get the songs from the html
html = the_html_bit.get_html(url)
songs = the_html_bit.read_songs(html)

# authenticate with spotify, lookup the songs then add them to a matching playlist (if doesn't exist then create one)
session = the_spotify_section.simple_authenticate(authentication["cid"],
                                                  authentication["secret"], authentication["username"])
tracks = the_spotify_section.find_tracks_in_spotify(songs, session[0])
playlist = the_spotify_section.get_playlist(session[0], authentication["username"])
the_spotify_section.add_to_playlist(tracks, session[0], authentication["username"], playlist)
