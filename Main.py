import open_instagram
import send_dm
import time

# instagram_name = input("Tell me instagram name of the participant.\n->")
instagram_name = "momose_0202"

open_instagram.open_instagram()
time.sleep(3)
send_dm.type_string(instagram_name)
time.sleep(1)
send_dm.type_tab()
time.sleep(0.1)
send_dm.type_enter()
time.sleep(0.5)
send_dm.type_tab()
time.sleep(0.1)
send_dm.type_tab()
time.sleep(0.1)
send_dm.type_tab()
time.sleep(0.1)
send_dm.type_tab()
time.sleep(0.1)
send_dm.type_enter()
time.sleep(1)
send_dm.type_string("Test mail")
send_dm.type_enter()
