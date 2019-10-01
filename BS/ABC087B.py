_a = int(input()) # 500円玉の数
_b = int(input()) # 100円玉の数
_c = int(input()) # 50円玉の数
 
_x = int(input()) # 目標金額
_count = 0 # 目標金額を満たすパターンのカウント
 
for _i in range(_a + 1):
  for _j in range(_b + 1):
    for _k in range(_c + 1):
      # 全パターンを検証
      if _i*500 + _j*100 + _k*50 == _x:
        _count = _count + 1
 
print(_count)