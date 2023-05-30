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
