# 不使用 eval 函数,来实现一个计算器的功能
import re
# expression = '35 + 25 * (32 / (4 + 25 - 40))'

# 计算时需用到的正则表达式
inner_bracket_search = re.compile(r'\([^()]+\)')  # 寻找最内层括号的规则
add = re.compile(r'(-?\d+\.?\d*\+-\d+\.?\d*)|(-?\d+\.?\d*\+\d+\.?\d*)')  # 寻找加法运算规则
sub = re.compile(r'(-?\d+\.?\d*--\d+\.?\d*)|(-?\d+\.?\d*-\d+\.?\d*)')    # 寻找减法运算规则
mul = re.compile(r'(\d+\.?\d*\*-\d+\.?\d*)|(\d+\.?\d*\*\d+\.?\d*)')     # 寻找乘法运算规则
div = re.compile(r'(\d+\.?\d*/-\d+\.?\d*)|(\d+\.?\d*/\d+\.?\d*)')       # 寻找除法运算规则
check_calc_status = re.compile(r'\(?\+?-?\d+\)?')       # 检查括号内运算是否完毕
del_bracket = re.compile(r'[^(].*[^)]')     # 去除括号规则


def jiafa(s):
    """计算表达式的加法运算"""
    split_exp = re.split(r'\+', add.search(s).group())
    return s.replace(add.search(s).group(), str(float(split_exp[0]) + float(split_exp[1])))


def jianfa(s):
    """计算表达式的减法运算"""
    split_exp = sub.search(s).group()
    if split_exp.startswith('-'):   # 将类似-2-1这种表达式转换成-（2+1）
        split_exp = split_exp.replace('-', '+')
        res = jiafa(split_exp).replace('+', '-')
    else:
        split_exp = re.split(r'-', split_exp)
        res = str(float(split_exp[0]) - float(split_exp[1]))
    return s.replace(sub.search(s).group(), res)


def chengfa(s):
    """计算表达式的乘法运算"""
    split_exp = re.split(r'\*', mul.search(s).group())
    print(s.replace(mul.search(s).group(), str(float(split_exp[0]) * float(split_exp[1]))))
    return s.replace(mul.search(s).group(), str(float(split_exp[0]) * float(split_exp[1])))


def chufa(s):
    """计算表达式的除法运算"""
    split_exp = re.split(r'/', div.search(s).group())
    return s.replace(div.search(s).group(), str(float(split_exp[0]) / float(split_exp[1])))


# while bracket.search(exp):
# inner_exp_search = inner_bracket_search.search(expression).group()
# print(inner_exp_search)
# a = jiafa(inner_exp_search)
# b = jianfa(a)
# print(b, re.search(r'[^(].*[^)]', b).group())

def calculator():
    while True:
        expression = input("Please enter an expression('q' for quiting): ")
        if expression == 'q':
            break
        else:
            expression = ''.join(expression.split())  # 去掉表达式中的空格符号
            # print(expression)
            # 如果输入的表达式首尾无括号，则统一格式为带括号的形式
            if not expression.startswith('('):
                expression = str('(%s)' % expression)
            while inner_bracket_search.search(expression):  # 检查表达式是否有括号
                expression = expression.replace('--', '+')  # 将 -- 这种符号换为 +
                expression_search = inner_bracket_search.search(expression).group()  # 将最内层符号及其内容赋值给变量

                # # 如表达式是否有除法运算存在（必须在乘法运算前），执行除法运算，并用运算结果替换原表达式
                if div.search(expression_search):
                    expression = expression.replace(expression_search, chufa(expression_search))

                # 如表达式是否有乘法运算存在，执行乘法运算，并用运算结果替换原表达式
                elif mul.search(expression_search):
                    expression = expression.replace(expression_search, chengfa(expression_search))

                # 如表达式是否有减法运算存在（必须在加法运算前），执行减法运算，并用运算结果替换原表达式
                elif sub.search(expression_search):
                    expression = expression.replace(expression_search, jianfa(expression_search))

                # 如表达式是否有加法运算存在，执行加法运算，并用运算结果替换原表达式
                elif add.search(expression_search):
                    expression = expression.replace(expression_search, jiafa(expression_search))

                # 如果括号内加减乘除几种运算均已执行完毕，执行去括号操作
                elif check_calc_status.search(expression_search):
                    # 去除最外层的括号()
                    expression = expression.replace(expression_search, del_bracket.search(expression_search).group())
            print('The answer is: %.2f.' % float(expression))


if __name__ == '__main__':
    calculator()
