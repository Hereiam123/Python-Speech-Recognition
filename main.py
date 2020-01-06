import speech_recognition as sr
import webbrowser
import time

r = sr.Recognizer()


# Record audio via speech recognition library
def record_audio(ask=False):

    # Set to device index 2 for the stereo mix use, instead
    # of microphone
    with sr.Microphone(device_index=2) as source:
        if ask:
            print("You asked to search.\n", ask)
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
        print("It is", time.ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        # Search google for related request
        url = 'https://google.com/search?q=' + search
        print('Here is what I found for '+search)
        webbrowser.get().open(url)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        # Search google for related location request
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location '+location)
    if 'exit' in voice_data:
        exit()


# Sleep keeps voice channel open
time.sleep(1)
print("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
