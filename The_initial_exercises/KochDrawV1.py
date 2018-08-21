# 科赫雪花的绘制
import turtle

# 科赫曲线的绘制
def koch(size, n):
	if n == 0:
		turtle.fd(size)
	else:
		for angle in [0, 60, -120, 60]:
			turtle.left(angle)
			koch(size/3, n-1)


def main():
	turtle.setup(800, 600)
	turtle.penup()
	turtle.goto(-200, 100)
	turtle.pendown()
	turtle.pensize(2)
	level = 4
	koch(400, level)
	turtle.right(120)
	koch(400, level)
	turtle.right(120)
	koch(400, level)
	turtle.hideturtle()
	# turtle.done()


main()