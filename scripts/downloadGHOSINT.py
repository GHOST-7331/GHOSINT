# I developed this script due to my preference for an alternative to PowerShell's method of downloading files. Consequently, I crafted a Python script to facilitate file downloads from the web.
# pip install requests

import requests
import sys
import os

def download_file(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Checks if the request was successful 
        if response.status_code == 200:
            # Extracts the filename from the URL
            filename = url.split('/')[-1]
            # Write the content of the response to a file
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"File '{filename}' downloaded successfully.")
        else:
            print(f"Failed to download file. HTTP status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
