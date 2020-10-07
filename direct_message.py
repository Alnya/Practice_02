import open_instagram
import send_dm
import time
import pyperclip


def input_message(message):
    pyperclip.copy(message)


def direct_message(name, message):
    open_instagram.instagram_account(name)
    time.sleep(5)
    send_dm.type_tab()
    time.sleep(1)
    send_dm.type_enter()
    time.sleep(3)
    input_message(message)
    time.sleep(1)
    send_dm.ctrl_v()
    time.sleep(1)
    send_dm.type_enter()
    time.sleep(1)
    send_dm.type_enter()
    time.sleep(1)
    send_dm.close_tab()


if __name__ == '__main__':
    direct_message("test_code01", "日本語入力のテスト\n改行のテスト")
