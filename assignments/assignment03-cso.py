# Retrieves the dataset for the "exchequer account(historical series)"
# from the CSO, and stores it into a file called "cso.json"
# Full url: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en
# Author: Joanna Kelly

import requests
import json

url_beginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
url_end = "/JSON-stat/1.0/en"
dataset = "FIQ02"
save_path = r"C:\Users\joann\Desktop\Web-Services-and-Applications\assignments\cso.json"

def get_all_as_file(dataset):
    with open(save_path, "wt") as fp:
        print(json.dumps(get_all(dataset)), file=fp)

def get_all(dataset):   
    url = url_beginning + dataset + url_end
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    get_all_as_file(dataset)
    print(f"cso.json successfully created!")