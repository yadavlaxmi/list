
a=list(map(int,input().split()))
i=0
max=a[0]
while i<len(a):
	if a[i]>max:
		max=a[i]
	i+=1

max1=a[0]
j=0
while j<len(a):
	if a[j]<max:
		if a[j]>max1:
			max1=a[j]
	j+=1
print(max1)


