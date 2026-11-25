import pyautogui as p
import win32api, win32con
import keyboard
import time
import random
b1=-932
b2=-894
b3=-814
b4=-770
y1=346
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.125)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q")==False:
    if p.pixel(b1,y1)[0]==0:
        click(b1,y1)
    if p.pixel(b2,y1)[0]==0:
            click(b2,y1)    
    if p.pixel(b3,y1)[0]==0:
            click(b3,y1)
    if p.pixel(b4,y1)[0]==0:
            click(b4,y1)
#while True==True?
#    p.displayMousePosition()