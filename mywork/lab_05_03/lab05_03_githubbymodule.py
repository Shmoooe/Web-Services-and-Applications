# Lab05.03 Using Packages
# Author: Joanna Kelly

import requests
from github import Github
from config import config as cfg

apikey = cfg["githubkey"]
g = Github(apikey)

#for repo in g.get_user().get_repos():
    #print(repo.name)

repo = g.get_repo("Shmoooe/aprivateone")
#print(repo.clone_url)

file_info = repo.get_contents("test.txt")
url_of_file = file_info.download_url
#print(url_of_file)

response = requests.get(url_of_file)
content_of_file = response.text
#print(content_of_file)

new_contents = content_of_file + " more stuff \n"
#print(new_contents)

git_hub_response = repo.update_file(file_info.path, "updated by prog", new_contents, file_info.sha)
print(git_hub_response)