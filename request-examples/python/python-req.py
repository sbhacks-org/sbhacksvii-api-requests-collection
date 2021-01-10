"""
This program shows you how to query an API in Python.

You must have the Python requests library, which you can install via:
pip install requests

"""
import json
import pprint
import requests
import sys
import urllib

# No Authentication

print('No Auth Request')
response = requests.get('https://catfact.ninja/fact')

if (response.status_code == 200):
    # Do things
    print(json.dumps(response.json(), indent=4))

print('\n')

# API Key Authentication
# Example with Yelp API
# In real life, do not paste your API key like this. Totally fine for a hackathon though :)

API_KEY = 'eHmKqxRtJ5qZ1YHew6iY5MyWrML85XYnwJ_KBp8P96CYVggoLc5leL0FD0T4vfreWmT33jRISTnQ6hE218HlZrIK6psJ-MZrXv62rSmK476tPddFIfesw6p7w6H6X3Yx'
URL = 'https://api.yelp.com/v3/businesses/search'

print('API Key Auth Request')

headers = {
    'Authorization': 'Bearer %s' % API_KEY,
}

# Optional URL params would be different for different APIs
url_params = {
    'term': 'delis'.replace(' ', '+'),
    'location': "isla vista".replace(' ', '+'),
    'limit': 2
}
response = requests.request('GET', URL, headers=headers, params=url_params)

if (response.status_code == 200):
    # Do things
    print(json.dumps(response.json(), indent=4))