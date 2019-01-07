# __author__: William Kwok
def bulk(self):
	print('%s is yelling...' % self.name)
class Dog(object):
	def __init__(self, name):
		self.name = name

	def eat(self, food):
		print('%s is eating %s...' % (self.name,food))

d = Dog('Lassie')
choice = input('>>>').strip()
if hasattr(d, choice):	 # 判断一个对象里是否有choice字符串的方法
	func = getattr(d, choice)  # 根据字符串，去获取对象里对应方法的内存地址
	func('baozi')
	print(d.name)
	delattr(d, 'name')	 # 删除指定字符串对应的属性

else:
	print('There is no %s attribute.' % choice)
	# 如果没有该属性，则为类指定一个属性
	setattr(d, choice, bulk) 	# 设定一个动态属性talk
	setattr(d, choice, None)  # 设定一个静态属性a
	print(getattr(d, choice))  #调用时参数不要写死
	# d.talk(d)
print(d.name)
