import base64


# 一个能处理去掉=的base64解码函数
def safe_base64_decode(s):
    while len(s) % 4 != 0:
        s += b'='
    return base64.b64decode(s)


assert b'abcd' == safe_base64_decode(b'YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA')
print('OK!')
