# coding = utf-8
"""Dictionary"""

"""
字典是一种可变容器模型
字典中每个键值（Key=>Value）用冒号：分割，每个队之间用逗号分割
整个字典包括在花括号 {}中
同一个键不应该 被赋值两次，如果被赋值两次，后一个值会被记住
"""
dict = {'Name': 'Jane', 'Year': '1995', 'Conutry': 'Germem'}
# 访问字典里的值
print(dict['Name'])
dict['Year'] = 1999  # 修改字典某些键值
dict['School'] = '合肥一中'  # 增加新的键值对
print(dict)

del dict['Conutry']

print(dict)
