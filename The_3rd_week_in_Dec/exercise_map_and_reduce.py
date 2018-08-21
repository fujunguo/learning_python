from functools import reduce


# 将名字首字母转换成大写
def normalize(name):
    return name.capitalize()


L1 = ['adam', 'lily', 'Tom']
L2 = map(normalize, L1)
print(list(L2))


# 求积运算
def prod(z):
    def prod1(x, y):
        return x * y
    return reduce(prod1, z)


print('3 * 5 * 7 *9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print("测试成功！")

else:
    print("测试失败！")


# 字符型数据转浮点型数据
def str2num(x):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
              '7': 7, '8': 8, '9': 9, '.': '.'}
    return DIGITS[x]


def num2float(x, y):
    pass


def str2float(s):
    pass
