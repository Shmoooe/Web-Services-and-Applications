# use my client id and secret (from spotify_config) to generate an access token

from spotify_config import config
import requests
import base64 

def get_access_token():
    # Load spotify API credentials from config
    client_id=config["client_id"]
    client_secret=config["client_secret"]

    token_url = "https://accounts.spotify.com/api/token"

    # Encode credentials in base64 for the authorization header
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }

    # This grant type allows the application to get an access token without a user login
    data = {"grant_type": "client_credentials"}

    response = requests.post(token_url, headers=headers, data=data)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
        print("Response body:", response.text)
        raise
    
    # Return the access token
    json_data = response.json()
    return json_data["access_token"]

def search_artist(name):
    # Get a valid access token
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    #Search for the artist by name, showing only 1 result
    params = {
        "q": name,
        "type": "artist",
        "limit": 1
    }

    response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    # If the artist is found, take the relevant details
    if data["artists"]["items"]:
        artist = data["artists"]["items"][0]
        return {
            "name": artist["name"],
            "genre": artist["genres"][0] if artist["genres"] else None,
            "popularity": artist["popularity"],
            "spotify_id": artist["id"]
        }
    else:
        raise Exception("No artist found")
    
# Testing
if __name__ == "__main__":
    print("Testing get_access_token()")
    token = get_access_token()
    print("Access token:", token)
