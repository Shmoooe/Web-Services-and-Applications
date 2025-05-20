# use my client id and secret to generate an access token

from spotify_config import config
import requests
import base64

def get_access_token():
    client_id=config["client_id"]
    client_secret=config["client_secret"]

    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic" + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(token_url, headers=headers, data=data)
    return response.json()["access_token"]