import logging
import functools

def text(level):
	def use_logging(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			print('Arguments were: %s, %s' % (args, kwargs))
			if level == 'warn':
				logging.warn("%s is running" % func.__name__)
			elif level == 'info':
				logging.info("%s is running" % func.__name__)
			return func(*args, **kwargs)	 # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
		return wrapper
	return use_logging

@text(level='warn')
def foo(*args, **kwargs):
	print(args, kwargs)

# foo = use_logging(foo)	# 因为装饰器 use_logging(foo) 返回的是函数对象 wrapper，这条语句相当于  foo = wrapper
foo(2, 3, y=5) # 执行foo()就相当于执行wrapper()
print(foo.__name__)