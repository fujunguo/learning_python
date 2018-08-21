# 1.对数字字符串进行进制转换
import functools
int2 = functools.partial(int, base=2)

print(int2("1000000"))
print(int2("1000000", base=10))

print(int2("1010101"))
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
# int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base，也就是：
# int2('10010')
# 相当于：
# kw = { 'base': 2 }
# int('10010', **kw)
print()

# 2.求一组数字的最大值
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))

