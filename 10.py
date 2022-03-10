l=[30,7,8,[5,68,9]]
i=0

n=[]
while i<len(l):
  if type(l[i])==type([]):
    j=0
    sum=0
    while j<len(l[j]):
      sum=sum +(l[j][i])
      j=j+1
      i=i+1
      n.append(sum)
      print(n)