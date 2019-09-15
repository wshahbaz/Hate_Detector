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
    target = os.path.join(APP_ROOT, "images/")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    #api processing portion
    API_URL = "https://hate-detector.azurewebsites.net/video"
    headers = {}
    response = requests.get('{}/files'.format(API_URL), headers=headers)
    ids = response["results"]
    
    ids = map(lambda sentence : sentence["id"], response["results"])
    # sentences = map(lambda sentence : sentence["sentence"], data["response"])
    # names = map(lambda sentence : sentence["name"], data["response"])
    # values = map(lambda sentence : sentence["value"], data["response"])
    # ratings = map(lambda sentence : sentence["rating"], data["response"])
    # numItems = 0
    # if (data["response"] and len(data["response"]) > 0):
    #     numItems = len(data["response"])

    # sum = 0
    # overall_rating = 0
    # for sentence in data["response"]:
    #     sum += sentence["value"]
    # avg = 1.0 * sum / len(data["response"])

    # if (avg < 33):
    #     overall_rating = "greenBack"
    # elif (avg < 67):
    #     overall_rating = "orangeBack"
    # else:
    #     overall_rating = "redBack"

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
    app.run(debug=True)