def gabonnaci(n):
  """
  Calcule les n premiers termes d'une suite numérique définie par récurrence.

  Args:
    n: Le nombre de termes à calculer.

  Returns:
    Une liste contenant les n premiers termes de la suite.
  """
  #gabonnaci because a little like Fibonacci or tribonnaci for example and I am Gab-Sint Choust

  suite = [0]  
  result = [suite.copy()]
  
  compteur_boucle2 = 1
  n_boucle2 = 1
  for i in range(1, n):
      nouvelle_suite = [suite[-1]]
      n_boucle2 = n_boucle2 + 1
      for j in range(1, len(suite)):
          nouvelle_suite.append(suite[j] + sum(suite[:j]))

      if n_boucle2 >= compteur_boucle2:
          n_boucle2 = 0
          nouvelle_suite.append(compteur_boucle2)
          compteur_boucle2 += 1

      nouvelle_suite.sort()

      suite = nouvelle_suite
      result.append(suite.copy())

  return result
# big thanks AI
n = 66
resultat = ma_suite(n)
print(resultat)
