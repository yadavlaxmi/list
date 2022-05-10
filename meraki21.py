# n=[19, 17, 12,17,17,18,10,17,14,12,19,17,12 13,11]
# Take out the duplicate from this list and put it in different list print it? 

n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
duplicate=[ ]
while i<len(n):
	if n[i] not in duplicate:
		duplicate.append(n[i])
	i+=1
print(duplicate)