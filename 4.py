a=[1,0,2,0,3,0]
l=[]
l1=[]
for i in a:
  if i!=0:
    l.append(i)
  else:
    l1.append (i)
l.extend (l1)
print(l)