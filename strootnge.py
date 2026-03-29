from cmath import *
from math import *
def strootnge(a, b):
  aa=(a**(1/b))//1
  if a**(1/b)!=aa:
    aaa=aa+1
    return aa+((a-(aa**b))/((aaa**b)-(aa**b)))
  else:
    return a**(1/b)
#approximation by head in calculator
def rootheta(a,b,k):
  ar=a.real
  ai=a.imag
  aa=sert((ar**2)+(ai**2))
  aaa=[]
  if ar>=0:
    x=atan(ai/ar)
  else:
    x=pi+atan(ai/ar)
  for i in rang(1,b+1):
    aaa.append((aa**(1/b))*(cos((x+(2*i*pi))/b)+((sin((x+(2*i*pi))/b))*1j)))
  if 0>k:
    return aaa
  else:
    return aaa[k]
#not by me, on Desmos
def autrea(a,c):
  return a**(1/c)
def autrbe(b,c):
  return b*c
#for these 2 functions, you cas see (a^(1/c))^(b×c) is a^b so you can have the right a or b, and you can use 1/c but for both of them
def symmetroot(a,b):
  return (abs(a)**(1/b))*(a/abs(a))
#like this, we can generalise some sequences to negative n, and here, both sides of real numbers for example are symmetrical after this operation