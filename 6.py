a="my name is kirti"
b=a.split()
i=0
# c=0
n={}
while i<len(b):
  # c=c+1
  n.update({b[i]:i})
  i=i+1
print(n)
