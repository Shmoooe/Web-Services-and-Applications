print("HELLO") 


from github import Github
from mywork.lab_05_03.config import config as cfg

apikey = cfg["githubkey"]
print("API key loaded:", "Yes" if apikey else "No")

g = Github(apikey)

for repo in g.get_user().get_repos():
    print(repo.name)
