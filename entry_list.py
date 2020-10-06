import pyautogui
import time
import webbrowser


def open_entry_list():
    webbrowser.open("https://drive.google.com/file/d/124ULL-5sQE89yTqmJyassTW9J5dkrxWV/view?usp=sharing")


def ctrl_s():
    pyautogui.keyDown("ctrl")
    pyautogui.press("s")
    pyautogui.keyUp("ctrl")


def alt_s():
    pyautogui.hotkey("alt", "s")


def tab():
    pyautogui.press("\t")


def enter():
    pyautogui.press("enter")


def string(x):
    pyautogui.typewrite(x)


def close_tab():
    pyautogui.hotkey("ctrl", "w")


def yes():
    pyautogui.press("y")


def backspace():
    pyautogui.press("backspace")


def main():
    open_entry_list()
    time.sleep(3)
    enter()
    time.sleep(3)
    ctrl_s()
    time.sleep(3)
    string("test.txt")
    time.sleep(0.5)
    for i in range(6):
        tab()
        time.sleep(0.2)
    enter()
    time.sleep(0.1)
    backspace()
    time.sleep(0.1)
    string("\\morinaga\\entrylist")
    time.sleep(0.1)
    enter()
    time.sleep(0.1)
    alt_s()
    time.sleep(0.3)
    yes()
    time.sleep(1)
    close_tab()


if __name__ == "__main__":
    main()
