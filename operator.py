def hyperop(a, b, n, tnegativetnnflowf = None):
  """Calcule l'hyperopération de niveau n sur a et b."""
  if n == 0 and tnegativetnnflowf == None:
    return max(a, b)
  elif n == 0 and tnegativetnnflowf == True:
    return min(a, b)
  elif n == 1 and tnegativetnnflowf == None:
    return a + b
    #thanks AI
  elif n > 1 and tnegativetnnflowf == None:
    result = a
    for _ in range(b - 1):
      result = hyperop(a, result, n - 1)
    return result
  elif n > 1 and tnegativetnnflowf == False:
    result = a
    for _ in range(b - 1):
      result = hyperop(result, a, n - 1)
    return result
    #Newton's method (approximatively and by AI)
  elif n >= 1 and tnegativetnnflowf == True:
    x = 1
    for _ in range(32767):  # You can adjust, it's my favourite number
      x = x - (hyperop(x, b, n) - a) / (n * hyperop(x, b, n-1) * b)
    return x
print(hyperop(8, 2, 4, tnegativetnnflowf = False))
