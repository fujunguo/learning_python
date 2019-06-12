import requests

# 功能：爬取网站上的 pdf 文档和其他压缩文件

for i in range(1, 13):
	url = 'http://static.education.makeblock.com/lesson'+ str(i) + '.pdf'
	res = requests.get(url)
	res.encoding = res.apparent_encoding
	with open('./第 '+ str(i) + ' 课课件.pdf', 'wb') as f:
		# res.content可以得到二进制文件信息
		f.write(res.content)
	print('第 {} 课下载成功。'.format(i))

print('课程下载完成...')


for i in range(1, 13):
	url1 = 'http://static.education.makeblock.com/Drawing-' + str(i) + '.rar'
	res1 = requests.get(url1)
	res1.encoding = res1.apparent_encoding
	if len(res1.content) > 1000:
		with open('./第 '+ str(i) + ' 课图纸.rar', 'wb') as f:
			f.write(res1.content)
		print('第 {} 课教案下载成功。'.format(i))
	else:
		print('第 {} 课教案下载失败。'.format(i))
		continue

print('教案1下载完成...')

for i in range(1, 13):
	url2 = 'http://static.education.makeblock.com/Drawing-' + str(i) + '.lq'
	res2 = requests.get(url2)
	res2.encoding = res2.apparent_encoding
	if len(res2.content) > 1000:
		with open('./第 '+ str(i) + ' 课图纸.rar', 'wb') as f:
			f.write(res2.content)
		print('第 {} 课教案下载成功。'.format(i))
	else:
		print('第 {} 课教案下载失败。'.format(i))
		continue

print('教案2下载完成...')
