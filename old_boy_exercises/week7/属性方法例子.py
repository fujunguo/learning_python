# __author__: William Kwok
class Flight(object):
	"""描述航班信息"""
	def __init__(self, name):
		self.name = name

	def checking_status(self):
		print('Checking the status of flight %s.' % self.name)
		return 1

	@property
	def flight_status(self):
		status = self.checking_status()
		if status == 0:
			print('Flight got canceled...')
		elif status == 1:
			print('Flight is arrived...')
		elif status == 2:
			print('Flight has departured...')
		else:
			print("Can't check the flight status...Please check it later.")

f = Flight('CA980')
print(f.__doc__)
f.flight_status # 将其改为普通方法，通过f.flight_status()调用似乎也没差别？