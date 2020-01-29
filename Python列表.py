# coding = utf-8
list = ['apple', 'juice', 'ice', [1, 2, 3]]
list1 = ['hello']
list[1] = 'hello'  # 更新列表
print(list)
del list[3][0]  # 删除列表中的某些元素
len(list)  # 长度
print(list + ['ok'])
print(list * 2)
print('ice' in list)
for x in list:
    print(x, end=' ')  # 迭代
print(max(list[3]))
print(min(list[3]))
"""Python中列表的操作方法
"""
list.append('AA')
print(list)

print(list.count('apple'))

print(list.copy())
