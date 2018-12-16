# __author__: William Kwok
import random

# 取[0, 1)之间的随机浮点数
print(random.random())
# 取[1,3]之间的随机整数
print(random.randint(1, 3))
# 取[1,3]之间的随机浮点数
print(random.uniform(1,3))
# 取传入序列中的随机序列,默认取1位
print(random.choice('abcdefg'))
ls = [1, 3, 5, 6, 9]
random.shuffle(ls)
print(ls)



