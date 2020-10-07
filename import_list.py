def import_list():
    path = "c:\\morinaga\\entrylist\\test.txt"
    with open(path, encoding="UTF-8") as file:
        s = file.read()
    entry_list = [[list(s.split(","))[j * 3 + i] for i in range(3)] for j in range(30)]
    return entry_list


if __name__ == '__main__':
    print(import_list())
