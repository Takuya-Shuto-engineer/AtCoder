_a, _b = map(int, input().split())
_common_divisors = []
_min = min([_a, _b])

def euclid(a, b):
  _mod = a % b
  if _mod == 0:
    return b
  else:
    return euclid(b, _mod)

for _i in range(_min):
  _num = _i + 1
  if _a % _num == 0 and _b % _num == 0:
    _common_divisors.append(_num)
    
print(" ".join(map(str, _common_divisors)))
"""
_count = 0
for _i in range(len(_common_divisors) - 1):
  for _j in range(len(_common_divisors) - (_i + 1) ):
    _k = _j + 1
    _max = max([_common_divisors[_i], _common_divisors[_i + _k]])
    _min = min([_common_divisors[_i], _common_divisors[_i + _k]])
    _max_divisor = euclid(_max, _min)
    if _max_divisor == 1:
      _count = _count + 1
print(_count)
"""