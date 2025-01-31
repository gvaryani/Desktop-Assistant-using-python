import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


#Taking voice from my system
#0:male voice
#1: female voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty ('rate', 150)

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("Hello I am Gunjan, I write code and I am a Data Scientist, how are you?")

# Speech Recognition
def takecommand():
    """
    This function will recognize voice and returns text
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Successfully")
        r.pause_threshold=1
        audio = r.listen(source)


        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    

#The function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon sir. How are you doing")

    else:
        speak("Good evening sir. How are you doing")
    
    speak("I am JARVIS. Tell me sir how can i help you")


text = takecommand()
speak(text)

if __name__ == "__main__":
    
    wish_me()

    while True:
        query = takecommand().lower()
        print(query)
   
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "Google" in query:
            speak("opening Google")
            webbrowser.open("Google.com")

        elif "Github" in query:
            speak("opening Github")
            webbrowser.open("Github.com")

        #This query for say the times
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")


        elif 'goodbye' in query:
            speak("ok sir. I am always here for you. bye bye")
            exit()