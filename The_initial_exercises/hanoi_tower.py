count = 0

# 汉诺塔问题采用函数+分支结构,
# 实现将N个圆盘从a柱子搬到c柱子
# 函数里采用递归算法，-递归链条、-递归基例
def solution(n, a, b, c):
	global count
	if n == 1:
		print(1, ':', a,'->',c)
		count += 1

	else:
		count += 1
		solution(n-1, a, c, b)
		print(n,':',a, '->', c)
		solution(n-1, b, a, c)


solution(4, 'A', 'B', 'C')
print(count)
# when n=3,	
# the first time:
#		count = 1
#		solution(2, a, c, b)->count = 2,solution(1, a, c, b),->count = 4
#		solution(2, b, a, c)->count = 5, solution(1, a, c, b)-solution(1, b, a, c)