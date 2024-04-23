import speech_recognition as sr
from requests import get
import pyttsx3
import cv2
import smtplib
import pyautogui
import webbrowser
import wikipedia
import os
import sys
import datetime
import random


#Text to speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#txt to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#speech to txt
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            return "None"
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "None"


#Wishing the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Jarvis at your service. Please tell me how can I help you today?")

#set brave as default browser


#main function
if __name__ == "__main__":
    #set brave as default browser
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))

    wishMe()
    while True:
        query = takeCommand().lower()
    
    #Defining System tasks

        #open notepad
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        
        #open cmd
        elif "open command prompt" in query:
            os.system("start cmd")

        #open webcam
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        
        #play music
        elif "play music" in query:
            music_dir = "C:\\Users\PMLS\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
        
    #Defining Online tasks

        #open wikipedia
        elif 'open wikipedia' in query:
            speak("What do you want me to search Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #open google   
        elif 'open google' in query:
            speak("What do you want me to search on google?")
            search = takeCommand().lower()
            webbrowser.get('brave').open(f"https://www.google.com/search?q={search}")
             
        #Find IP address
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is: {ip}")

        #open youtube
        elif 'open youtube' in query:
            #for brave browser
            webbrowser.get('brave').open("youtube.com")

            #for default browser
            #webbrowser.open("youtube.com")
        
        #Play song on youtube
        elif 'play song on youtube' in query:
            speak("What song do you want me to play?")
            song = takeCommand()
            #for brave browser
            webbrowser.get('brave').open(f"https://www.youtube.com/results?search_query={song}")

            #for default browser
            #webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        
        #open stackoverflow
        elif 'open stackoverflow' in query:
            #for brave browser
            webbrowser.get('brave').open("stackoverflow.com")

            #for default browser
            #webbrowser.open("stackoverflow.com")
        
        #open github
        elif 'open github' in query:
            #for brave browser
            webbrowser.get('brave').open("github.com")
            
            #for default browser
            #webbrowser.open("github.com")
        
        #open facebook
        elif 'open facebook' in query:
            #for brave browser
            webbrowser.get('brave').open("facebook.com")

            #for default browser
            #webbrowser.open("facebook.com")

        #open instagram
        elif 'open instagram' in query:
            #for brave browser
            webbrowser.get('brave').open("instagram.com")

            #for default browser
            #webbrowser.open("instagram.com")

        #open twitter
        elif 'open twitter' in query:
            #for brave browser
            webbrowser.get('brave').open("twitter.com")

            #for default browser
            #webbrowser.open("twitter.com")
        
        #open linkedin
        elif 'open linkedin' in query:
            #for brave browser
            webbrowser.get('brave').open("linkedin.com")

            #for default browser
            #webbrowser.open("linkedin.com")
        
        #open whatsapp
        elif 'open whatsapp' in query:
            #for brave browser
            webbrowser.get('brave').open("web.whatsapp.com")

            #for default browser
            #webbrowser.open("web.whatsapp.com")

        if 'exit' in query:
            speak("Thanks for using me. Have a good day!")
            sys.exit()
        
