import direct_message
import send_dm
import entry_list
import import_list


def search_dm(name, message):
    # 自身のインスタグラムアカウントのDM検索欄を開き、相手のアカウント名を検索してDMを送信。
    # グループを作ってメッセージを送信するならばこちらの方が適している。
    send_dm.main(name, message)


def direct_send(name, message):
    # 相手のインスタアカウントページに飛び、DMを送信。
    # タイポによる別アカウントへの誤送信は少ないと考えられる。
    # search_dmよりも早い。
    direct_message.direct_message(name, message)


def main():
    entry_list.main()
    # Google Spread SheetからGoogle Driveへ出力したテキストファイルをCドライブへ取得
    en_ls = import_list.import_list()
    # Cドライブへダウンロードした最新のテキストファイルをインポート、二次元リストへ(3*30)
    for i in range(len(en_ls)):
        if en_ls[i][1] == "":
            # 参加者がいなくなった時点でbreak
            break
        else:
            message = str(en_ls[i][0]) + " : " + str(en_ls[i][1])
            # {エントリーナンバー} : {参加者名}　の形でmessageへ代入
            direct_send(en_ls[i][2], message)
            # ブラウザから相手のインスタアカウントへmessageを送信
            print(f"{en_ls[i][0]}:{en_ls[i][1]} is completed.")
            # 無事に送信できたかどうかにかかわらず、出力。参加人数分このメッセージが出力される。
    print("All completed!")
    # 参加人数分送信したことを便宜的に出力。


if __name__ == '__main__':
    main()
