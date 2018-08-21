# 利用itertools模块计算圆周率
import itertools

# 自写
def pi(N):
    ns = itertools.count(1, 2)
    ns1 = itertools.takewhile(lambda x: x <= 2*N - 1, ns)
    ns2 = list(ns1)
    n = 0
    sum_ = 0
    for i in ns2:
        n = n + 1
        if n % 2 == 1:
            i = 4 / i
        else:
            i = -4 / i
        sum_ += i
        # print(i)
        # print(sum_)
    return sum_


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('Test Passed!')
print()


# other's
def pi_(M):
    odds = itertools.count(1, 2)
    odds_1 = itertools.takewhile(lambda x: x <= 2*M - 1, odds)
    L =[(4/x)*(-1)**((x-1)/2) for x in list(odds_1)]
    return sum(L)


print(pi_(10))
print(pi_(100))
print(pi_(1000))
print(pi_(10000))
print('OK!')
