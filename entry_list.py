import pyautogui
import time
import webbrowser
from settings import get_google_drive_path
from settings import get_entry_list_path


def open_entry_list():
    # Google Driveに保存されている、Google Spread Sheetから転記したテキストファイルをブラウザで開く
    webbrowser.open(get_google_drive_path())


def ctrl_s():
    # ctrl + s
    pyautogui.keyDown("ctrl")
    pyautogui.press("s")
    pyautogui.keyUp("ctrl")


def alt_s():
    # alt + s
    pyautogui.hotkey("alt", "s")


def tab():
    # tab
    pyautogui.press("\t")


def enter():
    # enter
    pyautogui.press("enter")


def string(message):
    # messageをキーボードから打つ
    pyautogui.typewrite(message)


def close_tab():
    # ctrl + w
    pyautogui.hotkey("ctrl", "w")


def yes():
    # y
    pyautogui.press("y")


def backspace():
    # backspace
    pyautogui.press("backspace")


def main():
    # entry_listをGoogle Driveから取得し、指定したCドライブ内のフォルダに指定した名前で保存
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
    string(get_entry_list_path())
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
