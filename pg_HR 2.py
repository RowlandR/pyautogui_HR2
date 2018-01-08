import pyautogui as pg
import time
pg.typewrite('Intiating Protocal',.1)
pg.pause = 2.5
pg.moveTo(107,750,0)
pg.click(107,750)
pg.typewrite('chrome\n',.1)
pg.hotkey('Enter')
pg.hotkey('winleft','up')
pg.typewrite('Netflix',.1)
pg.hotkey('Enter')
time.sleep(2)
if url !== "https://www.netflix.com/browse":
    pg.hotkey('tab')
    pg.hotkey('tab')
    time.sleep(1)
    pg.hotkey('enter')
    time.sleep(2)
    pg.hotkey('tab')
    pg.typewrite('public1@greenwichbio.com',.1)
    pg.hotkey('tab')
    pw = pg.password('Enter Password Below','Netflix Password Box','','*')
    pg.typewrite(pw,.1)
    pw = ""
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('enter')




###pg.password('Enter Password Here','Password Box'','*')###

###pg.hotkey('winleft','ctrl','d')###
