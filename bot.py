from pyautogui import *
import pyautogui as py
import time
import keyboard
import random
import win32api, win32con


###X:  332 Y:  646 RGB: (159, 164, 231)
##X:  399 Y:  651 RGB: (253,  18,   1)
###X:  477 Y:  643 RGB: (156, 162, 230)
##X:  603 Y:  637 RGB: (168, 173, 232)
#game source link https://www.agame.com/game/magic-piano-tiles

def click_pixel_pixel(x,y):
    #set mouse position
    win32api.SetCursorPos((x,y))

    #left button of mouse is pressed or is down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
    
    time.sleep(0.01) #delay  release by 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)#left button of mouse is released or is up

pos_x = [332,399,477,603]#created x-cordinates as list keeping y -coordinate constant



while keyboard.is_pressed('q')==False:
    for num in pos_x:
         if py.pixel(num,400)[0]==0:
             click_pixel_pixel(num,400)

    # if py.pixel(399,400)[0]==0:
    #     click_pixel(399,400)
    # if py.pixel(477,400)[0]==0:
    #     click_pixel(477,400)
    # if py.pixel(603,400)[0]==0:
    #     click_pixel(603,400)
