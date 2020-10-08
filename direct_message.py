import open_instagram
import send_dm
import time
import pyperclip


def input_message(message):
    # クリップボードにmessageをコピー。
    pyperclip.copy(message)


def direct_message(name, message):
    # 相手のインスタアカウントページに飛び、DMを送信。
    # タイポによる別アカウントへの誤送信は少ないと考えられる。
    # send_dmよりも早い。
    open_instagram.instagram_account(name)
    # nameのインスタアカウントページへ。
    time.sleep(5)
    send_dm.type_tab()
    time.sleep(1)
    send_dm.type_enter()
    # DM画面へ遷移。
    time.sleep(3)
    input_message(message)
    time.sleep(1)
    send_dm.ctrl_v()
    # messageをコピペして送信画面に入力。
    time.sleep(1)
    send_dm.type_enter()
    # 確定
    time.sleep(1)
    send_dm.type_enter()
    # 送信
    time.sleep(1)
    send_dm.close_tab()
    # ブラウザのタブを閉じる


if __name__ == '__main__':
    direct_message("test_code01", "日本語入力のテスト\n改行のテスト")
