import webbrowser
from settings import get_direct_message_path


def open_instagram():
    # 自分のインスタグラムアカウントからDM検索の画面を開く
    webbrowser.open("https://www.instagram.com/direct/new/")


def instagram_account(name):
    # nameのアカウントページを開く
    address = "https://www.instagram.com/" + str(name) + "/"
    webbrowser.open(address)


if __name__ == "__main__":
    # 動作確認として、テストアカウントページへ遷移
    instagram_account(get_direct_message_path())
    # open_instagram()
