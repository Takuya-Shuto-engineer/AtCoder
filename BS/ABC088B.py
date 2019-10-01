_n = int(input()) # カードの枚数
_cards = list(map(int, input().split(" "))) # カードリスト
 
_alice = 0 # アリスの得点
_bob = 0 # ボブの得点
_cards.sort(reverse = True) # 最高効率でカードを引くため，カードを降順にソートして先頭から取得
 
for _i, _card in enumerate(_cards):
  # アリスとボブが交互にカードを引く
  if _i % 2 == 0:
    _alice = _alice + _card
  else:
    _bob = _bob + _card
 
print(_alice - _bob) # アリスがどれくらいボブに差をつけたのか
