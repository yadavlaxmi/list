# Write a code and print  how many characters, spaces and length of the list? 

a='my name is swathi'
count=0
c1=0
i=0
while i<len(a):
		if a[i]==' ':
			count+=1
		else:
			c1+=1
		i+=1

print('total space:',count)
print('total chtr:',c1)
print("length of the list:",len(a))
