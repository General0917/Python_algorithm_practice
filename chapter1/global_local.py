total = 0 # totalという変数を宣言し初期値0を代入
def test_func(): # test_func()という関数を定義する
    global total # totalをグローバル変数として扱うと宣言
    loops = 20 # loopsという変数に20を代入
    for i in range(loops): # for文でloops回、繰り返す
        total += 10 # totalの値に10足し、totalに代入

print("totalの初期値", total) # totalの初期値を出力
test_func() # test_func()を呼び出す
print("関数実行後のtotalの値", total) # 関数実行後のtotalの値を出力