from pyautogui import click
from keyboard import press 
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pyttsx3
import speech_recognition
import pywhatkit


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e: 
        print("Say that again")
        return "None"
    return query

def YouTUbeAutomation(command):
    query = str(command)
    if 'pause' in query:
        press('space bar')
    elif'resume' in query or 'play' in query:
        press('space bar')
    elif'full screen' in query:
       press('f')
    elif'film screen' in query:
        press('t')
    elif'skip' in query:
        press('l')
    elif'back' in query:
        press('j')
    elif'increase' in query:
        press_and_release('SHIFT + .')
    elif'decrease' in query:
        press_and_release('SHIFT + ,')
    elif'previous' in query:
        press_and_release('SHIFT + p')
    elif'next' in query:
        press_and_release('SHIFT + n')
    elif'mute' in query:
        press('m')
    elif'unmute' in query:
        press('m')
    elif'miniplayer' in query:
        press('i')

    if "search" in query: 
        query = query.replace("youtube search","")
        query = query.replace("play song","")
        query = query.replace("Maggie","")
        web  = "https://www.youtube.com/results?search_query=" + query
        speak("This is what I found for your search!")
        pywhatkit.playonyt(query)
        speak("Done, Sir")
        sleep(4)