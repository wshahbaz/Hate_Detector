from flask import Flask
from flask import request
from flask import jsonify

from hatesonar import Sonar
import moviepy.editor as mp

import azure.cognitiveservices.speech as speechsdk
import time

app = Flask(__name__)

def video_to_audio(file_path):
    # link -> mp3 file and return the path to file
    print("Converting YouTube video to audio")
    video = mp.VideoFileClip(file_path)
    video.audio.write_audiofile("audio.wav", fps=16000, codec="pcm_s16le", ffmpeg_params=["-ac", "1"])


def speech_to_text(file_path):
    # throw the file to azure api and return text
    print("Converting speech audio to text")
    speech_key, service_region = "0ff27010d8924290946aef1640acfc8b", "canadacentral"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.audio.AudioConfig(filename=file_path)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    done = False
    text = []

    def stop_cb(evt):
        """callback that stops continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True
    def speech_recognized(evt):
        print('RECOGNIZED: {}'.format(evt))
        text.append(evt.result.text)
        
    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognized.connect(speech_recognized)
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)
    
    return " ".join(filter((lambda sentences: sentences != ""), text))

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
    file_path = video_to_audio("/path/to/file")
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