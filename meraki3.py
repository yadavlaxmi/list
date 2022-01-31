numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
while i<len(numbers):
  if numbers[i]>max:
    max=numbers[i]
  i=i+1
j=0
secondmax=0
while i<len(numbers):
  if numbers[j]<max:
    if numbers[j]>secondmax:
      secondmax=numbers[j]
  j=j+1
k=0
thirdmax=0
while k<len(numbers):
  if numbers[k]<max:
    if numbers[k]<secondmax:
      if numbers[k]>thirdmax:
        numbers[k]=thirdmax
  k=k+1
print(max)
print(secondmax)
print(thirdmax)


