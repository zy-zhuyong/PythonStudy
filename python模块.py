#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : python模块.py
@Author: yong.zhu
@Date  : 2020/1/17 14:23
@Tool  : PyCharm
'''
"""
-模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py
import 模块名称
- from … import 语句
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中
- from … import * 语句
把一个模块的所有内容全都导入到当前的命名空间也是可行的
①   __name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
   
②dir() 函数
内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:

③读和写操作open（）
- open（filename，mode）

"""

f = open("E:\zy\激活码.txt", "w+")
# f.write("python is better luangage\n你真是个带学家")
# f.close()
str = f.read()
print(str)
