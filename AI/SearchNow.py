import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


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

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def searchWikipedia(query):
    if "wikipedia" in query:
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        speak("Searching from wikipedia....")
        query = query.replace("Maggie","")
        results = wikipedia.summary(query,sentences = 1)
        speak("According to wikipedia..")
        print(results)
        speak(results)
def googlesearch(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("google","")
        query = query.replace("search google","")
        query = query.replace("search ","")
        query = query.replace("search in google","")
        speak("This is what I found on the web!")
        pywhatkit.search(query)

        try:
            result=googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No Speakable Data Avilable!")
