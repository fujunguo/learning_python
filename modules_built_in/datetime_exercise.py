import re
from datetime import datetime, timedelta, timezone


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    a = re.match(r'UTC([+-]{1}\d{1,2}):\d{1,2}', tz_str).group(1)
    tz = int(a)
    d_t = dt.replace(tzinfo=timezone(timedelta(hours=tz)))
    print(d_t)
    print(tz)
    return d_t.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('OK!')
