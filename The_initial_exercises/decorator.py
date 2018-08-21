def tag(name):
	def decorator(func):
		def wrapper(text):
			value = func(text)
			return "<{}>{}</{}>".format(name, value, name)
		return wrapper
	return decorator


@tag('a')	# 等价于 my_upper = tag('a')(my_upper)
def my_upper(Text):
	value = Text.upper()
	return value


print(my_upper('hello'))
