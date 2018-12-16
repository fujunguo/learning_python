# __author__: William Kwok
def foo():
	print('In the foo.')
	def bar():
		print('In the bar')
	bar()

foo()
