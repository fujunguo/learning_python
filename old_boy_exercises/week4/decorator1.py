# __author__: William Kwok
import time


def timer(func):
	# 实现装饰器知识储备
	# 1、函数即“变量”
	# 2、高阶函数
	# 3、嵌套函数
	# 高阶函数+嵌套函数=》装饰器
	def wrapper(*args, **kwargs):
		start_time = time.time()
		func()
		stop_time = time.time()
		print("The running time is {}".format(stop_time - start_time))
	return  wrapper


@timer
def func1():
	time.sleep(3)
	print('This is a test.')

func1()
