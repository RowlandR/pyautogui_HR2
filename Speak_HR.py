import win32com.client as wincl
import pyautogui as pg
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Tell me what video you are looking for")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")

try:
    words = r.recognize_google(audio)
    speak.Speak("Ok, let's look for " + r.recognize_google(audio))
    wb.open("https://www.google.com/search?q=" + words)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

"""
speak.Speak("Whats your favorite color")

answer = pg.prompt("Enter Your Favorite Color")

if answer == "orange":
    speak.Speak("My Favorite Color Is Orange Too")
elif answer == "blue":
    speak.Speak("Sure, lets go with that")
else:
    speak.Speak("You like the color " + answer)




speak.Speak("What kind of video should we watch?")

video = pg.prompt("Enter Video Below.")

speak.Speak("Ok, lets look for " + video + " on YouTube and see what we find")

wb.open("https://www.youtube.com/results?search_query=" + video)
"""
