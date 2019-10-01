_s = input() # 文字列を取得
_len = len(_s) # 文字列長

_answer = "YES" # 仮にYESとする

while(_len != 0):
  # 先頭から見ていき一致していれば削除する
  if _len >= 7 and _s[0:7] == "dreamer" and _s[5:10] != "erase": # dreamereraseの場合だけ，dreamerを優先する
    _s = _s.replace("dreamer", "", 1)
  elif _len >= 6 and _s[0:6] == "eraser":
    _s = _s.replace("eraser", "", 1)
  elif _len >= 5 and _s[0:5] == "dream":
    _s = _s.replace("dream", "", 1)
  elif _len >= 5 and _s[0:5] == "erase":
    _s = _s.replace("erase", "", 1)
  # 何も当てはまらないなら答えはNO
  else:
    _answer = "NO"
    break
  _len = len(_s)
print(_answer)
