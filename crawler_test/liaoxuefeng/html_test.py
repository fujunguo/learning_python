# coding = utf-8
# 只能爬取前几章内容，后续会出现“解析错误”提示，
# 不知是否是目标网站反爬虫引起的。待后续解决bug
import logging
import os
import re
import time

import requests
from bs4 import BeautifulSoup
import pdfkit


html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>

"""


class Crawler(object):
	"""
	爬虫基类
	"""
	name = None

	def __init__(self, name=None, **kwargs):
		if name is not None:
			self.name = name
		elif not getattr(self, 'name', None):
			raise ValueError("%s must have a name" % type(self).__name__)

	def parse(self):
			raise NotImplementdError



def parse_url_to_html(url, name):
	"""
	解析URL，返回HTML内容
	:param url:解析的URL
	:param name: 保存的HTML文件名
	:return: html
	"""

	headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
	}

	try:
		response = requests.get(url, headers=headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		# 正文
		body = soup.find_all(class_="x-wiki-content")[0]
		print(body)
		time.sleep(10)
		# 标题
		title = soup.find('h4').get_text()

		# 标题加入到正文的最前面，居中显示
		center_tag = soup.new_tag("center")
		title_tag = soup.new_tag("h1")
		title_tag.string = title
		center_tag.insert(1, title_tag)
		body.insert(1, center_tag)
		html = str(body)
		# print(html)
		# body中的img标签的src相对路径改成绝对路径
		pattern = "(<img .*?src=\")(.*?)(\")"

		def func(m):
			if not m.group(2).startswith("http"):
				rtn = m.group(1) + "http://www.liaoxuefeng.com" + m.group(2) + m.group(3)
				return rtn
			else:
				return m.group(1) + m.group(2) + m.group(3)

		html = re.compile(pattern).sub(func, html)
		html = html_template.format(content=html)
		html = html.encode("utf-8")
		with open(name, "wb") as f:
			f.write(html)
		return name
	except Exception as e:
		logging.error("解析错误", exc_info=True)


# url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
# parse_url_to_html(url)


def get_url_list():
	"""
	获取所有的URL目录列表
	"""
	headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
	}
	response = requests.get("https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000", headers=headers)
	soup = BeautifulSoup(response.content, "html.parser")
	menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[3]
	urls = []
	for li in menu_tag.find_all("li"):
		url = "http://www.liaoxuefeng.com" + li.a.get('href')
		urls.append(url)
	return urls


# print(get_url_list())
# with open('site.html', 'w') as f:
# 	f.write(str(get_url_list()))

def save_pdf(htmls ,file_name):
	"""
	把所有HTML文件转换成PDF文件
	:param htmls: html文件名
	:param file_name: pdf文件名
	:return:
	"""
	options = {
	'page-size': 'Letter',
	'encoding': 'UTF-8',
	'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
	'custom-header':[
		('Accept-Encoding', 'gzip')
		],
	'outline-depth': 10
	}
	pdfkit.from_file(htmls, file_name, options=options)



def main():
	start = time.time()
	urls = get_url_list()
	file_name = u"liaoxuefeng_python3_tutorial.pdf"
	htmls = [parse_url_to_html(url, str(index) + ".html") for index, url in enumerate(urls)]
	save_pdf(htmls, file_name)

	for html in htmls:
		os.remove(html)

	total_time = time.time() - start
	print(u"总共耗时: %f 秒" % total_time)



if __name__ == '__main__':
	main()


















