# __author__: William Kwok
import datetime,time

# 获取当前日期时间
a = datetime.datetime.now()
print(a)

# 时间戳直接转换成日期
b = datetime.date.fromtimestamp(time.time())
print(b)

# 当前时间+3天
c = a + datetime.timedelta(3)
print(c)

# 当前时间-3天
d = a + datetime.timedelta(-3)
print(d)

# 当前时间+3小时
e = a + datetime.timedelta(hours=3)
print(e)

# 时间替换
f = a.replace(minute=22, hour=22, second=22)
print(f)