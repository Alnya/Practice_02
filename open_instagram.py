import webbrowser


def open_instagram():
    webbrowser.open("https://www.instagram.com/direct/new/")


def instagram_account(x):
    address = "https://www.instagram.com/" + str(x) + "/"
    webbrowser.open(address)


if __name__ == "__main__":
    instagram_account("test_code01")
    # open_instagram()
