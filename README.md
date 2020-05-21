## radio-x

Web Scraper that generates a Spotify playlist based on last played songs on Radio X. 
Uses the URL at https://www.radiox.co.uk/radio/last-played-songs/

### Usage
Uses Beautiful Soup and Spotify's API to generate a Spotify playlist based on a html file from Radio X

### Setup
You will need to generate a venv, some setup scripts are provided to get this going.

Mac/Linux:
* cd into root directory for (should be radio-x or radio-x-master)
* run `bash setup/setup.sh (chmod to x if on Linux)`

Windows:
* Use Powershell, no intention of making this work for cmd.exe
* cd into root directory for (should be radio-x or radio-x-master) 
* run `.\setup\setup.ps1`

### Using
Mac/Linux (with script):
* cd into root directory and run `bash start.sh`

Mac/Linux (without script):
* cd into root directory and run `source python radiox/radiox_environment/bin/activate`
* run `python radiox`

Windows(with script):
* cd into root directory
* Using Powershell run `.\start.ps1

Windows:
* cd into root directory
* Using Powershell run .\radiox\radiox_environment\Scripts\Activate.ps1
* run python radiox

### Resources Used
* https://www.radiox.co.uk/radio/last-played-songs/
* https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* https://spotipy.readthedocs.io/en/2.12.0/
* https://www.w3schools.com/python/module_requests.asp