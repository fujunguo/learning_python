# __author__: William Kwok
def func(a, b, f):
	"""高阶函数的用法"""
	return f(a) + f(b)

re = func(3, -6, abs)
print(re)
