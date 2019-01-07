# __author__: William Kwok
# 经典类：class A VS 新式类：class A(object)
# “广度优先”继承策略：如类D同时继承类B、C时，当D中无构造函数__init__时，
# 它继承父类__init__时，找寻路线为:B->C->A,而“深度优先”策略则为：B->A->C
# python3中经典类和新式类，都是按照“广度优先”来继承的
# python2中经典类按照“深度优先”策略，新式类采用“广度优先”策略
class A:
	def __init__(self):
		print("A")


class B(A):
	pass
	# def __init__(self):
	# 	print("B")


class C(A):
	def __init__(self):
		print("C")


class D(B, C):
	pass
	# def __init__(self):
	# 	print("D")

obj = D()