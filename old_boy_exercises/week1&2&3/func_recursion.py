# __author__: William Kwok
def calc(n):
	"""
	递归的三个特点：
	1、必须有结束条件；
	2、进入更深一层的递归时，问题规模相比上次要有所减少；
	3、效率不高；
	"""
	print(n)
	if int(n/2) > 0:
		return calc(int(n/2))
	print('->', n)

calc(10)




