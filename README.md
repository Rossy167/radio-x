# Radio X Playlist Generator

Generates Spotify playlist from Last Played Songs on Radio X 

## Where I am at:

I am currently rewriting this project in JavaScript. I was hoping to find a way to get this working in the terminal on a raspberry pi, but it seems spotify will not allow authentication without a web browser.

### Before You Start

The environment that you're running in it is going to need the Spotipy, Requests and BeautifulSoup4 libraries. It uses authentication by getting your tokens from a .csv with the order client ID, secret ID, username. Alternatively, you can entire the details as args with the order client ID, secret ID, username. 


#### Explanation

Currently this code is intended to be ran on the backend, Spotify's API is not ideal for this, but I am using it as a regularly scheduled script on a Raspberry Pi. I am intending on rewriting some of the code in JavaScript and potentially putting it in a web environment.