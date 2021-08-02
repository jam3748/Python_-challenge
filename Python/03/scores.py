# 辞書
scores = {
    "山田" : 90,
    "高橋" : 100,
    "山本" : 70,
    "田中" : 85,
    "坂本" : 55
}

# 変数初期化
total = 0

# 計算
for score in scores.values():
    total += score
ave =  total / len(scores)

# 1回目の表示
print("合計：" + str(total) + "点")
print("平均：" + str(ave)+ "点")

# 辞書に"中田"を追加
scores["中田"] = 95

# 計算
total += scores["中田"]
ave = total / len(scores)

# 2回目の表示
print("合計：" + str(total) + "点")
print("平均：" + str(ave)+ "点")
