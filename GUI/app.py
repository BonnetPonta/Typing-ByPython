import tkinter
from json import load
from random import choice

# random : 1 // low : 2
SORT = 1

with open(r"Japanese.json", "r", encoding="utf-8_sig") as f:
    json_load = load(f)
# ValueError: too many values to unpack (expected 2) エラーがでたため、zip()でなく個別に格納
words_en = [word_en for word_en in json_load.keys()]
words_jp = [word_jp for word_jp in json_load.values()]

# ランダムな文字列 -> タイピング -> ローマ字をひらがなに変換
key = ""  # タイプした文字取得
ans = ""  # こたえ
indx = ""  # こたえのインデックス番号
typingWords = []  # 現在タイプしてるローマ字記憶
typedWords = ""  # typingWordsを連結
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
        print(f"typingWords: {typingWords}")
        print(f"key: {key}")
        typingWords.append(key)
    typedWords = "".join(typingWords)
    try:
        print(f"{ans} // {words_en[indx]} // {typingWords} // {typedWords}")
    except:
        pass
    if str(words_en[indx]) == str(typedWords):
        print("正解！！")
        clear_cnt += 1
        lbl[2]["text"] = f"正解数: {clear_cnt}"
        update_display()


def update_display():  # random表示
    global ans, indx, typingWords, low_cnt
    typingWords = []
    if SORT == 1:  # random
        ans = choice(words_jp)
    elif SORT == 2:  # 順次
        try:  # リスト外、つまり1通り終えたら最初から
            ans = words_jp[low_cnt]
        except:
            low_cnt = 0
            ans = words_jp[low_cnt]
        low_cnt += 1
    indx = words_jp.index(ans)
    lbl[0]["text"] = ans


def press_display():  # typed
    lbl[1]["text"] = typingWords
    tki.after(100, press_display)


# 文字表示GUI
tki = tkinter.Tk()
tki.title("文字を入力してください")
tki.geometry("600x400+500+150")
tki.bind("<KeyPress>", key_down)
lbl = [None]*3
for i in range(len(lbl)):
    lbl[i] = tkinter.Label(font=("Times New Roman", 80))
    lbl[i].pack()

press_display()
update_display()
tki.mainloop()
