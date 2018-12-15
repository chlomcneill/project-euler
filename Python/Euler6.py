def difference(n):
    a = 0
    for i in range(1,n+1):
        a += (i*i) # a = a + (i*i)
    b = 0
    for i in range(1,n+1):
        b = (sum(range(n+1)))**2
    diff = b - a
    print diff

difference(10) #Try with n=10 first, which gives 2640 - correct according to example