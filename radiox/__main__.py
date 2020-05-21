try:
    import csv
    import sys
    import the_html_bit
    import the_spotify_section
except ImportError:
    print('')
    print('Cannot import the modules required for Radio X')
    print('Did you run the setup script?')
    print('If so... did you activate the venv before running')
    print('You can run from start.sh or start.ps1 or you can activate the venv at __projectdir__/radiox/radiox_environment')
    print('')
    quit()

def radiox(url):

    # use environment variables later?
    # defo need to change the .json at least
    with open('radiox/resources/keys.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for line in readCSV:
            authentication = {
                "cid": line[0].strip(),
                "secret": line[1].strip(),
                "username": line[2].strip()
            }

    # get the html and then get the songs from the html
    html = the_html_bit.get_html(url)
    songs = the_html_bit.read_songs(html)

    # authenticate with spotify, lookup the songs then add them to a matching playlist (if doesn't exist then create one)
    session = the_spotify_section.simple_authenticate(authentication["cid"],
                                                    authentication["secret"], authentication["username"])
    tracks = the_spotify_section.find_tracks_in_spotify(songs, session[0])
    playlist = the_spotify_section.get_playlist(session[0], authentication["username"])
    the_spotify_section.add_to_playlist(tracks, session[0], authentication["username"], playlist)


if __name__ == "__main__":
    url = "https://www.radiox.co.uk/radio/last-played-songs/"
    radiox(url)
