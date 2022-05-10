# Sum of even numbers
# Sum of odd numbers
# Sum of all numbers
# Average of even numbers
# Average of odd numbers
# Average of all numbers
# Count of even numbers
# Count of odd numbers
# Count of all numbers? 

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=[ ]
odd=[ ]
sum=0
sum1=0
count=0
count1=0
avg=0
avg1=0
while i<len(elements):
	if elements[i]%2==0:
		even.append(elements[i])
		sum=sum+(elements[i])
		avg=avg+(elements[i])/len(elements)
		count+=1
	else:
		odd.append(elements[i])
		sum1=sum1+(elements[i])
		avg1=avg+(elements[i])/len(elements)
		count1+=1
		
	i+=1
print("sum of even num=",sum)
print("sum of odd num=",sum1)
print("sum of all num=",sum+sum1)
print("average of even num=",avg)
print("average of odd num=",odd)
print("avg of all num=",avg+avg1)
print("even num=",count)
print("odd num=",count1)
print("count of all the num=",len(elements))