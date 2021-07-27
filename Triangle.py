def shape(n):
    if n<=0:
        return
    shape(n-1)
    for i in range(n):
        print('*', end='')
    print()

shape(10)
