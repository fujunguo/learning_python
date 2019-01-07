# __author__: William Kwok
ls = [1, 2, 3]
d = {}
try:
	print(ls[3])
	open('text.txt')
	print(d['1'])  # try语句如有多个异常，只捕捉第一个异常
except IndexError as e:
	print('IndexError:', e)
# 如不清楚异常的具体类型，可在最后一个except语句中，使用用Exception关键字
except Exception as e:
	print('Exception:', e)
# 若try语句中的代码正常执行，else的语句将执行
else:
	print('Try-coding executes successfully.')
# 加入了try-except语句后，就算程序在执行过程中出现异常，try-except语句后的程序也将接着执行
print('The program ends.')
