# Write a code that counts the numbers between 20 and 40and then prints it's count? 
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
count=0
i=0
while i<len(numbers):
	if 20<=numbers[i]<=40:
		count+=1
	i+=1
print(count)	