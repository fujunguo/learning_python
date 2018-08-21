import chardet
print(chardet.detect(b'Hello, World!'))

# GBK是GB2312的超集
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data1 = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data1))

data2 = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data2))

# 用chardet检测编码，使用简单。
# 获取到编码后，再转换为str，就可以方便后续处理
# chardet支持检测中文、日文、韩文等多种语言

data3 = b'\xb5\xc7\xc2\xbc\xca\xa7\xb0\xdc\xa3\xac\xc7\xeb\xca\xb9\xd3\xc3\xb0\xb2' \
        b'\xc8\xab\xc1\xac\xbd\xd3\xa3\xa8\xc8\xe7ssl\xa3\xa9\xa3\xac\xcf\xea\xcf\xb8\xcb' \
        b'\xb5\xc3\xf7\xc7\xeb\xb2\xe9\xbf\xb4'
print(data3.decode('GBK'))
