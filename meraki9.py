#   Please see this list: sum of the list. 
# Marks=[
#       [78, 76, 94, 86, 88], 
#       [91, 71, 98, 65, 76], 
#       [95, 45, 78, 52, 49]
# ]

a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
i=0
sum=0
while i<len(a):
	j=0
	while j<len(a[i]):
		sum=sum+a[i][j]
		j=j+1
	i=i+1
print(sum)