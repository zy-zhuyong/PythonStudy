#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : python数据结构.py
@Author: yong.zhu
@Date  : 2020/1/17 14:36
@Tool  : PyCharm
'''
# 将列表当做堆栈使用：最先进入的元素最后被释放（先进后出）
stack = [0, 1, 2]
stack.append(3)
stack.append(4)
stack.pop()
stack.pop()
print(stack)

# 将列表当做队列使用:先进先出
from _collections import deque

qeque = deque(["Micchael", "John", "Eric"])
qeque.append("Jack")
print(qeque.popleft())

# 列表推导式
vec = [2, 4, 6]
print([3 * x for x in vec])
print([[x,x*x]for x in vec])