numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
c=0
while i<len(numbers):
  if numbers[i]>20 and numbers[i]<40:
    c=c+1
    print(c,numbers[i])
  i=i+1