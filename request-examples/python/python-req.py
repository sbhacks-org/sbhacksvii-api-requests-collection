"""
This program shows you how to query an API in Python.

You must have the Python requests library, which you can install via:
pip install requests

You'll also need Flask
pip install flask

maybe use pip3

Note: we put all our code into one file for this demo, but in your project you will probably want to organize things
into folders and files in order to separate the code into chunks that make sense. ex. the code for backend logic
probably should not be in the same file as the html/css. see https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/
"""

from flask import Flask, request # request for Flask, not the API
import json
import pprint
import requests
import sys
import urllib

# create Flask app
# to run this app
#   export FLASK_APP=python-req.py
#   flask run
app = Flask(__name__)

# set up requests parameters
# API Key Authentication
# Example with Yelp API
# In real life, do not paste your API key like this. Use a dot env. Totally fine for a hackathon though :)

API_KEY = 'eHmKqxRtJ5qZ1YHew6iY5MyWrML85XYnwJ_KBp8P96CYVggoLc5leL0FD0T4vfreWmT33jRISTnQ6hE218HlZrIK6psJ-MZrXv62rSmK476tPddFIfesw6p7w6H6X3Yx'
URL = 'https://api.yelp.com/v3/businesses/search'

print('API Key Auth Request')

headers = {
    'Authorization': 'Bearer %s' % API_KEY,
}

# routing decorator says "when you land on the page with this extension, we run this function"
# ex. @app.route('dogs') would run that function when we go to websitename.com/dogs/
@app.route('/')
def demo_front_page():
    return '''
        This is the front page of our app. Click below to go to the API page
        <form action="http://localhost:5000/API_page">
        <input type="submit" value="Go to API page" />
        </form>'''
@app.route('/API_page', methods=['GET', 'POST'])
def demo_API_page():
    if request.method == 'POST' and 'key' in request.form:
        if request.form['key'] == 'cat':
            response = requests.get('https://catfact.ninja/fact')
            if response.status_code == 200:
                return f'''cool fact: {response.json()['fact']}\n
                <form action="http://localhost:5000/API_page">
                <input type="submit" value="Go to API page" />
                </form>'''
            else:
                return '''cat api call failed\n
                <form action="http://localhost:5000/API_page">
                <input type="submit" value="Go to API page" />
                </form>'''
        else:
            # Optional URL params would be different for different APIs
            url_params = {
                'term': request.form['key'],
                'location': "isla vista",
                'limit': 1
            }
            response = requests.request('GET', URL, headers=headers, params=url_params)
            if response.status_code == 200 and len(response.json()['businesses']) > 0:
                business = response.json()['businesses'][0]
                return f'''top result is {business['name']}\n
                yelp link: {business['url']}\n
                rating: {business['rating']}\n
                <form action="http://localhost:5000/API_page">
                <input type="submit" value="Go to API page" />
                </form>'''
            else:
                return '''yelp: either API call failed or no businesses matching the searched term\n
                <form action="http://localhost:5000/API_page">
                <input type="submit" value="Go to API page" />
                </form>'''

    return '''
            Input 'cat' for a cat fact. otherwise queries yelp businesses in IV
            <form method="POST">
            input key: <input type="text" name="key"><br>
            <input type="submit" value="Submit"><br>
            </form>'''


