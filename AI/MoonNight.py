import os
import sys
import webbrowser
import pyttsx3
import speech_recognition 
import requests
import datetime
from bs4 import BeautifulSoup
import random
import winshell
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from gui import Ui_MainWindow
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",200)

    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()
    
    def takeCommand(self):
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

    def TaskExecution(self):
        
        while True:
         self.query = self.takeCommand().lower()
         if "wake up" in self.query or "good morning" in self.query or "good afternoon" in self.query or "good evening" in self.query or "start" in self.query:
            from GreetMe import greetMe
            greetMe() 

            while True:
                self.query = self.takeCommand().lower()
                
                if "go to sleep" in self.query or "chup" in self.query or "silent" in self.query or "small break" in self.query:
                    speak("Ok sir , You can me call anytime")
                    break

                elif "hello" in self.query:
                    speak("Hello sir, how are you ?")
                elif "who made you" in self.query:
                    speak("CIT sutdents made me, sir")
                elif "i am fine" in self.query or "I M fine" in self.query:
                    speak("that's great, sir")
                elif "how are you" in self.query:
                    speak("Perfect, sir")
                elif "thank you" in self.query or "ok good" in self.query or "good" in self.query:
                    speak("you are welcome, sir")
                elif "what your name" in self.query or  "whats your name" in self.query or "what ise your name" in self.query or  "what's your name" in self.query or "what is your name" in self.query:
                    speak("My name is Maggie, sir")
                elif "who are you" in self.query:
                    speak("I am your personal Ai, sir")
                elif "hay maggei" in self.query or "hii" in self.query or "hlo" in self.query :
                    speak("I am your personal Ai, sir")

                    
                

                elif "volume up" in self.query:
                    from keyvol import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume max" in self.query or "volume full" in self.query or "volume hundred percent" in self.query or "volume 100%" in self.query:
                    from keyvol import volumemax
                    speak("Turning volume max,sir")
                    volumemax()
                elif "volume mute" in self.query or "volume zero percent" in self.query or "volume 0%" in self.query:
                    from keyvol import volumemute
                    speak("Turning volume mute, sir")
                    volumemute()
                elif "volume down" in self.query:
                    from keyvol import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                    
                elif "youtube" in self.query or "YouTube" in self.query:
                    from youthub import YouTUbeAutomation
                    YouTUbeAutomation(self.query)

                elif "close" in self.query:
                    from Dictapp import closeappweb
                    closeappweb(self.query)

                elif "open" in self.query:   
                    self.query = self.query.replace("open","")
                    self.query = self.query.replace("Maggie","")
                    pyautogui.press("super")
                    pyautogui.typewrite(self.query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                    speak("Launching, sir") 

                
                elif "wikipedia" in self.query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(self.query)

                elif "google" in self.query:
                    from SearchNow import googlesearch
                    googlesearch(self.query)

                elif "tired" in self.query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=6IeL4ZUck2w") 
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=Rm5VI32UmDg")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=saCaYLaYyPg")
                
                elif "calculate" in self.query:
                    
                    from Calculatenumbers import Calc
                    self.query = self.query.replace("calculate","")
                    self.query = self.query.replace("Maggie","")
                    Calc(self.query)    

                    
                elif "temperature" in self.query or "weather" in self.query:
                    url = f"https://www.google.com/search?q={self.query}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{self.query} is {temp}")


                elif 'time' in self.query:
                     strTime = datetime.datetime.now().strftime("%I:%M:%S")    
                     speak(f"Sir, the time is {strTime}")

                elif 'date' in self.query:
                    year = (datetime.datetime.now().year)
                    month = (datetime.datetime.now().month)
                    date = (datetime.datetime.now().day)
                    speak("the current date is")
                    speak(date)
                    speak(month)
                    speak(year)

                elif "remember that" in self.query:
                    rememberMessage = self.query.replace("remember that","")
                    rememberMessage = self.query.replace("maggie","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in self.query:
                    remember = open("Remember.txt","r")
                    speak("You told me to " + remember.read())


                elif 'empty recycle bin' in self.query:
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    speak("Recycle Bin Recycled")
                
                elif "finally sleep" in self.query or "go to hell" in self.query or "exit" in self.query or "good night" in self.query:
                    speak("Going to sleep,sir")
                    exit()

                elif 'log out' in self.query:
                    os.system("shutdown -l")
                elif 'restart' in self.query:
                    os.system("shutdown /r /t 1")
                elif 'shutdown' in self.query:
                    os.system("shutdown /s /t 1")
                
                elif "where is" in self.query:
                    self.query = self.query.replace("where is", "")
                    location = self.query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.com/maps/place/" + location + "")
                

                elif "screenshot" in self.query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     image_date = f"screenshot_{str(datetime.datetime.now().day)}"
                     image_month = f"{str(datetime.datetime.now().month)}"
                     image_hour = f"{str(datetime.datetime.now().hour)}"
                     image_minute= f"{str(datetime.datetime.now().minute)}"
                     image_random = f"{random.randint(1,1000)}"
                     filepathloc = f"{image_date}-{image_month}_{image_hour}-{image_minute}_{image_random}.png"
                     im.save(filepathloc)
                
                elif "click my photo" in self.query or "take photo" in self.query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                
startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def run(self):
        self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("AI/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("AI/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
               
