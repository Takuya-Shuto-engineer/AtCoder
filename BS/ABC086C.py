_n = int(input()) # 計画リスト長
_coordinates = [[0, 0, 0]] # [時刻t, x座標, y座標]
while True:
  try:
    _coordinates.append(list(map(int, input().split()))) # 標準入力から旅行計画を取得
  except:
    break
_isPossible = 'Yes' # 出力形式に合わせてBooleanではなくstring
for _i in range(_n):
  _action_times = _coordinates[_i + 1][0] - _coordinates[_i][0] # 次の計画までの時刻，行動回数
  _diff_x = abs(_coordinates[_i + 1][1] - _coordinates[_i][1]) # 次の目的地までのx座標の差分
  _diff_y = abs(_coordinates[_i + 1][2] - _coordinates[_i][2]) # 次の目的地までのy座標の差分
  _minimum_action_times = _diff_x + _diff_y # 最低限必要な行動回数
  if _minimum_action_times > _action_times: 
    _isPossible = 'No' # 最低限必要な行動回数を確保できていない場合不可能
    break
  elif abs(_action_times - _minimum_action_times) % 2 != 0:
    _isPossible = 'No' # 余った行動回数が奇数なら不可能
    break
  else:
    continue
print(_isPossible) # 無事全計画リストの要素間を精査できたら可能
