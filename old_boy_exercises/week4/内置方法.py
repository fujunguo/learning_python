# __author__: William Kwok
#
print(all([0, 1, -2]))

#
print(any([0, 1, -2]))

#
print(bin(65535))

#
print(bool([0]))

#
a = bytes('abcde', encoding='utf-8')
b = bytearray('abcde', encoding='utf-8')
b[0] = 52
print(a, b)

# ASCII 码转换
print(chr(125))
print(ord('}'))


# 判断一个对象是否可以调用
def a():
	pass
print(callable(a))

# 匿名函数
calc = lambda n: 3 if n < 3 else 4
print(calc(6))

# 从一组数据中过滤出你想要的
print("Filter:")
res = filter(lambda n:n>5, range(10))
for i in res:
	print(i)

# 对传入的迭代对象里的每个值进行统一处理
print("Map:")
res1 = map(lambda n:n**2, range(10))
for i in res1:
	print(i)

# 把一个函数作用在一个序列上
# reduce把结果继续和序列的下一个元素
# 做累积计算
print("Reduce:")
import functools
res2 = functools.reduce(lambda x,y:x*y, range(1,11))
print(res2)

# 以键值对的方式返回当前程序的所有变量
print("Globals:")
print(globals())

# 将十进制转换为八进制
print(oct(9))

# 小数点后保留指定位数
print(round(3.1315926, 3))

# 对给定序列进行排序
a = { 9:5, 6:3, 2:3, 7:0, 0:7, 4:1, -2:0, -3:23}
print(sorted(a.items())) # 默认以key排序
print(sorted(a.items(), key=lambda x:x[1]))

# 合并两组数据
list_1 = [1, 2, 3, 4, 5]
list_2 = ['a', 'b', 'c', 'd']
for i in zip(list_1, list_2):
	print(i)
