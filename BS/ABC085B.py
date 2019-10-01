_n = int(input()) # 餅の数
_rice_cakes = [] # 餅のリスト
while True:
  try:
    _rice_cakes.append(int(input())) # 入力が終わるまで受け取る
  except:
    break
 
_rice_cakes.sort(reverse = True) # 降順にソート
 
_min = _rice_cakes[0] # 仮の最小値を先頭から受け取る
_count = 1 # リスト先頭の一つが既に積んであるため，最初から1
 
for _i in range(_n):
  # 今先頭にあるものより小さければ積める
  if _rice_cakes[_i] < _min:
    _min = _rice_cakes[_i] # 仮の最小値を更新
    _count = _count + 1 # 段数を更新
    
print(_count)