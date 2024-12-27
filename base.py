def base(charone, number, chartwo):
  """
  Converts a number from one base to another.

  Args:
    charone: A string representing the characters of the source base.
    number: A string representing the number to convert.
    chartwo: A string representing the characters of the destination base.

  Returns:
    A string representing the converted number.
  """
  i = 0
  total = 0
  position = []
  finish = ""
  for ii in range(len(number)):
    while charone[i] != number[-ii - 1]: 
      i += 1
    total += (len(charone)**ii) * i
    i = 0
  to = total
  while to > 0:
    position.append(chartwo[int(to % len(chartwo))])
    to //= len(chartwo)
  for j in range(len(position)):
    finish += position[-j - 1]
  return finish
#more than 2 screen where I make different codes for that and there crashed so thanks AI for help
print(base("♪⁰", "⁰⁰♪⁰⁰", "⁰♪"))
