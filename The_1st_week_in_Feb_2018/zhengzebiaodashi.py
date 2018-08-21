import re
print(re.match(r'\d{3}\-\d{3,8}$', '010-123456'))

# 常见判断方法
# test = '用户输入的字符串'
# if re.match(r'正则表达式')
#    print('OK')
# else:
#    print('Failed')

print('a b  c'.split(' '))
print(re.split(r'\s+', 'a b  c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

# 贪婪匹配
f = '102300'
f_ = re.match(r'^(\d+)(0*)$', f)
print(f_.groups())

f1 = '102300'
f1_ = re.match(r'^(\d+?)(0*)$', f1)
print(f1_.groups())
print()

# 编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print()

# 验证Email地址
mail_compile = re.compile(r'[0-9a-zA-Z\-_.#]*[@a-zA-Z.]*[com]$')


def is_valid_email(addr):
    a = mail_compile.match(addr)
    if a:
        return True
    else:
        return False


assert is_valid_email('1067644749@qq.com')
assert is_valid_email('bill.gates@microsoft.com')
assert is_valid_email('bob#example.com')
assert is_valid_email('mr-bob@example.com')
print('OK')
print()

# 提取带名字的email的地址
b = re.compile(r'(<?)([\s\w]*)(>?)([\w\s]*)@([\w.]*)$')


def name_of_email(addr):
    global b
    if b.match(addr):
        return b.match(addr).group(2)
    else:
        return None


assert name_of_email('tom@voyager.org') == 'tom'
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
print('OK!')

