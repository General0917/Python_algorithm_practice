def volume_sphere(r): # volume_sphere()という関数を定義する
    v = 4 * 3.14 * r**3 / 3 # 引数rの値から球の体積を計算しvに代入
    return v # vの値を返す

vs = volume_sphere(10) # 関数で計算した半径10の球の体積をvsに代入

print("半径10cmの球の体積は", vs, "cm3") # print()で球の体積を出力
print("半径20cmの球の体積は", volume_sphere(20), "cm3") # print()の引数にvolume_sphere()を記述し、半径20の球の体積を出力