import pyautogui
import time


def type_string(x):
    pyautogui.typewrite(x)


def type_tab():
    pyautogui.press("\t")


def type_enter():
    pyautogui.press("enter")


def close_tab():
    pyautogui.hotkey("ctrl", "w")


def main(name, message):
    type_string(name)
    time.sleep(2)
    type_tab()
    time.sleep(0.1)
    type_enter()
    time.sleep(0.5)
    type_tab()
    time.sleep(0.1)
    type_tab()
    time.sleep(0.1)
    type_tab()
    time.sleep(0.1)
    type_tab()
    time.sleep(0.1)
    type_enter()
    time.sleep(1)
    type_string(message)
    type_enter()
    time.sleep(0.1)
    close_tab()
