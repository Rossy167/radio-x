# Radio X Playlist Generator

Generates Spotify playlist from Last Played Songs on Radio X 

### Where I am at:

This portion of the project is done, and I am working on getting a few things sorted i.e logging older playlists for posterity. I am planning on rewriting this project in JavaScript, but have a few other things going on right now. I was hoping to find a way to get this working in the terminal on a raspberry pi, but it seems spotify will not allow authentication without a web browser. Therefore, I am running it on a GUI version of Raspian, but this isn't ideal.

### Before You Start

The environment uses the Spotipy, Requests and BeautifulSoup4 libraries. It uses authentication by getting your tokens from a .csv with the order client ID, secret ID, username. Alternatively, you can entire the details as args with the order client ID, secret ID, username. 

### Installation

To download the code:

```git clone https://github.com/rossy167/radiox```

Traverse into your newly downloaded code repo:

```cd radiox```

Install the requirements with:

```pipenv install --ignore-pipfile```

### Explanation

Currently this code is intended to be ran on the backend, Spotify's API is not ideal for this, but I am using it as a regularly scheduled script on a Raspberry Pi. I am intending on rewriting some of the code in JavaScript and potentially putting it in a web environment.
