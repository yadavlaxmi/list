# Write a code that works for any list, and that tells how many odd numbers and how many even numbers are there in a given list? 

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=[ ]
b=[ ]
while i<len(elements): 
    if elements[i]%2==0:
        a.append(elements[i])
    else:
        b.append(elements[i])
    i+=1
print("even=",a)
print("odd=",b)