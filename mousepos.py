import pyperclip
import pyautogui
import time
import psutil
import os
import keyboard 
c=0
try:    
    while True:
        x=pyautogui.position()
        print (x)
       
except KeyboardInterrupt:
    print('\nDone.')
