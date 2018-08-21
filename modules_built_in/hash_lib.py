import hashlib, random

# MD5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
md5.update('michael'.encode('utf-8'))
print(md5.hexdigest())
print()

# SHA1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
print('\n')


# 验证用户登录
def login(name, password):
    db = {
        'michael': 'e10adc3949ba59abbe56e057f20f883e',
        'bob': '878ef96e86145580c38c87f0410ad153',
        'alice': '99b1c2188db85afee403b1536010c2c9'
    }
    md_5 = hashlib.md5()
    md_5.update(password.encode('utf-8'))
    if db[name] == md_5.hexdigest():
        return True
    else:
        print('密码错误!')


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('Test Passed!')
print()


# 利用修改后的MD5算法验证用户登录
# 通过对原始口令加一个复杂字符串来实现，
# 俗称“加盐”,提高安全性
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.name = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])  # ?
        # print(self.salt)
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '1234567'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)


# assert login('michael', '1234567')
assert login('michael', '1234567')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
print('OK!')
assert not login('michael', '123456')
assert not login('bob', '123456')
assert not login('alice', '123456')
print('OK!')
