# __author__: William Kwok
class Dog(object):
	name = 'Missy'
	def __init__(self, name):
		self.name = name

	# 类方法只能访问类变量，不能访问实例变量
	@classmethod
	def eat(self):
		print('%s is eating %s.' % (self.name, 'd'))

d = Dog('Lassie')
d.eat()
