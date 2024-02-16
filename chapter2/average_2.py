score = [70, 98, 92, 88, 64] # 各教科の点数を配列で定義
total = 0 # 合計点を格納する変数を定義

for i in score: # 繰り返しiには点数が1つずつ入る
    total = total + i # totalにiの値が加える

average = total / len(score) # 平均点を求める

print("合計点:", total) # 合計点を出力
print("平均値:", average) # 平均点を出力