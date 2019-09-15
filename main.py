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

    text = request.form['text']
    # print(text)

    dictToSend = {'text': text}
    headers = {}
    response = requests.post(video_url, headers=headers, json=dictToSend)
    response = response.json()

    print(response)

    results = response['results']

    ids = [res['index'] for res in results]
    sentences = [res['sentence'] for res in results]
    colors = [res['rating'] for res in results]
    classes = [res['top_class'] for res in results]
    offensivess_scores = [res['offensivess_score'] for res in results]

    overall_rating = sum(offensivess_scores) * 100 / len(offensivess_scores)
    overall_rating = round(overall_rating, 2)

    return render_template(
        "home.html", 
        overall_offensiveness = overall_rating,
        ids = ids,
        names = sentences,
        classes = classes,
        ratings = offensivess_scores,
        numItems = len(ids),
        sentences = sentences,
        overall_rating = overall_rating
        )

    
    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)