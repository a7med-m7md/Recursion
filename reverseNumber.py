def revNum(n):
    if n!=0:
        print(n%10)
        revNum(n//10)
        
revNum(214)
