import pyautogui as gui
from time import sleep

phone = "1234567890"
split = [char for char in phone]
sleep(5)


def _dailer(no):
    sleep(2)
    button7location = gui.locateOnScreen(f'{no}.png', confidence=0.9)
    gui.click(button7location)


for x in split:
    print(x)
    _dailer(x)