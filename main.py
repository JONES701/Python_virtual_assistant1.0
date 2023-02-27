import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")

master="Yuvraj"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# Speak function will pronounce the string which is passed to it.
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will wish you as per current time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak("Good Morning Master"+master+"I am Jarvis. How may I help you?")

    elif hour>=12 and hour<16:
        speak("Good Afternoon"+master+"I am Jarvis. How may I help you?")
    
    else:
        speak("Good Evening"+master+"I am Jarvis. How may I help you?")

# This function will take command from microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

    try:
        print("Recognising..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please ")
        query=None

    return query

# this function is used for sending mail but now it is not possible
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server
    server.login('jon67es@gmail.com','thomasbilla')
    server.sendmail("vanshikha131619@gmail.com",to,content)
    server.close()

# Main program starts here !
speak("Initializing Jarvis...")
wishMe()

query=takeCommand()

# logic for executing tasks as per query

if 'wikipedia' in query.lower():
    speak('searching wikipedia...')
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    url='youtube.com'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    url='google.com'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open amazon' in query.lower():
    url='amazon.in'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir="D:\MUSIC\Mobile"
    songs=os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir,songs[0]))

elif 'the time' in query.lower():
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f" {master} the time is {strTime}")

elif 'open code' in query.lower():
    codePath="C:\\Users\\user\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    os.startfile(codePath)

elif 'email to vans' in query.lower():
    try:
        speak("What should I send")
        content=takeCommand()
        to="vanshikha131619@gmail.com"
        sendEmail(to,content)
        speak("Email has been sent successfully")
    except Exception as e:
        print(e)
