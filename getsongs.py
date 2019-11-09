import requests
import spotify
from bs4 import BeautifulSoup

website = "https://www.radiox.co.uk/radio/last-played-songs/"
page = requests.get(website)
soup = BeautifulSoup(page.content, "html.parser")

# so how the fuck do i read this...
# i guess slice before the point where the list starts, then slice when it ends
# then to json
# then make the json just names and bands
# then pass into spotify api

# skip <div class="details"> and then find the next one
# after <div class="details"> no2 we'll find <div id="song_promo_x"
# in the content of that we'll find track and artist
# go until we stop finding things with id beginning with song_promo
