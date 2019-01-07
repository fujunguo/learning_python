# __author__: William Kwok
class Dog(object):
	def __init__(self, name):
		self.name = name

	# 实际上跟类没什么关系了，只是类里面的一个普通函
	# 数，跟类的唯一关系是，调用时需要用到类名，它
	# 访问不了类或实例中的任何属性
	@staticmethod
	def eat():
		print('%s is eating %s.' % ('f', 'd'))

d = Dog('Lassie')
d.eat()
