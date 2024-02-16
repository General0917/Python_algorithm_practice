subject = ["国語", "数学", "英語", "理科", "社会"] # subjectという配列を宣言し、文字列を代入
score = [80, 100, 92, 96, 74] # scoreという配列を宣言し、数値を代入
total = 0 # totalという変数に0を代入

for i in range(5): # 繰り返しiは0から4まで5回繰り返す
    print(subject[i], "の点数は", score[i]) # subject、scoreの各要素の値を出力
    total += score[i] # totalにscore[i]の値を加える

print("合計点は", total) # 計算した合計点を出力