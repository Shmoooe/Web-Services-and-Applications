# a program that reads a file from a repository.
# the program replaces all the instances of the test "Andrew" with my own name.
# the program commits these changes and pushes it back to the repository.
# Author: Joanna Kelly

import requests
from github import Github

# temporarily adding this folder to my import path to access my config file
import sys 
sys.path.append("mywork/lab_05_03")
from config import config as cfg

# my connection to my github account
apikey = cfg["githubkey"]
g = Github(apikey) 

# Accessing my repo
repo = g.get_repo("Shmoooe/apublicone") 

# Downloading the contents of my repo
file_info = repo.get_contents("andrew.txt")
url_of_file = file_info.download_url

# Gets the contents of file as text
response = requests.get(url_of_file)
content_of_file = response.text

new_contents = content_of_file.replace("Andrew", "Joanna")

# Pushes change to github and adds commit message
git_hub_response = repo.update_file(file_info.path, "updated all instances of 'Andrew' to 'Joanna", new_contents, file_info.sha)
print(git_hub_response)