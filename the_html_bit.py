import requests
from bs4 import BeautifulSoup


def get_html(url):
    website = "https://www.radiox.co.uk/radio/last-played-songs/"
    page = requests.get(website)
    return BeautifulSoup(page.content, "html.parser")


def read_songs(html):
    tracks = []
    artists = []
    # get list of artists and tracks
    for a in html.find_all("div", id=lambda x: x and x.startswith('song_promo_')):
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
            print("my code is bad and i should feel bad")

    artist = None

    for a in html.find_all("div", id=lambda x: x and x.startswith('song_promo_')):
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
            print("my code is bad and i should feel bad")

    songs = [tracks, artists]
    return songs
