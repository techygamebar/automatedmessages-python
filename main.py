from sys import hash_info
import pyautogui
import time

time.sleep(5)

text = 'hello'
while True:
# for i in range(3):
    pyautogui.typewrite(text)
    time.sleep(1)
    pyautogui.press('enter')
