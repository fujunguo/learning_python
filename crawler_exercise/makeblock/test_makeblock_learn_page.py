import requests
from bs4 import BeautifulSoup
import time
import pdfkit
import os

def parse_url_to_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.find_all(class_="entry-content")
    html = str(body)
    with open('makeblock.html', 'w', encoding='utf-8') as f:
        f.write(html)
    return 'makeblock.html'


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
    'outline-depth': 10,
    }
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_file(htmls, file_name, options=options, configuration=config)


def main():
    start = time.time()
    url = "http://learn.makeblock.com/cn/laserbot/"
    file_name = u"LaserBot使用手册.pdf"
    htmls = parse_url_to_html(url) 
    save_pdf(htmls, file_name)
    os.remove(htmls)

    total_time = time.time() - start
    print(u"总共耗时: %f 秒" % total_time)


if __name__ == '__main__':
    main()
