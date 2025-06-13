from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
def w():
    keyboard.press('w')
    time.sleep(1)
    keyboard.release('w')
def s():
    keyboard.press('s')
    time.sleep(1)
    keyboard.release('s')
while 1 == 1:
    time.sleep(5)
    w()
    s()
