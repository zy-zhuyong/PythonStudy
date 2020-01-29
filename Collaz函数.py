# coding = utf-8

# def collatz(num):
#     if num % 2 == 0 :
#         return num//2
#     elif num % 2 == 1:
#         return 3*num + 1
#     else:
#         print('error')
# try:
#     num = int(input())
#     while num!=1:
#         print(collatz(num))
#         num = collatz(num)
# except ValueError :
#     print('valueError')
Sum = []
for a in range(1, 10, 1):
    Sum.append(a)
    print(Sum)

