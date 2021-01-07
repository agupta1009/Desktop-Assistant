from libraries import *
from main_screen import *
from initial_screen import *
from features import *
from take_input import *
from login import *
import sys
import os
import platform
import random
import touch
import ctypes
import subprocess
import datetime
import math
import webbrowser
import winshell
import smtplib,ssl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from win10toast import ToastNotifier
import speech_recognition as sr
import pyttsx3
import pyjokes
import time
from gtts import gTTS
import playsound
import webbrowser
import smtplib
import wikipedia
import datetime
from selenium import webdriver
import pyautogui as pg 
import clipboard
import pyperclip
from googletrans import Translator
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import pickle
import os.path

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
password=""
username=""
otp1=""
email=""
address=''

def speak(head,content):
    pyttsx3.speak(head)
    pyttsx3.speak(content)


def notification(result):
    toaster = ToastNotifier()
    
    msg=""
    for i in range(1,len(result)):
        msg=msg+result[i]+'\n'
    toaster.show_toast(result[0],msg,duration=5)
    speak(result[0],msg)

def wish_me():
    hr=datetime.datetime.now().hour
    if hr>=0 and hr<=12:
        pyttsx3.speak("Good morning user")
    elif hr>12 and hr<=16:
        pyttsx3.speak("Good afternoon user")
    else:
        pyttsx3.speak("good evening user")
    pyttsx3.speak('today is'+str(datetime.datetime.now().strftime("%A"))+'and its'+str(datetime.datetime.now().day)+"of"+str(datetime.datetime.now().strftime("%B"))+str(datetime.datetime.now().strftime("%Y")))


class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.ui.main_body_2.setGraphicsEffect(self.shadow)
        self.ui.widget.hide()
        self.show()
        self.ui.login_btn.clicked.connect(lambda:self.sendemail())
        self.ui.login_res_ok_btn_2.clicked.connect(lambda:self.ui.widget.hide())
        self.ui.login_res_ok_btn_2.clicked.connect(lambda:self.ui.widget_3.show())
        
        self.ui.login_btn_3.clicked.connect(lambda:self.validateLoginFields())


    # def check_email(self):
    #     global email
    #     email=self.ui.enter_email.text()
    #     if email=="":
    #         self.showLoginResponse('Email cannot be empty!')
    #         # return ""
    #     else:
    #         self.sendemail()

    def generateOTP(self) :
        digits = "0123456789"
        OTP = "" 
        for i in range(6) : 
            OTP += digits[math.floor(random.random() * 10)] 
        return OTP

    def sendemail(self):
        self.ui.enter_email.hide()
        self.ui.label_email.hide()
        self.ui.label_7.show()
        self.ui.password_3.show()
        global email
        email=self.ui.enter_email.text()
        if email=="":
            self.showLoginResponse('Email cannot be empty!')
        else:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('testsample1298@gmail.com', 'testsample50@')
            otp=self.generateOTP()
            global otp1
            otp1=otp
            self.ui.login_btn.hide()
            server.sendmail('testsample1298@gmail.com', self.ui.enter_email.text(), otp)
            server.close()

    def showLoginResponse(self, responseMessage):
        # Show the login response container
        self.ui.widget_3.hide()
        self.ui.widget.show()
        # Update the login response text
        self.ui.login_response_msg_2.setText(responseMessage)


    # Validate login field values
    def validateLoginFields(self):
        # Styles to be used to highlight input fiels on error or success
        successStyle = "border:3px solid  rgb(0, 255, 255);border-radius: 10px;"
        errorStyle = "border:3px solid  rgb(255, 0, 0);border-radius: 10px;"
        if not self.ui.username_3.text():
            # username is empty
            usernameResponse = " username can not be Empty. "
            self.ui.username_3.setStyleSheet(errorStyle)
        else:
            UsernameResponse = ""

        # Check Password
        if not self.ui.password_3.text():
            # Password is empty
            passwordResponse = " OTP can not be Empty. "
            self.ui.password_3.setStyleSheet(errorStyle)
        else:
            passwordResponse = ""

        
        # View responses
        if passwordResponse != "":
            loginResponse = passwordResponse
            self.showLoginResponse(loginResponse)

        else:
           
            global password
            password=otp1
            global username
            username=self.ui.username_3.text()
            

            # Check if the password is correct
            if self.ui.password_3.text() == otp1:
                passwordResponse = ""
                self.ui.password_3.setStyleSheet(successStyle)

            else:
                passwordResponse = " Incorrect OTP"
                self.ui.password_3.setStyleSheet(errorStyle)
             
             
    
            # Create a response msg
            if passwordResponse == "":
                loginResponse = " Login Successful. "
                self.main=SplashScreen2()
                self.main.show()
                self.close()

            elif passwordResponse != "" and usernameResponse != "":
                loginResponse = usernameResponse + " and " + passwordResponse
                self.showLoginResponse(loginResponse)

            else:
                loginResponse = usernameResponse + passwordResponse
                self.showLoginResponse(loginResponse)
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        pyttsx3.speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        # print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        # print(f"User said: {query}\n")
  
    except Exception as e:
        # print(e)    
        pyttsx3.speak("Unable to Recognize your voice.")  
        return "None"
     
    return query
def send(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('testsample1298@gmail.com', 'testsample50@')
    server.sendmail('testsample1298@gmail.com', to, content)
    server.close()


def get_audio():

    #It tane input from the user and returns string outputkes micropho

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print(" I am Listening...")
        r.phrase_time_limit=10
        audio = r.listen(source)

    try:   
        said = r.recognize_google(audio, language='en-in')
        return said
        # print(f"{name} {gender} said: {said}\n")
    except: 
        return "None"
    


class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.processcommand()
    def __del__(self):
        pass
    
    def voice(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            pyttsx3.speak('Hello what can i do for you')
            audio = r.record(source,duration=10)
            try:
                text = r.recognize_google(audio,language='en-in')
            except:
                pyttsx3.speak("Sorry could not recognize what you said")
                return ''
        return text

    def processcommand(self):
        self.query = self.voice()
            # self.query=takeCommand()
        if self.query=='':
            pyttsx3.speak('please try again later')
        else:
            self.query.lower()
            if "weather" in self.query:
                self.query=self.query.split()
                notification(weather(self.query[-1]))
            
            elif "close chrome" in self.query:
                        os.system('TASKKILL /F /IM Google Chrome.exe')

            elif "close task manager" in self.query:
                        os.system('TASKKILL /F /IM Taskmgr.exe')
 
            elif 'open stackoverflow' in self.query:
                pyttsx3.speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")
            elif 'send email ' in self.query and 'friend' in self.query:
                try:
                    
                    to = 'ankushsood50@gmail.com'
                    pyttsx3.speak("please tell the content")
                    content = takeCommand() 
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login('testsample1298@gmail.com', 'testsample50@')
                    server.sendmail('testsample1298@gmail.com', to, content)
                    server.close()
                    pyttsx3.speak("Email has been sent !")
                except Exception as e:
                    pyttsx3.speak("I am not able to send this email")   
        

            

            elif 'exit' in self.query:
                pyttsx3.speak("Thanks for giving me your time")
                self.close()

            elif 'joke' in self.query:
                pyttsx3.speak(pyjokes.get_joke())
            elif 'news' in self.query:
                notification(news())
            elif 'battery information' in self.query:
                notification(battery_info())
            elif 'movie detail' or 'movie details' in self.query:
                pyttsx3.speak('please tell the movie name')
                to=get_audio()
                notification(movie_info(to))
                t=''
            elif 'lock window' in self.query:
                pyttsx3.speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                pyttsx3.speak("Recycle Bin Recycled")
            elif "where is" in self.query or 'locate' in self.query:
                self.query = self.query.split()
                location = self.query[-1]
                pyttsx3.speak("User asked to Locate")
                pyttsx3.speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")
            elif "write a note" or 'make a note' or 'take a note' in self.query:
                pyttsx3.speak('please enter the filename where you want to save note')
                to=get_audio()
                to=to+'.txt'
                file = open(to, 'w')
                to=''
                pyttsx3.speak("What should i write, sir")
                note = takeCommand()
                pyttsx3.speak("Sir, Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
            elif "read" in self.query:
                try:
                    read()
                except:
                    pyttsx3.speak("no self.query selected please select a self.query")

            elif "type" in self.query:
                pyttsx3.speak("pls speak what you want me to type")
                pg.typewrite(get_audio())

            elif "select all" in self.query:
                pg.hotkey('ctrl','a')

            elif "close this window" in self.query:
                pg.hotkey('alt','f4')

            elif "open a new tab" in self.query:
                pg.hotkey('ctrl','n')

            elif "open a new incognito window" in self.query:
                pg.hotkey('ctrl','shelift','n')

            elif "copy" in self.query:
                pg.hotkey('ctrl','c')
                pyttsx3.speak('self.query copied to clipboard')

            elif "paste" in self.query:
                pg.hotkey('ctrl','v')

            elif "undo" in self.query:
                pg.hotkey('ctrl','z')

            elif "redo" in self.query:
                pg.hotkey('ctrl',)

            elif "save" in self.query:
                pg.hotkey('ctrl','s')

            elif "back" in self.query:
                pg.hotkey('browserback')

            elif "go up" in self.query:
                pg.hotkey('pageup') 

            elif "go to top" in self.query:
                pg.hotkey('home')

            elif "show note" in self.query:
                pyttsx3.speak('please enter the filename where you have saved the note')
                to=get_audio()
                to=to+'.txt'
                pyttsx3.speak("Showing Notes")
                file = open(to, "r") 
                to=''
                print(file.read())
                pyttsx3.speak(file.read(6))

            elif 'screenshot' in self.query:
                image=pg.screenshot()
                pyttsx3.speak("screen shot taken")
                pyttsx3.speak("what do you want to save it as?")
                filename=get_audio()
                image.save(filename+".png")
                
            elif 'translate' in self.query:        
                trans=Translator()
                pyttsx3.speak("Say the language to translate in")
                language=get_audio().replace(" ","")
                pyttsx3.speak("what to translate")
                content=get_audio()
                t=trans.translate(text=content,dest=language)
                pyttsx3.speak(f"{t.origin} in {t.dest} is{t.text}")
            # elif "beatbox" in self.query:
            #     beatboxes=['beatbox (1).wav','beatbox (2).wav','beatbox (3).wav','beatbox (4).wav','beatbox (5).wav','beatbox (6).wav','beatbox (7).wav' ]
            #     playsound.playsound(random.choice(beatboxes))
            elif "open terminal" in self.query:
                        os.startfile ("cmd")
            elif 'send message' in self.query:
                twilio_send_msg(self.query)
            elif 'call' in self.query:
                twilio_call(self.query)
            elif 'create file' in self.query:
                pyttsx3.speak('please tell the  name of file')
                to=get_audio()
                filename=to
                touch.touch(filename+'.txt')
            else:
                pyttsx3.speak('command not found')




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove window tlttle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.ui.main_body.setGraphicsEffect(self.shadow)
        # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.ui.footer_label.hide()
        self.ui.lineEdit.setText(username)
        self.ui.lineEdit_2.setText(email)
        # displays the landing page
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
    
        self.ui.pushButton_4.clicked.connect(lambda:self.close_app())
        self.ui.pushButton_3.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.speak_page))
        self.ui.pushButton_5.clicked.connect(lambda:self.animation_stop())
        self.ui.pushButton_3.clicked.connect(lambda:self.animation())
        self.ui.pushButton_6.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.accounts_page))
        self.show()

    
    def close_app(self):
        self.close()

    def animation_stop(self):
        if(hasattr(self.ui,'gi')):
            self.ui.gi.stop()
            self.ui.gif.clear()
            self.ui.footer_label.hide()
            self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        # if(hasattr(self.ui,'Dspeak')):
        #     self.ui.Dspeak.clear()
            


    def animation(self):
        self.ui.gi=QMovie("D:/ankush/projects/virtual_assistant/desktop assitant ui/gifloader.gif")
        self.ui.gi.setCacheMode(QMovie.CacheAll)
        self.ui.gif.setMovie(self.ui.gi)
        self.ui.gi.start() 
        self.ui.footer_label.show()
        self.ui.footer_label.setText("  Listening... & Computing...")
        self.ui.Dspeak=mainT()
        self.ui.Dspeak.start()
        



counter=0
count=0

class SplashScreen2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

       

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)
        

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO Virtual Assistant")

        # Change Texts
        
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        # wish_me()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global count

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(count)

        # CLOSE SPLASH SCREE AND OPEN APP
        if count > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            wish_me()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        count += 1

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO Virtual Assistant")

        # Change Texts
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> Login Page"))
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = LoginWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


class takeinput(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_takeinput()
        self.ui.setupUi(self)

        # Remove window tlttle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.ui.show()
        global address
        address=self.ui.input.text()
        self.ui.enter_btn.clicked.connect(lambda:self.close())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
