import functools, time


def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		start = time.time()
		fn(*args, **kw)
		end = time.time()
		print('Function %s() executed in %s ms' % (fn.__name__, end - start))
		return fn(*args, **kw)
	return wrapper


@metric
def fast(x, y):
	time.sleep(0.1234)
	return x + y


f = fast(11, 22)
print('The result %s is from Function:%s' % (f, fast.__name__))