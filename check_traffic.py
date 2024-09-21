import os
import webbrowser

from dotenv import load_dotenv
from github import Github


def get_github_repositories(username, token):
    g = Github(token)
    user = g.get_user(username)
    repos = user.get_repos()
    repo_names = [repo.name for repo in repos]
    return repo_names


def check_github_traffic_in_browser(username, token):
    repos = get_github_repositories(username, token)
    for repo in repos:
        url = f'https://github.com/{username}/{repo}/graphs/traffic'
        webbrowser.get(using='google-chrome').open(url)


def main():
    load_dotenv()
    token = os.getenv('GITHUB_TOKEN')
    username = os.getenv('GITHUB_USERNAME')
    check_github_traffic_in_browser(username, token)


if __name__ == '__main__':
    main()



    
