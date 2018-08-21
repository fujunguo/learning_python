# 将str写入StringIO
from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World!')
print(f.getvalue())
print()

# 从StingIO读取str
k = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = k.readline()
    if s == '':
        break
    print(s.strip())

