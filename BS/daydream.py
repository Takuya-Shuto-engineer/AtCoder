_s = input()
_len = len(_s)

_answer = "YES"

while(_len != 0):
  if _len >= 7 and _s[0:7] == "dreamer" and _s[5:10] != "erase":
    _s = _s.replace("dreamer", "", 1)
  elif _len >= 6 and _s[0:6] == "eraser":
    _s = _s.replace("eraser", "", 1)
  elif _len >= 5 and _s[0:5] == "dream":
    _s = _s.replace("dream", "", 1)
  elif _len >= 5 and _s[0:5] == "erase":
    _s = _s.replace("erase", "", 1)
  else:
    _answer = "NO"
    break
  _len = len(_s)
print(_answer)