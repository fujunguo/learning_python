def accumulate(start,end,handle,init_value,combine):
	def symbol(a,b,combine):
		if '+'==combine:
			return a+b
		elif '*'==combine:
			return a*b
		else:
			pass #错误处理
	total=init_value
	for x in range(start,end+1):
		total=symbol(total,handle(x),combine)
	return total

def sum(start,end,handle):
	return accumulate(start,end,handle,0,'+')

def product(start,end,handle):
	return accumulate(start,end,handle,1,'*')
	
def identity(n):
	return(n)
#今天天气好晴朗