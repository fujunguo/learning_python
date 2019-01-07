# __author__: William Kwok
# 服务器端
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6699
s.bind(('localhost', port))
s.listen()
while True:
	"""第一层while循环适用于Linux系统，Windows系统无法看出效果"""
	print('等待客户端连接...')
	conn, addr = s.accept()
	# conn 就是客户端连过来时，在服务器为其生成的一个连接实例
	# print(addr)
	print('已经有客户端连接进来了...')
	while True:
		data = conn.recv(1024)
		if len(data) == 0:
			break
		print('Message from client:', data.decode())
		conn.send(data.upper())
s.close()
