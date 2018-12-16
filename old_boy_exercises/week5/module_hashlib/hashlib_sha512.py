# __author__: William Kwok
import hashlib

a = hashlib.sha512()
a.update(b'abc')
print(a.hexdigest())
