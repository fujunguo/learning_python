#保留小数点后三位
from urllib import request

print("{0:.3f}".format(1/3))

#使用下划线填充文本，并保持文字处于中间位置
#使用(^)定义'_hello_'字符串长度为11
print('{0:_^11}'.format('hello'))

#基于关键词输出'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop',book='A Byte of Python'))

#打印格式
print('abc',end='')
print('123')

#转义序列
print('What\'s your name?')
print('This is the first line.\tThis is the second line')

print('This is the first line.\nThis is the second line')
print('This is the first line.\
This is the second line')

#逻辑行和物理行
a=5
print(a)

b=6;
print(b);

c=7;print(c)
