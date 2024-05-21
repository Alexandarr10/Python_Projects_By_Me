import pyautogui
import time

while True:
    pyautogui.moveRel(125, 0, duration=0.25)  # move right
    pyautogui.moveRel(0, 125, duration=0.25)  # move down
    pyautogui.moveRel(-125, 0, duration=0.25)  # move left
    pyautogui.moveRel(0, -125, duration=0.25)  # move up
    time.sleep(6)
