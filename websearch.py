import pywhatkit,pyttsx3
import wikipedia as  googleScrap
import webbrowser,requests
from bs4 import BeautifulSoup

def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    print("")
    print(f"==> MY AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()
    
def onGoogle(query):
    query=query.replace("search","")
    query=query.replace("on google","")
    try:
        speak("This is What I Found Sir...")
        pywhatkit.search(query)
    except:
        speak("Nothing Found Sir !")

def onYouTube(query):
    speak("This is What I Found Sir...")
    query=query.replace("search","")
    query=query.replace("youtube","")
    web="https://www.youtube.com/results?search_query="+query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done Sir !")

def onWikipedia(query):
    query=query.replace("wikipedia search","")
    query=query.replace("wikipedia","")
    result=googleScrap.summary(query,sentences=3)
    speak(result)

def getWeather(query):
    query=query.replace("what is","")
    search = query
    url = f"https://www.google.com/search?q={search}"
    req  = requests.get(url)
    data = BeautifulSoup(req.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current{search} is {temp}")

