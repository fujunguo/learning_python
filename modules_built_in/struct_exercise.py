import base64, struct


def bmp_info(data):
    data = bmp_data[:30]
    s = struct.unpack('<ccIIIIIIHH', bmp_data[:30])
    print(data)
    print(s)
    print()
    if s[0] == b'B' and (s[1] == b'M' or s[1] == b'A'):
        return {
            'width': s[6],
            'height': s[7],
            'color': s[9]
        }
    else:
        print('这不是一个位图文件！')
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAAD'
                            'ICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9/'
                            '/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/'
                            '/f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/'
                            '9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8A'
                            'Hz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//'
                            'f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/'
                            'AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3/'
                            '/f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//f'
                            'wB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//f'
                            'wB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9/'
                            '/3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHw'
                            'AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfA'
                            'B8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/A'
                            'HwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/'
                            '9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/'
                            '/f/9//38AAA==')

bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('OK!')
