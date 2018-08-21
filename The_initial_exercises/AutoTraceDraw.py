import turtle as t
t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor('red')
t.pensize(5)

# 数据获取
detals = []
f = open('data.txt')
for line in f:
	# 以data.txt文档中的第1行数据为例
	# 1、首先将该行数据中的换行符‘\n’以空字符‘’替代
	# 2、然后将第1行数据（此时为1个字符串）以逗号','为标志进行分割
	# 3、此时返回1个包含line中所有数据的列表
	# 4、使用map函数对该列表中的所有元素，进行eval函数去除引号，
	# 5、得到一个包含line元素的整数列表如[300,0,144,1,0,0]
	# 6、将这个整数列表添加到空列表detals中
	line = line.replace('\n', '')
	detals.append(list(map(eval, line.split(','))))
f.close()

# 自动绘制
for i in range(len(detals)):
	t.pencolor(detals[i][3], detals[i][4], detals[i][5])
	t.fd(detals[i][0])
	if detals[i][1]:
		t.right(detals[i][2])
	else:
		t.left(detals[i][2])
t.hideturtle()
t.done()