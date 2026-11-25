import keyboard
import win32api
import time
import pyautogui
a=0
#pyautogui.displayMousePosition()
while keyboard.is_pressed('p')==False:    
    while keyboard.is_pressed('q')==True:
        a+=1
        print(f"{win32api.GetCursorPos()} quina {a}")
        time.sleep(0.5)
#470RGB 75, 73, 142 480 725qqqq
#(1044, 308) quina 1
#(1344, 308) quina 2qq
#(1342, 759) quina 3
#(1044, 759) quina 4