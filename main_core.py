def set_up():
    help()
    # グローバル変数化
    global i, maru, batu, batu_lists, num
    i = input("練習したい文字を入力してください : ")
    print(f"{i} を設定しました")

    maru = batu = num = 0
    batu_lists = []


def end():
    # round(x,1) : 小数第2位を四捨五入
    print(
        f"終了します\n正解数 : {maru}\n不正解数 : {batu}\n正解率 : {round((maru/(maru+batu))*100,1)} %\n間違い集 : {batu_lists}")


def help():
    print(f"-end (-e): 終了します\n-next (-n): 練習したい文字を入力してください\n-help (-h): この画面を表示します")


set_up()

while True:
    num += 1
    x = input(f"{num} 回目 : {i} と入力してください : ")
    if i == x:
        print("〇")
        maru += 1

    elif x == "-end" or x == "-e":
        end()
        break
    elif x == "-next" or x == "-n":
        end()
        set_up()

    elif x == "-help" or x == "-h":
        help()
        num -= 1

    else:
        batu_lists.append(x)
        print(f"✕: {x}")
        batu += 1
