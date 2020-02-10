# coding = utf-8
"""
append ：追加元素
+ ， extend ：多个列表你相加
insert ：向指定位置插入一个元素
remove pop : 移除某一个元素
sort : 排序
[:] : 切片操作
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

list = ['apple', 'juice', 'ice', [1, 2, 3]]
list1 = ['hello']
list[1] = 'hello'  # 更新列表
print(list)
del list[3][0]  # 删除列表中的某些元素
len(list)  # 长度
print(list + ['ok'])
print(list * 2)
print('ice' in list)  # 判断元素是否在列表中
for x in list:
    print(x, end=' ')  # 迭代
print(max(list[3]))
print(min(list[3]))
"""
Python中列表的操作方法
"""
list.append('AA')
print(list)

print(list.count('apple'))

print(list.copy())
