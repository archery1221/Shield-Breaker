import time
import pyautogui
import threading
from pynput import keyboard

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

def a1():
#DEĞİŞTİRİLECEK SATIRLAR
    pyautogui.press('1')#<--- Balta Tuşunuz
    pyautogui.click(button='left')
    time.sleep(0.06)
    pyautogui.press('3')#<--- Kılıç Tuşunuz
#DEĞİŞTİRİLECEK SATIRLAR
def a2(key):
    try:
        if getattr(key, 'char', None) == 'r' or getattr(key, 'vk', None) == 0x52:
            threading.Thread(target=a1, daemon=True).start()
    except:
        pass

with keyboard.Listener(on_press=a2) as listener:
    listener.join()
