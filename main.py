from flask import Flask, render_template, jsonify, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import functools
import os
import requests

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contributors")
def contributors():
    return render_template("contributors.html")

@app.route("/upload", methods=["POST"])
def upload():
    #api processing portion
    # API_URL = "https://hate-detector.azurewebsites.net/video"
    api_root = "http://192.168.181.137:5000"

    video_url = api_root + '/video'

    headers = {}
    response = requests.get(video_url, headers=headers)

    print(response)

    # ids = response["results"]
    
    ids = map(lambda sentence : sentence["id"], response["results"])

    return render_template(
        "home.html", 
        overall_offensiveness = avg,
        ids = ids,
        names = names,
        values = values,
        ratings = ratings,
        numItems = numItems,
        sentences = sentences,
        overall_rating = overall_rating
        )


# https://hate-detector.azurewebsites.net/video


    # data = {
    #     "response": [
    #         {
    #             "id": 1,
    #             "sentence": "Hello",
    #             "name": "GOOD",
    #             "value": 13,
    #             "rating": "green"
    #         },
    #         {
    #             "id": 2,
    #             "sentence": "my name is",
    #             "name": "MILDLY INFURIATING",
    #             "value": 44,
    #             "rating": "orange"
    #         },
    #         {
    #             "id": 3,
    #             "sentence": "Wais",
    #             "name": "OFFENSIVE",
    #             "value": 99,
    #             "rating": "red"
    #         }
    #     ]
    # }    #the response of the API call



    
    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)