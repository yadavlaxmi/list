# Print expected table in list? 

# a=int(input("num"))
# i=1
# while i<=a:
# 	j=1
# 	b=[ ]
# 	while j<=10:
# 		k=i*j
# 		b.append(k)
	
# 		j+=1
# 	print(i,",",b,",",end=" ")
	# i+=1
 
# list=[1, 2,3,4,5,6,7,8,9,10]
# Find even, odd, even prime, odd prime? 

# list=[1,2,3,4,5,6,7,8,9,10]
# i=0
# even=[ ]
# odd=[ ]
# even_prime=[ ]
# odd_prime=[ ]
# while i<len(list):
# 	if list[i]%2==0:
# 		even.append(list[i])
# 		if list[i]==2:
			
# 			even_prime.append(2)
# 	else:
# 		odd.append(list[i])
# 		j=2
# 		while j<(list[i]):
# 			if list[i]%j==0:
# 				break
# 			else:
# 				j+=1
# 		if list[i]==j:
# 				odd_prime.append(list[i])
			
# 	i+=1
# print("even",even)
# print("odd",odd)
# print("even_prime",even_prime)
# print("odd_prime",odd_prime) 

# list=[4, 5]
# Output:-9

# list=[4,5]
# i=0
# sum=0
# while i<len(list):
# 	sum=sum+list[i]
# 	i+=1
# print(sum)


# list=[0,[3,5,[4,7,[10]]]
# Output:-[10]

# list=[0,[3,5,[4,7,[10]]]]
# print(list[1][2][2])

# list=["1", "2", " 3", "4"]
# list2=["5", "6", "7", " 8"]

# Output:-['15', '26', '37', '48']

# list=["1","2","3","4"]
# list1=["5","6","7","8"]
# i=0
# list2=[ ]
# while i<len(list):
# 		sum=list[i]+list1[i]
# 		list2.append(sum)
# 		i+=1
# print(list2)

# list=[1,2,3,4]
# list1=[5,6,7,8]
# Output:-[6, 8, 10, 12]

# list=[1,2,3,4]
# list1=[5,6,7,8]
# i=0
# list2=[ ]
# while i<len(list):
# 		sum=list[i]+list1[i]
# 		list2.append(sum)
# 		i+=1
# print(list2)

# name="swathi"
# Output:-[1, 's', 2, 'w', 3, 'a', 4, 't', 5, 'h', 6, 'i']


# name="swathi"
# k=[]
# i=0
# a=1
# while i<len(name):
# 	b=name[i]
# 	k.append(a)
# 	k.append(b)
# 	a+=1
# 	i+=1
# print(k)

# list=["hima","bindu","gundu","swathi","latha"]
# Output:-['h', 'i', 'n', 't', 'a']

# list=["hima","bindu","gundu","swathi","latha"]
# i=0
# a=[ ]
# while i<len(list):
# 	b=list[i]+list[i]
# 	a.append(b[i])
# 	i+=1
# print(a)


# c=["hima","bindu","gundu","swathi","latha",'gouthami']

# Output:-['himabindu', 'gunduswathi', 'lathagouthami']

# c=["hima","bindu","gundu","swathi","latha",'gouthami']
# i=0
# a=[ ]
# while i<len(c):
# 	b=c[i]+c[i+1]
# 	a.append(b)
# 	i+=2
# print(a)

# num=[2,5,1,7,5,9,1,5,8,2,1,10,0,6]
# Print list in ascending order and descending order? 

# A. Ascending order:

# num=[2,5,1,7,5,9,1,5,8,2,1,10,0,6]
# i=0
# while i<len(num):
# 	j=0
# 	while j<len(num):
# 		if (num[i]<num[j]):
# 			num[i],num[j]=num[j],num[i]
# 		j+=1
# 	i+=1
# print(num)

# B. Descending order:

# num=[2,5,1,7,5,9,1,5,8,2,1,10,0,6]
# i=0
# while i<len(num):
# 	j=0
# 	while j<len(num):
# 		if (num[i]>num[j]):
# 			num[i],num[j]=num[j],num[i]
# 		j+=1
# 	i+=1
# print(num)

# a=[" gud ia ","sw athi","me n tor"]
# Output should be
# ["gudia","Swathi","mentor"]

# a=[" gud ia ","sw athi","me n tor"]
# i=0
# space=[ ]
# while i<len(a):
# 	j=0
# 	st=''
# 	while j<len(a[i]):
# 		if a[i][j]!=' ':
# 			st+=a[i][j]
# 		j+=1
# 	space.append(st)
# 	i+=1
# print(space)

# a=[9, 2,4,6,7,9]
# Output:-[18, 9,10]

# a=[9,2,4,6,7,9]
# i=0
# b=[ ]
# while i<len(a):
# 	x=a[i-1]+a[-i]
# 	b.append(x)
# 	i+=2
# print(b)



# Total sum of nested list? 

# list=[[23,45],[4,5],[6]]
# i=0
# sum=0
# while i<len(list):
# 	j=0
# 	while j<len(list[i]):
# 		sum=sum+list[i][j]
# 		j+=1
# 	i+=1
# print(sum)


# Total sum of list? 
# a=[[23, 45], [4, 5[6]]]

# Output:-83

# a=[[23,45],[4,5,[6]]]
# i=0
# b=[ ]
# while i<len(a):
# 	if type(a[i])==list:
# 		j=0
# 		while j<len(a[i]):
# 			if type(a[i][j])==list:
# 				k=0
# 				while k<len(a[i][j]):
# 					b.append(a[i][j][k])
# 					k+=1
# 			else:
# 				b.append(a[i][j])
# 			j+=1
# 	else:
# 		b.append(a[i])
# 	i+=1
# print(b)
# i=0
# s=0
# while i<len(b):
# 	s=s+b[i]
# 	i+=1
# print(s)


# a=[1, 2,32,4,46]
# Output should be ["one ", " Two", "three two", " Four ", " Four six"]


# a=[1,2,32,4,46]
# i=0
# m=[]
# while i<len(a):
#     b=str(a[i])
#     j=0
#     s=" "
#     while j<len(b):  
#         if b[j]=="1":
#             s=s+"one"
#         elif b[j]=="2":
#             s=s+"two"
#         elif b[j]=="3":
#             s=s+"three"
#         elif b[j]=="4":
#             s=s+"four"
#         elif b[j]=="5":
#             s=s+"five"
#         elif b[j]=="6":
#             s=s+"six"
#         elif b[j]=="7":
#             s=s+"seven"
#         elif b[j]=="8":
#             s=s+"eight"
#         elif b[j]=="9":
#             s=s+"nine"
#         j+=1
#     i=i+1
#     m.append(s)
# print(m)


# *nested list in to single list? 
# n=[[3,4,[6],[45,6]]]
# i=0
# b=[ ]
# while i<len(n):
# 	if type(n[i])==list:
# 		j=0
# 		while j<len(n[i]):
# 			if type(n[i][j])==list:
# 				k=0
# 				while k<len(n[i][j]):
# 					b.append(n[i][j][k])
# 					k+=1
# 			else:
# 				b.append(n[i][j])
# 			j+=1
# 	else:
# 			b.append(n[i])
# 	i+=1
# print(b)


# Find out the minimum numbers in a list? 
# a=[[23,45,6],[23,4,5],[20,5,1]]
# Output:- 6  4  1

# a=[[23,45,6],[23,4,5],[20,5,1]]
# i=0
# b=[ ]
# while i<len(a):
# 	j=0
# 	c=a[i][j]
# 	while j<len(a[i]):
# 		if a[i][j]<c:
# 			c=a[i][j]
# 			b.append(c)
# 		j+=1
# 	print(c,end=' ')
# 	i+=1


# [5, 6,29,33,4,6] sort this list without using sort () method? 

# a=[5,6,29,33,4,6]
# i=0
# while i<len(a):
# 	j=0
# 	while j<len(a):
# 		if a[i]<a[j]:
# 			a[i],a[j]=a[j],a[i]
# 		j+=1
# 	i+=1
# print(a)


# find the maximum numbers ? 
# a=[[3,5,67],[3,5,45],[5,67,28]]
# i=0
# b=[ ]
# while i<len(a):
# 	j=0
# 	c=a[i][j]
# 	while j<len(a[i]):
# 		if a[i][j]>c:
# 			c=a[i][j]
# 			b.append(c)
# 		j+=1
# 	print(c,end=' ')
# 	i+=1


# Remove last three elements from the list? 

# a=[9,3,'5','v','t',56,77]
# i=0
# d=int(input('enter the num'))
# while i<len(a):
# 	print(a[:-d])
# 	i+=1
# 	break

# Write a python program to sum of element-wise three given lists? 

# list=[[3,4,5,],[5,6,7],[1,2,3]]
# a=1
# b=2
# i=0
# j=0
# d=[ ]
# while j<len(list):
# 	c=list[i][j]+list[a][j]+list[b][j]
# 	d.append(c)
# 	j+=1
# print(d)


# a=[1,5,10,12,16,20]
# b=[1,2,10,13,16]
# Output:-[1, 2,5,10,12,13,16,20]


# a=[1,5,10,12,16,20]
# b=[1,2,10,13,16]
# a.extend(b)
# i=0
# c=[]
# while i<len(a):
# 	if a[i] not in c:
# 		c.append(a[i])
# 	i+=1
# print(c)

# a=[1,342,75,23,98]
# b=[75,23,98,12,78,10,1]
# Output:-[1, 23,75,98]

# a=[1,342,75,23,98]
# b=[75,23,98,12,78,10,1]
# i=0
# c=[ ]
# while i<len(a):
# 	if a[i] in b:
# 		c.append(a[i])
# 	i+=1
# print(c)


# a=[5,6,7,[3,[4,5],6],8]
# # Output:-[3, [4, 5], 6]


# print(a[3])


# length of list?

# list=["kajal","ishani","truptimayee"]
# i=0
# while i<len(list):
# 	a=len(list[i])
# 	print(list[i],"=",a)
# 	i+=1

# length of list and position of index?

# list=["kajal","ishani","truptimayee"]
# i=0
# while i<len(list):
# 	a=len(list[i])
# 	print(i,list[i],"=",a)
# 	i+=1


# . how to count each words with index and position in the        question ❓❓❓


# a="hello priya "," how are you"
# b="".join(a)
# c=b.split()
# i=0
# while i<len(c):
# 	j=0
# 	while j<len(c[i]):
# 		print(i,c[i],len(c[i]))
# 		break
# 		j+=1
# 	i+=1
# print("total length",i)


# find out only integers in  for loop list
# list=[11, 34.1, 98.2, 43, 45.1, 54, 54]
# for x in list:
#     if int(x) == x:
#         print(x)
        

# find out only integers in  while loop list
# list=[11, 34.1, 98.2, 43, 45.1, 54, 54]
# i=0
# list1=[]
# while i<len(list):
#     if list[i]==int(i):
#         print(list[i])
#     i+=1


# find out same characters in given list

list=["geetha","neethu","geethu","seethu","geetham"]
i=0
list1=[]
while i<len(list):
    j=0
    while j<len(list):
        if list[i]==list[j]:
            list1.append(list[i][j])
        j+=1
    i+=1
print(list1)