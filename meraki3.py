# Even nd odd numbers in a list [1,2,3,4,5,6,7, 8,9,10]
x=[1,2,3,4,5,6,7,8,9,10]
i=0
a=[ ]
b=[ ]
while i<len(x): 
    if i%2==0:
        a.append(x[i])
    else:
        b.append(x[i])
    i+=1
print("odd=",a)
print("even=",b)