a=[[2,3,4],[5,6,7],[8,9,2]]
m=[]
i=0
while i<len(a):
	sum=0
	j=0
	while j<len(a):
		sum=sum+a[j][i]
		j=j+1
	i=i+1
	m.append(sum)
print(m)