import requests
from urllib.parse import urlparse
import base64

def list_files_from_github_url(repo_url):
    # Parse owner and repo from URL
    parsed_url = urlparse(repo_url)
    parts = parsed_url.path.strip('/').split('/')
    if len(parts) < 2:
        print("Invalid GitHub repository URL.")
        return []

    owner, repo = parts[0], parts[1]

    # GitHub API endpoint to list contents
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    response = requests.get(api_url)

    if response.status_code == 200:
        # Return list of files as array
        return [item['name'] for item in response.json() if item['type'] == 'file']
    else:
        print(f"❌ Failed to fetch contents: {response.status_code} - {response.text}")
        return []
    


def read_readme_from_github(repo_url):
    # Extract owner and repo name from URL
    parsed = urlparse(repo_url)
    parts = parsed.path.strip("/").split("/")
    if len(parts) < 2:
        print("❌ Invalid GitHub repo URL.")
        return

    owner, repo = parts[0], parts[1]

    # GitHub API endpoint to get README (uses default branch automatically)
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    response = requests.get(api_url, headers={"Accept": "application/vnd.github.v3+json"})

    if response.status_code == 200:
        content_encoded = response.json()['content']
        content_decoded = base64.b64decode(content_encoded).decode('utf-8')
        return content_decoded
    else:
        print(f"❌ Failed to fetch README: {response.status_code}")
        print(response.text)

 
