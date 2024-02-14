def posi_naga_zero(val): # posi_naga_zero()という関数を定義する
    if val > 0: # 引数valの値が0より大きいなら
        print(val, "は正の数である。") #「valは正の数である。」と出力
    elif val < 0: # そうでなく、valは0より小さいなら
        print(val, "は負の数である。") #「valは負の数である。」と出力
    else: # いずれでもなければ
        print(val, "はゼロである。") #「valはゼロである。」と出力

posi_naga_zero(-5) # 引数を与えて関数を呼び出す
posi_naga_zero(0.8) # 引数を与えて関数を呼び出す
posi_naga_zero(0) # 引数を与えて関数を呼び出す