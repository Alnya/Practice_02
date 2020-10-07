import direct_message
import send_dm

'''
instagram_name = input("Tell me instagram name of the participant.\n>>>")
print()
message = input("Type messages you want to send.\n>>>")

open_instagram.open_instagram()
time.sleep(3)
send_dm.main(instagram_name, message)
'''


def search_dm(name, message):
    send_dm.main(name, message)


def direct_send(name, message):
    direct_message.direct_message(name, message)


def main():
    direct_send("test_code01", "test")


if __name__ == '__main__':
    main()
