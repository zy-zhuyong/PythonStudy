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
# # for x in it:
# #     print(x,end = ' ')
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


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)

while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        sys.exit()
