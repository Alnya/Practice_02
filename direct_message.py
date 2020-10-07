import open_instagram
import send_dm
import time


def direct_message(x, message):
    open_instagram.instagram_account(x)
    time.sleep(5)
    send_dm.type_tab()
    time.sleep(1)
    send_dm.type_enter()
    time.sleep(2)
    send_dm.type_string(message)
    time.sleep(1)
    send_dm.type_enter()
    time.sleep(1)
    send_dm.type_enter()
    time.sleep(1)
    send_dm.close_tab()


if __name__ == '__main__':
    direct_message("test_code01", "tesuto \naaa")
