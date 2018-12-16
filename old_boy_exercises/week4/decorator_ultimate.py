# __author__: William Kwok
# 带参数的装饰器
username, passwd = 'William', 'abc123'
def auth(auth_type):
	print("Func type: {}".format(auth_type))
	def outwrapper(func):
		print("Func type: {}".format(func))
		def wrapper(*args, **kwargs):
			if auth_type == 'local':
				user = input("Username: ").strip()
				password = input("Password: ").strip()
				if user == username and password == passwd:
					print("\033[32;1mUser has passed authentication.\033[0m")
					res = func(*args, **kwargs)
				else:
					exit("\033[31;1mInvalid username or password.\033[0m")
				return res
			elif auth_type == 'ldap':
				print("\033[31;1mLdap is not valid.\033[0m")
		return wrapper
	return outwrapper

def index():
	print("Welcome to index page.")


@auth(auth_type='local')  # home = auth(auth_type)(home)
def home():
	print("Welcome to home page.")
	return "home page"


@auth(auth_type='ldap')
def bbs():
	print("Welcome to bbs page.")


index()
print(home())
bbs()