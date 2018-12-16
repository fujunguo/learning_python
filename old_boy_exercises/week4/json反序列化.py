# __author__: William Kwok
import json
# json 用于不同编程语言间的数据交换
f = open('test.text', 'r')
data = json.loads(f.read())
f.close()
print(type(data))
print(data['age'])

