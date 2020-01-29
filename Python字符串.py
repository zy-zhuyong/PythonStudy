# coding = utf-8
"""字符串的表示以单引号或者双引号来创建字符串"""

var1 = 'hello world'
var2 = 'python3.7'
print(f'我正在学习{var2[:-2]},学习编程{var1}', end='/t')
print(var1 + '  ' + var2)

"""Python转义字符:以反斜杠\+转义关键字"""

"""Python字符串运算符"""
a, b = 'Hello', 'Python'
print(a * 2)  # 字符串赋值
print(a + b)
print(a[0])
print(a[0:2])  # 遵循左闭右开原则
print('H' in a)
print('h' not in a)  # 身份运算

"""Python字符串的格式化：看基础知识.py"""
print(var1.title())
print(var1.swapcase())
print(var1.upper())
