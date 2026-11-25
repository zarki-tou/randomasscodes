import win32api,win32con
import time
import pyautogui
import keyboard
pic = pyautogui.screenshot(region=(1044,308, 1342, 759))
width, height = pic.size
flag=0
time.sleep(6)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.125)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('s')==False and keyboard.is_pressed('t')==False:
    while pyautogui.pixel(1047, 202)[0]==255 or pyautogui.pixel(1047,202)[0]==164:
        click(1047, 202)
    for x in range(0, width, 10):
                for y in range(0, height, 10):
        
                    r, g, b = pic.getpixel((x, y))
        
                    if  r==102 and g == 255 and b==102:
                        flag = 1
                        click(x+1044,y+308)
                        time.sleep(0.1)
                        continue
        
                if flag == 1:
                    continue
    else:
        click(244, 390) #clica no cookie
        time.sleep(0.0125)
    
    
#cookie (244, 390) rgb(196, 170, 125) cursor(1233, 350) rgb(160, 156, 144) upgrade(1047, 202) rgb(255, 253, 240)