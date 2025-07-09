import time
from pynput.keyboard import Controller

def espam():
    keyboard = Controller()  # Create controller instance
    while True:
        time.sleep(0.01)
        keyboard.press('e')
        time.sleep(0.01)
        keyboard.release('e')

input('Press Enter to start (you have 5 seconds to switch windows): ')
time.sleep(5)
espam()
