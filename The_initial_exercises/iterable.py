#判断一个对象是否是可迭代对象
from collections import Iterable
isinstance("abc",Iterable)
isinstance([1,2,3],Iterable)
isinstance(123,Iterable)

#对list实现类似Java那样的下标循环
#使用内置的enumerate函数可以把一个list
#变成索引-元素对，这样就能在for循环里迭代了
for i,value in enumerate([1,3,5]):
	print(i,value)
for x,y in [(1,2),(3,4),(5,6)]:
	print(x,y)
