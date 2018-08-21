from functools import reduce


# 求和
def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


# 乘积
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# 字符串转int型数据
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))
