from random import *
def randeum():
  points = 0
  continuer = 50
  tentative = randint(0, 1)
  while 0 < tentative:
    tentative = 0 + randint(0, 1)
    points = points + 1
    continuer = continuer / 2
    print(points, "points avec", continuer, "% d'avoir eu ce résultat et de s'arrêter juste après.")
  if 0 < points :
    print("fin!")
  else:
    print(points, "points avec", continuer, "% d'avoir eu ce résultat et de s'y être fait bloqué, perdu mais merci d'avoir joué !")
  
  return points
a = randeum()
print(a)
print(a+3)
print(a**a)
#v1 of randomaster, randeum because two is deux in French and random 2.0
