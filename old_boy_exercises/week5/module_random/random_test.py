# __author__: William Kwok
import random

"实现一个四位数字验证码的功能"
checkcode = ''

for i in range(4):
	current_number = random.randrange(0, 4)
	if current_number == i:
		tmp = chr(random.randint(65, 90))
	else:
		tmp = random.randint(0, 9)
	checkcode += str(tmp)

print(checkcode)