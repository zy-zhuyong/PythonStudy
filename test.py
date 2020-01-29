# coding = utf-8
def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 10
    eggs = 0
spam()
"""
局部作用域不能使用其他局部作用域的变量
"""

"""
数据类型转换
"""
num = int(input('请输入你的数字：'))
num1 = hex(num)
num2 = bin(num)
num3 = oct(num)
num4 = chr(num)

print(num1)
print(num2)
print(num3)
print(num4)