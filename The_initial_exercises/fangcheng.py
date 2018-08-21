import math
##求解ax^2+bx+c=0的两个解
def quadratic(a,b,c):
	M=b^2-4*a*c
	if M>=0:
		x1=-b-math.sqrt(M)
		x2=-b+math.sqrt(M)
		return x1,x2
	else:
		raise TypeError('此方程无解')
i=quadratic(1,2,-3)
#print(i)
print('该方程的两个解是',i)