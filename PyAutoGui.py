from pyautogui import *
from time import sleep

print(position())
sleep(3)

while(True):
    if (locateOnScreen('cust.png', region = (250, 540, 130, 20))) != None:
        press('space')
