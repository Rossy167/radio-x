#!/bin/bash

OLDWD=$(pwd) 
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P)"

cd $SCRIPTPATH
cd ..

{
    python3 -m venv radiox/radiox_environment
    source radiox/radiox_environment/bin/activate
    pip install requests
    pip install beautifulsoup4
    pip install spotipy
} &> /dev/null

cd $OLDWD
