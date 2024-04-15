import requests
import argparse
import os

parser = argparse.ArgumentParser(description='Create a repository on GitHub.')
parser.add_argument('repo_name', type=str, help='Name of the repository to create')
args = parser.parse_args()

token = os.environ.get('GITHUB_ACCESS_TOKEN')
if token is None:
    print("Error: GitHub token not found in environment variables.")

def create_github_repository(repo_name, token):
    url = 'https://api.github.com/user/repos'
    headers = {
        'Authorization': 'token ' + token,
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'name': repo_name,
        'auto_init': True,  # Initializes the repository with a README
        # Add more parameters as needed, such as description, private/public visibility, etc.
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print("Repository created successfully!")
        print("Repository URL:", response.json()["html_url"])
    else:
        print("Failed to create repository. Status code:", response.status_code)
        print("Response:", response.json())


create_github_repository(args.repo_name, token)
