from random import *
def randomaster(win, tie, lose, niw = 0, eit = 0, esol = 0):
  yes = win
  stop = tie
  no = lose
  maybe = randint(1, yes + stop + no)
  point = 0
  print(maybe)
  if maybe < yes + 1:
    while maybe < yes + 1:
      point += 1
      yes += niw
      stop += eit
      no += esol
      maybe = randint(1, yes + stop + no)
      print(maybe)
  elif maybe > yes + stop:
    while maybe > yes + stop:
      point -= 1
      yes += niw
      stop += eit
      no += esol
      maybe = randint(1, yes + stop + no)
      print(maybe)
  return point
# = 
# < 
# > 

# continuend, play, calcul
#"point" "+ win" or "- lose" "1" have + not used AND random of can be other thing than middle, number of times of game, operator and where in list for total "point" and like the 3rd best try with abs of the list of games × the len of list of games

# w = win, t = tie, l = lose
#start "maybe" random
print(randomaster(4, 1, 0, niw = 2))
