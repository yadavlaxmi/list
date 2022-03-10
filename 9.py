a=["my NAME"]
i=0
u=0
l=0
while i<len(a):
  j=0
  while j<len(a[i]):
    if a[i][j]>="a" and a[i][j]<="z":
      l=l+1
    elif a[i][j]>="A" and a[i][j]<="Z":
      u=u+1
    j=j+1
  i=i+1
print("upper",u)
print("lower",l)
   


# a="my NAME"
# c=0
# c1=0
# i=0
# while i<len(a):
#   if a[i]>="a" and a[i]<="z":
#     c=c+1
#   if a[i]>="A" and a[i]<="Z":
#     c1=c1+1
#   i=i+1
# print("lower",c)
# print("upper",c1)