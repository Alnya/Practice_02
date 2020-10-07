import pyautogui
import time
import open_instagram
import pyperclip


def type_string(x):
    pyautogui.typewrite(x)


def type_tab():
    pyautogui.press("\t")


def type_enter():
    pyautogui.press("enter")


def close_tab():
    pyautogui.hotkey("ctrl", "w")


def ctrl_v():
    pyautogui.hotkey("ctrl", "v")


def shift_tab():
    pyautogui.keyDown("shift")
    time.sleep(0.5)
    type_tab()
    time.sleep(0.1)
    type_tab()
    time.sleep(0.1)
    type_tab()
    time.sleep(0.1)
    pyautogui.keyUp("shift")


def main(name, message):
    open_instagram.open_instagram()
    time.sleep(5)
    pyperclip.copy(name)
    ctrl_v()
    time.sleep(2)
    type_tab()
    time.sleep(0.1)
    type_enter()
    time.sleep(2)
    shift_tab()
    type_enter()
    time.sleep(2)
    pyperclip.copy(message)
    ctrl_v()
    time.sleep(1)
    type_enter()
    time.sleep(1)
    close_tab()


if __name__ == '__main__':
    main("test_code01", "test_send_message")
