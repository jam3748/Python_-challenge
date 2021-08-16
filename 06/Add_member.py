# 読み込むファイルパス
file_path = './members.csv'

# IDを入力
print("IDを入力してください")
Id = input()

# 名前を入力
print("名前を入力してください")
name = input()

# 住所を入力
print("住所を入力してください")
adress = input()

# 電話番号を入力
print("電話番号を入力してください")
phone = input()

# 情報をリストに格納
info = [Id,name,adress,phone]

# 追記モードでファイルを開く
f = open(file_path, "a", encoding="UTF-8")

# ファイルに書き込む
for index, i in enumerate(info):
    if index != (len(info) - 1):
        f.write(i + ",")
    else:
        f.write(i + "\n")

# ファイルを閉じる
f.close()

# ファイルを開く
f = open(file_path, "r", encoding="UTF-8")

# ファイルを1行ごとのリストとして読み込む
lines = f.readlines()

# ファイルを閉じる
f.close()

# 各行を出力
for line in lines:
    print(line)
