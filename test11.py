# 打印1-100内的偶数
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)
# 复利计算函数
amount = input('principal amount:')
def invest():
    while 1 < 3:
        time = input('Year')
        invest = float(amount)*(1.05)**float(time)
        print('$'+str(invest))
invest()