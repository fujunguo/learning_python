# __author__: William Kwok
import time
def consumer(name):
	print("{}准备好吃包子了！".format(name))
	while True:
		baozi = yield
		print("包子【{}】来了，被【{}】吃了！".format(baozi, name))


def producer(name1):
	c1 = consumer('A')
	c2 = consumer('B')
	c1.__next__()
	c2.__next__()
	print("【{}】开始准备做包子啦！".format(name1))
	for i in range(10):
		time.sleep(0.5)
		print("做了一个包子，分成两半！")
		c1.send(i)  # 重新恢复生成器，同时发送一个值回去，赋予当前的yield表达式
		c2.send(i)


producer('小明')

