_n = int(input())
_list = list(map(int, input().split()))
_count = 0
 
def div(num):
  return num / 2
 
def mod(num):
  return num % 2
 
while True:
  _mod_list = list(map(mod, _list))
  if 1 in _mod_list:
    break
  _list = list(map(div, _list))
  _count = _count + 1
print(_count)
