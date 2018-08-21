#杨辉三角
def triangles():
	L=[1]
	while True:
		yield L
		L.append(0)
		L=[L[i-1]+L[i] for i in range(len(L))]

n=0
for t in triangles():
	print(t)
	n=n+1
	if n==10:
		break

#汉诺塔
def move(n,a,b,c):
	if n==1:
		print(a,'->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

#迭代器

#1.判断是否为iterable对象
from collections import Iterable
isinstance('abc',Iterable)

#2.判断是否是iterator对象
from collections import Iterator
isinstance('abc',Iterator)
isinstance((x*x for x in range(10)),Iterator)
isinstance([x*x for x in range(10)],Iterator)