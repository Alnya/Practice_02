import pyautogui


def type_string(x):
    pyautogui.typewrite(x)


def type_tab():
    pyautogui.press("\t")


def type_enter():
    pyautogui.press("enter")
