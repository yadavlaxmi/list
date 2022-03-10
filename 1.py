a=["a","b","c","d"]
b=[1,3,5,3]
i=0
m={}
while i<len(a):
  while i<len(b):
    m.update({a[i]:b[i]})
    i=i+1
  print(m)