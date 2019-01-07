# __author__: William Kwok


# 多态：一种接口，多种实现
class Animal(object):
	def __init__(self, name):
		self.name = name

	def talk(self):
		pass

	@staticmethod
	def animal_talk(obj):
		obj.talk()


class Cat(Animal):
	def talk(self):
		print('Meow!')


class Dog(Animal):
	def talk(self):
		print('Woof! Woof!')

c = Cat('Missy')
d = Dog('Lassie')
# c.talk()
# d.talk()
Animal.animal_talk(c)
Animal.animal_talk(d)