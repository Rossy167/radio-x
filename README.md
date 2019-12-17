# Radio X Playlist Generator

Generates Spotify playlist from Last Played Songs on Radio X 

## Before You Start

The environment that you're running in it is going to need the Spotipy, Requests and BeautifulSoup4 libraries. It uses authentication by getting your tokens from a .txt with the order client ID, secret ID, username. Probably best not mess with it at this phase, until I've got proper authentication going. But the core function works.

### Working On 

My short term task is to refactor all of the code to be a little more professional. The future plan for this is to have 2 forks: a flask or other web app type version that users can authenticate into with Spotify and then have it generate playlists for them, and a scheduled task to be ran on a server or home automation type device.

Authentication is probably the core difficulty in making both these forks work. I want users to be able to simply go to a website, it'll say "connect to spotify" at which point you're hooked up to a spotify login page and confirm button, then sorted. The scheduled task one will need some kind of automation to reauthenticate itself after the tokens expire.
