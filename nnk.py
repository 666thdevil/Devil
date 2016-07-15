import math
t = int(input())
list = []
i = 0
while(t!=0):
	a,b = int(input()), int(input())
	if (b%4 == 0):
		x=math.pow(a,4)
		list.append(x%10)
	else:
		x=math.pow(a,(b%4))
		list.append(x%10)
	t=t-1

for x in list:
	print(int(x))

print hello
print nnk
print sabarish
print prabha
print chethan
print maglin
print arihant
print shubh
print hi
