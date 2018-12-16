# __author__: William Kwok
def func(x, y, z):
	"""位置参数测试"""
	print(x)
	print(x, y)
	print(x, y, z)


def func1(x, y=1):
	"""默认参数测试"""
	print(x)
	print(x, y)

# 位置参数调用
func(1, 2, 3)
print()

# 关键字参数调用
func(z=3, x=1, y=2)
print()

# 关键字参数和位置参数同时调用
# 需要注意的是，关键字参数需放在位置参数后面
func(1, z=3, y=2)
print()

# 默认参数调用
func1(1)
func1(1, 2)
