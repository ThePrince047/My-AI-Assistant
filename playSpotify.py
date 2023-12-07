import os,pyttsx3,time
import pyautogui as gui
import pydirectinput as pdi

def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    print("")
    print(f"==> MY AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def openSpotify():
    speak("Spotify Playing...")
    os.system(f"start {r"C:\Users\Admin\OneDrive\Desktop\Spotify.lnk"}")
    time.sleep(5) 
    gui.press('space')

def playspotify(query):  
    speak("Searching Your Song in Spotify...")
    os.system(f"start {r"C:\Users\Admin\OneDrive\Desktop\Spotify.lnk"}")
    time.sleep(5)                                    
    gui.hotkey('ctrl','l')
    query=query.replace("in spotify","")
    query=query.replace("song","")
    query=query.replace("play","")
    gui.write(query,interval=0.1)
    time.sleep(2)
    gui.press('enter')
    gui.press('tab',presses=4)
    time.sleep(1)
    gui.press('down')
    gui.press('up')
    tell="Playing "+query
    speak(tell)
    time.sleep(1.5)
    gui.press('enter')
    time.sleep(0.5)

def nextSong():
    speak("Playing Next Song...")
    os.system(f"start {r"C:\Users\Admin\OneDrive\Desktop\Spotify.lnk"}")
    time.sleep(1)
    gui.hotkey('ctrl','right')
    time.sleep(1)
    gui.hotkey('alt','tab')

def lastSong():
    speak("Playing Previous Song...")
    os.system(f"start {r"C:\Users\Admin\OneDrive\Desktop\Spotify.lnk"}")
    time.sleep(1)
    gui.hotkey('ctrl','left')
    gui.hotkey('ctrl','left')
    time.sleep(1)
    gui.hotkey('alt','tab')
    
def pauseSong():
    speak("Pausing Song...")
    os.system(f"start {r"C:\Users\Admin\OneDrive\Desktop\Spotify.lnk"}")
    time.sleep(1)
    gui.press('space')
    gui.hotkey('alt','tab')
    
def resumeSong():
    speak("Resuming Song...")
    os.system(f"start {r"C:\Users\Admin\OneDrive\Desktop\Spotify.lnk"}")
    time.sleep(1)
    gui.press('space')
    gui.hotkey('alt','tab')
