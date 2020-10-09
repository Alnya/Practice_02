import pyautogui
import time
import open_instagram
import pyperclip


def type_string(message):
    # messageをキーボードから入力
    pyautogui.typewrite(message)


def type_tab():
    # tab
    pyautogui.press("\t")


def type_enter():
    # enter
    pyautogui.press("enter")


def close_tab():
    # ctrl + w
    pyautogui.hotkey("ctrl", "w")


def ctrl_v():
    # ctrl + v
    pyautogui.hotkey("ctrl", "v")


def shift_tab():
    # 検索した後決定までのプロセス
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
    # 自分のインスタアカウントページを開いた後、DM検索画面にてnameのアカウントを検索し、messageを送信する
    open_instagram.open_instagram()
    time.sleep(5)
    pyperclip.copy(name)
    ctrl_v()
    time.sleep(3)
    type_tab()
    time.sleep(0.1)
    type_enter()
    time.sleep(2)
    shift_tab()
    type_enter()
    time.sleep(3)
    pyperclip.copy(message)
    ctrl_v()
    time.sleep(1)
    type_enter()
    time.sleep(1)
    close_tab()


if __name__ == '__main__':
    # 動作確認として、test_code01へtest_send_messageを送る
    main("test_code01", "test_send_message")
