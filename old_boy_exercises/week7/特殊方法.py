# __author__: William Kwok
# 创建类的另一种方法
"""方式一"""
class Foo(object):
	def __init__(self, name):
		self.name = name

	def func(self):
		print('Hello, %s.' % self.name)


a = Foo('William')
a.func()

"""方式二，用type类创建"""
def __init__(self, name):
	self.name = name

def func(self):
	print('Hello, %s.' % self.name)
Foo1 = type('Foo1', (object,), {'func':func, '__init__':__init__})
b = Foo1('Jackie')
b.func()