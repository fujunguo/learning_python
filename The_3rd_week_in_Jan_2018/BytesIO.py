from io import BytesIO
# 写入bytes，注意写入的不是str
# 而是经过UTF-8编码的bytes
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 初始化BytesIO，然后读取bytes
s = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(s.read())
