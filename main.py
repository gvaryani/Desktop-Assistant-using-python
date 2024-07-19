import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


#Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getproperty('voices')
print(voices)
engine.setproperty('voice',voices[0].id)
engine.setproperty ('rate', 150)

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello I am a programmer, how are you?")

# Speech Recognition
def takecommand():
    """
    This function will recognize voice and returns text
    """
s=sr.Recognizer()
with sr.Microphone() as source:
    print("Listening Successfully")
    r.pause_threshold=1
    audio = r.listen(source)


    try:
        print('Recognizing..')
        r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
     
    
    except Exception as e:
        print("say it again please...")
        #return "None"
    return query

text=takeCommand()
speak(text)


if__name__ == "__main__":

query=takecommand().lower()
print(query)
if  "wikipedia" in query:
    speak("searching wikipedia")
    query = query.replace('wikipedia',"")
    results=wikipedia.summary(query,sentences=2)
    speak("According to wikipedia")
    print("results")
    speak("results")


elif "youtube" in query:
    speak("opening youtube")
    webbrowser.open("youtube.com")


elif "Google" in query:
    speak("opening Google")
    webbrowser.open("Google.com")

elif "Google" in query:
    speak("opening Google")
    webbrowser.open("Google.com")


   





















