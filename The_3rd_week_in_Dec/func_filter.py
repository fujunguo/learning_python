# 删掉偶数，保留奇数
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 删掉空字符串
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))


# 用Python实现筛选素数
def _odd_iter():
    n1 = 1
    while True:
        n1 = n1 + 2
        yield n1


def _not_divisible(n2):
    return lambda x: x % n2 > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n3 = next(it)
        yield n3
        it = filter(_not_divisible(n3), it)


for n4 in primes():

    if n4 < 1000:
        print(n4)

    else:
        break


# 利用filter()筛选出回数
def is_palindrome(n):
    # 利用字符串切片属性输出逆序字符串
    return str(n) == str(n)[::-1]


output = filter(is_palindrome, range(1, 1000))
print("1~1000:", list(output))

if list(filter(is_palindrome, range(1, 100))) == [1, 2, 3, 4, 5, 6, 7, 8, 9 ,11,
                                                  22, 33, 44, 55, 66, 77, 88, 99]:
    print("Congratulations! The test passed.")

else:
    print("Sorry, the test failed.")
