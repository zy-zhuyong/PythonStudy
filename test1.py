def math(m,n):
    xt = ''
    for n in range(1,n+1):
        # print("%d*%d=%d"%(m,n,m*n),end=' ')
        xt += "%d*%d=%d "%(m,n,m*n)
    print(xt)
for a in range(1,10):
    math(a,a)


