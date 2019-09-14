from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

def youtube_video_to_audio(link):
    print("Converting YouTube video to audio: link = {}".format(link))
    return None


def speech_to_text(audio_obj):
    print("Converting speech audio to text")
    return None


def classify_text(text):
    print("Classifying text with detector")

    dummy_results = {'clean': 0.16, 'hate': 0.84}
    return dummy_results


@app.route("/")
def hello():
    print("Request received: {}".format(request))
    return "Hello World!"


@app.route("/video")
def process_video():
    link = request.args.get('link')
    print("Video request received: link = {}".format(link))
    
    audio_obj = youtube_video_to_audio(link)

    text = speech_to_text(audio_obj)

    results = classify_text(text)

    return jsonify(results=results)


if __name__ == '__main__':
    app.run()