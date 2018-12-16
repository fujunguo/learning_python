from city_functions import name
import unittest

class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		full_name = name('santiago', 'chile')
		self.assertEqual(full_name, "Santiago,Chile")
	
	def test_city_country_population(self):
		full_name = name('santiago', 'chile', 5000000)
		self.assertEqual(full_name, "Santiago,Chile - population 5000000")

unittest.main()