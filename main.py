import speech_recognition as sr
r = sr.Recognizer()

# Set to device index 2 for the stereo mix use, instead
# of microphone
with sr.Microphone(device_index=2) as source:
    print("Say something!")
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    print(voice_data)
