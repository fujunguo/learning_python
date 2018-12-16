import getpass

_name = 'William'
_password = '123'

name = input("name:")
passwd = getpass.getpass("password:")

if _name == name and _password==passwd:
    print("Welcome user {}!".format(name))
else:
    print('Invalid username or password.')