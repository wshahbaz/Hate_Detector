import azure.cognitiveservices.speech as speechsdk
import time


def speech_recognize_continuous_from_file(filename, speech_key, service_region):
    """performs continuous speech recognition with input from an audio file"""
    # <SpeechContinuousRecognitionWithFile>
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.audio.AudioConfig(filename=filename)

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
    
    print(" ".join(filter((lambda sentences: sentences != ""), text)))

if __name__ == '__main__':
    filename = 'sample.wav'
    speech_key = "604c4624ee7b4a4d8b2b3ae41b77b6e1"
    service_region = "canadacentral"

    speech_recognize_continuous_from_file(filename, speech_key, service_region)