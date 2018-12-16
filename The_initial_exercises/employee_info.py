class Employee():
	"""docstring for Employee"""
	def __init__(self, firstname, lastname, salary):
		# super(Employee, self).__init__()
		'''__init__方法接收名、姓、薪水三个参数'''
		self.firstname = firstname
		self.lastname = lastname
		self.salary = salary

	def give_raise(self, addtion=5000):
		'''
		默认将薪水增加5000
		但同时也能接受其他薪水增加量
		'''
		self.salary += addtion