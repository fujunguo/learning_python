# -*- coding: utf-8 -*-
import time, functools
def log(func):
    def wrapper(*args, **kw):
        print("call %s:" % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print("2017-12-25")


now()


# decorator装饰器，装饰器不传入参数
# 相当于是f = log(f)
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args):
        start = time.time()
        print("begin call")
        result = fn(*args)  # 不能直接返回结果，不然执行时间不对
        end = time.time()
        print("end call")
        print("%s executed in %s ms.And the result is: %s" % (fn.__name__, end - start, result))
        return fn(*args)
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
print(f, s)
if f != 33:
    print("测试失败")
elif s != 7986:
    print("测试失败")


# 装饰器本身传入参数
# f = log('begin call')(f)






