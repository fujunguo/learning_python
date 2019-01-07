# __author__: William Kwok


class Human:
	# 定义一个父类
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def eat(self):
		print('%s is eating...' % self.name)

	def drink(self):
		print('%s is drinking...' % self.name)

	def sleep(self):
		print('%s is sleeping...' % self.name)


class Relationship:
	def make_friends(self, obj):
		print('%s is making friends with %s.' % (self.name, obj.name))


class Man(Human, Relationship):		# 多重继承
	# 定义一个Human的子类
	def __init__(self, name, age, hair):
		# 继承父类的其他属性
		# Human.__init__(self, name, age)的
		# 另一种写法——super
		super().__init__(name, age)
		self.hair = hair

	def game(self):
		print('%s is playing a game now.' % self.name)

	def sleep(self):
		# 覆写及调用父类的方法
		Human.sleep(self)
		print('%s is sleeping with another person.' % self.name)


class Woman(Human):
	def __init__(self, name, age, hair):
		Human.__init__(self, name, age)
		self.hair = hair

	def shopping(self):
		print('%s is shopping now...' % self.name)


m = Man('William', '32', 'short')
m.sleep()
m.game()
print()

w = Woman('Jane', '29', 'long')
w.sleep()
w.shopping()

m.make_friends(w)

