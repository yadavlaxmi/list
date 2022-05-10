# 31. Given the start and end of a range, write a Python program to print all negative numbers in a given
# range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1
# Input: start = -3, end = 4
# Output: -3, -2, -1

# A .

list=[-4,-3,-2,-1,0,1,2,3,4,5]
i=0
while i<len(list):
	if -4<=list[i]<5:
		if list[i]<0:
			print(list[i],end=" ")
	i+=1




# B.

# list=[-3,-2,-1,0,1,2,3,4,]
# i=0
# while i<len(list):
# 	if -4<=list[i]<5:
# 		if list[i]<0:
# 			print(list[i],end=" ")
# 	i+=1

