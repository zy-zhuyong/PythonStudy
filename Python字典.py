# coding = utf-8
"""Dictionary"""

"""
-字典是一种可变容器模型
字典中每个键值（Key=>Value）用冒号：分割，每个队之间用逗号分割
整个字典包括在花括号 {}中
同一个键不应该 被赋值两次，如果被赋值两次，后一个值会被记住

dict常用的操作：
- {'k' : 'v'},dict(zip(list_k,list_v)) :创建方法
- d['k],d.get('k')  :获取元素
- 'k' in d :检测k值是否存在
- d.keys() :获取所有的k
- d.values() ：获取所有的值
- del d['k'] ：删除k
- dl.update(d2) ：更新值，同k被覆盖
dir(dict)>>
 ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""
dict = {'Name': 'Jane',
        'Year': '1995',
        'Conutry': 'Germem'}
# 访问字典里的值
print(dict['Name'])
dict['Year'] = 1999  # 修改字典某些键值
dict['School'] = '合肥一中'  # 增加新的键值对
print(dict)

del dict['Conutry']

print(dict)
