# a=[1,2,3,4,5,6, 7,8,9,10]find the maximum number of in this list?
a=[1,2,3,4,5,6,7,8,9,10]
b=0
i=0
while i<len(a):
	if a[i]>b:
		b=a[i]
	i+=1
print(b)