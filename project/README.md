# Big Project
#### For Web Services and Applications

All code written in [Visual Studio Code](https://code.visualstudio.com/download).

This repository contains 5 files as follows:

1. README.md

2. [app.py](https://github.com/Shmoooe/Web-Services-and-Applications/blob/main/project/app.py)

3. [dao.py](https://github.com/Shmoooe/Web-Services-and-Applications/blob/main/project/dao.py)

4. [requirements.txt](https://github.com/Shmoooe/Web-Services-and-Applications/blob/main/project/requirements.txt)

5. [spotify.py](https://github.com/Shmoooe/Web-Services-and-Applications/blob/main/project/spotify.py)


### app.py
This file contains the Flask app with endpoints for interacting with the API and database through imported functions from dao.py and spotify.py.

### dao.py
This is my data access object, containing all functions for interacting with my database in SQL.

### requirements.txt 
A text file that outlines all packages contained in the virtual environment for running this project.

### spotify.py 
Contains functions for interacting with spotify specifically, such as generating an access token and searching for artists.

### Local files (not in repo)
- .gitignore excludes:
    
    - venv/ - the virtual environment folder

    - spotify_config.py - contains sensitive Spotify credentials

## Testing the API
All endpoints can be tested in [Postman](https://crimson-satellite-440197.postman.co/) or cURL in your terminal

_Note: I have yet to implement the AJAX-based web interface, so testing is currently done via API tools only._

## /venv
To set up the virtual environment, the user must open their command line or terminal and navigate to their desired folder. When inside, type the prompt ```python -m venv venv``` to create it. Then to run the virtual environment, type the command ```\venv\Scripts\activate.bat```. To install the requirements run ```pip install -r requirements.txt```.