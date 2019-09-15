from flask import Flask
from flask import request
from flask import jsonify

from hatesonar import Sonar

app = Flask(__name__)

def youtube_video_to_audio(link):
    # link -> mp3 file and return the path to file
    print("Converting YouTube video to audio: link = {}".format(link))
    return None


def speech_to_text(file_path):
    # throw the file to azure api and return text
    print("Converting speech audio to text")
    return None


def classify_texts(texts):
    print("Classifying texts with detector")

    texts = texts.split(".")[:-1]

    rating_map = {"neither": "green", "offensive_language": "orange", "hate_speech": "red"}

    sonar = Sonar()
    results = []
    for i, sentence in enumerate(texts):
        sentence_res = sonar.ping(text=sentence)
        top_class = sentence_res["top_class"]
        sentence_output = {"index": i+1, "sentence": sentence, "top_class": top_class, "rating": rating_map[top_class]}
        results.append(sentence_output)

    return results


@app.route("/")
def hello():
    print("Request received: {}".format(request))
    return "Hello World!"


@app.route("/video")
def process_video():
    link = request.args.get('link')
    print("Video request received: link = {}".format(link))
    
    file_path = youtube_video_to_audio(link)
    texts = speech_to_text(file_path)

    # dummy text
    texts = "Pedophiles are fucking immature assholes. \
            I still use Internet Explorer. \
            I hope your baby’s retarded. \
            Nicki Minaj is immensely talented. \
            Carl Sagan deserves to have cancer. \
            I fucked your mom. \
            At least I'm not a Jew."

    results = classify_texts(texts)

    return jsonify(results=results)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')