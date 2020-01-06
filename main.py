import speech_recognition as sr
from time import ctime

r = sr.Recognizer()


# Record audio via speech recognition library
def record_audio():

    # Set to device index 2 for the stereo mix use, instead
    # of microphone
    with sr.Microphone(device_index=2) as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I didn\'t get that')
        except sr.RequestError:
            print("Sorry, I am not active")
        return voice_data


# Respond to user voice input
def respond(voice_data):
    if 'what is your name' in voice_data:
        print("My name is giogle")
    if 'what time is it' in voice_data:
        print("It is", ctime())


print("How can I help you?")
voice_data = record_audio()
respond(voice_data)
