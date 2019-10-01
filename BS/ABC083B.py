_n, _a, _b = map(int, input().split(" ")) # _n: 1以上N以下のN, _a: A以上のA, _b: B以下のB
 
_total = 0 # 10進法での各桁の和がA以上B以下であるものの総和
for _i in range(_n):
  _num = str(_i + 1) # 各桁を参照するためにstrに変換
  _len = len(_num) # 長さを受け取る
  _sum = 0 # 各桁の総和
  for _j in range(_len):
    _sum = _sum + int(_num[_j])
  if _a <= _sum <= _b:
    _total = _total + int(_num)
 
print(_total)