import unittest
from employee_info import Employee

'''测试Employee类'''
class TestEmployeeInfo(unittest.TestCase):
	'''
	编写测试用例，分别测试默认情况下，
	雇员薪水增加量和指定薪水增加量的程序，
	是否正常运行。
	'''
	def setUp(self):
		'''
		使用setUp()方法，只需创建一次对象实例，
		即可在每个测试方法中使用它们，而无需重复
		创建实例
		'''
		self.aemployee = Employee('Jacky', 'Ma', 5000)

	def test_give_default_raise(self):
		self.aemployee.give_raise()
		self.assertEqual(self.aemployee.salary, 10000)

	def test_give_custom_raise(self):
		self.aemployee.give_raise(10000)
		self.assertEqual(self.aemployee.salary, 15000)


unittest.main()