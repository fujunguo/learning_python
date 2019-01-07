# __author__: William Kwok
# 作用：把一个方法变成静态属性
# 访问该方法时，则不能用()来调用
class Dog(object):
	def __init__(self, name):
		self.name = name
		self.__food = None

	@property
	def eat(self):
		print('%s is eating %s.' % (self.name, self.__food))

	# 若要给属性方法eat传参，需用下面的装饰器方式
	@eat.setter
	def eat(self, food):
		print('Set to food:', food)
		self.__food = food

	# 直接用del *.eat无法删除所传参数，需要再写一个装饰器
	@eat.deleter
	def eat(self):
		del self.__food
		print('Deleting successfully.')

d = Dog('Lassie')
d.eat
d.eat = 'baozi'
d.eat
del d.eat


