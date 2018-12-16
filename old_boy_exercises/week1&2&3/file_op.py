f = open('we.txt', 'r', encoding='utf-8')

# 读取文件最高效的方式，是对f对象进行遍历
# 1、f.readlines方法会将文件所有内容（无论文件多大）
# 读取到计算机内存中，故该方法只适合读取小文件
# 2、需求：不打印第十行，因为变量f是一个迭代器
# 故无法使用enumerate方法,所以程序中
# 需要自己定义一个变量对循环进行计数

count = 0
for line in f:
	if count == 9:
		print('------------我是分割线------------')
		count += 1
		continue 
	print(line.strip())
	count += 1
print(f.tell())
print(f.seek(0))
print(f.tell())
print(f.encoding)