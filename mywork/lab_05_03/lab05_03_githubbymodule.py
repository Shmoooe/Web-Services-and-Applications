# Lab05.03 Using Packages
# Author: Joanna Kelly


from github import Github
from config import config as cfg

apikey = cfg["githubkey"]

g = Github(apikey)

#for repo in g.get_user().get_repos():
    #print(repo.name)

repo = g.get_repo("")
