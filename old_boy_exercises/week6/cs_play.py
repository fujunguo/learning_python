# __author__: William Kwok


class Role:
	n = 123	 # 类变量，用途：大家共有的属性，节省内存
	n_list = []

	def __init__(self, name, role, weapon, life_value=100, money=15000):
		# 构造函数：在实例化时做一些类的初始化工作
		self.name = name	# 实例变量（静态属性）
		self.role = role
		self.weapon = weapon
		# 变量（属性）前加双下划线__后，意味着该属性为私有属性，
		# 在类结构体外面无法随意访问（只能在类内部访问），
		# 如r1.__life_value会调用不成功
		self.__life_value = life_value
		self.money = money

	def __del__(self):
		# 析构函数：在实例释放、销毁的时候自动执行，通常用于做一些
		# 收尾工作，如关闭一些数据库连接、打开的一些临时文件
		print('{} is dead.'.format(self.name))

	def shot(self):		# 类的方法，功能（动态属性）
		print('shooting...')

	# 私有方法，跟私有属性一样的访问限制
	def __got_shot(self):
		self.__life_value -= 30
		print('Ah...,I got shot...')

	# 内部访问私有属性和私有方法
	def show_status(self):
		self.__got_shot()
		print("Life value:", self.__life_value)

	def buy_gun(self, gun_name):
		print('%s just bought %s.' % (self.name, gun_name))


# 把一个类编程一个具体对象的过程，叫实例化（初始化）。
r1 = Role('Alex', 'police', 'AK47')
r1.show_status()
r1.buy_gun('AK47') # 相当于Role.buy_gun(r1, 'AK47')
# 给r1.n赋值相当于r1对象里，新增了一个属性值n，而非真正
# 修改类变量，但是变量如果是指向一个列表对象n_list的话，
# 对象和类则共用同一个内存变量，一发牵动全身
r1.n = '改类变量'
r1.n_list.append('From r1')
r1.name = 'William' # 修改属性值
r1.bullet_prove = True # 新增一个属性
del r1.bullet_prove # 删除一个属性
print("实例变量：", r1.n, r1.name, r1.n_list, "类变量：", Role.n, Role.n_list)
# del r1  # 提前执行析构函数
print()

r2 = Role('Jack', 'terrorist', 'B22')
r2.show_status()
r2.n_list.append('From r2')
print("实例变量：", r2.n, r2.n, "类变量：", Role.n_list)


