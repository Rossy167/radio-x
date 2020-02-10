# Radio X Playlist Generator

Generates Spotify playlist from Last Played Songs on Radio X 

## Before You Start

The environment that you're running in it is going to need the Spotipy, Requests and BeautifulSoup4 libraries. It uses authentication by getting your tokens from a .csv with the order client ID, secret ID, username. Probably best not mess with it at this phase, until I've got proper authentication going. But the core function works.

### Working On 

This project is going to have 2 implementations, both being quite different. One being a node.js application that uses the Implicit Grant auth flow, because it's very clean and easy for the user. The other will be a simple Python program that runs on a backend server on scheduled basis. The Python program will use Authorization Code flow as it's being ran long term in a secure location.

Currently the project only includes the Python program, which is about prepped for setting up on the server. The core functionality that needs adding is a setup file to pass in the auth keys as environment variables in the args rather than in a plain text .csv 
