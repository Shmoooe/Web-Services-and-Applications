# use my client id and secret to generate an access token

print("====> Script is executing")
from spotify_config import config
import requests
import base64

def get_access_token():
    client_id=config["client_id"]
    client_secret=config["client_secret"]

    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(token_url, headers=headers, data=data)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
        print("Response body:", response.text)
        raise

    json_data = response.json()
    return json_data["access_token"]

if __name__ == "__main__":
    print("Testing get_access_token()")
    token = get_access_token()
    print("Access token:", token)
