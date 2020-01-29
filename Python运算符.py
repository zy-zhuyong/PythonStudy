# coding = utf-8
print('这里是运算符的介绍！！！')
"""
Python 基本运算符
加 +
减 -
乘 * 
除 /
求余 %
幂次方 ** 
整除 //

"""
a = 10
b = 20
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a%b=',a%b)
print('a**b=',a**b)
print('a//b',a//b)

"""
Python的符合运算符
加 +=
减 -=
乘 *=
除 /=
求余 %=
幂次方 **= 
整除 //=
海象运算符 := *Python 3.8新增运算符
"""
a+=1
print(a)
# print(a*=2)
# print(a**2)
# print(a//=2)

"""
比较运算符（==等于 ，！=不等于，>大于,<小于,<=小于等于,>=大于等于)布尔类型(True,False)

"""
print('name' == 'Name')
print(42 != '42')
print(1 > 2)
print(1 < 2 <3)
print(4 <= 3)
print(3 >= 4)
print(abs(-10)>len('length of the word'))

"""逻辑运算符
and 与
or 或
not 非

"""
#向已创建的列表中添加新元素和列表的索引
list = ['zhuyong','25','男','tester','basketball']
list.append('see mv')
print(list)
print(list[0],list[-1])
print('zhuyong' in list)#成员身份
print('Zhuyong' not in list)
"""in 和 not in是成员运算符"""

"""位运算符
 &  按位与运算

 |  按位或运算

 ^  按位异或运算
 
 ~  按位取反

 >>  右移运算

 <<  左移运算

"""
num1 = 0b10101010
num2 = 0b10001000
print(num1&num2)
print(num1|num2)
print(num1^num2)
print(~num1)
print(num1>>2)
print(num1<<2)