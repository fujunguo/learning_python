# 求和函数--返回求和后的结果
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print(calc_sum(1, 3, 5, 7, 9))


# 求和函数--返回求和的函数
def lazy_sum(*args):
    def sum_():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum_
    # 我们在函数lazy_sum中又定义了函数sum_，并且，内部函数sum_可以引用外部函数lazy_sum的参数和局部变量，
    # 当lazy_sum返回函数sum_时，相关参数和变量都保存在返回的函数中，这种程序结构称为闭包（Closure）
    # 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。


f = lazy_sum(1, 3, 5, 7, 9)
print(f)    # 返回求和函数
print(f())  # 返回求和后的值

