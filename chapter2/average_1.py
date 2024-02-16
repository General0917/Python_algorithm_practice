subject = ["国語", "数学", "英語", "理科", "社会"] # 各教科を配列で定義
score = [70, 98, 92, 88, 64] # 各教科の点数を配列で定義
total = 0 # 合計点を格納する変数を定義

for i in range(len(score)): # 繰り返しiは0から4まで5回(range(len(score))で5回)繰り返す
    print(subject[i], "の点数:", score[i]) # 各教科名と点数を出力する
    total += score[i] # totalにscore[i]の値を代入する

average = total / len(score) # 平均点を求める

print("合計点:", total) # 合計点を出力
print("平均値:", average) # 平均点を出力