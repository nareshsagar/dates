import requests

def search_bitbucket_server_repository(base_url, project_key, repository_slug, search_string):
    # API endpoint to search files
    search_endpoint = f"{base_url}/rest/api/1.0/projects/{project_key}/repos/{repository_slug}/browse"

    # Set up authentication
    auth = ('username', 'password')  # Replace with your Bitbucket Server credentials

    # Get the list of files in the repository
    response = requests.get(search_endpoint, auth=auth)
    if response.status_code != 200:
        print(f"Failed to retrieve file list. Status code: {response.status_code}")
        return

    files_data = response.json()

    # Iterate through the files and search for the string
    for file in files_data['values']:
        file_path = file['path']

        # Download the file content
        file_content_url = file['links']['self'][0]['href']
        response = requests.get(file_content_url, auth=auth)
        if response.status_code != 200:
            print(f"Failed to download file content: {file_path}. Status code: {response.status_code}")
            continue

        file_content = response.text

        # Check if the search string is present in the file content
        if search_string in file_content:
            print(f"Found '{search_string}' in file: {file_path}")

# Example usage
search_bitbucket_server_repository('https://bitbucket.example.com', 'my-project', 'my-repo', 'search-string')


import subprocess
import os

def clone_and_modify_repo(repo_url, username, password):
    # Extract repository name from URL
    repo_name = repo_url.split("/")[-1].split(".git")[0]

    # Clone the repository
    clone_command = f"git clone {repo_url}"
    try:
        subprocess.run(clone_command.split(), check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to clone the repository: {repo_url}")
        return

    # Change directory to the cloned repository
    repo_dir = os.path.join(os.getcwd(), repo_name)
    os.chdir(repo_dir)

    # Make changes to a file
    file_path = "path/to/file.txt"
    with open(file_path, "a") as file:
        file.write("Added some changes")

    # Commit the changes
    subprocess.run(["git", "add", file_path])
    subprocess.run(["git", "commit", "-m", "Made some changes"])

    # Push the changes to the repository
    subprocess.run(["git", "push", "origin", "master"])

    # Create a pull request
    pull_request_title = "My Pull Request"
    pull_request_body = "Please review my changes"
    subprocess.run(["git", "request-pull", "-m", pull_request_title, "origin/master"])

# Example usage
repo_url = "https://bitbucket.org/username/repository.git"
username = "your_username"
password = "your_password"

clone_and_modify_repo(repo_url, username, password)



##############

import subprocess
import os

def clone_and_search_repo(repo_url, username, password, search_string):
    # Extract repository name from URL
    repo_name = repo_url.split("/")[-1].split(".git")[0]

    # Clone the repository
    clone_command = f"git clone {repo_url}"
    try:
        subprocess.run(clone_command.split(), check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to clone the repository: {repo_url}")
        return []

    # Change directory to the cloned repository
    repo_dir = os.path.join(os.getcwd(), repo_name)
    os.chdir(repo_dir)

    # Search for the string in files and directories
    matching_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                content = f.read()
                if search_string in content:
                    matching_files.append(file_path)

    return matching_files

# Example usage
repo_url = "https://bitbucket.org/username/repository.git"
username = "your_username"
password = "your_password"
search_string = "your_search_string"

matching_files = clone_and_search_repo(repo_url, username, password, search_string)
if matching_files:
    result = "\n".join(matching_files)
    print(f"Matching files:\n{result}")
else:
    print("No matching files found.")


    
####################

import git
import os

def clone_and_modify_repo(repo_url, username, password, file_path, new_content, commit_message):
    # Extract repository name from URL
    repo_name = repo_url.split("/")[-1].split(".git")[0]

    # Clone the repository
    repo_dir = os.path.join(os.getcwd(), repo_name)
    try:
        git.Repo.clone_from(repo_url, repo_dir, auth=(username, password))
    except git.GitCommandError:
        print(f"Failed to clone the repository: {repo_url}")
        return

    # Change directory to the cloned repository
    os.chdir(repo_dir)

    try:
        # Open the file and modify its content
        with open(file_path, "w") as f:
            f.write(new_content)

        # Initialize a Git repo
        repo = git.Repo(repo_dir)

        # Add the modified file to the index
        repo.index.add([file_path])

        # Commit the changes
        repo.index.commit(commit_message)

        # Push the changes to the remote repository
        origin = repo.remote(name="origin")
        origin.push()

        print("Changes committed and pushed successfully.")
    except Exception as e:
        print(f"An error occurred while modifying the repository: {str(e)}")

# Example usage
repo_url = "https://bitbucket.org/username/repository.git"
username = "your_username"
password = "your_password"
file_path = "path/to/file.txt"
new_content = "New content"
commit_message = "Modified file"

clone_and_modify_repo(repo_url, username, password, file_path, new_content, commit_message)
