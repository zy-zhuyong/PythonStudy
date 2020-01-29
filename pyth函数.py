# coding = utf - 8
import time

"""
语法：
def 函数名（参数列表）：
    函数体
    
参数类型：
    必需参数
    关键字参数
    默认参数
    不定长参数
    
"""


def sapm():
    global eggs  # 全局变量
    eggs = 'spam'


def bacon():
    eggs = 'bacon'  # 局部变量


def ham():
    return eggs  # return 关键字函数返回值或者表达式


eggs = 42
sapm()
print(eggs)
print('\n')

"""必需参数"""


def printme(str):
    print(str)
    return


printme('输出的就是这些')
print('\n')

"""关键字参数"""
printme(str='Runoob')

"""默认参数"""


def printinfo(name, age=22):
    print(f'姓名：{name}')
    print(f'年龄：{age}')
    return


printinfo(name='Jack')  # 函数调用时并没有传入age的值
printinfo('Bob', 34)
print('\n')

"""不定长参数!!!!!!!!!!!!!!
def functionname( [formal_args,] *var_args_tuple ):
     #函数文档字符串
    function_suite
    return [expresssion]

def functionname( [formal_args,] **var_args_tuple ):
     #函数文档字符串
    function_suite
    return [expresssion]
"""
"""加了一个*号的参数会以元组（Tuple）的形式导入"""


def printinfo1(agr1, *vartuple):
    # 打印传入的参数
    print(f'输出：\n{agr1}\n{vartuple}')


printinfo1(70, 60, 50)
print('\n')


def printinfo2(agr1, *vartuple):
    # 打印传入的参数
    print(f'输出：\n{agr1}')
    for var in vartuple:
        print(var)
    return


printinfo2(70, 60, 50)
print('\n')

"""加了两个**号的参数会以字典（Dict)的形式导入"""


def printinfo3(agr1, **vardict):
    # 打印传入的参数
    print(f'输出：\n{agr1}\n{vardict}')


printinfo3(1, a=1, b=2)
print('\n')

"""匿名函数lambda
所谓匿名，意义在于不再用def这样的标准语句的形式定义一个函数
基本语法：lambda [agr1,agr2,....,agrn]:experession

"""

sum = lambda agr1, agrg2: agr1 + agrg2

print(f'两数相加之和为：{sum(10, 20)}')

""":return语句
#return[表达式]用于退出函数
"""


def sum(a, b):
    total = a + b
    print(f'函数内：{total}')
    return total


# 调用函数
total = sum(1, 2)
print(f'函数外：{total}')
print('\n')


def odd(x):
    if x % 2 != 0:
        # print(x)
        return x
    else:
        # print(0)
        return x


a = odd(3)
b = odd(4)
print(a + b)
