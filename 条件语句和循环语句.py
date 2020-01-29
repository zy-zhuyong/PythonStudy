# coding = utf-8
# Fibonacci series:斐波那契数列
# 两个元素的总和确定下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=' ')
    a, b = b, a + b
print(' ')
# 狗的你年龄的判断

"""条件判断语句：if elif ... if"""
age = int(input('请输入你家狗狗的年龄：'))
print(' ')
if age <= 0:
    print('Are kidding me?')
elif age == 1:
    print('May 14 years old man')
elif age >= 2:
    hunman = 22 + (age - 2) * 5
    print(f'may {hunman} years old man')
else:
    print('your input error')

"""循环语句"""

"""while循环
var = int(input("please input:"))
while condtion:
    表达式 
else condition：
    表达式
"""

"""for循环
for <variable> in <sequence>:
    <statement>
els:
    <statement>
    
"""

"""range函数"""
sum = 0
for n in range(1, 100, 2):
    if sum > 300:
        break
    sum += n
    print(f'n=', n)
    print(f'sum=', sum)
"""<<<break语句>>>可以跳出for和while循环体"""

"""<<<continue>>>语句跳过当前循环块中的剩余语句"""

n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue  # 继续执行执行前面的语句
    print(n)
    if n < 0:
        break  # 跳出循环

for leter in 'Runoob':

    if leter == 'b':
        break
    elif leter == 'o':
        continue
    print(f'当前字母为：{leter}')
