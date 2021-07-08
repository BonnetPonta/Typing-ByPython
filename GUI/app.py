import tkinter
from json import load
from random import choice
from sys import exit

# random : 1 |or| low : 2
SORT = 1
# length 1..
LENGTH = 5
# debug True |or| False
DEBUG_MODE = True


# 文字表示GUI
tki = tkinter.Tk()
tki.title("Typing GUI Ver.1.1")
tki.geometry("800x400+400+150")
lbl = [None]*3
for i in range(len(lbl)):
    lbl[i] = tkinter.Label(font=("Times New Roman", 80))
    lbl[i].pack()

with open(r"Japanese.json", "r", encoding="utf-8_sig") as f:
    json_load = load(f)
    # ValueError: too many values to unpack (expected 2) エラーがでたため、zip()でなく個別に格納
    words_en = [word_en for word_en in json_load.keys()]
    words_jp = [word_jp for word_jp in json_load.values()]

# ランダムな文字列 -> タイピング -> ローマ字をひらがなに変換
key = ""  # タイプした文字取得
ans = []  # こたえ
indx = []  # こたえのインデックス番号
typingWords = []  # 現在タイプしてるローマ字記憶
typedWords = ""  # typingWordsを連結
Words_en1 = []  # words_en[indx]
Words_en2 = ""  # Words_en1を連結
low_cnt = 0  # 順次モードの時のインデックス番号
clear_cnt = 0  # 正解数


def key_down(e):  # typeイベントハンドラー
    global key, typingWords, clear_cnt
    key = e.keysym
    if key == "BackSpace":
        try:  # typingWordsに何もないときに削除した際のエラー回避
            typingWords.pop(-1)
        except:
            pass
    else:
        if DEBUG_MODE:
            print(f"typingWords: {typingWords}")
            print(f"key: {key}")
        typingWords.append(key)
    typedWords = "".join(typingWords)
    Words_en1 = [words_en[i] for i in indx]
    Words_en2 = "".join(Words_en1)
    try:
        if DEBUG_MODE:
            print(f"{ans} // {Words_en2}  // {typedWords} // {typingWords}")
    except:
        pass
    if str(Words_en2) == str(typedWords):
        if DEBUG_MODE:
            print("正解！！")
        clear_cnt += LENGTH
        lbl[2]["text"] = f"正解数: {clear_cnt}"
        update_display()


tki.bind("<KeyPress>", key_down)


def update_display():  # random表示
    global ans, indx, typingWords, low_cnt
    typingWords = []
    ans = []
    indx = []
    if not 0 <= LENGTH:  # 1以上の数字かつ整数か
        print(f"\n\nLENGTH を1以上の整数に設定してください。\n現在設定値: {LENGTH}\n終了します。")
        exit()
    for _ in range(LENGTH):
        if SORT == 1:  # random
            w = choice(words_jp)
            ans.append(w)
            indx.append(words_jp.index(w))
        elif SORT == 2:  # 順次
            print(f"{len(words_jp)} // {low_cnt}")
            ans.append(words_jp[low_cnt])
            indx.append(low_cnt)
            low_cnt += 1
            if len(words_jp) == low_cnt:  # １通り表示したらリセット
                low_cnt = 0
    lbl[0]["text"] = "".join(ans)


def press_display():  # typed
    lbl[1]["text"] = typingWords
    tki.after(100, press_display)


press_display()
update_display()
tki.mainloop()
