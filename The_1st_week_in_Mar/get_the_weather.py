from urllib import request
import json

# citycode = '101010100'
# url = request.urlopen('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
# content = url.read().decode('utf-8')
# data = json.loads(content)
# print(type(data), '\n', data) # dict
# print(type(content), '\n') # str
# result = data['weatherinfo']
# print(result,'\n')

# str_temp = ('%s\n%s ~%s' % (result['weather'], result['temp1'],result['temp2']))
# print(str_temp)

url1 = 'http://m.weather.com.cn/data5/city.xml'
content1 = request.urlopen(url1).read().decode('utf-8')
provinces = content1.split(',')
print(content1)
