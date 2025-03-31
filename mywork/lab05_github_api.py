# Test my new github api to get info from the private repository I created
# Author: Joanna Kelly

import requests
import json
from config import apikeys as cfg

url = "https://api.github.com/repos/Shmoooe/aprivateone"
apiKey = cfg["githubapi"]
filename = "private_repo.json"

response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()

with open(filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)
    print(response.status_code)