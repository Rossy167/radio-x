import requests
import spotify
from bs4 import BeautifulSoup

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

print(tracks)
print(artists)

# so how the fuck do i read this...
# i guess slice before the point where the list starts, then slice when it ends
# then to json
# then make the json just names and bands
# then pass into spotify api

# skip <div class="details"> and then find the next one
# after <div class="details"> no2 we'll find <div id="song_promo_x"
# in the content of that we'll find track and artist
# go until we stop finding things with id beginning with song_promo
