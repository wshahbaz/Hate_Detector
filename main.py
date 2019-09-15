from flask import Flask, render_template, jsonify
import functools
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contributors")
def contributors():
    return render_template("contributors.html")

@app.route("/video-info", methods=['GET'])
def getOffensiveness():
    context = 20
    data = {
        "response": [
            {
                "id": 1,
                "sentence": "Hello",
                "name": "GOOD",
                "value": 13,
                "rating": "green"
            },
            {
                "id": 2,
                "sentence": "my name is",
                "name": "MILDLY INFURIATING",
                "value": 44,
                "rating": "orange"
            },
            {
                "id": 3,
                "sentence": "Wais",
                "name": "OFFENSIVE",
                "value": 99,
                "rating": "red"
            }
        ]
    }    #the response of the API call
    ids = map(lambda sentence : sentence["id"], data["response"])
    sentences = map(lambda sentence : sentence["sentence"], data["response"])
    names = map(lambda sentence : sentence["name"], data["response"])
    values = map(lambda sentence : sentence["value"], data["response"])
    ratings = map(lambda sentence : sentence["rating"], data["response"])
    numItems = len(data["response"])

    sum = 0
    overall_rating = 0
    for sentence in data["response"]:
        sum += sentence["value"]
    avg = 1.0 * sum / len(data["response"])

    if (avg < 33):
        overall_rating = "greenBack"
    elif (avg < 67):
        overall_rating = "orangeBack"
    else:
        overall_rating = "redBack"

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
    
if __name__ == "__main__":
    app.run(debug=True)