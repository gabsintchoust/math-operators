def egal(number, result, possibilities):
  if abs(number-result)<abs(possibilities):
    return True
  elif abs(number-result)==abs(possibilities):
    return None
  elif abs(number-result)>abs(possibilities):
    return False
degrées_celsius_humain = print(egal(37.4, 36.5, 0.8))
