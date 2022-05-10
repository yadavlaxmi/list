# marks = [
#  [78, 76, 94, 86, 88],
#  [91, 71, 98, 65, 76],
#  [95, 45, 78, 52, 49]
# ]
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
avg=0
i=0
while i<len(marks):
	j=0
	while j<len(marks):
		avg0=sum(marks[0])/len(marks[0])
		avg1=sum(marks[1])/len(marks[1])
		avg2=sum(marks[2])/len(marks[2])
		j+=1
	i+=1
print("year1=",avg0)
print("year2=",avg1)
print("year3=",avg2)
