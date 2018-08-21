from datetime import datetime, timedelta

# 获取当前日期时间
now = datetime.now()
print(now)
# print(type(now))

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
print(dt.timestamp())
print()

# timestamp转换为datetime
t = dt.timestamp()
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))
print()

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print()

# datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))
print()

# datetime加减
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print()


