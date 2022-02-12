"""
watch out for blank lines
watch out for using the word space at end of line
Please be careful which window this types into
"""

import pyautogui
import time

spaces = 0 
delay_speed = 0.1 #Bigger number slower typing


def tabbing_mech(line): #Needed for IDEs
    global spaces
    count_space = 0
    for char in line:
        if char == " ":
            count_space += 1
        else:
            break
    print(count_space, spaces, line)

    if spaces > count_space:
        back_tab = (spaces - count_space) // 4 #Number of spaces per indent
        spaces = count_space
        print("tab back")
        for i in range(back_tab):
            pyautogui.keyDown('shift')
            pyautogui.press('tab')
            pyautogui.keyUp('shift')
        return line.replace("  ", "")
    elif count_space == 0:
        return line
    elif spaces == count_space:
        return line.replace("  ", "")
    elif spaces < count_space:
        print("indenting")
        spaces = count_space
        return line.replace("  ", "")


for i in range(3): #Seconds before it starts typing
    time.sleep(1)
    print(i)

with open("code.txt", 'r') as f:
    for lines in f:
        #type_me = lines #Use this if on a word processor
        type_me = tabbing_mech(lines) #Used for IDEs
        pyautogui.typewrite(type_me, delay_speed)
