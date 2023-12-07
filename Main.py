#all modules
import pyttsx3 
import speech_recognition as sr
from websearch import *
from openApps import *
from playSpotify import *
import random,datetime

#Speaking Function
def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    print("")
    print(f"==> MY AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

#Greetings of Time
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    elif hour>18 and hour<20:
        speak("Good Evening !")
    else:
        speak("Good Night !")
    speak("How Can I Assist You Sir ?")

#Speech recognition
def speechrecognizer():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,0,5)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language="en")
            return query.lower()
        except:
            return ""
#Main function
def mainexecute(query):
    randomn=random.randint(0,25)
    Query=str(query).lower()
    print("")
    print(f"==> Prince : {query}")

    #Basic Greetings with AI
    if "hello" in Query:
        speak("Hello Sir , How Are You ?")
    elif "i am fine" in Query:
        speak("Happy To Hear That Sir !")
    elif "bye" in Query or "go to sleep" in Query:
        speak("Have A Good Day!")
        exit()
    elif "how are you?" in Query:
        speak("I am As Fine As You Sir !")
    elif "Thank You" in Query:
        speak("It's My Pleasure !")
    
    # Main Tasks
    elif "time" in Query:
        import time
        t=time.strftime("%I:%M:%S")
        speak(f"Time is : {t}")
    
    #Applications Tasks
    elif "open" in Query:
        openApp(Query)
    elif "close" in Query:
        closeApp(Query)
    #Web Related Tasks
    elif "google" in Query:
        onGoogle(Query)
    elif "youtube" in Query:
        onYouTube(Query)
    elif "wikipedia" in Query:
        onWikipedia(Query)
    elif "weather" in Query:
        getWeather(Query)


    #OS related Tasks
    elif "play song" in Query:
        openSpotify()
    elif "in spotify" in Query:
        playspotify(Query)        
    elif "next song" in Query:
        nextSong()         
    elif "last song" in Query:
        lastSong()
    elif "pause song" in Query:
        pauseSong()
    elif "resume song" in Query:
        resumeSong()
                                                           
    # elif "play music" in Query:
    #     music_dir='C:\\Users\\Admin\\Music\\'
    #     songs=os.listdir(music_dir)
    #     os.startfile(os.path.join(music_dir,songs[randomn]))
    # elif "next song" in Query:
    #     music_dir='C:\\Users\\Admin\\Music\\'
    #     songs=os.listdir(music_dir)
    #     os.startfile(os.path.join(music_dir,songs[randomn+1]))
    # elif "previous song" in Query:
    #     music_dir='C:\\Users\\Admin\\Music\\'
    #     songs=os.listdir(music_dir)
    #     randomn=random.randint(0,25)
    #     os.startfile(os.path.join(music_dir,songs[randomn-1]))

#calling 
wish()
while True:
    query=speechrecognizer()
    mainexecute(query)