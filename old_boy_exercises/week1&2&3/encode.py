# __author__: William Kwok
import sys
print(sys.getdefaultencoding())

s = '你好'
print(s.encode('gbk'), type(s))
print(s.encode())
print(s.encode('utf-8').decode('utf-8'))
f = open()