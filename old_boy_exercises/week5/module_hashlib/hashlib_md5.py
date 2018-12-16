# __author__: William Kwok
import hashlib

# 生成一个md5对象
m = hashlib.md5()

m.update(b'Hello')
print(m.hexdigest())

# 生成的hash 值为字符串"HelloIt's me"组合加密过的
m.update(b"It's me.")
print(m.hexdigest())

n = hashlib.md5()
n.update("HelloIt's me.".encode(encoding='utf-8'))
print(n.hexdigest())
