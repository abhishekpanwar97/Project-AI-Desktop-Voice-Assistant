import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine= pyttsx3.init('sapi5')
# sapi5 is a microsoft windows voice API
voices= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak( audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour >=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("I am Anne Montgomery Sir. Please tell me how may I help you")


def takeCommand():
    #It takes microphone input from the user and returns a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        #print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        #print("mmmmmm")
        #print(query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('from_to_send@gmail.com','password_my')
    server.sendmail('from_to_send@gmail.com',to,content)
    server.close()



if __name__ == '__main__':
    #speak("Fuck me as hard as you can")
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
    
    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2);
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir= 'D:\\Non Critical\\songs\\Favorite Songs2' #path to songs folder
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to abhishek' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "whom_to_send@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry ! Email can't be sent at the moment")
        elif 'quit' in query:
            exit()