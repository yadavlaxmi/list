# User can answer either 1,2,3 or 4.Now u have taken answer as an input from the user now you need to check if the user has given correct answer or not. If the answer is right then u have to print "aapka number sahi hai " If the answer is wrong then u have to print "aapka number galath hair"? 

a=int(input("num"))
i=0
while i<=a:
	if a<=4:
		print("apka num sahi hay")
		break
	else:
		print("apka num galath hay")
		break
	i+=1 

