# Count occurrence:
# How many times a certain character or word appears? 

# list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# list1=[ ]
# while i<len(list):
# 	j=0
# 	count=0
# 	while j<len(list):
# 		if list[i] == list[j]:
# 			count+=1
# 		j+=1
# 	if list[i] not in list1:
# 		list1+=list[i]
# 		print([list[i],count])
# 	i+=1

        # (OR)
list= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
m=[ ]
while i<len(list):
	j=0
	count=0
	n=[ ]
	while j<len(list):
		if list[i] == list[j]:
			count+=1
		j+=1
	n.append(list[i])
	n.append(count)
	if n not in m:
		m.append(n)
	i+=1
print(m)