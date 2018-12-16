# __author__: William Kwok
def fib(m):
	n, a, b = 0, 0, 1
	while n < m:
		yield b  # 返回生成器对象
		a, b = b, a + b # t = (b, a+b) a = t[0] b = t[1]
		n = n + 1
	return "Done."


g = fib(20)
while True:
	try:
		x = next(g)
		print("g: ", x)
	except StopIteration as e:
		print("Generator returns value: ", e.value)
		break




