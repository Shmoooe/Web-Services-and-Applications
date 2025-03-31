# Using an api key to convert the wikipedia website into a pdf.
# Author: Joanna Kelly

import requests
import urllib.parse
from config import apikeys as cfg

target_url = "https://example.com"

apikey = cfg["htmltopdfkey"]

apiurl = "https://api.html2pdf.app/v1/generate"

params = {'url': target_url, 'apiKey': apikey, "noImages": "true",  "viewportWidth": 800 }
parsedparams = urllib.parse.urlencode(params)
request_url = apiurl + "?" + parsedparams

response = requests.get(request_url)
print(response.status_code)

result = response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)


