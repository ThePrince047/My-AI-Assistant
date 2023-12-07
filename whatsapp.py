import pyttsx3
import pyautogui as gui
import os

def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    print("")
    print(f"==> MY AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()
