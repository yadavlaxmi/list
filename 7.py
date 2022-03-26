a=[1,2,3,1,2,3]
m=[]
i=0
while i<len(a):
  if a[i] not in m:
    m.append(a[i])
  i=i+1
print(m)
