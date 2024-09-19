"""
Functions for data handling
"""

# imports
import requests


# functions
def fetch_data(url: str):
    res = requests.get(url)
    if res.status_code != 200:
        print(f"Error!! Could not connect. Code: {res.status_code}")
        return None
    return res.json()
