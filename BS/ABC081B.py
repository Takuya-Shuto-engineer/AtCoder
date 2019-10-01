_n = int(input()) # 系列長
_list = list(map(int, input().split())) # 数字のリスト
_count = 0 # 行動回数
 
def div(num): # mapに渡すための割り算
  return num / 2
 
def mod(num): # mapに渡すための余り計算
  return num % 2
 
while True:
  _mod_list = list(map(mod, _list)) # 2で割った余りを計算する
  if 1 in _mod_list: # 奇数があったら終了
    break
  _list = list(map(div, _list)) # 全て偶数なら2で割る
  _count = _count + 1
print(_count)
