"""
This program shows you how to query an API in Python.

You must have the Python requests library, which you can install via:
pip install requests

You'll also need Flask (you might have to use pip3)
pip install flask

to run this app
    export FLASK_APP=app.py
    flask run

Note: we put all our code into one file for this demo, but in your project you will probably want to organize things
into folders and files in order to separate the code into chunks that make sense. ex. the code for backend logic
probably should not be in the same file as the html/css. see https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/
"""

from flask import Flask, request, render_template # request for Flask, not the API
import json
import pprint
import requests
import sys
import urllib

# create Flask app

app = Flask(__name__)

# set up requests parameters

# routing decorator says "when you land on the page with this extension, we run this function"
# ex. @app.route('dogs') would run that function when we go to websitename.com/dogs/
@app.route('/')
def demo_front_page():
    # return a HTML page
    # i'm just returning a string, but you should use flask's render_template to return an HTML (example below)
    return '''
        This is the front page of our app. Click below to go to the API page
        <form action="http://localhost:5000/API_page">
        <input type="submit" value="Go to API page" />
        </form>'''

# allow both GET and POST requests to this route
# this means when we go to websitename.com/API_page flask will check for requests from it's own request handler
# this is the one we imported from flask
@app.route('/API_page', methods=['GET', 'POST'])
def demo_API_page():
    # check if we received a request from our own form
    if request.method == 'POST' and 'key' in request.form:
        # if the user inputted 'cat'
        if request.form['key'] == 'cat':
            # send request to some URL and it returns a response object which has meta and regular data in it
            response = requests.get('https://catfact.ninja/fact')
            if response.status_code == 200:
                return render_template('page.html', response_text=response.json()['fact'])
            else:
                return render_template('page.html', response_text="cat api call failed")
        # if the user didn't input cat but still input something, we query yelp for it
        else:
            # yelp requires API keys
            # API Key Authentication
            # In real life, do not paste your API key like this. Use a dot env. Totally fine for a hackathon though :)

            API_KEY = 'eHmKqxRtJ5qZ1YHew6iY5MyWrML85XYnwJ_KBp8P96CYVggoLc5leL0FD0T4vfreWmT33jRISTnQ6hE218HlZrIK6psJ-MZrXv62rSmK476tPddFIfesw6p7w6H6X3Yx'
            URL = 'https://api.yelp.com/v3/businesses/search'

            headers = {
                'Authorization': 'Bearer %s' % API_KEY,
            }

            # Now yelp knows it's us
            # you should have the API key declared outside of a function. we put it here just to show where we use it

            # Optional URL params would be different for different APIs
            url_params = {
                'term': request.form['key'],
                'location': "isla vista",
                'limit': 1
            }
            # same idea as previous api
            response = requests.request('GET', URL, headers=headers, params=url_params)
            if response.status_code == 200 and len(response.json()['businesses']) > 0:
                business = response.json()['businesses'][0]
                return render_template('page.html', term=request.form['key'], restaurant_name=business['name'], restaurant_url=business['url'], restaurant_img_url=business['image_url'], restaurant_rating=str(business['rating']))
            else:
                return render_template('page.html', response_text="yelp: either API call failed or no businesses matching the searched term")

    # if no request from our form, then show the form
    return render_template('page.html')