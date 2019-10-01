_a, _b = map(int, input().split(" ")) # 二つの整数を取得
if _a*_b%2 == 0: # 積の偶奇判定
  print("Even")
else:
  print("Odd")