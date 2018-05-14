#Helps people feel happy

import pyautogui as pg
import webbrowser
import time

mood = pg.prompt(
"""
How do you want to feel?
a) happy
c) angry
d) scared

"""
    )
if mood == "a":
    video = pg.prompt(
    """
    How Funny?
    a)Kinda Funny
    b)Funny
    c)Very Funny
    """
        )
elif mood == "c":
    video = pg.prompt(
    """
    How Angry?
    a)Kinda Angry
    b)Angry
    c)Very Angry
    """
        )
elif mood == "d":
    video = pg.prompt(
    """
    How Scary?
    a)Kinda Scary
    b)Scary
    c)Very Scary
    """
        )

if mood == "a" and video == "a":
    webbrowser.open("https://www.youtube.com/watch?v=11quU3nqkVE")
if mood == "a" and video == "b":
    webbrowser.open("https://www.youtube.com/watch?v=zjPwjNLETPA")
if mood == "a" and video == "c":
    webbrowser.open("https://www.youtube.com/watch?v=kVJSMRy1cBg")
if mood == "c" and video == "a":
    webbrowser.open("https://www.mememaker.net/template/scary-bilbo-still-scary")
if mood == "c" and video == "b":
    webbrowser.open("https://www.mememaker.net/template/scary-bilbo-still-scary")
if mood == "c" and video == "c":
    webbrowser.open("https://www.mememaker.net/template/scary-bilbo-still-scary")
if mood == "d" and video == "a":
    webbrowser.open("https://www.youtube.com/watch?v=cdg193GvnBA")
if mood == "d" and video == "b":
    webbrowser.open("https://www.youtube.com/watch?v=YhSPDqqgO3Y")
if mood == "d" and video == "c":
    webbrowser.open("https://www.youtube.com/watch?v=hY7dQnVnqmQ")









