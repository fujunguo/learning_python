# __author__: William Kwok
import time


def timer(func):	# func = foo
	def wrapper(*args, **kwargs):
		start_time = time.time()
		print('{} is running...'.format(func))
		func(*args, **kwargs)	# run foo()
		stop_time = time.time()
		print('The running time is {}'.format(stop_time-start_time))
	return wrapper


@timer	# foo = timer(foo)
def foo1():
	time.sleep(3)
	print('In the foo.')


@timer
def foo2(name, age):
	time.sleep(2)
	print("Name:{}, Age:{}".format(name, age))

foo1()
foo2('William', 23)