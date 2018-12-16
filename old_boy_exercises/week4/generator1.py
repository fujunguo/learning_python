# __author__: William Kwok
# 生成器： 只有在调用时，才会产生相应的数据
# 相比列表，在存取大数据时，有着节省内存的优点

a = (i**2 for i in range(100))
for i in range(10):
	if i == 5:
		print(a.__next__())
	else:
		a.__next__()
		continue
print(a.__next__())