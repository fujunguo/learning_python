# __author__: William Kwok
import os

# 获取当前工作目录
print(os.getcwd())

# 切换工作目录
os.chdir(r'C:\Users')
print(os.getcwd())

# 递归创建目录
os.makedirs(r'C:\a\b\c')

# 递归清除空目录
os.removedirs(r'C:\a\b\c')

# 新建单个目录
os.mkdir(r'C:\a')

# 删除单个目录
os.rmdir(r'C:\a')

# 删除一个文件
# os.remove(r'C:\ANG0')

# 列出指定目录下的所有文件和子目录（列表形式），包括隐藏文件
os.chdir(r'C:\\')
print(os.listdir())

# 输出当前平台使用的路径分隔符
print(os.sep)

# 输出当前平台使用的行终止符
os.linesep # '\r\n' Linux中为'\n'

# 输出当前平台使用的路径分隔符
print(os.pathsep)

# 获取系统环境编程
print(os.environ)

# 获取当前系统名
print(os.name)

# 运行shell命令
os.system('dir')
os.system('cd d:')

# 获取当前文件的绝对路径
print(os.path.abspath(__file__))

# 将path分割成目录和文件名的二元组返回
print(os.path.split(r'C:\Users\a.txt'))

# os.path.split的第一个元素
print(os.path.dirname(r'C:\Users\a.txt'))

# os.path.split的第一个元素
print(os.path.basename(r'C:\Users\a.txt'))

# 判断目录是否存在
print(os.path.exists(r'C:\Users\a'))

