for __ in range(int(input("Enter runs: "))):
    a,b,c=list(map(int,input().split()))
    x = min(a,b)
    y = min(b,c)
    z = min(c,a)
    if(x==y and y==z and z==x):
        print("YES")
    else:
        print("No")