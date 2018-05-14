import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=zpWbXltP43o"]
music = ["https://www.youtube.com/watch?v=zjPwjNLETPA"]
answer = pg.prompt(
"""
Which would you like to do?
a) watch videos
b) listen to music

"""
    )

if answer == "a":
    for i in videos:
         webbrowser.open(i)
elif answer == "b":
    for i in music:
        webbrowser.open(i)
