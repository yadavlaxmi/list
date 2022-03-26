b=[[6,8,9],[9,0]]
i=0
sum1=0
while i<len(b):
  j=0
  while j<len(b[i]):
    sum1=sum1+b[i][j]
    j=j+1
  i=i+1
print(sum1)
