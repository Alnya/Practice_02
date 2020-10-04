import open_instagram
import send_dm
import time

instagram_name = input("Tell me instagram name of the participant.\n>>>")
print()
message = input("Type messages you want to send.\n>>>")

open_instagram.open_instagram()
time.sleep(3)
send_dm.main(instagram_name, message)
