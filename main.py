from sys import hash_info
import pyautogui
import time

time.sleep(5)

text = 'hello'
while True:
    pyautogui.typewrite(text)
    time.sleep(1)
    pyautogui.press('enter')
