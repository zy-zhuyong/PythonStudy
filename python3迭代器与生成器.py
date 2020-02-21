# coding = utf -8
"""
   迭代器是可以记住遍历的位置的对象
   迭代对象从集合的第一个元素开始访问，直到所有的元素被访问才结束，迭代器只能往前不能后退
   迭代器的两个基本方法：
   ① iter()
   ②  next()
   字符串、元组、列表都可用于创建迭代器

"""
import sys

# list = range(1,5)
# it = iter(list)
# for x in it:
#     print(x,end = ' ')
#
# """使用next（）函数"""
#
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

""" StopIteration异常用于表示迭代的完成，防止出现无限循环的情况吗 """

"""
生成器（generator）
跟普通函数不同生成器是一个返回迭代器的函数，只能用于迭代操作，更简单一点理解生成器就是一个迭代器。
在调用生成器时，每次遇到yield函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next（）方法时从当前
位置继续运行
"""

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(3)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        sys.exit()
