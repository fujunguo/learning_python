# __author__: William Kwok
import os

# import module1
from module1 import say_hi
# #####模块的导入优化
# 如果导入模块中的某个函数在导入后用的次数较多，
# 那么直接导入这个函数，相较于 import module1 更为高效

say_hi('William')

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
