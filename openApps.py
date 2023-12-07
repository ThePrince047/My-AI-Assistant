import pyttsx3,os

dictapp = {"cmd":"cmd","paint":"paint","word":"winword",
           "excel":"excel","chrome":"chrome","vscode":"code",
           "powerpoint":"powerpnt","calculator":"calc","powershell":"powershell"
        }

def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    print("")
    print(f"==> MY AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def openApp(query):
    query = query.replace('open',"")
    speak("Launching {query}")
    keys=list(dictapp.keys())
    for app in keys:
        if app in query:
            os.system(f"start {dictapp[app]}")

def closeApp(query):
    query = query.replace('close',"")       
    speak("Closing {query}...")
    keys = list(dictapp.keys())
    for app in keys:
        if app in query:
            os.system(f"taskkill /f /im {dictapp[app]}.exe")

