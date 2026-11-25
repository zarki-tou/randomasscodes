from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
a=-1
time.sleep(0.5)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (255, 219, 195)
#(-969, 296) ec
#(-369, 296) dc
#(-368, 710) db
#(-969, 712) eb
while keyboard.is_pressed('space') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(0,0, 1360, 768))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if  r == 255 and g == 255 and b == 255:
                flag = 1
                a+=1
                click(480,725)
                pyautogui.typewrite(str(a*5))
                keyboard.press_and_release('enter')
                time.sleep(5)
                break

        if flag == 1:
            break