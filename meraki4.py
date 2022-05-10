# Check whether the list is palindrome or not? 
name=[ 'n', 'i', 't', 'i', 'n' ]
rev=name[: :-1]
i=0
while i<len(name):
		if name==rev:
			i+=1
			print("Haan! palindrome hai")
			break
		else:
			print("nahi ! palindrome nahi hai")