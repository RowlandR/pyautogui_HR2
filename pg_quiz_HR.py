import pyautogui as pg
import time
import webbrowser

points = 0

# Question
answer = pg.prompt(
"""
Which would you rather do?
a)Are you a boy
b)Are you a girl
c)All of the above
"""
    )

# Give Points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question
answer = pg.prompt(
"""
Which would you rather do with your free time?
a)Binge Watch Netflix
b)Not do homework   :I
c)Binge watch Brushy Studios and Ender Slicer and then cry softly in your sleep
"""
    )

# Give Points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question
answer = pg.prompt(
"""
When it is ok to cry?
a)At the Grand Canyon
b)Getting hit by a school bus
c)Reading your report card realizing that you got 3 d's and a 4
"""
    )

# Give Points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question
answer1 = pg.prompt(
"""
Which would you rather play?
a)Fortnite
b)GTA V
c)Pokemon
d)Netflix
"""
    )

# Give Points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += -2

# Question
answer1 = pg.prompt(
"""
Which would you rather do on the weekend?
a)Hang out with friends
b)Binge and Game at the same time on Netflix and Xbox
c)All of the above
"""
    )

# Give Points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3





#END OF SURVEY

pg.alert("You are...")

#Melow Lawer
if points < 9:
    pg.alert("Cool Guy")
    webbrowser.open("https://i.pinimg.com/originals/1e/47/1c/1e471c0dcfa769b22b8f6439b91028d4.gif")

#Papi Dashiel
elif points >=9 and points < 12:
    pg.alert("Papi Beruchin")
    webbrowser.open("https://i.ytimg.com/vi/qyltybhSmjI/hqdefault.jpg")

#Something else
if points >= 12:
    pg.alert("???")
    webbrowser.open("http://i0.kym-cdn.com/photos/images/newsfeed/000/171/180/tumblr_lpycb2FGGZ1qg45tj.gif")
