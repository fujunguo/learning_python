# __author__: William Kwok
import time


# 高阶函数
def bar():
	time.sleep(3)
	print('In the bar.')


def foo1(func):
	start_time = time.time()
	func()
	stop_time = time.time()
	print('The running time of func is {}s.'.format(stop_time-start_time))
foo1(bar)
print()


def foo2(func):
	print(func)
	return func

bar = foo2(bar)
bar()

