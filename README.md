## radio-x

Web Scraper that generates a Spotify playlist based on last played songs on Radio X. 
Uses the URL at https://www.radiox.co.uk/radio/last-played-songs/

### Usage
Uses Beautiful Soup and Spotify's API to generate a Spotify playlist based on a html file from Radio X. 

I have a daily commute of roughly 2 hours and I get pretty tired of listening to the same tunes over and over. I also get pretty tired of constantly looking for more music to listen to, technically I'm quite busy. So I tune into the radio, I really like Radio X and their music choice, but honestly, the hosts can be a bit frustrating, and I really want to avoid ads. So I wrote a script to solve this.

The idea is that every few hours have my Pi run this script, and I keep a constantly rotating playlist that is mostly always fresh... you know, radio rotations can get a bit stale too.

The basic body of the script is as follows:

The HTML part grabs the .html file at https://www.radiox.co.uk/radio/last-played-songs/ and parses the file looking for songs, it all song name and their corresponding artists and then adds them to a list. The HTML script then passes that part onto the Spotify API part, which looks up each song and artist, and finds the song's ID on Spotify. Once it has a list of IDs, it then adds all the IDs to the playlist. It will overwrite a playlist called 'Radio X (code generated)' and  if it can't find one it will create one.   

### Setup
You will need to generate a venv, some setup scripts are provided to get this going.

Mac/Linux:
* cd into root directory for (should be radio-x or radio-x-master)
* run `bash setup/setup.sh (chmod to x if on Linux)`

Windows:
* Use Powershell, no intention of making this work for cmd.exe
* cd into root directory for (should be radio-x or radio-x-master) 
* run `.\setup\setup.ps1`

You may delete setup folder, though I would recommend the python package works first (this is why I don't delete it programmatically). You can, of course, create and manage own venv you will at the bare minimum need `spotipy, beautifulsoup4, requests`.  

### Using
Mac/Linux: cd into root directory and run `bash start.sh`

Windows: using Powershell, cd into root directory and run `.\start.ps1`

You can also manually run the script, activate the venv at radiox/radiox_environment/ and then run python radiox from root. It's just like... why not use mine right?

### Resources Used
* https://www.radiox.co.uk/radio/last-played-songs/
* https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* https://spotipy.readthedocs.io/en/2.12.0/
* https://www.w3schools.com/python/module_requests.asp
