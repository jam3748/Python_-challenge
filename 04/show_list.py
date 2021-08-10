def output_list(list):
    text = ""
    # enumerate()でインデックスを取得
    for index, value in enumerate(list):
        # 最後の要素でない場合
        if index != (len(list) - 1):
            text += "「" + str(value) + "」と"
        # 最後の要素の場合
        else:
            text += "「" + str(value) + "」です。"
    print("このリストの中身は" + text)
    
sample_list = ["山田", 100, "太郎", True]
output_list(sample_list)