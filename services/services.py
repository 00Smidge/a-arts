"""
Functions for data handling
"""

# imports
import requests


# functions
def fetch_data(url, params):
    res = requests.get(url, params)
    if res.status_code != 200:
        print(f"Error!! Could not connect. Code: {res.status_code}")
        return None
    return res.json()
