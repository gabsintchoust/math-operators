def pascal(fin,unx,uny,pasx,pasy):
  n=uny+(fin*pasy)
  lines=[]
  for i in range(0,n+1):
    line=[1]
    for k in range(1,i+1):
      coeff=line[-1]*(i-k+1)//l
      line.append(coeff)
    lines.append(line)
  ligne=[lines[uny][unx]]
  for i in range(1,fin+1):
    ligne.append(lines[uny+(i*past)][unx+(i*pas)])
  return ligne