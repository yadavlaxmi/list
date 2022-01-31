name=[ 'n', 'i', 't', 'i', 'n' ]
i=0
while i<len(name):
  b=(name[-1::-1])
  i=i+1
print(b)

if name==b:
  print("palidrome")
else:
  print("not palidrome")
