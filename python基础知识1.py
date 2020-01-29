"""
判断变量名是否为关键字
"""

import keyword

print(keyword.kwlist)
print(keyword.iskeyword('async'))

"""
-变量的命名
-以字母、数字、下划线组成
"""
print('变量的命名')
myName = 'Tom'  # 小驼峰命名
print(myName)
SchoolName = '安徽建筑大学'  # 大驼峰命名
print(SchoolName)

"""
-Python的数据类型：
①int  整型
②float  浮点型
③str   字符串
④bool   布尔型
⑤list  列表
⑥tuple  元组
⑦set  集合
⑧dict  字典-键值对
⑨复数

"""
print('Python的数据类型')
num1 = 1
num2 = 1.0
num3 = 'heima'
num4 = True
num5 = False
num6 = [1, 2, 3]
num7 = (1, 2, 3)
num8 = {1, 2, 3}
num9 = {'Year': '2019', 'Month': '12', 'Day': '26'}
num10 = 1 + 2j
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(num5))
print(type(num6))
print(type(num7))
print(type(num8))
print(type(num9))
print(type(num10))

"""
-格式化输出符号
%s 字符串(功能较强大)
%d 有符号的十进制整数( %nd 整数位数）
%f 浮点数  （%.nf  小数位数）
%c 字符
%u 有符号的十进制整数
%o 八进制整数
%x 十六进制整数（小写）ox
%X 十六进制整数（大写）OX
%e 科学计数法小写e
%E 科学计数法小写E

"""
# 1.我叫XX，今年我的年龄是X岁，我的体重是X.Xkg，我的学号是XXXX
name = 'Tom'
age = 18
weight = 88.8
stu_id = 6
print('我叫%s，今年我的年龄是%d岁，我的体重是%.2fkg，我的学号是%03d,明年%d岁了.' % (name, age, weight, stu_id, age + 1))
print('我叫%s，今年我的年龄是%d岁，我的体重是%fkg，我的学号是%d,明年%d岁了.' % (name, age, weight, stu_id, age + 1))
print('我叫%s，今年我的年龄是%s岁，我的体重是%skg，我的学号是%s,明年%s岁了.' % (name, age, weight, stu_id, age + 1))
"""
-格式化字符串扩展
-语法：f'{表达式}'
-Python3.6中新增的格式化语法
"""
print(f'我叫{name}，今年我的年龄是{age}岁，我的体重是{weight}kg，我的学号是{stu_id},明年{age + 1}岁了.')

"""
-转义字符：\n 换行  \t 制表
print('输出的内容'，end = '结束符号'）python自带默认换行‘\n’

"""

print('\thello\nworld')

"""输入input（）"""

keyword = input('请输入你的密码：')

print(f'你的密码是：{keyword}')

"""Pthon数据类型转换
-用数据类型转换函数进行转换

int()
float()
str()
complex()
eval()
chr()
hex()
bin()
oct()
"""

n1 = int(input(''))
print(int(n1))
print(float(n1))
print(str(n1))
print(complex(n1))
# print(eval(n1))
print(chr(n1))
print(hex(n1))
print(bin(n1))
print(oct(n1))
