import requests

r = requests.get('https://www.douban.com/')  # 豆瓣首页
print(r.status_code)
print("Encoding style: '%s'" % r.encoding)
print()
# print(r.text)

# 获得bytes对象
r1 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r1.url)
# print(r1.content)

# 获取json对象
r2 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r2.json())

# 传入HTTP header
r3 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r3.text)

# 发送post请求
# r = requests.post('https://account.douban.com/login', data={'form_email': 'abc@example.com', 'form_passwd': '123456'})
