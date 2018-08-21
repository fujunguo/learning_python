from sys import argv

# 把argv中的东西解包，将所有的参数依次赋予左边的变量名
script, first, second, third = argv

# 从用户手上得到更多的输入
a = int(input())
b = input()

print("The script is called:", script, a, b)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
