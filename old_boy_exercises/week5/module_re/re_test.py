# __author__: William Kwok
import re

"""re.match()，一个字符串的开始位置
起匹配正则表达式，返回match对象，如果
第一个字符无法匹配，它将不会再继续往后
匹配（无论后续字符串是否有符合匹配条件的）"""
a = re.match(r'[0-9]\d{5}', '100081BIT')
print('a:', a.group())

"""re.search()在一个字符串中搜索匹配
正则表达式的第一个位置（无论后续字符串
是否还有符合匹配条件的），返回match对象"""
b = re.search(r'[0-9]\d{5}', 'BIT100081 TSU100084')
print('b:', b.group())

"""re.findall()搜索字符串，以列表类型
返回全部能匹配的子串"""
c = re.findall(r'[0-9]\d{5}', 'BIT100081 TSU100084')
print('c:', c)

"""re.split()将一个字符串按照正则表达式
匹配结果进行分割，返回列表类型"""
d = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print('d:', d)

"""re.sub()在一个字符串中替换所有匹配正则
表达式的子串，并返回替换后的字符串"""
e = re.sub(r'[1-9]\d{5}',':zipcode', 'BIT100081 TSU100084')
print('e:', e)

"""re.I(re.IGNORECASE)匹配时忽略大小写"""
f = re.match(r'[a-z]+', 'ABCDe', flags=re.I)
print('f:', f.group())

"""(...)分组匹配，被括起来的表达式将作为分组"""
g1 = re.match(r'(abc){2}a(123|456)c', 'abcabca456c')
g2 = re.search('(abc){2}(\|\|=){2}', 'Williamabcabc||=||=')
print('g1:', g1.group())
print('g2:', g2.group())

"""(?P<name>...)分组匹配，除了原有的
编号外，再指定一个额外的别名"""
h1 = re.search('(?P<id>[0-9]+)', 'abcd1234dafag')
h2 = re.match('(?P<Province>[0-9]{2})(?P<City>[0-9]{4})(?P<Birthday>[0-9]{8})', '500234199307154748')
print('h1:', h1.groupdict()) # 返回字典类型
print('h2:', h2.groupdict())