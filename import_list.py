from settings import get_import_list_path


def import_list():
    # 指定したパスのテキストファイルを取得し、UTF-8でエンコードして3*30の二次元リストを作成し、返却する
    path = get_import_list_path()
    with open(path, encoding="UTF-8") as file:
        s = file.read()
    entry_list = [[list(s.split(","))[j * 3 + i] for i in range(3)] for j in range(30)]
    return entry_list


if __name__ == '__main__':
    print(import_list())
