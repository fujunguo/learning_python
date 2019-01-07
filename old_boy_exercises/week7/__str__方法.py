# __author__: William Kwok
class Dog(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		"""将对象格式化成一个字符串，不写该
		方法的话，打印对象时默认返回内存地址"""
		return 'Name is %s.' % self.name


d = Dog('Missy')
print(d)
