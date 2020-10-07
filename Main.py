import direct_message
import send_dm
import entry_list
import import_list


def search_dm(name, message):
    send_dm.main(name, message)


def direct_send(name, message):
    direct_message.direct_message(name, message)


def main():
    entry_list.main()
    en_ls = import_list.import_list()
    for i in range(len(en_ls)):
        if en_ls[i][1] == "":
            break
        else:
            message = str(en_ls[i][0]) + " : " + str(en_ls[i][1])
            direct_send(en_ls[i][2], message)
            print(f"{en_ls[i][1]} is completed.")
    print("all complete!")


if __name__ == '__main__':
    main()
