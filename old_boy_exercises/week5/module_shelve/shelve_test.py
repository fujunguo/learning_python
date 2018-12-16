# __author__: William Kwok
# shelve 模块可以看成是 pickle 模块的升级版

import shelve, datetime
d = shelve.open('shelve_test')

name = ['William', 'Rain', 'Jack']
data = {'Age':24, 'Job':'IT'}
time = datetime.datetime.now()

"""写入数据"""
# d['name'] = name # 持续化列表
# d['data'] = data # 持续化dict
# d['time'] = time
# d.close()

"""读取数据"""
print(d.get('name'))
print(d.get('data'))
print(d.get('time'))