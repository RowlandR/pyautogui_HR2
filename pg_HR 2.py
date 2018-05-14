import pyautogui as pg
import time
pg.typewrite('Intiating Protocal',.1)
pg.pause = 2.5
pg.hotkey('winleft','ctrl','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.1)
pg.hotkey('Enter')
time.sleep(2)
pg.hotkey('winleft','up')
pg.typewrite('Netflix',.1)
pg.hotkey('Enter')

time.sleep(2)
pg.hotkey('tab')
pg.hotkey('tab')
time.sleep(1)
pg.hotkey('enter')
time.sleep(2)
pg.hotkey('tab')
pf = pg.username('Enter Username below','Netflix Username Box','','*')
pg.typewrite(pf,.1)
pf = ""
pg.hotkey('tab')
pw = pg.password('Enter Password Below','Netflix Password Box','','*')
pg.typewrite(pw,.1)
pw = ""
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('enter')




###pg.password('Enter Password Here','Password Box'','*')###

###pg.hotkey('winleft','ctrl','d')###
