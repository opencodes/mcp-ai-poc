from lib import list_files_from_github_url, read_readme_from_github


def main():
    """List files in a GitHub repository"""
    print("Starting main function...")
    repo = "https://github.com/opencodes/BuildHub"
    files = list_files_from_github_url(repo)
    readme_content = read_readme_from_github(repo)
    print(f"Files in repo={repo}", files)
    print(f"Readme from repo={repo}", readme_content)


 
if __name__ == "__main__":
    main()
     