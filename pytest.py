# coding : utf-8
"""
本例子演示返回值和return语句
"""
import random
def getanswer(answernumber):
    if answernumber == 1:
        return 'a'
    elif answernumber == 2:
        return  'b'
    elif answernumber == 3:
        return 'c'
    elif answernumber == 4:
        return 'd'
print(getanswer(random.randint(1,4)))