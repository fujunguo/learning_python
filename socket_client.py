# __author__: William Kwok
# 客户端
import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6699
c.connect(('localhost', port))
while True:
	msg = input('>>:').strip()
	if len(msg) == 0:
		continue
	# 数据的发送与接收，都必须是bytes类型
	c.send(msg.encode())
	data = c.recv(1024)
	print('Message from server:', data.decode())
c.close()


