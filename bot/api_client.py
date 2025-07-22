import requests

from config import base_url

def get_all_books():
    response = requests.get(f"{base_url}/books")
    
    if response.status_code == 200:
        return response.json()
    
    return []

def get_all_authors():
    response = requests.get(f"{base_url}/authors")
    
    if response.status_code == 200:
        return response.json()
    
    return []