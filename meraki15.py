
# Sum of nested list:
# a=[1, 2,[3, 4,[5, 6]]]? 
a=[1,2,[3,4,[5,6]]]
i=0
sum=0
while i<len(a):
	if type(a[i])==type([ ]):
		j=0
		while j<len(a[i]):
			if type(a[j])==type([ ]):
				k=0
				while k<len(a[i][j]):
					sum=sum+a[i][j][k]
					k+=1
			else:
				sum=sum+a[i][j]
			j+=1
	else:
		sum=sum+a[i]
	i+=1
print(sum)