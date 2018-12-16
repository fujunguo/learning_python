# __author__: William Kwok
import sys

# 获取 python 版本
print(sys.version)

# 退出程序，正常退出时exit(0)
# sys.exit(n)

# 命令行参数List，第一个参数是程序本身路径
print(sys.argv)

# 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.path)