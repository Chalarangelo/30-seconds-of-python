import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I'm Jarvis How may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)
    try:
        print("Rcognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)

    except Exception as e:
        # print(e)
        print("I didn't Understand please say that again")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is ", strTime)
        elif "open visual studio code" in query:
            codePath = "C:\\Users\\ACER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
