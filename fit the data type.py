for __ in range(int(input("Enter runs: "))):
    n, x=list(map(int,input().split()))
    if x<=n:
        print(x)
    else:
        while (x>n):
            x = x-n-1
        print(x)
        #bad code 
        # y = (n-x)+1 
        # if y>0:
        #     print(y)
        # else:
        #     print(-y)