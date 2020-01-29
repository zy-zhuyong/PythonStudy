"""全局变量可以在局部作用域中读取"""
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
