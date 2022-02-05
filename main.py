"""
Can't handle # sometimes
"""

import pyautogui
import time
spaces = 0
delay_speed = 0.1

def tabbing_mech(line):
    global spaces
    count_space = 0
    for char in line:
        if char ==" ":
            count_space +=1
        else: break
    print(count_space,spaces,line)

    if spaces > count_space:
        back_tab = (spaces - count_space) // 4
        spaces = count_space
        print("tab back")
        for i in range(back_tab):
            pyautogui.keyDown('shift')
            pyautogui.press('tab')
            pyautogui.keyUp('shift')
        return line.replace("  ","")
    elif count_space == 0:
        return line
    elif spaces == count_space:
        return line.replace("  ","")
    elif spaces < count_space:
        print("indenting")
        spaces = count_space
        return line.replace("  ","")


for i in range(3):
    time.sleep(1)
    print(i)

with open("code", 'r') as f:
    for lines in f:
            tabbed_lines = tabbing_mech(lines)
            pyautogui.typewrite(tabbed_lines,delay_speed)
