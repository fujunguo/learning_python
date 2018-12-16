# __author__: William Kwok
import time

# 时间戳
a = time.time()
print(a)


# struct_time
b = time.gmtime()
c = time.localtime()
print(b)
print(c)
d = time.mktime(c)
print(d)

# 格式化字符串
ftime = time.strftime("%Y-%m-%d %H:%M:%S", c)
print(ftime)
ptime = time.strptime(ftime, "%Y-%m-%d %H:%M:%S")
print(ptime)