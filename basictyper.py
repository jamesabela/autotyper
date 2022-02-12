"""
This is the simplest version for basic word processors
"""
import pyautogui
import time

delay_speed = 0.1 #Bigger number slower typing

for i in range(3): #Seconds before it starts typing
    time.sleep(1)
    print(i)

with open("code.txt", 'r') as f:
    for lines in f:
        type_me = lines
        pyautogui.typewrite(type_me, delay_speed)
